"""Statistics model: stores per-game results and supports JSON serialization."""

from typing import Optional
import datetime


class Statistics:
    """Model representing the outcome of a single game.

    Fields:
    - has_won: bool
    - draws: int
    - date: Optional[datetime.date]
    """

    def __init__(
        self, has_won: bool = False, draws: int = 0, date: Optional[object] = None
    ):
        """Create a Statistics instance.

        `date` may be a datetime.date, an ISO date string, or None.
        """
        self.set_has_won(has_won)
        self.set_draws(draws)
        self.set_date(date)

    # string representation
    def __str__(self) -> str:
        return f"Match: {'Won' if self.get_has_won() else 'Lost'} | Draws: {self.get_draws()}"

    # setters
    def set_has_won(self, has_won: bool) -> bool:
        self.__has_won = bool(has_won)
        return self.__has_won

    def set_draws(self, draws: int) -> int:
        self.__draws = int(draws)
        return self.__draws

    def set_date(self, date: Optional[object]) -> Optional[datetime.date]:
        """Set the Statistics date from several accepted representations.

        Accepts a datetime.date, an ISO date string, or None and returns the
        stored datetime.date or None.
        """
        if date is None:
            self.__date = None
        else:
            if isinstance(date, datetime.date):
                self.__date = date
            elif isinstance(date, str):
                # parse ISO-format date string
                try:
                    self.__date = datetime.date.fromisoformat(date)
                except Exception:
                    # fallback: attempt to parse common formats via datetime
                    try:
                        self.__date = datetime.datetime.fromisoformat(date).date()
                    except Exception:
                        # last resort: do not convert, set None
                        self.__date = None
            else:
                # unknown type: try to coerce to date via isoformat if possible
                try:
                    self.__date = datetime.date(date)
                except Exception:
                    self.__date = None
        return self.__date

    # getters
    def get_has_won(self) -> bool:
        return getattr(self, "_Statistics__has_won", getattr(self, "__has_won", False))

    def get_draws(self) -> int:
        return getattr(self, "_Statistics__draws", getattr(self, "__draws", 0))

    def get_date(self) -> Optional[datetime.date]:
        return getattr(self, "_Statistics__date", getattr(self, "__date", None))

    # serialization helpers
    def to_dict(self) -> dict:
        """Return a JSON-serializable dict representation."""
        date = self.get_date()
        return {
            "has_won": self.get_has_won(),
            "draws": self.get_draws(),
            "date": date.isoformat() if date is not None else None,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Statistics":
        """Create a Statistics from a dict produced by to_dict()."""
        if not isinstance(data, dict):
            raise TypeError("from_dict expects a dict")
        date = data.get("date", None)
        if isinstance(date, str):
            try:
                date = datetime.date.fromisoformat(date)
            except Exception:
                date = None
        return cls(
            has_won=data.get("has_won", False), draws=data.get("draws", 0), date=date
        )
