import os
from flask import Flask, request, jsonify, send_from_directory
from filesearch import search_files
import shutil

app = Flask(__name__, static_folder='.')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/search')
def search():
    filename = request.args.get('filename')
    directory = request.args.get('directory', '.')
    
    if not filename:
        return jsonify({"error": "filename parameter is required"}), 400
    
    if not os.path.exists(directory):
        return jsonify({"error": f"Directory '{directory}' does not exist"}), 400
    
    matches = search_files(directory, filename)
    
    # Add file details to the response
    files_with_details = []
    for match in matches:
        try:
            stat = os.stat(match)
            files_with_details.append({
                "path": match,
                "name": os.path.basename(match),
                "size": stat.st_size,
                "modified": stat.st_mtime
            })
        except Exception as e:
            files_with_details.append({
                "path": match,
                "name": os.path.basename(match),
                "error": str(e)
            })
    
    return jsonify({
        "query": filename,
        "directory": os.path.abspath(directory),
        "count": len(matches),
        "files": files_with_details
    })

@app.route('/copy', methods=['POST'])
def copy_files():
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "JSON body is required"}), 400
    
    file_paths = data.get('file_paths', [])
    destination_folder = data.get('destination_folder', 'copied_files')
    
    if not file_paths:
        return jsonify({"error": "file_paths list is required"}), 400
    
    # Create destination folder
    os.makedirs(destination_folder, exist_ok=True)
    
    copied_files = []
    failed_files = []
    
    for file_path in file_paths:
        try:
            if os.path.exists(file_path):
                filename = os.path.basename(file_path)
                destination_path = os.path.join(destination_folder, filename)
                shutil.copy2(file_path, destination_path)
                copied_files.append(filename)
            else:
                failed_files.append({"file": file_path, "error": "File not found"})
        except Exception as e:
            failed_files.append({"file": file_path, "error": str(e)})
    
    return jsonify({
        "copied": copied_files,
        "failed": failed_files,
        "destination": os.path.abspath(destination_folder)
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)