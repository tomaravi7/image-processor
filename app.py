from flask import Flask, render_template, request, send_file, jsonify, url_for
from rembg import remove
from PIL import Image
from io import BytesIO
import os
import uuid
import shutil

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp'}
UPLOAD_FOLDER = 'static/uploads'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def convert_image(input_image, target_format):
    if input_image.mode == 'RGBA':
        background = Image.new('RGB', input_image.size, (255, 255, 255))
        background.paste(input_image, mask=input_image.split()[3])
        input_image = background

    if input_image.mode != 'RGB':
        input_image = input_image.convert('RGB')

    output = BytesIO()
    
    if target_format.upper() == 'PNG':
        input_image.save(output, format='PNG')
    elif target_format.upper() in ['JPG', 'JPEG']:
        input_image.save(output, format='JPEG', quality=95)
    else:
        raise ValueError(f"Unsupported target format: {target_format}")

    output.seek(0)
    return Image.open(output)

def clear_uploads_folder():
    for filename in os.listdir(UPLOAD_FOLDER):
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    clear_uploads_folder()

    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'status': 'error', 'message': 'No file part'}), 400
        
        file = request.files['file']
        action = request.form.get('action')
        new_extension = request.form.get('new_extension')
        
        if file.filename == '':
            return jsonify({'status': 'error', 'message': 'No selected file'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'status': 'error', 'message': 'Invalid file type. Allowed types are PNG, JPG, JPEG, WEBP'}), 400
        
        try:
            input_image = Image.open(file.stream)

            if action == 'remove_bg':
                output_image = remove(input_image, post_process_mask=True)
                target_format = 'png'  
            elif action == 'change_extension':
                if new_extension:
                    target_format = new_extension.lower()
                    if target_format != input_image.format.lower():
                        output_image = convert_image(input_image, target_format.upper())
                    else:
                        output_image = input_image
                else:
                    return jsonify({'status': 'error', 'message': 'New extension is required for conversion'}), 400
            else:
                return jsonify({'status': 'error', 'message': 'Invalid action'}), 400

            # Generate a unique filename
            filename = f"{str(uuid.uuid4())}.{target_format}"
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            output_image.save(filepath)
            
            image_url = url_for('static', filename=f'uploads/{filename}')
            return jsonify({'status': 'success', 'message': 'Image processed successfully', 'image_url': image_url})
        except Exception as e:
            app.logger.error(f"Error processing image: {str(e)}")
            return jsonify({'status': 'error', 'message': f"Error processing image: {str(e)}"}), 500
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5100)
