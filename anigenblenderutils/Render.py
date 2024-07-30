import bpy
import os


class AnimationRenderer:
    """
    A class for rendering animations using Blender.

    ...

    Attributes
    ----------
    output_dir : str
        The output directory for rendered animations.
    video_format : str
        The video format for the rendered animation.
    start_frame : int
        The starting frame for rendering.
    end_frame : int
        The ending frame for rendering.
    include_audio : bool
        Whether to include an audio file in the rendered animation.
    audio_file : str
        The path to the audio file to include in the animation, if include_audio is True.
    
    Methods
    -------
    __init__(output_dir, video_format, start_frame, end_frame, include_audio, audio_file=None)
        Initialize the AnimationRenderer with the specified settings.
    render()
        Render the animation using the specified settings.
    run()
        Run the animation rendering process.
    """

    def __init__(self, output_dir, video_format, start_frame, end_frame, include_audio, audio_file=None):
        """
        Initialize the AnimationRenderer.

        Args:
            output_dir (str): The output directory for rendered animations.
            video_format (str): The video format for the rendered animation.
            start_frame (int): The starting frame for rendering.
            end_frame (int): The ending frame for rendering.
            include_audio (bool): Whether to include an audio file in the rendered animation.
            audio_file (str, optional): The path to the audio file to include in the animation, if include_audio is True.
        """
        self.output_dir = output_dir
        self.video_format = video_format
        self.start_frame = start_frame
        self.end_frame = end_frame
        self.include_audio = include_audio
        self.audio_file = audio_file

    def render(self):
        """
        Render the animation using the specified settings.
        """
        # Override the context for rendering
        context = bpy.context.copy()
        context["area"] = context["screen"].areas[0]
        context["region"] = context["area"].regions[0]

        # Set the output path and video format
        bpy.context.scene.render.filepath = os.path.join(
            self.output_dir, "rendered_animation"
        )
        bpy.context.scene.render.image_settings.file_format = self.video_format

        # Set the video codec
        bpy.context.scene.render.ffmpeg.format = "MPEG4"
        bpy.context.scene.render.ffmpeg.codec = "H264"

        # Set the frame range
        bpy.context.scene.frame_start = self.start_frame
        bpy.context.scene.frame_end = self.end_frame

        if self.include_audio and self.audio_file:
            # Clear existing sequences
            bpy.context.scene.sequence_editor_clear()

            # Add a new video sequence editor
            bpy.context.scene.sequence_editor_create()

            # Add the audio file to the sequence editor
            bpy.context.scene.sequence_editor.sequences.new_sound(
                name="Audio",
                filepath=self.audio_file,
                channel=1,
                frame_start=self.start_frame
            )

            # Enable audio mixing
            bpy.context.scene.render.ffmpeg.audio_codec = 'AAC'
            bpy.context.scene.render.ffmpeg.audio_bitrate = 192

        # Render the animation
        bpy.ops.render.render(animation=True, write_still=True)

    def run(self):
        """
        Run the animation rendering process.
        """
        self.render()
        print("Animation rendering complete.")

if __name__ == "__main__":
    # Set the output directory for rendered animations
    output_dir = "output"

    # Set the video format for the rendered animation
    video_format = "FFMPEG"

    # Set the start and end frames for rendering
    start_frame = 1
    end_frame = 250

    # Set whether to include audio in the rendered animation
    include_audio = True

    # Set the audio file path if including audio
    audio_file = "path/to/your/audiofile.mp3" if include_audio else None

    # Create an instance of the AnimationRenderer class
    animation_renderer = AnimationRenderer(output_dir, video_format, start_frame, end_frame, include_audio, audio_file)

    # Run the animation rendering process
    animation_renderer.run()