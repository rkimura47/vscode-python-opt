import pytest

from components.scip.example import ScipExample


@pytest.mark.parametrize("example_name", ["simple", "twt1", "golomb7"])
def test_scip_examples(example_name: str):
    getattr(ScipExample, example_name).run()
