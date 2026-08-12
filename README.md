# AI Movie Recap Generator V2

An AI-powered Python desktop application that automatically analyzes a video, detects scenes, transcribes audio, uses Gemini AI to identify important moments, and generates a short movie recap.

## Features

* Select video files directly from the desktop application
* Display video information:

  * Resolution
  * Duration
  * File size
* Automatic scene detection using PySceneDetect
* Audio transcription using OpenAI Whisper
* AI-generated recap story using Google Gemini
* AI-based important scene selection
* Configurable recap duration:

  * 30 seconds
  * 60 seconds
  * 90 seconds
* Automatic clip extraction
* Video effects support
* CustomTkinter-based graphical user interface
* Automatic final video generation

## Tech Stack

* Python
* CustomTkinter
* MoviePy
* OpenAI Whisper
* Google Gemini API
* PySceneDetect
* FFmpeg
* Pillow
* python-dotenv

## Project Structure

```text
AI-Movie-Recap-V2/
│
├── core/
│   ├── audio_extractor.py
│   ├── clip_extractor.py
│   ├── effects.py
│   ├── recap_builder.py
│   ├── scene_detector.py
│   ├── scene_ranker.py
│   ├── scene_selector.py
│   ├── story_generator.py
│   ├── subtitle_generator.py
│   ├── thumbnail_extractor.py
│   ├── transcriber.py
│   └── video_info.py
│
├── gui/
│   └── app.py
│
├── config.py
├── main.py
├── .gitignore
└── README.md
```

## How It Works

```text
Input Video
     ↓
Video Information
     ↓
Scene Detection
     ↓
Whisper Transcription
     ↓
Gemini AI Story Generation
     ↓
AI Important Scene Selection
     ↓
Clip Extraction
     ↓
Effects Processing
     ↓
Final Recap Video
```

## Requirements

* Python 3.12+ recommended
* FFmpeg
* Gemini API key

## Installation

Clone the repository:

```bash
git clone https://github.com/aditichaurasia-48/AI-Movie-Recap-V2.git
cd AI-Movie-Recap-V2
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Environment Setup

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Never commit the `.env` file or expose your API key publicly.

## Run the Application

```bash
python main.py
```

Then select a video, choose the desired recap duration, configure the available options, and click **Create Recap**.

## Current Status

The current version is a working prototype.

The main pipeline is functional:

* Scene detection
* Whisper transcription
* Gemini story generation
* AI scene selection
* Clip extraction
* Video recap generation
* Desktop GUI

Audio output is currently disabled in the stable prototype while the audio-processing pipeline is being improved.

## Future Improvements

* Restore audio safely using FFmpeg
* Add automatic subtitles
* Add AI-generated hook text overlays
* Add background music
* Improve transitions and visual effects
* Improve exact 30/60/90-second duration control
* Add recap preview inside the GUI
* Add progress bar and processing logs
* Improve performance for longer videos
* Package the application as a Windows executable

## Author

**Aditi Chourasiya**

Python Developer | AI & Automation Projects

## License

This project is currently provided for learning and portfolio purposes.
