import os
import argparse
import hashlib

def hash_file(filename):
    """
    This function returns the SHA-256 hash of the file passed into it
    """
    # Make a hash object
    h = hashlib.sha256()

    # Open file for reading in binary mode
    with open(filename, 'rb') as file:
        chunk = 0
        while chunk != b'':
            # Read only 1024 bytes at a time
            chunk = file.read(1024)
            h.update(chunk)
    
    # Return the hex representation of digest
    return h.hexdigest()

def find_videos_starting_with_prefix(base_dir, prefix):
    """
    This function checks each folder from 0+ to 6- to see if there are any video files starting with the given prefix
    and compares them to the corresponding files in the 'all-data' directory.
    """
    all_data_dir = os.path.join(base_dir, 'all-data')
    # Loop through problem numbers from 0 to 6
    for i in range(7):
        for suffix in ['+', '-']:
            dir_path = os.path.join(base_dir, f"{i}{suffix}")
            if not os.path.exists(dir_path):
                print(f"Directory {dir_path} not found. Skipping...")
                continue

            files = os.listdir(dir_path)
            # Check if any video file starts with the prefix
            for file in files:
                if file.startswith(prefix) and (file.endswith('.mp4') or file.endswith('.mov')):
                    file_path = os.path.join(dir_path, file)
                    all_data_file_path = os.path.join(all_data_dir, file)
                    # Check if the file exists in all-data
                    if os.path.exists(all_data_file_path):
                        # Compare files using hash
                        if hash_file(file_path) == hash_file(all_data_file_path):
                            print(f"Files are the same: {file_path} and {all_data_file_path}")
                        else:
                            print(f"Files differ: {file_path} and {all_data_file_path}")
                    else:
                        print(f"File not found in all-data: {all_data_file_path}")

def main():
    parser = argparse.ArgumentParser(description="Check and compare video files starting with a specific prefix.")
    parser.add_argument('base_dir', type=str, help="Path to the base directory containing all the data")
    parser.add_argument('prefix', type=str, help="The number prefix to check for in video filenames")

    args = parser.parse_args()
    
    find_videos_starting_with_prefix(args.base_dir, args.prefix)

if __name__ == "__main__":
    main()
