import os
import argparse

def count_files(base_dir, output_file):
    """
    Counts files in each classification directory under Train, Test, and the original classification folders,
    and writes the counts to a specified text file, focusing on CSV files for the original folders.
    """
    with open(output_file, 'w') as f:
        # First count CSV files in the original dataset directories 0+ to 6-
        f.write("Counts for original dataset directories (CSV files only):\n")
        for i in range(7):
            for suffix in ['+', '-']:
                dir_path = os.path.join(base_dir, f"{i}{suffix}")
                if not os.path.exists(dir_path):
                    f.write(f"Directory {dir_path} not found. Skipping...\n")
                    continue

                # Count only CSV files
                csv_count = len([file for file in os.listdir(dir_path) if file.endswith('.csv')])
                f.write(f"Number of CSV files in {i}{suffix}: {csv_count}\n")
        
        f.write("\n")  # Separate the sections for clarity

        # Then process Train and Test directories
        for category in ['Train', 'Test']:
            f.write(f"Counts for {category} (All files):\n")
            for i in range(7):
                for suffix in ['+', '-']:
                    dir_path = os.path.join(base_dir, 'datas', category, f"{i}{suffix}")
                    if not os.path.exists(dir_path):
                        f.write(f"Directory {dir_path} not found. Skipping...\n")
                        continue

                    # Count all files in the directory
                    file_count = len([name for name in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, name))])
                    f.write(f"Number of files in {i}{suffix}: {file_count}\n")

def main():
    parser = argparse.ArgumentParser(description="Count CSV files in classification folders and report the numbers in a text file.")
    parser.add_argument('base_dir', type=str, help="Path to the base directory containing the folders 0+ to 6- and datas")

    args = parser.parse_args()

    # Define the output file path
    output_file_path = os.path.join(args.base_dir, 'datas', 'howMany.txt')
    
    count_files(args.base_dir, output_file_path)

if __name__ == "__main__":
    main()

