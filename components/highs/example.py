import enum

from components.highs import golomb_ruler, simple, twt1


class HighsExample(str, enum.Enum):
    golomb7 = "golomb7"
    golomb8 = "golomb8"
    golomb9 = "golomb9"
    simple = "simple"
    twt1 = "twt1"

    def run(self) -> None:
        match self:
            case HighsExample.golomb7:
                golomb_ruler.run_example(L=25, n=7)
            case HighsExample.golomb8:
                golomb_ruler.run_example(L=34, n=8)
            case HighsExample.golomb9:
                response = input(
                    "Warning: This example usually takes 2.5 - 3 minutes to solve, "
                    "during which HiGHS cannot be interrupted. Enter y to continue: "
                )
                if response == "y":
                    golomb_ruler.run_example(L=44, n=9)
            case HighsExample.simple:
                simple.run_example()
            case HighsExample.twt1:
                twt1.run_example()
            case _:
                raise ValueError(f"Unknown HiGHS example {self}")
