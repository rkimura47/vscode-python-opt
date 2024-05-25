import enum

from components.ortools import golomb_ruler, golomb_ruler_cpsat, simple


class ORToolsExample(str, enum.Enum):
    golomb7 = "golomb7"
    golomb8 = "golomb8"
    golomb9 = "golomb9"
    golomb9_cpsat = "golomb9_cpsat"
    golomb10_cpsat = "golomb10_cpsat"
    golomb11_cpsat = "golomb11_cpsat"
    simple = "simple"

    def run(self) -> None:
        match self:
            case ORToolsExample.golomb7:
                golomb_ruler.run_example(L=25, n=7)
            case ORToolsExample.golomb8:
                golomb_ruler.run_example(L=34, n=8)
            case ORToolsExample.golomb9:
                golomb_ruler.run_example(L=44, n=9)
            case ORToolsExample.golomb9_cpsat:
                golomb_ruler_cpsat.run_example(L=44, n=9)
            case ORToolsExample.golomb10_cpsat:
                golomb_ruler_cpsat.run_example(L=55, n=10)
            case ORToolsExample.golomb11_cpsat:
                golomb_ruler_cpsat.run_example(L=72, n=11)
            case ORToolsExample.simple:
                simple.run_example()
            case _:
                raise ValueError(f"Unknown OR-Tools example {self}")
