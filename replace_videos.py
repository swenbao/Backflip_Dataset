import os
import shutil
import argparse

def replace_videos_with_all_data(base_dir, prefix):
    """
    This function copies video files from the 'all-data' directory to other specified directories
    if they start with the given prefix.
    """
    all_data_dir = os.path.join(base_dir, 'all-data')
    # Check and copy the relevant files to each directory
    for i in range(7):
        for suffix in ['+', '-']:
            target_dir = os.path.join(base_dir, f"{i}{suffix}")
            if not os.path.exists(target_dir):
                print(f"Directory {target_dir} not found. Skipping...")
                continue

            # Get all files in the all-data folder that start with the prefix
            all_data_files = [f for f in os.listdir(all_data_dir) if f.startswith(prefix) and (f.endswith('.mp4') or f.endswith('.mov'))]
            
            # Process each file
            for file in all_data_files:
                source_file = os.path.join(all_data_dir, file)
                destination_file = os.path.join(target_dir, file)
                
                # Check if file exists in the target directory before replacing
                if os.path.exists(destination_file):
                    # Copy the file from all-data to the target directory
                    shutil.copy2(source_file, destination_file)
                    print(f"Copied {file} to {target_dir}")
                else:
                    print(f"No need to replace {file} in {target_dir} as it does not exist there.")

def main():
    parser = argparse.ArgumentParser(description="Replace video files with those from the all-data directory.")
    parser.add_argument('base_dir', type=str, help="Path to the base directory containing all the data")
    parser.add_argument('prefix', type=str, help="The number prefix of video filenames to replace")

    args = parser.parse_args()

    replace_videos_with_all_data(args.base_dir, args.prefix)

if __name__ == "__main__":
    main()
