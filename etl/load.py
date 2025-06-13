from pathlib import Path
import pandas as pd

PROCESSED_DIR = Path('data/processed')
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def save_summary(df: pd.DataFrame, filename: str) -> None:
    """Save processed data to CSV."""
    df.to_csv(PROCESSED_DIR / filename, index=False)
