import enum

from components.coinor import simple


class CoinORExample(str, enum.Enum):
    simple = "simple"

    def run(self) -> None:
        match self:
            case CoinORExample.simple:
                simple.run_example()
            case _:
                raise ValueError(f"Unknown COIN-OR example {self}")
