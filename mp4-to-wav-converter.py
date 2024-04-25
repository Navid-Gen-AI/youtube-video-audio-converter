#This code is to convert mp4 to wav
import os
from moviepy.editor import AudioFileClip

# Function to convert MP4 files to WAV
def convert_to_wav(input_file, output_file):
    audio_clip = AudioFileClip(input_file)
    audio_clip.write_audiofile(output_file, fps=44100, codec='pcm_s16le')

# Directory containing MP4 files
directory = r"C:\Users\hessa\Downloads\BEST"

# Convert each MP4 file to WAV
for file in os.listdir(directory):
    if file.endswith(".mp4"):
        input_file = os.path.join(directory, file)
        output_file = os.path.join(directory, os.path.splitext(file)[0] + ".wav")
        convert_to_wav(input_file, output_file)
        print(f"Converted {input_file} to {output_file}")