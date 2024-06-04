import os

def check_mirrored_pairs(base_dir):
    """
    This function checks each folder from 0+ to 6- to ensure that every non-mirrored video file
    has its corresponding mirrored video file.
    """
    # Loop through problem numbers from 0 to 6
    for i in range(7):
        for suffix in ['+', '-']:
            dir_path = os.path.join(base_dir, f"{i}{suffix}")
            if not os.path.exists(dir_path):
                print(f"Directory {dir_path} not found. Skipping...")
                continue

            files = os.listdir(dir_path)
            # Filter out files to only include non-mirrored video files and ignore .DS_Store
            non_mirrored_files = [file for file in files if (not file.endswith('_mirrored.mp4') and not file.endswith('_mirrored.mov') and file != ".DS_Store")]


            # Check for each non-mirrored file if its mirrored counterpart exists
            for file in non_mirrored_files:
                basename, ext = os.path.splitext(file)
                mirrored_filename = f"{basename}_mirrored{ext}"

                # Check if the mirrored file exists in the same folder
                if mirrored_filename not in files:
                    print(f"Missing mirrored pair for {file} in {dir_path}")
                else:
                    pass
                    # print(f"Found mirrored pair for {file} in {dir_path}")

def main():
    # Set the path to the base directory containing all the data
    base_dir = "."
    check_mirrored_pairs(base_dir)

if __name__ == "__main__":
    main()
