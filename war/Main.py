"""Application entrypoint module.

Provides a tiny Main wrapper that launches the Shell CLI. Kept minimal so it
is safe to import in tests without side-effects.
"""

try: #Try imports for executing Main normally
    from Shell import Shell
except: #Except imports for UnitTesting. To prevent module not found Error.
    from .Shell import Shell


class Main:
    """Minimal application wrapper that launches the Shell CLI."""

    def run(self):
        """Run the main program by starting the Shell command loop."""

        Shell().cmdloop()


if __name__ == "__main__":
    Main().run()