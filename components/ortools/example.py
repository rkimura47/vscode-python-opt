import enum

from components.ortools import simple


class ORToolsExample(str, enum.Enum):
    simple = "simple"

    def run(self) -> None:
        match self:
            case ORToolsExample.simple:
                simple.run_example()
            case _:
                raise ValueError(f"Unknown OR-Tools example {self}")
