# File Search API

A lightweight file search API that can be deployed to Vercel.

## Features

- Search for files by name in any directory
- RESTful API for programmatic access
- Lightweight deployment package

## API Endpoints

### Search for files
```
GET /search?filename={filename}&directory={directory}
```

### Health check
```
GET /health
```

## Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python api.py
   ```

3. Open your browser to http://localhost:3000

## Deploying to Vercel

1. Create a new project in Vercel
2. Connect your Git repository
3. Import the `vercel-deploy` folder
4. Set the build command to `pip install -r requirements.txt`
5. Set the output directory to `.`
6. Deploy!

## Project Structure

- `api.py` - Main Flask application with API endpoints
- `filesearch.py` - Core file search functionality
- `requirements.txt` - Python dependencies
- `vercel.json` - Vercel deployment configuration

## Usage

1. Enter a list of filenames (one per line) in the text area
2. Specify the directory to search in
3. Specify the destination folder for copied files
4. Click "Search Files" to find the files
5. Click "Copy Files" to copy the found files to the destination folder# filenamesearch
