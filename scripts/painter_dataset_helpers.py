# standard library

# third-party
import kagglehub
from kagglehub.exceptions import UnauthenticatedError

# local
from painter_dataset_config import COMPETITION, DATA_DIR, EXPECTED_DATASETS


def ensure_dataset_downloaded():
    """Ensure competition data is available locally."""
    try:
        validate_dataset_structure()
    except ValueError as e:
        # Failed structure validation falls through to the download attempt below.
        print(e)
        print("Proceeding to KaggleHub competition_download to handle the download attempt.")
    else:
        # All structure and file-count checks passed, so skip downloading.
        return

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    try:
        kagglehub.competition_download(COMPETITION, output_dir=str(DATA_DIR))
    except Exception:
        raise


def _normalize_downloaded_files():
    """Perform any required cleanup or normalization of the files."""
    pass


def load_datasets():
    """Download competition data and return all four dataset folder paths."""
    try:
        ensure_dataset_downloaded()
    except UnauthenticatedError as e:
        err_msg = f"\nError: {e}"
        instructions_msg = "\nKaggleHub failed to authenticate."
        instructions_msg += "\nPlease ensure you have a valid Kaggle API token."
        instructions_msg += "\nObtain a Kaggle API token from your Kaggle account settings."
        instructions_msg += "\nPlace token in default location: ~/.kaggle/access_token"
        instructions_msg += "\nFor more info, see: https://www.kaggle.com/docs/api"
        print(f"{err_msg}\n{instructions_msg}")

        exception_msg = "\nFailed to authenticate with Kaggle."
        raise UnauthenticatedError(exception_msg) from e
    except Exception as e:
        err_msg = "An error occurred while downloading or normalizing the dataset."
        print(f"{err_msg} - {e}")
        raise RuntimeError("Failed to download and normalize the dataset.") from e

    return {name: DATA_DIR / name for name in EXPECTED_DATASETS}


def validate_dataset_structure():
    """Check all competition folders and their expected file counts and formats."""
    discrepancies = []
    for directory, expected_count in EXPECTED_DATASETS.items():
        path = DATA_DIR / directory
        if not path.is_dir():
            discrepancies.append(f"{path}: expected directory is missing or is not a directory")
            continue

        suffix = "." + directory.rsplit("_", 1)[1]
        files = [entry for entry in path.iterdir() if entry.is_file()]
        matching_count = sum(entry.suffix.lower() == suffix for entry in files)
        if len(files) != expected_count or matching_count != expected_count:
            discrepancies.append(
                f"{path}: expected {expected_count} {suffix} files; "
                f"found {matching_count} matching files and {len(files)} total files"
            )

    if discrepancies:
        raise ValueError("Dataset structure mismatch:\n" + "\n".join(discrepancies))


def build_dataset_overview(datasets):
    """Summarize all competition folder paths and actual file counts."""
    return {
        name: {
            "path": datasets[name],
            "file_count": sum(entry.is_file() for entry in datasets[name].iterdir()),
        }
        for name in EXPECTED_DATASETS
    }
