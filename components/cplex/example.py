import enum

from components.cplex import golomb_ruler, simple, twt1


class CplexExample(str, enum.Enum):
    golomb6 = "golomb6"
    golomb7 = "golomb7"
    golomb8 = "golomb8"
    simple = "simple"
    twt1 = "twt1"

    def run(self) -> None:
        match self:
            case CplexExample.golomb6:
                golomb_ruler.run_example(L=17, n=6)
            case CplexExample.golomb7:
                golomb_ruler.run_example(L=25, n=7)
            case CplexExample.golomb8:
                golomb_ruler.run_example(L=34, n=8)
            case CplexExample.simple:
                simple.run_example()
            case CplexExample.twt1:
                twt1.run_example()
            case _:
                raise ValueError(f"Unknown CPLEX example {self}")
