import os
import shutil
import argparse

def copy_corresponding_csvs(base_dir):
    """
    Copies corresponding CSV files for each video in directories 0+ to 6- from the all-data directory.
    """
    # Define the path to the all-data directory where CSV files are stored
    all_data_dir = os.path.join(base_dir, 'all-data')

    # Loop through the classification directories
    for i in range(7):
        for suffix in ['+', '-']:
            # Define the path to the current classification directory
            class_dir = os.path.join(base_dir, f"{i}{suffix}")
            if not os.path.exists(class_dir):
                print(f"Directory {class_dir} not found. Skipping...")
                continue

            # List all video files in the current directory
            video_files = [f for f in os.listdir(class_dir) if f.endswith(('.mp4', '.mov'))]

            # Iterate over each video file to find and copy the corresponding CSV
            for video_file in video_files:
                # Build the CSV filename from the video filename
                csv_filename = video_file + '.csv'
                csv_source_path = os.path.join(all_data_dir, csv_filename)

                # Check if the corresponding CSV file exists in the all-data directory
                if os.path.exists(csv_source_path):
                    # Define the destination path for the CSV file
                    csv_dest_path = os.path.join(class_dir, csv_filename)
                    # Copy the CSV file to the classification directory
                    shutil.copy(csv_source_path, csv_dest_path)
                    print(f"Copied {csv_filename} to {class_dir}")
                else:
                    print(f"CSV file {csv_filename} not found in all-data for video {video_file}")

def main():
    parser = argparse.ArgumentParser(description="Copy CSV files from all-data to corresponding classification directories based on video files.")
    parser.add_argument('base_dir', type=str, help="Path to the base directory containing the folders 0+ to 6- and all-data")

    args = parser.parse_args()

    copy_corresponding_csvs(args.base_dir)

if __name__ == "__main__":
    main()

