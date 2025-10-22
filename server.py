import subprocess
import os
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "File Search API",
        "endpoints": {
            "search": "/search/<filename>?directory=.",
            "copy": "/copy"
        }
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)