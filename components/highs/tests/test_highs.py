import pytest

from components.highs.example import HighsExample


@pytest.mark.parametrize("example_name", ["simple", "twt1", "golomb7"])
def test_highs_examples(example_name: str):
    getattr(HighsExample, example_name).run()
