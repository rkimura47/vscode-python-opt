import enum

from components.coinor import golomb_ruler, simple, twt1


class CoinORExample(str, enum.Enum):
    golomb7 = "golomb7"
    golomb8 = "golomb8"
    golomb9 = "golomb9"
    simple = "simple"
    twt1 = "twt1"

    def run(self) -> None:
        match self:
            case CoinORExample.golomb7:
                golomb_ruler.run_example(L=25, n=7)
            case CoinORExample.golomb8:
                golomb_ruler.run_example(L=34, n=8)
            case CoinORExample.golomb9:
                golomb_ruler.run_example(L=44, n=9)
            case CoinORExample.simple:
                simple.run_example()
            case CoinORExample.twt1:
                twt1.run_example()
            case _:
                raise ValueError(f"Unknown COIN-OR example {self}")
