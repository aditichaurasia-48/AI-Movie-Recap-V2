def rank_scenes(scene_list, target_duration=60):
    """
    Select best scenes for recap.

    Args:
        scene_list: [(start, end), ...]
        target_duration: recap duration in seconds

    Returns:
        Selected scenes
    """

    if not scene_list:
        return []

    total_movie_duration = scene_list[-1][1]

    if target_duration == 30:
        percent = 0.08
    elif target_duration == 60:
        percent = 0.15
    else:
        percent = 0.22

    keep = max(5, int(len(scene_list) * percent))

    return scene_list[:keep]