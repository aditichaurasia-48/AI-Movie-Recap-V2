def select_scenes(all_scenes, selected_numbers, target_duration):
    """
    Select AI-important scenes first, then add other scenes
    until the recap reaches close to the target duration.
    """

    if not all_scenes:
        return []

    selected_scenes = []
    used_indexes = set()
    total_duration = 0

    # 1. AI-selected scenes ko priority do
    for number in selected_numbers:

        index = number - 1

        if 0 <= index < len(all_scenes):
            start, end = all_scenes[index]
            duration = end - start

            if total_duration + duration <= target_duration:
                selected_scenes.append((start, end))
                used_indexes.add(index)
                total_duration += duration

    # 2. Agar target duration abhi complete nahi hua,
    #    remaining scenes add karo
    for index, (start, end) in enumerate(all_scenes):

        if index in used_indexes:
            continue

        duration = end - start

        if total_duration + duration <= target_duration:
            selected_scenes.append((start, end))
            used_indexes.add(index)
            total_duration += duration

        if total_duration >= target_duration * 0.90:
            break

    # 3. Chronological order me arrange karo
    selected_scenes.sort(key=lambda scene: scene[0])

    print(f"Target Duration: {target_duration}s")
    print(f"Final Duration: {total_duration:.2f}s")

    return selected_scenes