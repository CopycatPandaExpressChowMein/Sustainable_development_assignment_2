from Deck import Deck
from Player import Player
from Intelligence import Intelligence
from CardHand import CardHand


class Game:
    """Represent the game logic and also the state of the game"""

    def __init__(self):
        """initialises the game with default value"""
        self.mode = "You against AI"
        self.deck = Deck()
        self.players = []

    def start(self):
        """Starts the game"""
        player_name = input("Enter your name:")
        human = Player(player_name)
        ai = Intelligence("AI")
        self.players = [human, ai]
        self.deck.create()
        self.deck.shuffle()
        hands = self.deck.split()
        self.players[0].set_hand(CardHand(hands[0]))
        self.players[1].set_hand(CardHand(hands[1]))

        print(f"{human.get_name()} vs AI, The Game has started!")

    def pickmode(self):
        """allows player to pick a mode"""
        self.mode = "You against AI"
        print("Standard War card game")

    def cheat(self):
        """Display both players' hands and allow swapping one card.

        This helper is intended for testing. It shows each player's hand and
        lets the user swap a single card between the selected player and the
        opponent. Swapped-in cards are placed on top of each hand so they will
        be drawn next.
        """
        # Ensure players are initialized
        if not getattr(self, "players", None) or len(self.players) < 2:
            print("No active game or fewer than two players. Start a game first to use cheat().")
            return

        # Use the game's players list
        players = self.players

        # Display each player's hand with indices
        for i, p in enumerate(players):
            hand = p.get_hand()
            cards = hand.getHand() if hand is not None else []
            display = ", ".join(f"[{idx}] {str(c)}" for idx, c in enumerate(cards))
            print(f"{i+1}) {p.get_name()} - {len(cards)} cards: {display}")

        # Prompt for which player to act as (index or name)
        choice = input("Which player are you? Enter 1 or 2 (or player name): ").strip()
        src_idx = None
        if choice in ("1", "2"):
            src_idx = int(choice) - 1
        else:
            # Match by name
            for i, p in enumerate(players):
                if p.get_name() == choice:
                    src_idx = i
                    break

        if src_idx is None or src_idx not in (0, 1):
            print("Invalid player selection. Aborting cheat.")
            return

        tgt_idx = 1 - src_idx
        src_hand_obj = players[src_idx].get_hand()
        tgt_hand_obj = players[tgt_idx].get_hand()

        if src_hand_obj is None or tgt_hand_obj is None:
            print("One of the players does not have a hand. Aborting cheat.")
            return

        src_hand = src_hand_obj.getHand()
        tgt_hand = tgt_hand_obj.getHand()

        if not src_hand:
            print(f"{players[src_idx].get_name()} has no cards to swap.")
            return
        if not tgt_hand:
            print(f"{players[tgt_idx].get_name()} has no cards to swap.")
            return

        # Show detailed hands
        print(f"\nYour hand ({players[src_idx].get_name()}):")
        for i, c in enumerate(src_hand):
            print(f"  {i}: {c}")
        print(f"\nOpponent's hand ({players[tgt_idx].get_name()}):")
        for i, c in enumerate(tgt_hand):
            print(f"  {i}: {c}")

        try:
            s_index = int(input("Enter index of your card to give away: ").strip())
            t_index = int(input("Enter index of opponent's card to take: ").strip())
        except ValueError:
            print("Invalid index input. Aborting cheat.")
            return

        if s_index < 0 or s_index >= len(src_hand) or t_index < 0 or t_index >= len(tgt_hand):
            print("Index out of range. Aborting cheat.")
            return

        # Swap the selected cards and place the taken cards on top
        s_card = src_hand.pop(s_index)
        t_card = tgt_hand.pop(t_index)

        src_hand.insert(0, t_card)
        tgt_hand.insert(0, s_card)

        print(f"Swapped your {s_card} with opponent's {t_card}. The taken cards were placed on top of each hand.")
        

    def draw_cards(self, war_pile=None):
        # Initialize war pile to keep cards on table for war rounds
        if war_pile is None:
            war_pile = []

        hand0 = self.players[0].get_hand()
        hand1 = self.players[1].get_hand()

        # Check if any player ran out of cards, game over condition
        if len(hand0.getHand()) == 0:
            print(f"{self.players[1].get_name()} wins the game! {self.players[0].get_name()} has no more cards.")
            return
        if len(hand1.getHand()) == 0:
            print(f"{self.players[0].get_name()} wins the game! {self.players[1].get_name()} has no more cards.")
            return

        # Each player draws a card
        card1 = hand0.drawcard()
        card2 = hand1.drawcard()

        print(f"{self.players[0].get_name()} played {card1}")
        print(f"{self.players[1].get_name()} played {card2}")

        # Put these cards on war pile
        war_pile.extend([card1, card2])

        # Compare card values using correct get_value() method
        if card1.get_value() > card2.get_value():
            print(f"{self.players[0].get_name()} wins the round and takes {len(war_pile)} cards.")
            # Fix: add each card using addCard instead of addcards
            for c in war_pile:
                hand0.addCard(c)
            war_pile.clear()
        elif card1.get_value() < card2.get_value():
            print(f"{self.players[1].get_name()} wins the round and takes {len(war_pile)} cards.")
            for c in war_pile:
                hand1.addCard(c)
            war_pile.clear()
        else:
            print("War! Players place one card face down and one card face up.")

            # Check if players have enough cards for war
            if len(hand0.getHand()) < 2:
                print(f"{self.players[0].get_name()} cannot continue war - loses!")
                for c in war_pile + hand0.getHand():
                    hand1.addCard(c)
                hand0.getHand().clear()
                return
            if len(hand1.getHand()) < 2:
                print(f"{self.players[1].get_name()} cannot continue war - loses!")
                for c in war_pile + hand1.getHand():
                    hand0.addCard(c)
                hand1.getHand().clear()
                return

            # Each player places one card face down (on war pile)
            war_pile.append(hand0.drawcard())
            war_pile.append(hand1.drawcard())

            # Recursively call draw_cards to determine who wins the war
            self.draw_cards(war_pile)

