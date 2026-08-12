from scenedetect import open_video, SceneManager
from scenedetect.detectors import ContentDetector


def detect_scenes(video_path, threshold=30):
    """
    Detect scenes from a video.

    Returns:
        [
            (start_time, end_time),
            ...
        ]
    """

    video = open_video(video_path)

    scene_manager = SceneManager()
    scene_manager.add_detector(ContentDetector(threshold=threshold))

    scene_manager.detect_scenes(video)

    scene_list = scene_manager.get_scene_list()

    scenes = []

    for start, end in scene_list:
        scenes.append(
            (
                start.get_seconds(),
                end.get_seconds()
            )
        )

    return scenes