import os
import json

from dotenv import load_dotenv
from google import genai

load_dotenv()


class StoryGenerator:

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in .env")

        self.client = genai.Client(api_key=api_key)

    def generate(self, transcript_segments, scenes):

        transcript = " ".join(
            segment["text"].strip()
            for segment in transcript_segments
        )

        scene_data = []

        for index, scene in enumerate(scenes, start=1):
            start, end = scene

            scene_data.append({
                "scene_number": index,
                "start": start,
                "end": end
            })

        prompt = f"""
You are an expert movie recap writer and scene selector.

Create a short, engaging movie recap from the transcript.

You are also given the detected scenes with their timestamps.

Select the most important scenes for the recap.

Return ONLY valid JSON with exactly these fields:

{{
    "title": "short title",
    "hook": "strong opening hook",
    "summary": "concise recap summary",
    "important_scenes": [1, 3, 7]
}}

Rules:
- important_scenes must contain only scene numbers provided below.
- Select scenes that are important to the story.
- Avoid unnecessary or repetitive scenes.
- Keep the hook short and engaging.
- Do not invent events that are not supported by the transcript.

TRANSCRIPT:
{transcript}

DETECTED SCENES:
{json.dumps(scene_data, indent=2)}
"""

        response = self.client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
            config={
                "response_mime_type": "application/json"
            }
        )

        story = json.loads(response.text)

        story["transcript"] = transcript

        return story