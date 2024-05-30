#!/bin/bash

# Check if the directory argument is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <destination_directory>"
  exit 1
fi

# Set the destination directory
DEST_DIR="$1"

# Remove and copy the 39-right.mov file if it exists in the destination directory
if [ -f "$DEST_DIR/39-right.mp4" ]; then
  rm "$DEST_DIR/39-right.mp4"
  echo "Removed $DEST_DIR/39-right.mp4"
  cp ./all-data/39-right.mov "$DEST_DIR"
  echo "Copied ./all-data/39-right.mov to $DEST_DIR"
fi

# Remove and copy the 39-right_mirrored.mov file if it exists in the destination directory
if [ -f "$DEST_DIR/39-right_mirrored.mp4" ]; then
  rm "$DEST_DIR/39-right_mirrored.mp4"
  echo "Removed $DEST_DIR/39-right_mirrored.mp4"
  cp ./all-data/39-right_mirrored.mov "$DEST_DIR"
  echo "Copied ./all-data/39-right_mirrored.mov to $DEST_DIR"
fi

