import bpy
import os
from datetime import datetime

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
    
    Methods
    -------
    __init__(output_dir, video_format, start_frame, end_frame)
        Initialize the AnimationRenderer with the specified settings.
    generate_filename()
        Generate a filename based on the current date and time.
    render()
        Render the animation using the specified settings.
    run()
        Run the animation rendering process.
    """
    
    def __init__(self, output_dir, video_format, start_frame, end_frame):
        """
        Initialize the AnimationRenderer.

        Args:
            output_dir (str): The output directory for rendered animations.
            video_format (str): The video format for the rendered animation.
            start_frame (int): The starting frame for rendering.
            end_frame (int): The ending frame for rendering.
        """
        self.output_dir = output_dir
        self.video_format = video_format
        self.start_frame = start_frame
        self.end_frame = end_frame

    def generate_filename(self):
        """
        Generate a filename based on the current date and time.

        Returns:
            str: The generated filename.
        """
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"rendered_animation_{current_time}.mp4"

    def render(self):
        """
        Render the animation using the specified settings.

        Returns:
            str: The filename of the rendered animation.
        """
        filename = self.generate_filename()
        
        # Override the context for rendering
        context = bpy.context.copy()
        context["area"] = context["screen"].areas[0]
        context["region"] = context["area"].regions[0]

        # Set the output path and video format
        bpy.context.scene.render.filepath = os.path.join(self.output_dir, filename)
        bpy.context.scene.render.image_settings.file_format = self.video_format

        # Set the video codec
        bpy.context.scene.render.ffmpeg.format = "MPEG4"
        bpy.context.scene.render.ffmpeg.codec = "H264"

        # Set the frame range
        bpy.context.scene.frame_start = self.start_frame
        bpy.context.scene.frame_end = self.end_frame

        # Render the animation
        bpy.ops.render.render(animation=True, write_still=True)

        return filename

    def run(self):
        """
        Run the animation rendering process.

        Returns:
            str: The filename of the rendered animation.
        """
        filename = self.render()
        print("Animation rendering complete.")
        return filename

if __name__ == "__main__":
    # Set the output directory for rendered animations
    output_dir = "output"

    # Set the video format for the rendered animation
    video_format = "FFMPEG"

    # Set the start and end frames for rendering
    start_frame = 1
    end_frame = 250

    # Create an instance of the AnimationRenderer class
    animation_renderer = AnimationRenderer(output_dir, video_format, start_frame, end_frame)

    # Run the animation rendering process and get the filename
    rendered_filename = animation_renderer.run()
    print(f"Rendered animation saved as: {rendered_filename}")