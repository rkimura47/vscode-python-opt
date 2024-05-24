import enum

from components.scip import simple


class ScipExample(str, enum.Enum):
    simple = "simple"

    def run(self) -> None:
        match self:
            case ScipExample.simple:
                simple.run_example()
            case _:
                raise ValueError(f"Unknown SCIP example {self}")
