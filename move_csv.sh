#!/bin/zsh

# Define the base directory containing all relevant subfolders
base_dir="."

# Define the source directory for the CSV files
source_dir="${base_dir}/all-data"

# Define an array of target directories excluding the source directory
target_dirs=(Good 0+ 0- 1+ 1- 2+ 2- 3+ 3- 4+ 4- 5+ 5- 6+ 6-)

# Loop through each CSV file in the source directory
for csv in "${source_dir}"/*.csv; do
    # Extract the base name of the CSV file (without the extension)
    base_name=$(basename "$csv" .csv)
    echo ${base_name}
    # Loop through each target directory
    for dir in "${target_dirs[@]}"; do
        # Construct the full path to the target directory
        full_dir="${base_dir}/${dir}"

        # Check for video files with the same base name in the target directory
        if ls "${full_dir}/${base_name}".* 1> /dev/null 2>&1; then
            # If a matching video file is found, copy the CSV file to this directory
            echo "Matching video file found: ${base_name} in ${full_dir}"
	    cp "$csv" "${full_dir}/"
        fi
    done
done

