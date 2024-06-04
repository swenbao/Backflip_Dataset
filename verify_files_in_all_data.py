import os
import hashlib
import argparse

def hash_file(filepath):
    """
    Compute the SHA-256 hash of the file specified by 'filepath'.
    This provides a unique fingerprint of the file's content.
    """
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def verify_files(base_dir):
    """
    Verifies that each file in subdirectories from 0+ to 6- exists in the 'all-data' directory
    with the same content.
    """
    all_data_dir = os.path.join(base_dir, 'all-data')
    all_data_files = {f: hash_file(os.path.join(all_data_dir, f)) for f in os.listdir(all_data_dir)}

    # Check each classification folder
    for i in range(7):
        for suffix in ['+', '-']:
            class_dir = os.path.join(base_dir, f"{i}{suffix}")
            if not os.path.exists(class_dir):
                print(f"Directory {class_dir} not found. Skipping...")
                continue

            # Verify each file in the classification folder
            for file in os.listdir(class_dir):
                file_path = os.path.join(class_dir, file)
                if file in all_data_files:  # First, check if the file name exists in all-data
                    # Next, compare the hash of both files
                    if hash_file(file_path) == all_data_files[file]:
                        pass
                        # print(f"File {file} in {class_dir} matches the one in all-data.")
                    else:
                        print(f"File {file} in {class_dir} does not match the content in all-data.")
                else:
                    print(f"File {file} in {class_dir} is missing in all-data.")

def main():
    parser = argparse.ArgumentParser(description="Verify that files in classification folders exist in 'all-data' with matching content.")
    parser.add_argument('base_dir', type=str, help="Path to the base directory containing all the data")
    
    args = parser.parse_args()
    verify_files(args.base_dir)

if __name__ == "__main__":
    main()
