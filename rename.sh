#!/bin/zsh

# Loop through all files in the current directory
for file in *; do
    # Check if the file has an uppercase .MOV or .MP4 extension
    if [[ $file == *.MOV || $file == *.MP4 ]]; then
        # Extract the base name and convert the extension to lowercase
        base_name="${file%.*}"
        ext="${file##*.}"
        new_name="${base_name}.$(echo "$ext" | tr '[:upper:]' '[:lower:]')"

        # Rename the file
        mv "$file" "$new_name"
    fi
done

