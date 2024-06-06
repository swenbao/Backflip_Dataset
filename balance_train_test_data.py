import os
import shutil
import random
import argparse

def count_files_in_directory(directory):
    """
    Count the number of files in the specified directory.
    """
    return len([name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))])

def duplicate_files(directory, target_count):
    """
    Duplicate files in the specified directory until the file count reaches the target count,
    with detailed logging for debugging.
    """
    files = [name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))]
    current_count = len(files)
    print(f"Starting duplication in {directory}: {current_count} files, target is {target_count}")

    while current_count < target_count:
        # Randomly select a file to duplicate
        file_to_duplicate = random.choice(files)
        base, ext = os.path.splitext(file_to_duplicate)
        
        # Generate a new filename by appending a duplicate count
        duplicate_count = 1
        new_file = f"{base}.{duplicate_count}{ext}"
        while os.path.exists(os.path.join(directory, new_file)):
            duplicate_count += 1
            new_file = f"{base}.{duplicate_count}{ext}"

        # Copy the file
        shutil.copy(os.path.join(directory, file_to_duplicate), os.path.join(directory, new_file))
        print(f"Duplicated {file_to_duplicate} to {new_file} in {directory}")
        files.append(new_file)
        current_count += 1

    print(f"Completed duplication in {directory}, total files now: {len(os.listdir(directory))}")

def balance_directories(train_dir, test_dir, subdir):
    """
    Balance the number of files in the specified subdirectory within Train and Test directories.
    """
    train_subdir = os.path.join(train_dir, subdir)
    test_subdir = os.path.join(test_dir, subdir)

    # Count the number of files in both directories
    train_count = count_files_in_directory(train_subdir)
    test_count = count_files_in_directory(test_subdir)

    # Determine the target count
    target_count = max(train_count, test_count)

    # Balance the number of files by duplicating in the directory with fewer files
    if train_count < target_count:
        print(f"Balancing {train_subdir}")
        duplicate_files(train_subdir, target_count)
    if test_count < target_count:
        print(f"Balancing {test_subdir}")
        duplicate_files(test_subdir, target_count)

def main():
    parser = argparse.ArgumentParser(description="Balance the number of files in Train and Test directories.")
    parser.add_argument('base_dir', type=str, help="Path to the base directory containing the datas folder")

    args = parser.parse_args()

    # Define the paths to the Train and Test directories
    train_dir = os.path.join(args.base_dir, 'datas', 'Train')
    test_dir = os.path.join(args.base_dir, 'datas', 'Test')

    # Balance each classification subdirectory
    for i in range(7):
        for suffix in ['+', '-']:
            subdir = f"{i}{suffix}"
            balance_directories(train_dir, test_dir, subdir)

if __name__ == "__main__":
    main()

