import pytest

from components.choco.example import ChocoExample


@pytest.mark.parametrize("example_name", ["simple", "twt1", "golomb9"])
def test_choco_examples(example_name: str):
    getattr(ChocoExample, example_name).run()
