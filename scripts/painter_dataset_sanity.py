# standard library

# third-party
from kagglehub.exceptions import UnauthenticatedError

# local
from painter_dataset_config import DATASET_FORMAT
from painter_dataset_helpers import (
    build_dataset_overview,
    load_datasets,
    validate_dataset_structure,
)


def main():
    # Load/download dataset
    try:
        datasets = load_datasets()
    except (UnauthenticatedError, RuntimeError) as e:
        raise RuntimeError(f"Dataset loading failed: {e}") from e

    # Validate dataset integrity/structure
    try:
        validate_dataset_structure()
    except ValueError as e:
        raise ValueError(f"Dataset structure validation failed: {e}") from e

    # Summarize dataset
    overview = build_dataset_overview(datasets)
    for name, details in overview.items():
        print(f"{name}: {details['file_count']:,} files — {details['path']}")

    if DATASET_FORMAT not in ("jpg", "tfrec"):
        raise ValueError(f"Unsupported dataset format: {DATASET_FORMAT!r}; expected 'jpg' or 'tfrec'.")

    print(f"\nConfigured dataset format: {DATASET_FORMAT}")
    for name in ("monet", "photo"):
        print(f"Selected {name} folder: {datasets[f'{name}_{DATASET_FORMAT}']}")


if __name__ == "__main__":
    main()
