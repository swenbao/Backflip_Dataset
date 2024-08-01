import os
import pandas as pd

def process_directory(directory):
    """
    Processes a single directory to create data.csv and info.csv files.
    """
    header = "NOSE_x,NOSE_y,NOSE_score,LEFT_EYE_x,LEFT_EYE_y,LEFT_EYE_score,RIGHT_EYE_x,RIGHT_EYE_y,RIGHT_EYE_score,LEFT_EAR_x,LEFT_EAR_y,LEFT_EAR_score,RIGHT_EAR_x,RIGHT_EAR_y,RIGHT_EAR_score,LEFT_SHOULDER_x,LEFT_SHOULDER_y,LEFT_SHOULDER_score,RIGHT_SHOULDER_x,RIGHT_SHOULDER_y,RIGHT_SHOULDER_score,LEFT_ELBOW_x,LEFT_ELBOW_y,LEFT_ELBOW_score,RIGHT_ELBOW_x,RIGHT_ELBOW_y,RIGHT_ELBOW_score,LEFT_WRIST_x,LEFT_WRIST_y,LEFT_WRIST_score,RIGHT_WRIST_x,RIGHT_WRIST_y,RIGHT_WRIST_score,LEFT_HIP_x,LEFT_HIP_y,LEFT_HIP_score,RIGHT_HIP_x,RIGHT_HIP_y,RIGHT_HIP_score,LEFT_KNEE_x,LEFT_KNEE_y,LEFT_KNEE_score,RIGHT_KNEE_x,RIGHT_KNEE_y,RIGHT_KNEE_score,LEFT_ANKLE_x,LEFT_ANKLE_y,LEFT_ANKLE_score,RIGHT_ANKLE_x,RIGHT_ANKLE_y,RIGHT_ANKLE_score"
    data_frames = []  # To hold all data frames for concatenation
    info_lines = [f"{os.path.basename(directory)},0,24,"]  # First line for info.csv

    for file_name in sorted(os.listdir(directory)):
        if file_name.endswith('.csv'):
            file_path = os.path.join(directory, file_name)
            # Read the CSV file
            df = pd.read_csv(file_path, header=None)
            data_frames.append(df)

            # Collect info for info.csv
            frame_count = len(df)
            info_lines.append(f"{file_name},1920,1080,{frame_count}")

    # Merge all data frames for data.csv
    full_data = pd.concat(data_frames, ignore_index=True)
    full_data.to_csv(os.path.join(directory, 'data.csv'), index=False, header=[header])

    # Write info.csv
    with open(os.path.join(directory, 'info.csv'), 'w') as f:
        for line in info_lines:
            f.write(line + '\n')

def main():
    base_dir = './datas'  # Adjust path as necessary
    for category in ['Train', 'Test']:
        for i in range(7):
            for suffix in ['+', '-']:
                directory = os.path.join(base_dir, category, f"{i}{suffix}")
                if os.path.exists(directory):
                    print(f"Processing directory: {directory}")
                    process_directory(directory)

if __name__ == "__main__":
    main()

