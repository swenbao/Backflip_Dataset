import os
import shutil
import argparse
import random

def setup_directory_structure(base_dir):
    """
    Sets up the directory structure for training and testing datasets.
    """
    datas_dir = os.path.join(base_dir, 'datas')
    train_dir = os.path.join(datas_dir, 'Train')
    test_dir = os.path.join(datas_dir, 'Test')

    # Create directories for Train and Test
    for directory in [train_dir, test_dir]:
        os.makedirs(directory, exist_ok=True)
        # Create classification subdirectories within Train and Test
        for i in range(7):
            for suffix in ['+', '-']:
                os.makedirs(os.path.join(directory, f"{i}{suffix}"), exist_ok=True)

def distribute_files(base_dir):
    """
    Distributes CSV files into the training and testing datasets with an 80:20 split.
    """
    train_dir = os.path.join(base_dir, 'datas', 'Train')
    test_dir = os.path.join(base_dir, 'datas', 'Test')

    # Iterate through each classification directory
    for i in range(7):
        for suffix in ['+', '-']:
            class_dir = os.path.join(base_dir, f"{i}{suffix}")
            if not os.path.exists(class_dir):
                print(f"Directory {class_dir} not found. Skipping...")
                continue

            # Collect all CSV files in the current classification directory
            csv_files = [f for f in os.listdir(class_dir) if f.endswith('.csv')]
            random.shuffle(csv_files)  # Shuffle the list to randomize file selection

            # Determine the split index for an 80:20 ratio
            split_index = int(len(csv_files) * 0.8)

            # Separate files into training and testing sets
            train_files = csv_files[:split_index]
            test_files = csv_files[split_index:]

            # Copy files to their respective Train and Test directories
            for file in train_files:
                shutil.copy(os.path.join(class_dir, file), os.path.join(train_dir, f"{i}{suffix}", file))
                print(f"Copied {file} to {os.path.join(train_dir, f'{i}{suffix}')}")
            for file in test_files:
                shutil.copy(os.path.join(class_dir, file), os.path.join(test_dir, f"{i}{suffix}", file))
                print(f"Copied {file} to {os.path.join(test_dir, f'{i}{suffix}')}")
                
def main():
    parser = argparse.ArgumentParser(description="Organize CSV files into training and testing datasets.")
    parser.add_argument('base_dir', type=str, help="Path to the base directory containing the folders 0+ to 6-")

    args = parser.parse_args()

    setup_directory_structure(args.base_dir)
    distribute_files(args.base_dir)

if __name__ == "__main__":
    main()

