from moviepy.editor import *
from PIL import Image
import numpy as np
import os
import tkinter as tk
from tkinter import filedialog

input_folder = None
overlay_folder = None
output_folder = None

def convert_to_1x1(clip):
    new_width = min(clip.size)
    new_height = new_width
    x_center = (clip.size[0] - new_width) / 2
    y_center = (clip.size[1] - new_height) / 2
    return clip.crop(x_center, y_center, x_center + new_width, y_center + new_height)

def nearest_aspect_ratio(nilai):
    smallest_diff = float('inf')
    nearest_value = None
    # 21:9, 16:9, 16:10, 1:1, 4:3
    target = [2.3636364, 1.7777778, 1.6, 1.3333333, 1]

    for target_item in target:
        absolute_diff = abs(nilai - target_item)
        if absolute_diff < smallest_diff:
            smallest_diff = absolute_diff
            nearest_value = target_item

    return nearest_value

def resize_frame(frame):

    frame_array = np.array(frame)

    if isinstance(frame_array, tuple):
        height, width = frame_array

    frame_array = np.array(frame_array)

    height, width = frame_array.shape[:2]

    print("Height:", height)
    print("Width:", width)

    if width > height:
        longest_val = width
        shortest_val = height

    else :
        longest_val = height
        shortest_val = width

    real_aspect_ratio = longest_val / shortest_val
    print("Real Aspect Ratio:", real_aspect_ratio)
    nearest_value = nearest_aspect_ratio(float(real_aspect_ratio))
    # print(f"Nearest Aspect Ratio: {nearest_value}.")

    if nearest_value == 2.3636364:
        new_width = 2560
        new_height = int(new_width * (9/21))
        print(f"New Aspect Ratio : 21:9: {new_width} x {new_height}")    
        
    elif nearest_value ==  1.7777778:
        new_width = 1920
        new_height = int(new_width * (9/16))
        print(f"New Aspect Ratio : 16:9 (FHD): {new_width} x {new_height}")
    
    elif nearest_value == 1.6:
        new_width = 1920
        new_height = int(new_width * (10/16))
        print(f"New Aspect Ratio : 16:10: {new_width} x {new_height}") 

    elif nearest_value ==  1.3333333:
        new_width = 1280
        new_height = int(new_width * (3/4))
        print(f"New Aspect Ratio : 4:3: {new_width} x {new_height}")
    
    elif nearest_value == 1:
        new_width = 1000
        new_height = new_width
        print(f"New Aspect Ratio : 1:1: {new_width} x {new_height}")
        
    else:
        print("Function Aspect Ratio Error")

    if width > height:
        print(f"Lanscape - New Resolution: {new_width} x {new_height}")

    else :
        temp = new_width
        new_width = new_height
        new_height = temp
        print(f"Portrait - New Resolution: {new_width} x {new_height}")
        
    resized_frame = np.array(Image.fromarray(frame_array).resize((new_width, new_height)))
    return resized_frame


def select_overlay_folder():
    global overlay_folder
    overlay_folder = filedialog.askdirectory()
    overlay_folder_entry.delete(0, tk.END)
    overlay_folder_entry.insert(0, overlay_folder)

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
    
    if input_folder is None:
        log_text.insert(tk.END, "Input folder is not defined.\n")
        return

    if overlay_folder is None:
        log_text.insert(tk.END, "Overlay folder is not defined.\n")
        return

    if output_folder is None:
        log_text.insert(tk.END, "Output folder is not defined.\n")
        return


    video_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f)) and f.endswith('.mp4')]
    
    overlay_files = [f for f in os.listdir(overlay_folder) if os.path.isfile(os.path.join(overlay_folder, f)) and f.endswith('.mp4')]

    for video_file in video_files:
        input_path = os.path.join(input_folder, video_file)
        output_path = os.path.join(output_folder, "processed_" + video_file)
        
        current_index = video_files.index(video_file)
        overlay_path = os.path.join(overlay_folder, overlay_files[current_index])
        

        log_text.insert(tk.END, f"Processing {video_file}...\n")
        log_text.insert(tk.END, f"Overlay Path {overlay_path}...\n")
        log_text.update()
        
        clip = VideoFileClip(input_path)
        overlay = VideoFileClip(overlay_path).subclip(0, clip.duration)
        
        resized_clip = clip.fl_image(resize_frame)
        resized_overlay = overlay.fl_image(resize_frame)
        
        final_clip = convert_to_1x1(resized_clip)
        square_overlay = convert_to_1x1(resized_overlay)
        
        transparent_overlay = square_overlay.set_opacity(0.2)
        mute_overlay = transparent_overlay.without_audio()
        
        
        layering_clip = CompositeVideoClip([final_clip, mute_overlay])
        speedup_clip = layering_clip.speedx(2)
        render_clip = speedup_clip
        render_clip.write_videofile(output_path, logger=None)
        
        log_text.insert(tk.END, f"{video_file} processed successfully.\n")
        log_text.update()

    log_text.insert(tk.END, "All videos processed successfully.\n")
    log_text.update() 


root = tk.Tk()
root.title("Video Processing")

input_folder_label = tk.Label(root, text="Input Folder:")
input_folder_label.grid(row=0, column=0)

input_folder_entry = tk.Entry(root, width=50)
input_folder_entry.grid(row=0, column=1)

browse_input_button = tk.Button(root, text="Browse", command=select_input_folder)
browse_input_button.grid(row=0, column=2)

overlay_folder_label = tk.Label(root, text="Overlay Folder:")
overlay_folder_label.grid(row=1, column=0)

overlay_folder_entry = tk.Entry(root, width=50)
overlay_folder_entry.grid(row=1, column=1)

browse_overlay_button = tk.Button(root, text="Browse", command=select_overlay_folder)
browse_overlay_button.grid(row=1, column=2)

output_folder_label = tk.Label(root, text="Output Folder:")
output_folder_label.grid(row=2, column=0)

output_folder_entry = tk.Entry(root, width=50)
output_folder_entry.grid(row=2, column=1)

browse_output_button = tk.Button(root, text="Browse", command=select_output_folder)
browse_output_button.grid(row=2, column=2)

process_button = tk.Button(root, text="Process Videos", command=process_videos)
process_button.grid(row=3, column=1)

log_text = tk.Text(root, width=60, height=10)
log_text.grid(row=4, columnspan=3)

root.mainloop()




