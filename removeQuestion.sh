#!/bin/bash

# Define the directory to search in
directory="$1"

# Check if the directory argument is given
if [[ -z "$directory" ]]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

# File to store the paths of affected files
log_file="affected_filenames.txt"

# Check for files with '❓' in their names and process them
find "$directory" -type f -name '*❓*' | while IFS= read -r file; do
    echo "$file" >> "$log_file"  # Log the file path
    new_name=$(echo "$file" | tr -d '❓')  # Create a new filename by removing '❓'
    mv "$file" "$new_name"  # Rename the file
done

echo "Processing complete. Check '$log_file' for the list of affected files."

