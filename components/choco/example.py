import enum

from components.choco import golomb_ruler, simple, twt1

class ChocoExample(str, enum.Enum):
    golomb9 = "golomb9"
    golomb10 = "golomb10"
    golomb11 = "golomb11"
    simple = "simple"
    twt1 = "twt1"

    def run(self) -> None:
        match self:
            case ChocoExample.golomb9:
                golomb_ruler.run_example(L=44, n=9)
            case ChocoExample.golomb10:
                golomb_ruler.run_example(L=55, n=10)
            case ChocoExample.golomb11:
                golomb_ruler.run_example(L=72, n=11)
            case ChocoExample.simple:
                simple.run_example()
            case ChocoExample.twt1:
                twt1.run_example()
            case _:
                raise ValueError(f"Unknown Choco example {self}")
