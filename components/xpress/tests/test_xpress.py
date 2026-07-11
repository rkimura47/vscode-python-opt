import pytest

from components.xpress.example import XpressExample


@pytest.mark.parametrize("example_name", ["simple", "twt1", "golomb7"])
def test_xpress_examples(example_name: str):
    getattr(XpressExample, example_name).run()
