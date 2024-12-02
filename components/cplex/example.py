import enum

from components.cplex import golomb_ruler, golomb_ruler_cpo, simple, twt1


class CplexExample(str, enum.Enum):
    golomb6 = "golomb6"
    golomb7 = "golomb7"
    golomb8 = "golomb8"
    golomb9_cpo = "golomb9_cpo"
    golomb10_cpo = "golomb10_cpo"
    golomb11_cpo = "golomb11_cpo"
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
            case CplexExample.golomb9_cpo:
                golomb_ruler_cpo.run_example(L=44, n=9)
            case CplexExample.golomb10_cpo:
                golomb_ruler_cpo.run_example(L=55, n=10)
            case CplexExample.golomb11_cpo:
                golomb_ruler_cpo.run_example(L=72, n=11)
            case CplexExample.simple:
                simple.run_example()
            case CplexExample.twt1:
                twt1.run_example()
            case _:
                raise ValueError(f"Unknown CPLEX example {self}")
