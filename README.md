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
    streamlit app.py
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


Model Details
The image detection model used in this project is a pre-trained Keras model. The model is trained on a dataset of various image classes and can predict the content of images with a certain level of accuracy.

Contributing
Contributions are welcome! Please feel free to open issues or submit pull requests.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
This project is inspired by the need for a simple yet powerful API backend for image processing tasks.
Special thanks to the creators and contributors of Flask, Streamlit, Keras, and other libraries used in this project.