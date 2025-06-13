import pandas as pd


def aggregate_sales(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate total exports per state and sort descending."""
    summary = df.groupby('state')['total exports'].sum().reset_index()
    return summary.sort_values('total exports', ascending=False)
