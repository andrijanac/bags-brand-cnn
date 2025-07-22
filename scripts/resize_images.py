from PIL import Image
import os

root = "dataset_updated"
skipped = 0
processed = 0

for brand in os.listdir(root):
    brand_path = os.path.join(root, brand)
    if not os.path.isdir(brand_path):
        continue

    for file in os.listdir(brand_path):
        path = os.path.join(brand_path, file)
        try:
            img = Image.open(path)
            img = img.resize((224, 224))
            img.save(path)
            processed += 1
        except Exception as e:
            print(f"Skipping: {path} (error: {e})")
            skipped += 1

if skipped == 0:
    print(f"All {processed} images resized successfully.")
else:
    print(f"{processed} images resized successfully, {skipped} were skipped.")