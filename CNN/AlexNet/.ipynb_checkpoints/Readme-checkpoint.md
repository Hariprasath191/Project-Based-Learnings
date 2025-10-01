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



Flow of Work : 

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
