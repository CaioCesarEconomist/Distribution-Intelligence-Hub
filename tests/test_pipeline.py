import pandas as pd
from pathlib import Path
from etl.run_pipeline import extract, transform


def test_transform():
    df = extract()
    summary = transform(df)
    assert not summary.empty
    assert 'state' in summary.columns
    assert summary['total exports'].dtype != object
