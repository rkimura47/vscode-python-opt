import pytest

from components.gurobi.example import GurobiExample


@pytest.mark.parametrize("example_name", ["simple", "twt1", "golomb7"])
def test_gurobi_examples(example_name: str):
    getattr(GurobiExample, example_name).run()
