# bank_data_generator/writer.py

import csv
import os
from typing import List, Dict
from utils.constants import OUTPUT_PATH


def write_to_csv(data: List[Dict[str, any]], filename: str, output_dir: str = OUTPUT_PATH) -> None:

    if not data:
        print(f"No data to write for {filename}.")
        return

    # Checks the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    keys = list(data[0].keys())
    filepath = os.path.join(output_dir, filename)

    with open(filepath, 'w', newline="", encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys, delimiter="|")
        writer.writeheader()
        writer.writerows(data)

    print(f"Data successfully written to {filepath}")
