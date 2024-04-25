from moviepy.editor import *
from PIL import Image
import numpy as np
import os
import tkinter as tk
from tkinter import filedialog

def convert_to_1x1(clip):
    new_width = min(clip.size)
    new_height = new_width
    x_center = (clip.size[0] - new_width) / 2
    y_center = (clip.size[1] - new_height) / 2
    return clip.crop(x_center, y_center, x_center + new_width, y_center + new_height)

new_width, new_height = 1080, 1920

def resize_frame(frame):
    frame_array = np.array(frame)
    resized_frame = np.array(Image.fromarray(frame_array).resize((new_width, new_height)))
    return resized_frame

def select_input_folder():
    global input_folder
    input_folder = filedialog.askdirectory()
    input_folder_entry.delete(0, tk.END)
    input_folder_entry.insert(0, input_folder)

def select_output_folder():
    global output_folder
    output_folder = filedialog.askdirectory()
    output_folder_entry.delete(0, tk.END)
    output_folder_entry.insert(0, output_folder)

def process_videos():
    if not input_folder or not output_folder:
        log_text.insert(tk.END, "Input and output folders are not selected.\n")
        return


    # List all video files in the input folder
    video_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f)) and f.endswith('.mp4')]

    for video_file in video_files:
        input_path = os.path.join(input_folder, video_file)
        output_path = os.path.join(output_folder, "processed_" + video_file)
        
        clip = VideoFileClip(input_path).subclip(1, 3)
        resized_clip = clip.fl_image(resize_frame)
        
        final_clip = convert_to_1x1(resized_clip).speedx(2)
        final_clip.write_videofile(output_path)
        
        log_text.insert(tk.END, f"{video_file} processed successfully.\n")

    log_text.insert(tk.END, "All videos processed successfully.\n")

# GUI for selecting input and output folders
root = tk.Tk()
root.title("Video Processing")

# Select input folder
input_folder_label = tk.Label(root, text="Input Folder:")
input_folder_label.grid(row=0, column=0)

input_folder_entry = tk.Entry(root, width=50)
input_folder_entry.grid(row=0, column=1)

browse_input_button = tk.Button(root, text="Browse", command=select_input_folder)
browse_input_button.grid(row=0, column=2)

# Select output folder
output_folder_label = tk.Label(root, text="Output Folder:")
output_folder_label.grid(row=1, column=0)

output_folder_entry = tk.Entry(root, width=50)
output_folder_entry.grid(row=1, column=1)

browse_output_button = tk.Button(root, text="Browse", command=select_output_folder)
browse_output_button.grid(row=1, column=2)

# Process videos button
process_button = tk.Button(root, text="Process Videos", command=process_videos)
process_button.grid(row=2, column=1)

# Log text widget
log_text = tk.Text(root, width=60, height=10)
log_text.grid(row=3, columnspan=3)

root.mainloop()