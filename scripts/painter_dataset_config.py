# standard library
from pathlib import Path

# third-party

# local

# constants
COMPETITION = "gan-getting-started"
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data" / "raw"
DATASET_FORMAT = "jpg"  # "jpg" or "tfrec"
EXPECTED_DATASETS = {
    "monet_jpg": 300,
    "photo_jpg": 7038,
    "monet_tfrec": 5,
    "photo_tfrec": 20,
}
