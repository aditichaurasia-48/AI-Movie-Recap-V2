import os

from moviepy import concatenate_videoclips
from moviepy.video.io.VideoFileClip import VideoFileClip

from core.effects import EffectsProcessor


class RecapBuilder:

    def __init__(self):
        self.effects = EffectsProcessor()

    def build(
        self,
        clip_paths,
        output_path,
        fade=False,
        zoom=False,
        transition=False
    ):
        os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)

        clips = []

        for path in clip_paths:
            clip = VideoFileClip(path, audio=False)

            clip = self.effects.apply(
                clip,
                fade=fade,
                zoom=zoom,
                transition=transition
            )

            clips.append(clip)

        if not clips:
            raise ValueError("No clips available to build recap.")

        final_video = concatenate_videoclips(
            clips,
            method="compose"
        )

        final_video.write_videofile(
            output_path,
            codec="libx264",
            audio=False
        )

        final_video.close()

        for clip in clips:
            clip.close()

        return output_path