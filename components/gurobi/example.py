import enum

from components.gurobi import golomb_ruler, simple, twt1


class GurobiExample(str, enum.Enum):
    golomb7 = "golomb7"
    golomb8 = "golomb8"
    golomb9 = "golomb9"
    simple = "simple"
    twt1 = "twt1"

    def run(self) -> None:
        match self:
            case GurobiExample.golomb7:
                golomb_ruler.run_example(L=25, n=7)
            case GurobiExample.golomb8:
                golomb_ruler.run_example(L=34, n=8)
            case GurobiExample.golomb9:
                golomb_ruler.run_example(L=44, n=9)
            case GurobiExample.simple:
                simple.run_example()
            case GurobiExample.twt1:
                twt1.run_example()
            case _:
                raise ValueError(f"Unknown Gurobi example {self}")
