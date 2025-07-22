import os
import random
import shutil
from pathlib import Path

dataset_dir = Path("dataset_updated")
output_dir = Path("dataset_split")
split_ratio = 0.8

if output_dir.exists():
    shutil.rmtree(output_dir)
output_dir.mkdir(parents=True, exist_ok=True)

for brand_dir in dataset_dir.iterdir():
    if brand_dir.is_dir():
        images = list(brand_dir.glob("*"))
        random.shuffle(images)

        split_idx = int(len(images) * split_ratio)
        train_images = images[:split_idx]
        val_images = images[split_idx:]

        for split_name, split_images in [("train", train_images), ("val", val_images)]:
            target_dir = output_dir / split_name / brand_dir.name
            target_dir.mkdir(parents=True, exist_ok=True)

            for img in split_images:
                shutil.copy(img, target_dir / img.name)

print("Dataset split completed and saved in 'dataset_split'")