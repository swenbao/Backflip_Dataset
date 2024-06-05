import os
import argparse

def delete_videos(base_dir, prefix, log_file):
    """
    Deletes video files starting with the specified prefix in directories from 0+ to 6-,
    and logs their paths to a text file.
    """
    # Loop through the classification directories
    for i in range(7):
        for suffix in ['+', '-']:
            dir_path = os.path.join(base_dir, f"{i}{suffix}")
            if not os.path.exists(dir_path):
                print(f"Directory {dir_path} not found. Skipping...")
                continue

            print(f"Checking files in directory: {dir_path}")
            for file in os.listdir(dir_path):
                if file.startswith(prefix) and (file.endswith('.mp4') or file.endswith('.mov')):
                    file_path = os.path.join(dir_path, file)
                    os.remove(file_path)  # Delete the file
                    print(f"Deleted {file_path}")
                    # Log the deleted file path
                    with open(log_file, 'a') as log:
                        log.write(file_path + '\n')

def main():
    parser = argparse.ArgumentParser(description="Delete videos based on prefix and log deletions.")
    parser.add_argument('base_dir', type=str, help="Path to the base directory containing the folders 0+ to 6-")
    parser.add_argument('prefix', type=str, help="The number prefix of video filenames to delete")
    parser.add_argument('log_file', type=str, help="File path to log deleted video paths")

    args = parser.parse_args()

    delete_videos(args.base_dir, args.prefix, args.log_file)

if __name__ == "__main__":
    main()

