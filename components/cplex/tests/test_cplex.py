import pytest

from components.cplex.example import CplexExample


@pytest.mark.parametrize(
    "example_name", ["simple", "twt1", "golomb6", "golomb9_cpo"]
)
def test_cplex_examples(example_name: str):
    getattr(CplexExample, example_name).run()
