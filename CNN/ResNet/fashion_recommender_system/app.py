# 1️⃣ Import Libraries
import streamlit as st
import os
import numpy as np
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.preprocessing import image
from sklearn.metrics.pairwise import cosine_similarity
from PIL import Image

# 2️⃣ Load Pretrained ResNet50 (feature extractor)
model = ResNet50(weights='imagenet', include_top=False, pooling='avg')

# 3️⃣ Function to extract feature vector
def get_feature_vector(img):
    if isinstance(img, str):  # file path
        img = image.load_img(img, target_size=(224, 224))
    else:  # uploaded file
        img = Image.open(img).resize((224,224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    features = model.predict(x)
    return features.flatten()

# 4️⃣ Prepare Dataset Features (run once)
dataset_folder = "fashion_images/"
image_paths = [os.path.join(dataset_folder, f) for f in os.listdir(dataset_folder)]
feature_vectors = [get_feature_vector(p) for p in image_paths]
feature_vectors = np.array(feature_vectors)

# 5️⃣ Function to recommend similar images
def recommend_similar(query_img, feature_vectors, image_paths, top_n=5):
    query_vector = get_feature_vector(query_img)
    similarities = cosine_similarity([query_vector], feature_vectors)[0]
    top_indices = similarities.argsort()[-top_n:][::-1]
    return [image_paths[i] for i in top_indices]

# 6️⃣ Streamlit App UI
st.title("Fashion Recommendation System")
st.write("Upload a fashion image and get similar recommendations!")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    st.write("Finding similar items...")
    
    recommended_images = recommend_similar(uploaded_file, feature_vectors, image_paths, top_n=5)
    
    st.write("### Recommended Fashion Items")
    cols = st.columns(len(recommended_images))
    for col, img_path in zip(cols, recommended_images):
        col.image(img_path, use_column_width=True)
