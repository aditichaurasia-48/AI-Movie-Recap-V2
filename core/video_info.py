import os
from moviepy.video.io.VideoFileClip import VideoFileClip


def get_video_info(video_path):
    """
    Returns:
    {
        movie_name,
        resolution,
        duration,
        fps,
        file_size
    }
    """

    video = VideoFileClip(video_path)

    width, height = video.size

    duration = int(video.duration)

    hours = duration // 3600
    minutes = (duration % 3600) // 60
    seconds = duration % 60

    duration_text = f"{hours:02}:{minutes:02}:{seconds:02}"

    size = os.path.getsize(video_path)

    if size < 1024 * 1024:
        size_text = f"{size / 1024:.2f} KB"
    elif size < 1024 * 1024 * 1024:
        size_text = f"{size / (1024 * 1024):.2f} MB"
    else:
        size_text = f"{size / (1024 * 1024 * 1024):.2f} GB"

    data = {
        "movie_name": os.path.basename(video_path),
        "resolution": f"{width} × {height}",
        "duration": duration_text,
        "fps": round(video.fps, 2),
        "file_size": size_text,
    }

    video.close()

    return data