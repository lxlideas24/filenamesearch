# File Search & Copy Tool

A web-based tool to search for files by name and copy them to a destination folder.

## Features

- Search for files by name in any directory
- Copy found files to a specified destination folder
- Web-based interface for easy use
- RESTful API for programmatic access

## Local Development

1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python api.py
   ```

4. Open your browser to http://localhost:3000

## API Endpoints

### Search for files
```
GET /search?filename={filename}&directory={directory}
```

### Copy files
```
POST /copy
{
  "file_paths": ["path/to/file1", "path/to/file2"],
  "destination_folder": "destination_folder_name"
}
```

## Deploying to Vercel

1. Install the Vercel CLI:
   ```bash
   npm install -g vercel
   ```

2. Login to your Vercel account:
   ```bash
   vercel login
   ```

3. Deploy the project:
   ```bash
   vercel
   ```

4. Follow the prompts to deploy to Vercel

## Project Structure

- `api.py` - Main Flask application with API endpoints
- `filesearch.py` - Core file search functionality
- `index.html` - Frontend interface
- `requirements.txt` - Python dependencies
- `vercel.json` - Vercel deployment configuration

## Usage

1. Enter a list of filenames (one per line) in the text area
2. Specify the directory to search in
3. Specify the destination folder for copied files
4. Click "Search Files" to find the files
5. Click "Copy Files" to copy the found files to the destination folder# filenamesearch
