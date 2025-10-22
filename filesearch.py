import os
import sys
import argparse

def search_files(directory, filename):
    """Search for files with the given name in the directory and subdirectories."""
    matches = []
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if filename.lower() in file.lower():
                matches.append(os.path.join(root, file))
    
    return matches

def main():
    parser = argparse.ArgumentParser(description='Search for files by name')
    parser.add_argument('filename', help='Name or partial name of the file to search for')
    parser.add_argument('--directory', '-d', default='.', 
                        help='Directory to search in (default: current directory)')
    
    args = parser.parse_args()
    
    print(f"Searching for '{args.filename}' in '{os.path.abspath(args.directory)}'...")
    
    matches = search_files(args.directory, args.filename)
    
    if matches:
        print(f"\nFound {len(matches)} match(es):")
        for match in matches:
            print(f"  {match}")
    else:
        print(f"\nNo files found matching '{args.filename}'")

if __name__ == "__main__":
    main()