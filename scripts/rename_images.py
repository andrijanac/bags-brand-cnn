import os

root = "dataset_updated"

for brand in os.listdir(root):
    brand_path = os.path.join(root, brand)
    if not os.path.isdir(brand_path):
        continue

    count = 1
    for filename in sorted(os.listdir(brand_path)):
        old_path = os.path.join(brand_path, filename)
        ext = os.path.splitext(filename)[1].lower()
        if ext not in [".jpg", ".jpeg", ".png"]:
            continue

        new_filename = f"{brand}_{count:03d}.jpg"
        new_path = os.path.join(brand_path, new_filename)
        os.rename(old_path, new_path)
        count += 1

print("Images renamed successfully.")