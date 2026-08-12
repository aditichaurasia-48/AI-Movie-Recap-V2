from moviepy import vfx


class EffectsProcessor:

    def apply(self, clip, fade=False, zoom=False, transition=False):
        effects = []

        if fade:
            effects.append(vfx.FadeIn(0.5))
            effects.append(vfx.FadeOut(0.5))

        if zoom:
            effects.append(
                vfx.Resize(
                    lambda t: 1 + (0.05 * t / max(clip.duration, 1))
                )
            )

        for effect in effects:
            clip = clip.with_effects([effect])

        return clip