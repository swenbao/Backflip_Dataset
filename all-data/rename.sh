#!/bin/zsh

# Loop through all files in the current directory
for file in *; do
    # Check if the file name starts with a specific prefix (emoji ✅ in this case)
    if [[ $file == ✅* ]]; then
        # Remove the prefix and convert the extension to lowercase
        new_name=$(echo "$file" | sed -E 's/^✅//' | tr '[:upper:]' '[:lower:]')

        # Rename the file
        mv "$file" "$new_name"
    fi
done

