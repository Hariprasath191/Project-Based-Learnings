AlexNet :
| Layer No. | Type            | Filters / Neurons            | Activation     | Purpose                |
| --------- | --------------- | ---------------------------- | -------------- | ---------------------- |
| 1         | Conv            | 96 filters (11×11, stride 4) | ReLU           | Detects edges & colors |
| 2         | Max Pool        | 3×3                          | -              | Reduces size           |
| 3         | Conv            | 256 filters (5×5)            | ReLU           | Detects textures       |
| 4         | Max Pool        | 3×3                          | -              |                        |
| 5         | Conv            | 384 filters (3×3)            | ReLU           | Detects shapes         |
| 6         | Conv            | 384 filters (3×3)            | ReLU           | Complex patterns       |
| 7         | Conv            | 256 filters (3×3)            | ReLU           | High-level abstraction |
| 8         | Max Pool        | 3×3                          | -              |                        |
| 9         | Flatten + FC    | 4096 neurons                 | ReLU + Dropout | Decision making        |
| 10        | Fully Connected | 4096 neurons                 | ReLU + Dropout |                        |
| 11        | Output Layer    | 1000 neurons                 | Softmax        | Final classification   |


# Real-Time Face Mask Detection using AlexNet

This project implements a **real-time face mask detection system** using the **AlexNet** Convolutional Neural Network. The system detects whether individuals are wearing masks through live webcam feed.

---

## Flow of Work

```
            Start
              |
              V
      [Collect Dataset]
              |
              |---> Folders: "mask", "without_mask" (and optionally more classes)
              |
              V
      [Preprocess Images]
              |
              |---> Resize to 224x224
              |---> Normalize pixels (0-1)
              |---> Data Augmentation (rotation, zoom, shear, flip)
              |
              V
    [Build AlexNet Model]
              |
              |---> Conv Layers → Feature Extraction
              |---> Fully Connected Layers → Classifier
              |---> Output Layer → Softmax (number of neurons = number of classes)
              |
              V
        [Train Model]
              |
              |---> Input: Training dataset
              |---> Validation: Validation dataset
              |---> Loss: Categorical Crossentropy
              |---> Optimizer: Adam
              |
              V
    [Save Trained Model]
              |
              V
  [Real-Time Face Detection]
              |
              |---> Capture Webcam Frame
              |---> Convert to Grayscale
              |---> Detect Faces using Haar Cascade
              |
              V
    [Face Preprocessing]
              |
              |---> Crop Face
              |---> Resize to 224x224
              |---> Normalize and Expand Dimensions
              |
              V
  [Prediction using AlexNet]
              |
              |---> Predict class: Mask / No Mask / Other
              |
              V
  [Display Results on Webcam]
              |
              |---> Draw Bounding Box + Label
              |
              V
    [Exit on 'q' key]
              |
              V
             End
```

---

## GitHub Repository

You can find the full project here: [AlexNet Face Mask Detection](https://github.com/Hariprasath191/Project-Based-Learnings/tree/main/CNN/AlexNet)

---

## Features

* Real-time face mask detection via webcam.
* Extendable to any number of classes by adding more folders.
* Built using **AlexNet**, **TensorFlow/Keras**, and **OpenCV**.
* Data augmentation applied for better generalization.

---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/Hariprasath191/Project-Based-Learnings.git
```

2. Navigate to the project folder:

```bash
cd Project-Based-Learnings/CNN/AlexNet
```

3. Install required dependencies:

```bash
pip install tensorflow opencv-python numpy matplotlib
```

4. Train the model using your dataset or load the pre-trained model.
5. Run the real-time detection script:

```bash
python real_time_mask_detection.py
```

Press **'q'** to exit the webcam feed.

---

## Notes

* Dataset should be organized in folders representing each class (e.g., `mask`, `without_mask`, `sunglasses`).
* The **last layer of AlexNet** should have neurons equal to the number of classes.
* Can be extended for any classification task with min
