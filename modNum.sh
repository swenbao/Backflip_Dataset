#!/bin/bash

# Check if a directory was provided as an argument
if [ -z "$1" ]; then
    echo "Please provide a directory path as an argument."
    exit 1
fi

# Define the directory to check from the first argument
DIRECTORY=$1

# Check if '232-right.mp4' exists and rename it
if [ -f "$DIRECTORY/232-right.mp4" ]; then
    mv "$DIRECTORY/232-right.mp4" "$DIRECTORY/205-right.mp4"
    echo "Renamed '232-right.mp4' to '205-right.mp4'"
else
    echo "'232-right.mp4' does not exist in the directory"
fi

# Check if '232-right_mirrored.mp4' exists and rename it
if [ -f "$DIRECTORY/232-right_mirrored.mp4" ]; then
    mv "$DIRECTORY/232-right_mirrored.mp4" "$DIRECTORY/205-right_mirrored.mp4"
    echo "Renamed '232-right_mirrored.mp4' to '205-right_mirrored.mp4'"
else
    echo "'232-right_mirrored.mp4' does not exist in the directory"
fi

