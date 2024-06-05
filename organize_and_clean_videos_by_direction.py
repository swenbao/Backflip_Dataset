import os
import shutil
import argparse

def clean_directory(directory):
    """
    Remove all files in the specified directory to clean it before new files are copied.
    """
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Removed {file_path}")

def organize_videos(base_dir):
    """
    Organizes video files into 'left' and 'right' directories based on specific naming patterns,
    and cleans these directories before moving new files in.
    """
    # Loop through the classification directories
    for i in range(7):
        for suffix in ['+', '-']:
            dir_path = os.path.join(base_dir, f"{i}{suffix}")
            if not os.path.exists(dir_path):
                print(f"Directory {dir_path} not found. Skipping...")
                continue

            # Prepare 'left' and 'right' directories
            left_dir = os.path.join(dir_path, 'left')
            right_dir = os.path.join(dir_path, 'right')
            os.makedirs(left_dir, exist_ok=True)
            os.makedirs(right_dir, exist_ok=True)

            # Clean directories before copying new files
            clean_directory(left_dir)
            clean_directory(right_dir)

            # Check each file in the directory
            for file in os.listdir(dir_path):
                if os.path.isdir(os.path.join(dir_path, file)):
                    continue  # Skip subdirectories
                file_path = os.path.join(dir_path, file)

                # Determine the correct directory based on the file name
                if 'left_mirrored' in file:
                    shutil.copy(file_path, right_dir)
                    print(f"Copied {file} to {right_dir}")
                elif 'right_mirrored' in file:
                    shutil.copy(file_path, left_dir)
                    print(f"Copied {file} to {left_dir}")
                elif 'left' in file and 'left_mirrored' not in file:
                    shutil.copy(file_path, left_dir)
                    print(f"Copied {file} to {left_dir}")
                elif 'right' in file and 'right_mirrored' not in file:
                    shutil.copy(file_path, right_dir)
                    print(f"Copied {file} to {right_dir}")

def main():
    parser = argparse.ArgumentParser(description="Organize videos into 'left' and 'right' directories based on naming patterns and clean directories first.")
    parser.add_argument('base_dir', type=str, help="Path to the base directory containing the folders 0+ to 6-")

    args = parser.parse_args()

    organize_videos(args.base_dir)

if __name__ == "__main__":
    main()

