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
    docker run -p 80:5100 imgprocessor:1.0
    ```

## Usage
1. Navigate to `http://localhost:80` in your web browser.
2. Drag and drop an image or click to select a file.
3. Choose the desired action (remove background or convert format) and select the target format if converting.
4. Click "Process Image" to upload and process your image.
5. Download the processed image from the link provided.

## UI
![Screenshot 2024-07-17 220417](https://github.com/user-attachments/assets/34e9cafb-db9b-4a92-a5c3-8424dd31c412)
![Screenshot 2024-07-17 220408](https://github.com/user-attachments/assets/7911aa96-0267-4eac-8487-e130e911ba3d)
![Screenshot 2024-07-17 220329](https://github.com/user-attachments/assets/091deffa-0947-48fc-9296-ded37f8a6047)
