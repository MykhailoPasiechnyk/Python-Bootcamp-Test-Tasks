from moviepy.editor import VideoFileClip
import os


def get_gif_name(file_name):
    gif_names = []
    dir_path = os.getcwd()
    for path in os.scandir(dir_path):
        if path.is_file():
            if file_name in path.name:
                gif_names.append(path.name)

    gif_count = str(len(gif_names))
    return f'{file_name}-example-{gif_count}.gif'


def convert_video_to_gif(url):
    gif_name = get_gif_name("TikTok")

    try:
        video_clip = VideoFileClip(url)
        video_clip.write_gif(gif_name)
    except OSError as e:
        print(e, 'Not correct url')
    else:
        return os.path.abspath(f'{gif_name}')


# for testing
# convert_video_to_gif(
#     'https://v16-webapp.tiktok.com/b665ff39ebd310121ded0675f4c8ddc1/62e83ff0/video/tos/useast2a/tos-useast2a-ve-0068c003/d3402df7040545c3aa18a46b1f498864/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=4494&bt=2247&btag=80000&cs=0&ds=3&ft=eXd.6H-oMyq8Zlyc1we2N1ioyl7Gb&mime_type=video_mp4&qs=0&rc=PGUzaDVlZmZnZDZpZDk6PEBpanl4dzY6ZmVrZTMzNzczM0A2YGE0X2EzNTYxNi0tXzZfYSNfaWFjcjRva2ZgLS1kMTZzcw%3D%3D&l=20220801150440010192045157203A0737')
