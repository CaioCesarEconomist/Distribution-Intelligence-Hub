from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))
import yaml
from etl.extract import load_config, load_raw_data
from etl.transform import aggregate_sales
from etl.load import save_summary

CONFIG_FILE = Path('src/config/config.yaml')


def main() -> None:
    config = load_config(CONFIG_FILE)
    raw_file = config.get('raw_file', 'sample_sales.csv')
    processed_file = config.get('processed_file', 'sales_summary.csv')

    df = load_raw_data(raw_file)
    summary = aggregate_sales(df)
    save_summary(summary, processed_file)
    print(f"Pipeline complete. Output: data/processed/{processed_file}")


if __name__ == "__main__":
    main()
