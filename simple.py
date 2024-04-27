
# from moviepy.editor import VideoFileClip, concatenate_videoclips
# clip1 = VideoFileClip("wa/w1.mp4")
# clip2 = VideoFileClip("wa/w2.mp4")
# final_clip = concatenate_videoclips([clip1,clip2])
# final_clip.write_videofile("my_concatenation.mp4")






# from moviepy.editor import *

# video_clip1 = VideoFileClip("wa/w1.mp4")
# audio_clip1 = AudioFileClip("wa/w1_audio.mp3")
# video_clip2 = VideoFileClip("wa/w2.mp4")
# audio_clip2 = AudioFileClip("wa/w2_audio.mp3")

# final_clip1 = CompositeVideoClip([video_clip1, audio_clip1.set_duration(video_clip1.duration)])
# final_clip2 = CompositeVideoClip([video_clip2, audio_clip2.set_duration(video_clip2.duration)])


# final_clip = concatenate_videoclips([final_clip1, final_clip2])
# final_clip.write_videofile("my_concatenation.mp4")






# from moviepy.editor import *
# clip1 = VideoFileClip("wa/w1.mp4")
# clip2 = VideoFileClip("wa/w2.mp4")
# clip1.audio.write_audiofile("my_concatenation.mp3")







from moviepy.editor import *
clip1 = VideoFileClip("wa/w1.mp4")
clip2 = VideoFileClip("wa/w2.mp4")
final_clip = concatenate_videoclips([clip1,clip2])
final_clip.write_videofile("my_concatenation.mp4")




# from moviepy.editor import *
# clip1 = VideoFileClip("wa/w1.mp4")
# clip2 = VideoFileClip("wa/w2.mp4")
# final_clip = concatenate_videoclips([clip1,clip2])
# final_clip.write_videofile("my_concatenation.mp4")
