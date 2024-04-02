# ML API Backend for Image Processing

This repository contains a Flask-based backend API for image processing tasks using a pre-trained Keras model. It allows users to upload images and receive predictions about the content of those images.

## Features

- **Image Detection**: Upload an image and receive predictions about its content.
- **Pre-trained Model**: Utilizes a pre-trained Keras model for image classification.
- **Streamlit Integration**: Includes a Streamlit-powered front end for local testing and visualization.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/ml-api-backend.git
    cd ml-api-backend
    ```

2. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask app:

    ```bash
    streamlit run app.py
    ```

## Usage

### API Endpoints

#### `POST /detection`

- **Description**: Perform image detection on the uploaded image.
- **Request Body**: Form data with the uploaded image file.
- **Response**: JSON object containing prediction results.

Example:

```bash
curl -X POST -F "file=@/path/to/your/image.jpg" http://localhost:5000/home

