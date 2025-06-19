import csv
from typing import List, Dict

def save_to_csv(filename: str, board_data: List[Dict[str, int]]):
    """Zapisuje listę pozycji statków jako CSV."""
    with open(filename, mode='w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['ship_id', 'row', 'col', 'horizontal'])
        writer.writeheader()
        writer.writerows(board_data)

def load_from_csv(filename: str) -> List[Dict[str, int]]:
    """Wczytuje pozycje statków z CSV."""
    with open(filename, mode='r', newline='') as f:
        reader = csv.DictReader(f)
        return [ {'ship_id': int(row['ship_id']),
                  'row': int(row['row']),
                  'col': int(row['col']),
                  'horizontal': row['horizontal'].lower() == 'true' }
                 for row in reader ]
