import typer
from typing_extensions import Annotated

from components.choco.example import ChocoExample
from components.coinor.example import CoinORExample
from components.cplex.example import CplexExample
from components.gurobi.example import GurobiExample
from components.highs.example import HighsExample
from components.ortools.example import ORToolsExample
from components.scip.example import ScipExample
from components.xpress.example import XpressExample

app = typer.Typer(no_args_is_help=True)


@app.command(no_args_is_help=True)
def choco(
    choco_example: Annotated[
        ChocoExample, typer.Argument(help="The Choco example to run")
    ],
) -> None:
    """Run the Choco example EXAMPLE."""
    choco_example.run()


@app.command(no_args_is_help=True)
def coinor(
    coinor_example: Annotated[
        CoinORExample, typer.Argument(help="The COIN-OR example to run")
    ],
) -> None:
    """Run the COIN-OR example EXAMPLE."""
    coinor_example.run()


@app.command(no_args_is_help=True)
def cplex(
    cplex_example: Annotated[
        CplexExample, typer.Argument(help="The CPLEX example to run")
    ],
) -> None:
    """Run the CPLEX example EXAMPLE."""
    cplex_example.run()


@app.command(no_args_is_help=True)
def gurobi(
    gurobi_example: Annotated[
        GurobiExample, typer.Argument(help="The Gurobi example to run")
    ],
) -> None:
    """Run Gurobi example EXAMPLE."""
    gurobi_example.run()


@app.command(no_args_is_help=True)
def highs(
    highs_example: Annotated[
        HighsExample, typer.Argument(help="The HiGHS example to run")]
) -> None:
    """Run HiGHS example EXAMPLE."""
    highs_example.run()


@app.command(no_args_is_help=True)
def ortools(
    ortools_example: Annotated[
        ORToolsExample, typer.Argument(help="The OR-Tools example to run")
    ],
) -> None:
    """Run OR-Tools example EXAMPLE."""
    ortools_example.run()


@app.command(no_args_is_help=True)
def scip(
    scip_example: Annotated[
        ScipExample, typer.Argument(help="The SCIP example to run")
    ],
) -> None:
    """Run SCIP example EXAMPLE."""
    scip_example.run()


@app.command(no_args_is_help=True)
def xpress(
    xpress_example: Annotated[
        XpressExample, typer.Argument(help="The Xpress example to run")
    ],
) -> None:
    """Run Xpress example EXAMPLE."""
    xpress_example.run()


if __name__ == "__main__":
    app()
