import os
import shutil
import random
import argparse

def duplicate_file(source_path, target_dir):
    """
    Duplicates a file within the specified directory, ensuring the new file has a unique name.
    """
    base, ext = os.path.splitext(os.path.basename(source_path))
    count = 1
    new_filename = f"{base}.{count}{ext}"
    while os.path.exists(os.path.join(target_dir, new_filename)):
        count += 1
        new_filename = f"{base}.{count}{ext}"
    shutil.copy(source_path, os.path.join(target_dir, new_filename))
    print(f"Duplicated {os.path.join(target_dir, new_filename)}")

def balance_directories(dir_one, dir_two):
    """
    Ensures that two directories have the same number of files by duplicating files in the directory with fewer files.
    """
    files_one = [f for f in os.listdir(dir_one) if f.endswith('.csv')]
    files_two = [f for f in os.listdir(dir_two) if f.endswith('.csv')]
    count_one, count_two = len(files_one), len(files_two)

    if count_one < count_two:
        # Duplicate files in dir_one to match the count of dir_two
        while len(files_one) < len(files_two):
            file_to_duplicate = random.choice(files_one)
            duplicate_file(os.path.join(dir_one, file_to_duplicate), dir_one)
            files_one.append(file_to_duplicate)  # Update the list to reflect the new file count
    elif count_two < count_one:
        # Duplicate files in dir_two to match the count of dir_one
        while len(files_two) < len(files_one):
            file_to_duplicate = random.choice(files_two)
            duplicate_file(os.path.join(dir_two, file_to_duplicate), dir_two)
            files_two.append(file_to_duplicate)

def main():
    parser = argparse.ArgumentParser(description="Balance the number of files in Train directory pairs.")
    parser.add_argument('train_dir', type=str, help="Path to the Train directory containing the folders 0+ to 6-")

    args = parser.parse_args()

    # Balance each pair of directories within Train
    for i in range(7):
        dir_one = os.path.join(args.train_dir, f"{i}+")
        dir_two = os.path.join(args.train_dir, f"{i}-")
        if os.path.exists(dir_one) and os.path.exists(dir_two):
            balance_directories(dir_one, dir_two)
        else:
            print(f"One or both directories do not exist: {dir_one}, {dir_two}")

if __name__ == "__main__":
    main()

