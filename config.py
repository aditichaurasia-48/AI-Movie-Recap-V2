from dataclasses import dataclass, field


@dataclass
class ProjectState:

    video_path: str = ""

    video_name: str = ""

    duration: int = 30

    selected_scenes: list = field(default_factory=list)

    transcript: str = ""

    story: str = ""

    recap_path: str = ""