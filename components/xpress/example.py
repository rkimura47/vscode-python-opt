import enum

from components.xpress import golomb_ruler, simple


class XpressExample(str, enum.Enum):
    golomb7 = "golomb7"
    golomb8 = "golomb8"
    golomb9 = "golomb9"
    golomb12 = "golomb12"
    simple = "simple"

    def run(self) -> None:
        match self:
            case XpressExample.golomb7:
                golomb_ruler.run_example(L=25, n=7)
            case XpressExample.golomb8:
                golomb_ruler.run_example(L=34, n=8)
            case XpressExample.golomb9:
                golomb_ruler.run_example(L=44, n=9)
            case XpressExample.golomb12:
                golomb_ruler.run_example(L=85, n=12)
            case XpressExample.simple:
                simple.run_example()
            case _:
                raise ValueError(f"Unknown Xpress example {self}")
