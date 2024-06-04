import os
import argparse

def find_videos_starting_with_prefix(base_dir, prefix):
    """
    This function checks each folder from 0+ to 6- to see if there are any video files starting with the given prefix.
    """
    # Loop through problem numbers from 0 to 6
    for i in range(7):
        for suffix in ['+', '-']:
            dir_path = os.path.join(base_dir, f"{i}{suffix}")
            if not os.path.exists(dir_path):
                print(f"Directory {dir_path} not found. Skipping...")
                continue

            files = os.listdir(dir_path)
            # Check if any video file starts with the prefix
            filtered_files = [file for file in files if file.startswith(prefix) and (file.endswith('.mp4') or file.endswith('.mov'))]

            if filtered_files:
                print(f"Folder {dir_path} contains files starting with '{prefix}': {filtered_files}")

def main():
    parser = argparse.ArgumentParser(description="Check for video files starting with a specific prefix in specified folders.")
    parser.add_argument('base_dir', type=str, help="Path to the base directory containing all the data")
    parser.add_argument('prefix', type=str, help="The number prefix to check for in video filenames")

    args = parser.parse_args()
    
    find_videos_starting_with_prefix(args.base_dir, args.prefix)

if __name__ == "__main__":
    main()
