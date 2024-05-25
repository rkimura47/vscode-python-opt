import enum

from components.scip import golomb_ruler, simple


class ScipExample(str, enum.Enum):
    golomb7 = "golomb7"
    golomb8 = "golomb8"
    golomb9 = "golomb9"
    simple = "simple"

    def run(self) -> None:
        match self:
            case ScipExample.golomb7:
                golomb_ruler.run_example(L=25, n=7)
            case ScipExample.golomb8:
                golomb_ruler.run_example(L=34, n=8)
            case ScipExample.golomb9:
                golomb_ruler.run_example(L=44, n=9)
            case ScipExample.simple:
                simple.run_example()
            case _:
                raise ValueError(f"Unknown SCIP example {self}")
