import cv2
import os
import shutil

def extract_frames(video_path, output_folder):
    # Check if the output folder exists; if so, remove it
    if os.path.exists(output_folder):
        shutil.rmtree(output_folder)
    # Create the output folder afresh
    os.makedirs(output_folder)

    # Load the video
    video = cv2.VideoCapture(video_path)
    count = 0
    success = True

    try:
        # Loop until the video has frames to read
        while success:
            # Read a frame from the video
            success, image = video.read()
            # Check if a frame was successfully read
            if success:
                # Save the frame as an image file
                cv2.imwrite(os.path.join(output_folder, f"frame_{count:04d}.jpg"), image)
                count += 1

    except Exception as e:
        print(f"Error processing video {video_path}: {e}")

    finally:
        # Release the video capture object
        video.release()
        print(f"Extracted {count} frames from {video_path}")

def process_all_videos(directory):
    # List all files in the directory
    files = os.listdir(directory)
    for file in files:
        # Check if the file is a video based on its extension
        if file.endswith(('.mp4', '.avi', '.mov', '.mkv', 'MOV', 'MP4')):  # add or remove extensions as needed
            video_path = os.path.join(directory, file)
            output_folder = os.path.join(directory, f"{os.path.splitext(file)[0]}_frames")
            try:
                extract_frames(video_path, output_folder)
            except Exception as e:
                print(f"Failed to process {video_path}: {e}")

# Directory containing all the videos
video_directory = './all-data/'
process_all_videos(video_directory)

