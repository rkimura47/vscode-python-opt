import enum

from components.xpress import simple


class XpressExample(str, enum.Enum):
    simple = "simple"

    def run(self) -> None:
        match self:
            case XpressExample.simple:
                simple.run_example()
            case _:
                raise ValueError(f"Unknown Xpress example {self}")
