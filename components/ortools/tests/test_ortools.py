import pytest

from components.ortools.example import ORToolsExample


@pytest.mark.parametrize(
    "example_name", ["simple", "twt1", "golomb7", "golomb9_cpsat"]
)
def test_ortools_examples(example_name: str):
    getattr(ORToolsExample, example_name).run()
