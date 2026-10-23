"""Inference utilities for the authors' unchanged style_monet generator."""

# standard library
import hashlib
from pathlib import Path
from urllib.request import urlretrieve

# third-party
import numpy as np
from PIL import Image
import torch
from torch import nn

# local
from cyclegan_generator import ResnetGenerator


CHECKPOINT_URL = "https://efrosgans.eecs.berkeley.edu/cyclegan/pretrained_models/style_monet.pth"


def load_pretrained_generator(checkpoint_path, device):
    """Load pretrained parameters strictly, omitting obsolete InstanceNorm buffers."""
    checkpoint_path = Path(checkpoint_path)
    if not checkpoint_path.exists():
        checkpoint_path.parent.mkdir(parents=True, exist_ok=True)
        temporary_path = checkpoint_path.with_suffix(".download")
        urlretrieve(CHECKPOINT_URL, temporary_path)
        temporary_path.replace(checkpoint_path)

    generator = ResnetGenerator(3, 3, ngf=64, norm_layer=nn.InstanceNorm2d, n_blocks=9)
    state = torch.load(checkpoint_path, map_location="cpu", weights_only=True)
    expected = generator.state_dict()
    # Older checkpoints contain InstanceNorm statistics unused by this architecture.
    obsolete = [key for key in state if key not in expected]
    for key in obsolete:
        module_name, buffer_name = key.rsplit(".", 1)
        module = generator.get_submodule(module_name)
        if not isinstance(module, nn.InstanceNorm2d) or buffer_name not in (
            "running_mean", "running_var", "num_batches_tracked"
        ):
            raise ValueError(f"Unexpected checkpoint entry: {key}")
        del state[key]
    generator.load_state_dict(state, strict=True)
    generator.requires_grad_(False)
    generator.eval()
    generator.to(device)
    print(f"Loaded {len(state)} parameter tensors; omitted {len(obsolete)} legacy buffers.")
    print(f"Checkpoint SHA256: {hashlib.sha256(checkpoint_path.read_bytes()).hexdigest()}")
    return generator


def translate_photo(generator, image_path, device):
    """Translate one RGB photo to a 256×256 RGB painting without augmentation."""
    with Image.open(image_path) as image:
        image = image.convert("RGB")
        if image.size != (256, 256):
            image = image.resize((256, 256), Image.Resampling.BICUBIC)
        pixels = np.asarray(image, dtype=np.float32) / 127.5 - 1.0
    tensor = torch.from_numpy(pixels.transpose(2, 0, 1).copy()).unsqueeze(0).to(device)
    with torch.inference_mode():
        result = generator(tensor)[0].cpu()
    if not torch.isfinite(result).all():
        raise ValueError(f"Nonfinite output for {image_path}")
    pixels = ((result.permute(1, 2, 0).numpy() + 1.0) * 127.5).clip(0, 255).astype(np.uint8)
    return Image.fromarray(pixels)
