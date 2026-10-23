# Model Implementation Options

<br>

## Overview
This table outlines possible approaches to the photo-to-Monet task at different levels of implementation and training. It serves as a planning reference, but not all notebooks are required. Therefore, some notebooks may be postponed.

<br>

| Notebook | Option | Reuses existing model implementation | Starts with pretrained weights | Trains on our data | Notes |
| --- | --- | --- | --- | --- | --- |
| [02 — Pretrained model](../notebooks/02_pre_trained_model.ipynb) | Pretrained inference | Yes | Yes | No | use pre-existing model that was pre-trained (as is) |
| [03 — Fine-tuned model](../notebooks/03_fine_tuned_model.ipynb) | Fine-tuning | Yes | Yes | Yes | use pre-existing model that was pre-trained but we do some fine-tuning|
| [04 — Train from Scratch](../notebooks/04_train_from_scratch_model.ipynb) | Train existing implementation from scratch | Yes | No | Yes | use pre-existing model that has not been trained at all and do the training ourselves |
| [05 — Bespoke model](../notebooks/05_bespoke_model.ipynb) | Write and train our own implementation | No | No | Yes | write a model ourselves (networks, losses, training loop, etc) and do the training ourselves |

