from PIL import Image
import os

brands = ["jacquemus", "longchamp", "themoire"]

input_dir = "dataset"
output_dir = "dataset_updated"

for brand in brands:
    input_folder = os.path.join(input_dir, brand)
    output_folder = os.path.join(output_dir, brand)
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)

        if not filename.lower().endswith(".jpg"):
            try:
                img = Image.open(input_path).convert("RGB")
                new_name = os.path.splitext(filename)[0] + ".jpg"
                output_path = os.path.join(output_folder, new_name)
                img.save(output_path, "JPEG")
                print(f"Converted: {filename} -> {new_name}")
            except Exception as e:
                print(f"Skipped: {filename} (error: {e})")