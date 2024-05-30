import os
import subprocess
import mimetypes

input_folder = "./"

for filename in os.listdir(input_folder):
    filepath = os.path.join(input_folder, filename)

    # Check if the file is a regular file and if its MIME type is a video
    if os.path.isfile(filepath):
        mime_type, _ = mimetypes.guess_type(filepath)
        if mime_type and mime_type.startswith("video"):
            # Get the file name and extension
            file_name, file_extension = os.path.splitext(filename)

            # Create the output file path
            output_file = os.path.join(input_folder, f"{file_name}_mirrored{file_extension}")

            # Use FFmpeg to mirror the video
            try:
                subprocess.run(["ffmpeg", "-i", filepath, "-vf", "hflip", "-acodec", "copy", output_file], check=True)
            except FileNotFoundError:
                print("FFmpeg not found. Please ensure it is installed and added to your PATH.")
