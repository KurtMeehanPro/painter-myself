# I’m Something of a Painter Myself

## Overview

This project explores photo-to-Monet image translation for Kaggle’s [I’m Something of a Painter Myself](https://www.kaggle.com/competitions/gan-getting-started/) competition. The challenge is to generate 7,000–10,000 Monet-style images using generative adversarial networks (GANs). Our first baseline uses the original CycleGAN authors’ pretrained photo-to-Monet generator without training or fine-tuning.

Submissions are evaluated using [Memorization-informed Fréchet Inception Distance (MiFID)](https://www.kaggle.com/competitions/gan-getting-started/overview/evaluation), which compares generated images with real Monet paintings while accounting for training-image memorization. Lower scores are better.

## Results Summary

Image generation succeeds, but a Kaggle submission error currently prevents scoring. See [Kaggle submission issue](docs/kaggle-submission-deprecated-parameter.md).

## Documentation

- **Project README** — The project's top-level README, the document you're reading right now.
- [Model implementation options](docs/model_implementation_choices.md) — Compares pretrained inference, fine-tuning, training an existing implementation from scratch, and writing our own implementation.
- [Kaggle submission issue](docs/kaggle-submission-deprecated-parameter.md) — Documents the submission error preventing a competition score.

## Layout

- `data/raw/` contains competition files downloaded from Kaggle and is excluded from Git.
- `data/checkpoints/` contains downloaded pretrained model weights and is excluded from Git.
- `data/outputs/` contains generated image previews and output ZIPs and is excluded from Git.
- `docs/` — See the [Documentation](#documentation) section above.
- `notebooks/` contains numbered exploration, modeling, and Kaggle submission notebooks, including placeholder notebooks for possible training approaches.
- `scripts/` contains dataset helpers, model helpers, and the original authors’ generator code and license.
- `tests/` currently contains a placeholder for future tests.

## Setup

Use **Python 3.14.8** with [requirements.txt](requirements.txt). Install the packages:

```bash
python -m pip install -r requirements.txt
```

### Kaggle Authentication
Authenticate with Kaggle before downloading competition data. Generate an API token in your [Kaggle account settings](https://www.kaggle.com/settings/api) and save the token in `~/.kaggle/access_token`, as described in the [KaggleHub authentication instructions](https://github.com/Kaggle/kagglehub#authenticate). Accept the [competition rules](https://www.kaggle.com/competitions/gan-getting-started/rules) on Kaggle.

## Dataset sanity check

Run:

```bash
python scripts/painter_dataset_sanity.py
```

The script:

- reuses complete local data or attempts a KaggleHub download into `data/raw/`,
- verifies all four expected dataset folders, file counts, and file extensions,
- reports each folder's path and file count, the configured dataset format, and the selected Monet and photo folders.
