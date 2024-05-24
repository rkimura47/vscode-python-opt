import enum

from components.cplex import simple, twt1


class CplexExample(str, enum.Enum):
    simple = "simple"
    twt1 = "twt1"

    def run(self) -> None:
        match self:
            case CplexExample.simple:
                simple.run_example()
            case CplexExample.twt1:
                twt1.run_example()
            case _:
                raise ValueError(f"Unknown CPLEX example {self}")
