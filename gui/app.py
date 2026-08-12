import customtkinter as ctk
from tkinter import filedialog
import os

from core.video_info import get_video_info
from core.scene_detector import detect_scenes
from core.scene_ranker import rank_scenes
from core.transcriber import Transcriber
from core.story_generator import StoryGenerator
from core.clip_extractor import ClipExtractor
from core.recap_builder import RecapBuilder
from core.scene_selector import select_scenes

class MovieRecapApp:

    def __init__(self):
        self.setup_window()
        self.create_variables()

        # ---------------- Main Layout ----------------


        # ---------------- Main Layout ----------------

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=2)

        self.root.grid_rowconfigure(0, weight=1)

        self.left_frame = ctk.CTkScrollableFrame(self.root, corner_radius=15)
        self.left_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.right_frame = ctk.CTkFrame(self.root, corner_radius=15)
        self.right_frame.grid(row=0, column=1, padx=(0, 20), pady=20, sticky="nsew")

        # ---------------- Title ----------------

        title = ctk.CTkLabel(
            self.root,
            text="🎬 AI Movie Recap Generator V2",
            font=("Arial", 28, "bold")
        )
        title.pack(in_=self.left_frame, pady=25)

        # ---------------- Selected Movie ----------------

        self.movie_label = ctk.CTkLabel(
            self.root,
            text="No movie selected",
            font=("Arial", 16)
        )
        self.movie_label.pack(in_=self.left_frame, pady=10)
        settings_title = ctk.CTkLabel(
            self.left_frame,
            text="⚙️ Output Settings",
            font=("Arial", 18, "bold")
        )
        settings_title.pack(pady=(25, 10))

        # ---------------- Browse Button ----------------

        browse_btn = ctk.CTkButton(
            self.root,
            text="📂 Browse Movie",
            command=self.browse_movie,
            width=220,
            height=40
        )
        browse_btn.pack(in_=self.left_frame, pady=15)

        radio30 = ctk.CTkRadioButton(
            self.left_frame,
            text="30 Seconds",
            variable=self.duration_var,
            value="30"
        )
        radio30.pack(anchor="w", padx=20, pady=5)

        radio60 = ctk.CTkRadioButton(
            self.left_frame,
            text="60 Seconds",
            variable=self.duration_var,
            value="60"
        )
        radio60.pack(anchor="w", padx=20, pady=5)

        radio90 = ctk.CTkRadioButton(
            self.left_frame,
            text="90 Seconds",
            variable=self.duration_var,
            value="90"
        )
        radio90.pack(anchor="w", padx=20, pady=5)
        effects_title = ctk.CTkLabel(
            self.left_frame,
            text="✨ Effects",
            font=("Arial", 18, "bold")
        )
        effects_title.pack(pady=(15, 8))
        ctk.CTkCheckBox(
            self.left_frame,
            text="Fade",
            variable=self.fade_var
        ).pack(anchor="w", padx=20, pady=3)

        ctk.CTkCheckBox(
            self.left_frame,
            text="Zoom",
            variable=self.zoom_var
        ).pack(anchor="w", padx=20, pady=3)

        ctk.CTkCheckBox(
            self.left_frame,
            text="Transition",
            variable=self.transition_var
        ).pack(anchor="w", padx=20, pady=3)

        ctk.CTkCheckBox(
            self.left_frame,
            text="Subtitles",
            variable=self.subtitle_var
        ).pack(anchor="w", padx=20, pady=3)

        ctk.CTkCheckBox(
            self.left_frame,
            text="Hook Text",
            variable=self.hook_var
        ).pack(anchor="w", padx=20, pady=3)

        ctk.CTkCheckBox(
            self.left_frame,
            text="Background Music",
            variable=self.music_var
        ).pack(anchor="w", padx=20, pady=2)
        create_btn = ctk.CTkButton(
            self.left_frame,
            text="🚀 CREATE RECAP",
            width=240,
            height=45,
            font=("Arial", 16, "bold"),
            command=self.create_recap
        )
        create_btn.pack(pady=(10, 10))

        # ---------------- Status ----------------

        self.status = ctk.CTkLabel(
            self.root,
            text="Status : Waiting...",
            font=("Arial", 15)
        )
        self.status.pack(in_=self.left_frame, pady=20)

        # ---------------- Right Panel ----------------

        video_title = ctk.CTkLabel(
            self.right_frame,
            text="🎥 Video Information",
            font=("Arial", 22, "bold")
        )
        video_title.pack(pady=(25, 20))

        self.info_movie = ctk.CTkLabel(
            self.right_frame,
            text="Movie : No movie selected",
            anchor="w",
            font=("Arial", 16)
        )
        self.info_movie.pack(fill="x", padx=20, pady=5)

        self.info_resolution = ctk.CTkLabel(
            self.right_frame,
            text="Resolution : --",
            anchor="w",
            font=("Arial", 16)
        )
        self.info_resolution.pack(fill="x", padx=20, pady=5)

        self.info_duration = ctk.CTkLabel(
            self.right_frame,
            text="Duration : --",
            anchor="w",
            font=("Arial", 16)
        )
        self.info_duration.pack(fill="x", padx=20, pady=5)

        self.info_size = ctk.CTkLabel(
            self.right_frame,
            text="File Size : --",
            anchor="w",
            font=("Arial", 16)
        )
        self.info_size.pack(fill="x", padx=20, pady=5)

    def setup_window(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()
        self.root.title("AI Movie Recap Generator V2")

        self.root.state("zoomed")  # Windows maximize
        self.root.resizable(True, True)

    def create_variables(self):
        self.selected_movie = None
        self.duration_var = ctk.StringVar(value="30")

        self.fade_var = ctk.BooleanVar(value=True)
        self.zoom_var = ctk.BooleanVar(value=True)
        self.transition_var = ctk.BooleanVar(value=True)
        self.subtitle_var = ctk.BooleanVar(value=True)
        self.hook_var = ctk.BooleanVar(value=True)
        self.music_var = ctk.BooleanVar(value=False)

    def browse_movie(self):

        file = filedialog.askopenfilename(
            title="Select Movie",
            filetypes=[
                ("Video Files", "*.mp4 *.mkv *.avi *.mov")
            ]
        )

        if file:
            try:
                video = get_video_info(file)

                self.selected_movie = file

                self.movie_label.configure(text=video["movie_name"])
                self.status.configure(text="✅ Movie Selected")

                self.info_movie.configure(
                    text=f"Movie : {video['movie_name']}"
                )

                self.info_resolution.configure(
                    text=f"Resolution : {video['resolution']}"
                )

                self.info_duration.configure(
                    text=f"Duration : {video['duration']}"
                )

                self.info_size.configure(
                    text=f"File Size : {video['file_size']}"
                )

            except Exception as e:
                self.status.configure(
                    text="❌ Failed to load movie"
                )
                print(e)

    def create_recap(self):

        if not self.selected_movie:
            self.status.configure(text="❌ Please select a movie first.")
            return

        self.status.configure(text="🔍 Detecting Scenes...")
        self.root.update()

        scenes = detect_scenes(self.selected_movie)

        self.status.configure(text="🎤 Transcribing Audio...")
        self.root.update()

        transcriber = Transcriber()

        segments = transcriber.transcribe(
            self.selected_movie
        )
        self.status.configure(text="🤖 Generating Story...")
        self.root.update()

        story_generator = StoryGenerator()

        story = story_generator.generate(
            segments,
            scenes
        )

        print(story)

        print("AI Important Scenes:")
        print(story["important_scenes"])

        ai_scene_numbers = story.get("important_scenes", [])

        selected_scenes = select_scenes(
            scenes,
            ai_scene_numbers,
            int(self.duration_var.get())
        )

        if not selected_scenes:
            print("AI did not select valid scenes. Using ranked scenes.")

            selected_scenes = rank_scenes(
                scenes,
                int(self.duration_var.get())
            )

        print("AI Selected Scenes:", ai_scene_numbers)
        print("Final Scenes for Clips:", selected_scenes)

        self.status.configure(text="✂️ Extracting Clips...")
        self.root.update()

        extractor = ClipExtractor()

        clip_files = extractor.extract(
            self.selected_movie,
            selected_scenes
        )
        self.status.configure(text="🎬 Building Recap...")
        self.root.update()

        builder = RecapBuilder()

        output_path = builder.build(
            clip_files,
            "output/final_recap.mp4",
            fade=self.fade_var.get(),
            zoom=self.zoom_var.get(),
            transition=self.transition_var.get()
        )

        print(f"Extracted Clips: {len(clip_files)}")

        print(f"Transcript Segments: {len(segments)}")

        print(f"Total Scenes: {len(scenes)}")
        print(f"Selected Scenes: {len(selected_scenes)}")

        print("========== SETTINGS ==========")
        print("Duration:", self.duration_var.get(), "seconds")
        print("Fade:", self.fade_var.get())
        print("Zoom:", self.zoom_var.get())
        print("Transition:", self.transition_var.get())
        print("Subtitles:", self.subtitle_var.get())
        print("Background Music:", self.music_var.get())

        self.status.configure(
            text="✅ Recap Created Successfully!"
        )

    def run(self):
        self.root.mainloop()