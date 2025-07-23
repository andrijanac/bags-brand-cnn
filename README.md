# Handbag Brand Classifier (CNN Project)

A simple image classification project using Convolutional Neural Networks (CNN) to classify handbag images into three brands: **Jacquemus**, **Longchamp**, and **Themoire**.

---

## Project Goal

The goal of this project is to better understand how image classification works using neural networks. Through this process, I’m creating and organizing my own dataset of handbag images, training a model to recognize three different brands, and tracking how the model improves over time during training.

---

## Project Structure

This section describes the structure of files and folders used throughout the project:

```
bags-brand-cnn/
├── dataset/
│   ├── jacquemus/
│   ├── longchamp/
│   └── themoire/
├── dataset_updated/    
│   ├── jacquemus/
│   ├── longchamp/
│   └── themoire/
├── dataset_split/       
│   ├── train/
│   │   ├── jacquemus/
│   │   ├── longchamp/
│   │   └── themoire/
│   └── val/
│       ├── jacquemus/
│       ├── longchamp/
│       └── themoire/
├── scripts/            
│   ├── convert_to_jpg.py
│   ├── resize_images.py
│   ├── rename_images.py
│   ├── split_dataset.py
│   └── train_model.py
├── handbag_brand_classifier.keras  
├── README.md          
└── venv/                
```

---

## Step-by-Step Process

### 1. Convert to JPG

**Script:** `convert_to_jpg.py`

* Converts all images in `dataset/` to `.jpg` format  
* Saves the converted images into a new folder: `dataset_updated/`  
* Maintains the original folder structure by brand

### 2. Rename Images

**Script:** `rename_images.py`

* Renames all images in `dataset_updated/` using a consistent format, such as `brand_001.jpg`, `brand_002.jpg`, etc.  
* Helps standardize filenames for easier processing in later steps

### 3. Resize Images

**Script:** `resize_images.py`

* Resizes all images in `dataset_updated/` to 224x224 pixels  
* Overwrites the original files with resized versions, keeping the existing folder structure

### 4. Split Dataset

**Script:** `split_dataset.py`

* Splits the contents of `dataset_updated/` into training and validation sets  
* Saves the result in a new folder: `dataset_split/`, with `train/` and `val/` subfolders  
* Uses an 80/20 split ratio by default

### 5. Train the Model

**Script:** `train_model.py`

* Loads images from `dataset_split/train/` and `dataset_split/val/`  
* Builds and trains a simple Convolutional Neural Network (CNN) using TensorFlow and Keras  
* Saves the trained model as `handbag_brand_classifier.keras` for future use

---

## Model Performance

Trained for **10 epochs**. Below is the validation accuracy per epoch:

```text
Epoch 1: val_accuracy = 0.4583
Epoch 2: val_accuracy = 0.6667
Epoch 3: val_accuracy = 0.5833
Epoch 4: val_accuracy = 0.5833
Epoch 5: val_accuracy = 0.8333
Epoch 6: val_accuracy = 0.8333
Epoch 7: val_accuracy = 0.9583
Epoch 8: val_accuracy = 0.9583
Epoch 9: val_accuracy = 0.9167
Epoch 10: val_accuracy = 1.0000
```
### Training Output Screenshot

Below is a screenshot of the model training log showing accuracy and loss values across all 10 epochs.

<img width="1033" height="434" alt="image" src="https://github.com/user-attachments/assets/c91e3eb5-6133-4419-8f1b-9228f6783a4d" />

---

## How to Run the Project

To run the full pipeline from dataset preparation to model training, follow the steps below.  
Make sure you are in the **root folder** of the project before running the scripts.

### 1. Run preprocessing scripts (in order)

```bash
python3 scripts/convert_to_jpg.py
python3 scripts/rename_images.py
python3 scripts/resize_images.py
python3 scripts/split_dataset.py
```
These scripts will convert images to .jpg, rename them in a consistent format, resize them to 224x224, and split the dataset into training and validation sets.

### 2. Create and activate a virtual environment

```bash
python3.10 -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install required libraries

```bash
pip install tensorflow
pip install Pillow
```

### 4. Train the model

```bash
python3 scripts/train_model.py
```
---

## Conclusion

This project provided hands-on experience with building a basic image classification pipeline using neural networks. Through dataset preparation, model training, and evaluation, I gained a clearer understanding of each step in the process. The final model reached 100% validation accuracy, which suggests high performance on the given dataset, though further testing on unseen data would be needed for real-world validation.

## Author

Andrijana Čanić, 2025
