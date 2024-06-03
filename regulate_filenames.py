import os
import re

def rename_files_in_directory(directory):
    """
    Process all files in the given directory to ensure their names are standardized.
    """
    for filename in os.listdir(directory):
        # Construct full file path
        old_path = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(old_path):
            continue

        # Split the filename into name and extension, and clean spaces
        name, extension = os.path.splitext(filename)
        clean_name = name.replace(" ", "")  # Remove spaces

        # Ensure the extension is in lower case
        clean_extension = extension.lower()

        # Normalize the basename to lower case and correct format
        clean_name = re.sub(r"(\d+)-([LlRr][EeIiFfGgHhTt]+)(_mirrored)?", lambda m: f"{m.group(1)}-{m.group(2).lower()}{m.group(3) if m.group(3) else ''}", clean_name)

        # Construct the new filename and its full path
        new_filename = f"{clean_name}{clean_extension}"
        new_path = os.path.join(directory, new_filename)

        # Rename the file if the new name is different from the old one
        if new_path != old_path:
            os.rename(old_path, new_path)
            print(f"Renamed '{old_path}' to '{new_path}'")

def main():
    # Directory containing the datasets
    base_dir = "."

    # Include the main data folder and all classification folders
    directories = [os.path.join(base_dir, 'all-data')] + [os.path.join(base_dir, f"{i}{suffix}") for i in range(7) for suffix in ['+', '-']]

    # Process each directory
    for directory in directories:
        print(f"Processing directory: {directory}")
        rename_files_in_directory(directory)

if __name__ == "__main__":
    main()
