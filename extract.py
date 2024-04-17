import cv2
import os

def extract_frames(video_path, output_folder):
    # Check if the output folder exists; if not, create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Load the video
    video = cv2.VideoCapture(video_path)
    count = 0
    success = True

    # Loop until the video has frames to read
    while success:
        # Read a frame from the video
        success, image = video.read()
        # Check if a frame was successfully read
        if success:
            # Save the frame as an image file
            cv2.imwrite(os.path.join(output_folder, f"frame_{count:04d}.jpg"), image)
            count += 1

    # Release the video capture object
    video.release()
    print(f"Extracted {count} frames from {video_path}")

def process_all_videos(directory):
    # List all files in the directory
    files = os.listdir(directory)
    for file in files:
        # Check if the file is a video based on its extension
        if file.endswith(('.mp4', '.avi', '.mov', '.mkv')):  # add or remove extensions as needed
            video_path = os.path.join(directory, file)
            output_folder = os.path.join(directory, f"{os.path.splitext(file)[0]}_frames")
            extract_frames(video_path, output_folder)

# Directory containing all the videos
video_directory = './all-data/'
process_all_videos(video_directory)
