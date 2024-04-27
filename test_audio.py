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
        print(f"New Aspect Ratio : 1:1 (persegi): {new_width} x {new_height}")
        
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








clip1 = VideoFileClip("wa/w1.mp4")
clip2 = VideoFileClip("wa/w2.mp4").subclip(0, clip1.duration)


resized_clip1 = clip1.fl_image(resize_frame)
resized_clip2 = clip2.fl_image(resize_frame)
final_clip1 = convert_to_1x1(resized_clip1)

final_clip2 = convert_to_1x1(resized_clip2)
final_clip2 = final_clip2.set_opacity(0.2)
final_clip2 = final_clip2.without_audio()

# final_clip = concatenate_videoclips([final_clip1,final_clip2]).speedx(2)
final_clip = CompositeVideoClip([final_clip1, final_clip2])


final_clip.write_videofile("test_audio.mp4", logger=None)

