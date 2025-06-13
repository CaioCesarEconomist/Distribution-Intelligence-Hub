import pandas as pd
import yaml
from pathlib import Path

RAW_DIR = Path('data/raw')
PROCESSED_DIR = Path('data/processed')
CONFIG_FILE = Path('src/config/config.yaml')
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

with open(CONFIG_FILE) as cfg_file:
    cfg = yaml.safe_load(cfg_file)

RAW_FILE = RAW_DIR / cfg.get('raw_file', 'sample_sales.csv')
PROCESSED_FILE = PROCESSED_DIR / cfg.get('processed_file', 'sales_summary.csv')


def extract() -> pd.DataFrame:
    """Load raw sales data."""
    return pd.read_csv(RAW_FILE)


def transform(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate sales by state and compute total exports."""
    summary = df.groupby('state')['total exports'].sum().reset_index()
    summary = summary.sort_values('total exports', ascending=False)
    return summary


def load(df: pd.DataFrame) -> None:
    """Save transformed data."""
    df.to_csv(PROCESSED_FILE, index=False)


def main() -> None:
    data = extract()
    summary = transform(data)
    load(summary)
    print(f"Pipeline complete. Output: {PROCESSED_FILE}")


if __name__ == '__main__':
    main()
