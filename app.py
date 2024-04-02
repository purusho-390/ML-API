import streamlit as st
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import json
from flask import Flask, request, jsonify
from flask_cors import CORS


model_path = "model_path"
class_names_path = "label_path"

@st.cache(allow_output_mutation=True)
def load_keras_model(model_path):
    model = load_model(model_path, compile=False)
    return model

@st.cache
def load_class_names(class_names_path):
    with open(class_names_path, "r") as file:
        class_names = file.readlines()
    return class_names

def preprocess_image(image):
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array
    return data

def predict_image(image, model, class_names):
    data = preprocess_image(image)
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index].strip()  
    confidence_score = float(prediction[0][index])
    return {"class": class_name, "confidence": confidence_score}

model = load_keras_model(model_path)
class_names = load_class_names(class_names_path)

@st.cache(allow_output_mutation=True)
def get_prediction(image):
    return predict_image(image, model, class_names)

@st.cache(allow_output_mutation=True)
def process_image(image):
    image = Image.open(image).convert("RGB")
    prediction = get_prediction(image)
    return prediction


app = Flask(__name__)
CORS(app)  

@app.route('/home', methods=['POST'])
def detect_image():
    uploaded_file = request.files['file']
    if uploaded_file is not None:
        prediction = process_image(uploaded_file)
        return jsonify(prediction)
    else:
        return jsonify({'error': 'No file uploaded'})

if __name__ == '__main__':
    # Run the Flask app without the reloader
    app.run(debug=True, use_reloader=False)
