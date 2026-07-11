import pytest

from components.coinor.example import CoinORExample


@pytest.mark.parametrize("example_name", ["simple", "twt1", "golomb7"])
def test_coinor_examples(example_name: str):
    getattr(CoinORExample, example_name).run()
