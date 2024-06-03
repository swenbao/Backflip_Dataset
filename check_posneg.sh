#!/bin/bash

# Directory containing the classifications
dataset_dir="."

# Loop through each problem number
for i in {0..6}; do
    plus_folder="${dataset_dir}/${i}+"
    minus_folder="${dataset_dir}/${i}-"

    # Check if directories exist
    if [[ ! -d "$plus_folder" || ! -d "$minus_folder" ]]; then
        echo "Folder missing for problem $i, skipping..."
        continue
    fi

    # List all files in both folders and sort them
    plus_files=$(ls "$plus_folder")
    minus_files=$(ls "$minus_folder")

    # Use comm command to find common files
    duplicates=$(comm -12 <(echo "$plus_files" | sort) <(echo "$minus_files" | sort))

    # Check for duplicates and report
    if [[ -n $duplicates ]]; then
        echo "Duplicate videos found for problem $i:"
        echo "$duplicates"
    else
        echo "No duplicates found for problem $i."
    fi
done

