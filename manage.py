import enum

import typer
from typing_extensions import Annotated

app = typer.Typer(no_args_is_help=True)


class CoinORExample(str, enum.Enum):
    simple = "simple"


@app.command(no_args_is_help=True)
def coinor(
    example: Annotated[
        CoinORExample, typer.Argument(help="The COIN-OR example to run")
    ],
) -> None:
    """Run the COIN-OR example EXAMPLE."""
    from components.coinor import simple

    match example:
        case CoinORExample.simple:
            simple.run_example()
        case _:
            raise ValueError(f"Unknown COIN-OR example {example}")


class CplexExample(str, enum.Enum):
    simple = "simple"
    twt1 = "twt1"


@app.command(no_args_is_help=True)
def cplex(
    example: Annotated[CplexExample, typer.Argument(help="The CPLEX example to run")],
) -> None:
    """Run the CPLEX example EXAMPLE."""
    from components.cplex import simple, twt1

    match example:
        case CplexExample.simple:
            simple.run_example()
        case CplexExample.twt1:
            twt1.run_example()
        case _:
            raise ValueError(f"Unknown CPLEX example {example}")


class GurobiExample(str, enum.Enum):
    golomb7 = "golomb7"
    golomb8 = "golomb8"
    golomb9 = "golomb9"
    simple = "simple"
    twt1 = "twt1"


@app.command(no_args_is_help=True)
def gurobi(
    example: Annotated[GurobiExample, typer.Argument(help="The Gurobi example to run")],
) -> None:
    """Run Gurobi example EXAMPLE."""
    from components.gurobi import golomb_ruler, simple, twt1

    match example:
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
            raise ValueError(f"Unknown Gurobi example {example}")


class ORToolsExample(str, enum.Enum):
    simple = "simple"


@app.command(no_args_is_help=True)
def ortools(
    example: Annotated[
        ORToolsExample, typer.Argument(help="The OR-Tools example to run")
    ],
) -> None:
    """Run OR-Tools example EXAMPLE."""
    from components.ortools import simple

    match example:
        case ORToolsExample.simple:
            simple.run_example()
        case _:
            raise ValueError(f"Unknown OR-Tools example {example}")


class ScipExample(str, enum.Enum):
    simple = "simple"


@app.command(no_args_is_help=True)
def scip(
    example: Annotated[ScipExample, typer.Argument(help="The SCIP example to run")],
) -> None:
    """Run SCIP example EXAMPLE."""
    from components.scip import simple

    match example:
        case ScipExample.simple:
            simple.run_example()
        case _:
            raise ValueError(f"Unknown SCIP example {example}")


class XpressExample(str, enum.Enum):
    simple = "simple"


@app.command(no_args_is_help=True)
def xpress(
    example: Annotated[XpressExample, typer.Argument(help="The Xpress example to run")],
) -> None:
    """Run Xpress example EXAMPLE."""
    from components.xpress import simple

    match example:
        case XpressExample.simple:
            simple.run_example()
        case _:
            raise ValueError(f"Unknown Xpress example {example}")


if __name__ == "__main__":
    app()
