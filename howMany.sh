#!/bin/bash

# Directory to be inspected
dir="."

# Loop through each item in the directory
for subdir in "$dir"/*; do
    if [ -d "$subdir" ]; then  # Check if it's a directory
        # Count the number of files in the directory
        count=$(find "$subdir" -type f | wc -l)
        # Print the directory name and the count of files
        echo "$(basename "$subdir"): $count files"
    fi
done

