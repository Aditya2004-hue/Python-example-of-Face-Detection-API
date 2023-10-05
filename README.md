# Python-example-of-Face-Detection-API
Implementing face detection using API's 
# Face Detection using API

This project demonstrates how to perform face detection using an API. It sends an image to a remote server, receives face detection results, and displays the results on the image.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Code Explanation](#code-explanation)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Introduction

In this project, we provide a Python script that takes an input image, sends it to a specified API server, and receives face detection results. The code then displays the detected faces on the image, along with their confidence scores, bounding boxes, and landmarks.

This can be useful for various applications, including security systems, facial recognition, and image analysis, by utilizing an external face detection service via an API.

## Prerequisites

Before you can run this code, make sure you have the following:

1. **Python**: You need to have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Python Libraries**: You will need the following Python libraries, which you can install using pip:

   - `requests`: To make HTTP requests.
   - `json`: To handle JSON data.
   - `cv2` (OpenCV): For image processing.
   - `numpy`: For numerical operations.
   - `os`: For handling file operations.

   You can install these libraries using the following command:

   ```bash
   pip install requests opencv-python-headless numpy
   ```

3. **Input Image**: You should have an input image for face detection. Replace `"path of image"` in the code with the actual path to your image.

4. **API Server**: This code assumes that there is an API server running at a specified URL. Make sure the server is set up and running, and replace `"url of server"` with the actual URL of the API server.

## Getting Started

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/face-detection-using-api.git
   ```

2. Navigate to the project directory:

   ```bash
   cd face-detection-using-api
   ```

3. Open the Python script (`face_detection.py`) and replace the following placeholders:

   - `"path of image"` with the actual path to your input image.
   - `"url of server"` with the actual URL of the API server.
   - `"path to save the output image"` with the directory where you want to save the image with face detection results.

## Code Explanation

Here's a brief explanation of the code:

1. Load the input image using OpenCV.

2. Convert the image to a base64 string for sending it as JSON data in the API request.

3. Send a POST request to the API server with the image data.

4. If the API response is successful (HTTP status code 200), parse the response JSON and extract face detection information.

5. Draw bounding boxes around detected faces, display their confidence scores, and mark facial landmarks on the image using OpenCV.

6. Save the image with face detection results to the specified output directory.

7. Display the image with the face detection results.

## Usage

To run the code, execute the following command in your terminal:

```bash
python face_detection.py
```

This will send the input image to the API server, receive face detection results, display them on the image, and save the result in the specified output directory.

Feel free to customize the code and adapt it to your specific use case and API endpoints.

## Example

Here's how you can run the code with a sample image:

```bash
python face_detection.py
```

This will demonstrate the face detection process using the provided sample code.

## Contributing

Contributions to this project are welcome. You can open issues, fork the repository, and submit pull requests to contribute improvements or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code as per the license terms.
