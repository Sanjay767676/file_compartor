# app.py
import os
from flask import Flask, render_template, request
from utils import extract_text_from_file, compare_texts, get_differences

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare():
    file1 = request.files.get('file1')
    file2 = request.files.get('file2')
    
    if not file1 or not file2:
        return "Please upload two files", 400

    # Save files to the upload folder
    file1_path = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
    file2_path = os.path.join(app.config['UPLOAD_FOLDER'], file2.filename)
    file1.save(file1_path)
    file2.save(file2_path)
    
    try:
        text1 = extract_text_from_file(file1_path)
        text2 = extract_text_from_file(file2_path)
        print("Extracted Text from File 1:\n", text1)
        print("Extracted Text from File 2:\n", text2)
    except Exception as e:
        return f"Error extracting text: {str(e)}", 500
    
    similarity = compare_texts(text1, text2)
    differences = get_differences(text1, text2)
    
    return render_template('result.html', similarity=similarity, differences=differences)

if __name__ == '__main__':
    app.run(debug=True)
