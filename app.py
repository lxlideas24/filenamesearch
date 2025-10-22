import streamlit as st
import os
import shutil

# Import the search function from filesearch.py
from filesearch import search_files

def copy_files_to_folder(file_list, source_directory, destination_folder):
    """Copy files from file_list to destination_folder"""
    # Create destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)
    
    copied_files = []
    failed_files = []
    
    for file_path in file_list:
        try:
            # Get just the filename from the path
            filename = os.path.basename(file_path)
            destination_path = os.path.join(destination_folder, filename)
            
            # Copy the file
            shutil.copy2(file_path, destination_path)
            copied_files.append(filename)
        except Exception as e:
            failed_files.append((os.path.basename(file_path), str(e)))
    
    return copied_files, failed_files

def main():
    st.title("📁 File Search & Copy Application")
    st.markdown("Search for specific files and copy them to a destination folder")
    
    # Get user input
    st.subheader("1. File List")
    filenames_input = st.text_area("Enter filenames (one per line):", 
                                  help="Enter each filename on a new line")
    
    st.subheader("2. Search Directory")
    search_directory = st.text_input("Directory to search in:", ".", 
                                    help="Directory where to search for the files")
    
    st.subheader("3. Destination Folder")
    destination_folder = st.text_input("Destination folder for copied files:", 
                                      "copied_files", 
                                      help="Folder where found files will be copied to")
    
    # Add a search and copy button
    search_copy_button = st.button("🔍 Search & Copy Files")
    
    # Add some spacing
    st.markdown("---")
    
    # Perform search when button is clicked
    if search_copy_button:
        if not filenames_input.strip():
            st.warning("Please enter at least one filename to search for")
            return
            
        if not search_directory:
            search_directory = "."
            
        # Check if search directory exists
        if not os.path.exists(search_directory):
            st.error(f"Search directory '{search_directory}' does not exist")
            return
            
        # Parse filenames
        filenames = [f.strip() for f in filenames_input.strip().split('\n') if f.strip()]
        
        if not filenames:
            st.warning("No valid filenames found in the input")
            return
        
        st.info(f"Searching for {len(filenames)} files...")
        
        # Search for each file
        found_files = []
        missing_files = []
        
        for filename in filenames:
            matches = search_files(search_directory, filename)
            if matches:
                # If multiple matches found, use the first one
                found_files.extend(matches)
            else:
                missing_files.append(filename)
        
        # Display search results
        st.subheader("Search Results")
        if found_files:
            st.success(f"Found {len(found_files)} file(s):")
            for i, file_path in enumerate(found_files, 1):
                file_size = os.path.getsize(file_path)
                st.markdown(f"**{i}.** `{os.path.basename(file_path)}` ({file_size} bytes) - {file_path}")
        else:
            st.warning("No files were found")
            
        if missing_files:
            st.error(f"Missing {len(missing_files)} file(s):")
            for filename in missing_files:
                st.markdown(f"- `{filename}`")
        
        # Copy files if any were found
        if found_files:
            st.subheader("Copying Files")
            with st.spinner(f"Copying {len(found_files)} file(s) to '{destination_folder}'..."):
                copied_files, failed_files = copy_files_to_folder(found_files, search_directory, destination_folder)
            
            if copied_files:
                st.success(f"Successfully copied {len(copied_files)} file(s) to '{destination_folder}':")
                for filename in copied_files:
                    st.markdown(f"- `{filename}`")
                    
            if failed_files:
                st.error(f"Failed to copy {len(failed_files)} file(s):")
                for filename, error in failed_files:
                    st.markdown(f"- `{filename}`: {error}")

if __name__ == "__main__":
    main()