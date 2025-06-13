from etl.extract import load_raw_data, load_config
from etl.transform import aggregate_sales


def test_aggregate_sales():
    cfg = load_config()
    df = load_raw_data(cfg.get('raw_file'))
    summary = aggregate_sales(df)
    assert not summary.empty
    assert 'state' in summary.columns
    assert summary['total exports'].dtype != object
