import os
import shutil

def delete_extracted_frame_folders(directory):
    # List all items in the directory
    items = os.listdir(directory)
    for item in items:
        # Full path of the item
        item_path = os.path.join(directory, item)
        # Check if the item is a directory and follows the naming convention for frame folders
        if os.path.isdir(item_path) and item.endswith('_frames'):
            try:
                # Remove the directory and all its contents
                shutil.rmtree(item_path)
                print(f"Deleted folder: {item_path}")
            except Exception as e:
                print(f"Failed to delete {item_path}: {e}")

# Directory containing all the video-derived frame folders
video_directory = './all-data/'
delete_extracted_frame_folders(video_directory)

