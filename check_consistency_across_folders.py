import os
import hashlib
import argparse

def hash_file(filepath):
    """
    Compute the SHA-256 hash of the file specified by 'filepath'.
    This function opens the file in binary read mode, reads it in chunks to handle large files, and updates
    the hash object for each chunk, returning the hexadecimal SHA-256 hash of the entire file.
    """
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def compare_files(base_dir, prefix):
    """
    Compares files with a given prefix in the subdirectories from 0+ to 6- to check if their contents are identical.
    Reports on directories with mismatched content and confirms if all content matches across directories.
    """
    file_hashes = {}
    discrepancies_found = False  # Flag to track if any discrepancies are found

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
                    file_hash = hash_file(file_path)

                    if file not in file_hashes:
                        file_hashes[file] = (file_hash, dir_path)
                    else:
                        if file_hashes[file][0] != file_hash:
                            print(f"Content mismatch found for {file}:")
                            print(f" - {dir_path} differs from {file_hashes[file][1]}")
                            discrepancies_found = True

    if not discrepancies_found:
        print("All videos are the same across 0+/ ~ 6-/")

def main():
    parser = argparse.ArgumentParser(description="Check consistency of videos across folders based on prefix.")
    parser.add_argument('base_dir', type=str, help="Path to the base directory containing all the data")
    parser.add_argument('prefix', type=str, help="The number prefix of video filenames to check")

    args = parser.parse_args()
    
    compare_files(args.base_dir, args.prefix)

if __name__ == "__main__":
    main()
