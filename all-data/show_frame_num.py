import os
import cv2

def count_frames(video_path):
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    
    # Check if the video file opened successfully
    if not cap.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return -1
    
    # Get the total number of frames in the video
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Release the video capture object
    cap.release()
    
    return total_frames

def main():
    # Get the current directory
    current_dir = os.getcwd()
    
    # List all files in the current directory
    files = os.listdir(current_dir)
    
    # Filter video files (assuming .mp4, .avi, .mov, .mkv extensions)
    video_files = [file for file in files if file.endswith(('.mp4', '.avi', '.mov', '.mkv', '.MOV', 'MP4'))]
    
    if len(video_files) == 0:
        print("No video files found in the current directory.")
        return
    
    # Create or open a file to write the output
    output_file = open("frame_counts.txt", "w")
    
    # Iterate through each video file and count frames
    for video_file in video_files:
        video_path = os.path.join(current_dir, video_file)
        total_frames = count_frames(video_path)
        output_file.write(f"Video file: {video_file}, Total frames: {total_frames}\n")
    
    # Close the output file
    output_file.close()

if __name__ == "__main__":
    main()

