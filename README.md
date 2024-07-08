# Image Processor

A web application built with Flask that allows users to remove backgrounds from images and convert images between various formats (PNG, JPG, JPEG, SVG). The application uses `rembg` for background removal and `Pillow` for image processing, providing a user-friendly interface for seamless image transformations.

## Features
1. Remove background from images (PNG, JPG, JPEG)
2. Convert images to various formats (PNG, JPG, JPEG)

## Installation
1. Clone the repository:
    ```bash
    git clone [repo link]
    ```
2.  ```bash
    docker build -t imgprocessor:1.0 .
    ```
3.  ```bash
    docker run -p 5100:5100 imgprocessor:1.0
    ```

## Usage
1. Navigate to `http://localhost:5100` in your web browser.
2. Drag and drop an image or click to select a file.
3. Choose the desired action (remove background or convert format) and select the target format if converting.
4. Click "Process Image" to upload and process your image.
5. Download the processed image from the link provided.
