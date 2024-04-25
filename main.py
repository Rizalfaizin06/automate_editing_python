from moviepy.editor import *
from PIL import Image
import numpy as np
# Fungsi untuk mengonversi klip video menjadi rasio aspek 1:1
def convert_to_1x1(clip):
    new_width = min(clip.size)
    new_height = new_width
    x_center = (clip.size[0] - new_width) / 2
    y_center = (clip.size[1] - new_height) / 2
    return clip.crop(x_center, y_center, x_center + new_width, y_center + new_height)

# Define the dimensions for resizing
new_width, new_height = 1080, 1920

# Function to resize frame
def resize_frame(frame):
    # Convert frame to NumPy array
    frame_array = np.array(frame)
    # Resize frame
    resized_frame = np.array(Image.fromarray(frame_array).resize((new_width, new_height)))
    return resized_frame

clip1 = VideoFileClip("v1.mp4").subclip(1,3)
clip2 = VideoFileClip("v2.mp4").subclip(1,3)

# Resize video clip using ffmpeg directly
resized_clip1 = clip1.fl_image(resize_frame).fx(vfx.colorx, 1.8)
resized_clip2 = clip2.fl_image(resize_frame)

# Ensure clips have the same dimensions for proper overlay
# if clip1.w != clip2.w or clip1.h != clip2.h:
#     clip1 = clip1.resize((clip2.w, clip2.h))  # Resize clip1 to match clip2

# Set transparency for clip1 using alpha blending
transparent_clip1 = resized_clip1.set_opacity(0.2)  # 0.2 represents 20% transparency

# Create a CompositeVideoClip for layering
# final_clip = CompositeVideoClip([resized_clip2, transparent_clip1])
final_clip = concatenate_videoclips([resized_clip2,transparent_clip1])

final_clip = convert_to_1x1(final_clip).speedx(2)
# Write the final video with transparency
final_clip.write_videofile("kecilGabung3.mp4")