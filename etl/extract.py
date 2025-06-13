from pathlib import Path
import pandas as pd
import yaml

RAW_DIR = Path('data/raw')
CONFIG_FILE = Path('src/config/config.yaml')


def load_config(path: Path = CONFIG_FILE) -> dict:
    """Load YAML configuration file."""
    with open(path) as cfg_file:
        return yaml.safe_load(cfg_file)


def load_raw_data(filename: str) -> pd.DataFrame:
    """Read raw CSV file from the raw data directory."""
    return pd.read_csv(RAW_DIR / filename)
