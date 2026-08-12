from moviepy.video.io.VideoFileClip import VideoFileClip
import os


class ClipExtractor:

    def __init__(self, output_folder="temp/clips"):
        self.output_folder = output_folder
        os.makedirs(output_folder, exist_ok=True)

    def extract(self, video_path, scenes):

        clip = VideoFileClip(video_path, audio=False)

        output_files = []

        for index, (start, end) in enumerate(scenes):

            output_path = os.path.join(
                self.output_folder,
                f"scene_{index + 1}.mp4"
            )

            subclip = clip.subclipped(start, end)

            subclip.write_videofile(
                output_path,
                codec="libx264",
                audio=False,
                logger=None
            )

            subclip.close()

            output_files.append(output_path)

        clip.close()

        return output_files