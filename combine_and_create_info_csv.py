import os
import pandas as pd
import glob

def combine_csv_files(directory, output_data_file, output_info_file):
    """
    Combines CSV files in the given directory into a single CSV file and creates an info CSV.
    """
    # Get all CSV files in the directory
    csv_files = glob.glob(os.path.join(directory, '*.csv'))
    combined_csv = pd.DataFrame()
    info_data = []

    # Define headers for the combined CSV
    headers = [
        "NOSE_x", "NOSE_y", "NOSE_score",
        "LEFT_EYE_x", "LEFT_EYE_y", "LEFT_EYE_score",
        "RIGHT_EYE_x", "RIGHT_EYE_y", "RIGHT_EYE_score",
        "LEFT_EAR_x", "LEFT_EAR_y", "LEFT_EAR_score",
        "RIGHT_EAR_x", "RIGHT_EAR_y", "RIGHT_EAR_score",
        "LEFT_SHOULDER_x", "LEFT_SHOULDER_y", "LEFT_SHOULDER_score",
        "RIGHT_SHOULDER_x", "RIGHT_SHOULDER_y", "RIGHT_SHOULDER_score",
        "LEFT_ELBOW_x", "LEFT_ELBOW_y", "LEFT_ELBOW_score",
        "RIGHT_ELBOW_x", "RIGHT_ELBOW_y", "RIGHT_ELBOW_score",
        "LEFT_WRIST_x", "LEFT_WRIST_y", "LEFT_WRIST_score",
        "RIGHT_WRIST_x", "RIGHT_WRIST_y", "RIGHT_WRIST_score",
        "LEFT_HIP_x", "LEFT_HIP_y", "LEFT_HIP_score",
        "RIGHT_HIP_x", "RIGHT_HIP_y", "RIGHT_HIP_score",
        "LEFT_KNEE_x", "LEFT_KNEE_y", "LEFT_KNEE_score",
        "RIGHT_KNEE_x", "RIGHT_KNEE_y", "RIGHT_KNEE_score",
        "LEFT_ANKLE_x", "LEFT_ANKLE_y", "LEFT_ANKLE_score",
        "RIGHT_ANKLE_x", "RIGHT_ANKLE_y", "RIGHT_ANKLE_score"
    ]

    for csv_file in csv_files:
        # Read the CSV file
        temp_df = pd.read_csv(csv_file, header=None)
        temp_df.columns = headers  # Assign the correct headers
        combined_csv = pd.concat([combined_csv, temp_df], ignore_index=True)

        # Extract video information for the info CSV
        video_file = os.path.basename(csv_file).replace('.csv', '')
        resolution = "1920x1080"  # Replace with actual resolution if available
        frame_count = len(temp_df)
        info_data.append([video_file, resolution, frame_count])

    # Save the combined CSV file with headers
    combined_csv.to_csv(output_data_file, index=False)

    # Create the info CSV
    info_df = pd.DataFrame(info_data, columns=['Video', 'Resolution', 'Frame Count'])
    info_df.to_csv(output_info_file, index=False, header=True)

def process_directories(base_dir):
    """
    Process each directory within Train and Test to create combined and info CSVs.
    """
    for category in ['Train', 'Test']:
        category_path = os.path.join(base_dir, 'datas', category)
        for i in range(7):
            for suffix in ['+', '-']:
                folder_name = f"{i}{suffix}"
                dir_path = os.path.join(category_path, folder_name)
                output_data_file = os.path.join(dir_path, f"{folder_name}_data.csv")
                output_info_file = os.path.join(dir_path, f"{folder_name}_info.csv")
                combine_csv_files(dir_path, output_data_file, output_info_file)
                print(f"Processed {dir_path}")

def main():
    parser = argparse.ArgumentParser(description="Combine CSV files and create informational summaries.")
    parser.add_argument('base_dir', type=str, help="Base directory containing the Train and Test folders")

    args = parser.parse_args()

    process_directories(args.base_dir)

if __name__ == "__main__":
    main()

