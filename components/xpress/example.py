import enum

from components.xpress import golomb_ruler, simple, twt1


class XpressExample(str, enum.Enum):
    golomb7 = "golomb7"
    golomb8 = "golomb8"
    golomb9 = "golomb9"
    golomb11 = "golomb11"
    simple = "simple"
    twt1 = "twt1"

    def run(self) -> None:
        match self:
            case XpressExample.golomb7:
                golomb_ruler.run_example(L=25, n=7)
            case XpressExample.golomb8:
                golomb_ruler.run_example(L=34, n=8)
            case XpressExample.golomb9:
                golomb_ruler.run_example(L=44, n=9)
            case XpressExample.golomb11:
                golomb_ruler.run_example(L=72, n=11)
            case XpressExample.simple:
                simple.run_example()
            case XpressExample.twt1:
                twt1.run_example()
            case _:
                raise ValueError(f"Unknown Xpress example {self}")
