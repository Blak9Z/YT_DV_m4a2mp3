import os
import subprocess

# Prompt for the folder path containing .m4a files
default_folder = os.path.join(os.path.expanduser("~"), "Music")
folder_path = input(f"Enter the folder path containing .m4a files (default: {default_folder}): ")
if not folder_path:
    folder_path = default_folder

# Check if the folder exists
if not os.path.isdir(folder_path):
    print("Invalid folder path. Please make sure the folder exists.")
else:
    # Iterate through all files in the specified folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".m4a"):
            m4a_path = os.path.join(folder_path, filename)
            mp3_path = os.path.join(folder_path, os.path.splitext(filename)[0] + ".mp3")
            
            # Convert the .m4a file to .mp3 using ffmpeg
            subprocess.run(["ffmpeg", "-i", m4a_path, mp3_path])
            
            # Check if the .mp3 file was created successfully
            if os.path.isfile(mp3_path):
                # Remove the original .m4a file
                os.remove(m4a_path)
                print(f"Converted and replaced: {filename} -> {os.path.basename(mp3_path)}")
            else:
                print(f"Failed to convert {filename}.")

# Keep the script open until user presses Enter
input("Press Enter to exit...")
