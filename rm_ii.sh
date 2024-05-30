#!/bin/bash

# Check if the directory argument is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <destination_directory>"
  exit 1
fi

# Set the destination directory
DEST_DIR="$1"

# Remove and copy the 39-right.mov file if it exists in the destination directory
if [ -f "$DEST_DIR/213-left.mov" ]; then
  rm "$DEST_DIR/213-left.mov"
  echo "Removed $DEST_DIR/213-left.mov"
  cp ./all-data/213-left.mov "$DEST_DIR"
  echo "Copied ./all-data/213-left.mov to $DEST_DIR"
fi

# Remove and copy the 39-right_mirrored.mov file if it exists in the destination directory
if [ -f "$DEST_DIR/213-left_mirrored.mov" ]; then
  rm "$DEST_DIR/213-left_mirrored.mov"
  echo "Removed $DEST_DIR/213-left_mirrored.mov"
  cp ./all-data/213-left_mirrored.mov "$DEST_DIR"
  echo "Copied ./all-data/213-left_mirrored.mov to $DEST_DIR"
fi

