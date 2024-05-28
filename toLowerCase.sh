#!/bin/bash

# The directory to be processed
directory="$1"

# Check if the directory argument is given
if [[ -z "$directory" ]]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

# Find all files and rename them to lowercase
find "$directory" -depth -type f | while IFS= read -r file; do
    dirname=$(dirname "$file")
    basename=$(basename "$file")
    lowercase=$(echo "$basename" | tr '[:upper:]' '[:lower:]')
    if [[ "$basename" != "$lowercase" ]]; then
        mv "$dirname/$basename" "$dirname/$lowercase"
    fi
done

echo "All files have been renamed to lowercase."

