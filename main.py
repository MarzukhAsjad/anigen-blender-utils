import os, sys, bpy

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)
from anigenblenderutils.RenameAction import RenameAction
from anigenblenderutils.FindAndImport import FindAndImport
from anigenblenderutils.BlendMotion import BlendMotion
from anigenblenderutils.AdjustFrames import AdjustFrames
from anigenblenderutils.MakeInvisible import MakeInvisible
from anigenblenderutils.Render import AnimationRenderer as Render
from anigenblenderutils.ExportFBX import FBXExporter as Exporter
import config as Config

def main():
    # Import the motions from the config file
    motions = Config.MOTIONS

    # Convert the motions to filenames with .fbx extension
    fbx_files = [motion + ".fbx" for motion in motions] 

    # Import the fbx files, i.e., the motions
    find_and_import = FindAndImport(Config.IMPORT_PATH, fbx_files)
    find_and_import.run()

    # Rename the actions for each of the motions (preprocessing)
    for motion in motions:
        rename_action = RenameAction(motion)
        rename_action.run()
    # Blend the motions for each of the motions
    for motion in motions:
        blend_motion = BlendMotion("idle", motion)
        blend_motion.run()

    # Fix the strips timings for all the NLA tracks
    adjust_frames = AdjustFrames("idle", offset=10)
    adjust_frames.fix_strips_timings()

    # Make the armature objects invisible in the outliner
    make_invisible = MakeInvisible()
    make_invisible.run()
    # Render the animation to the output directory with video format
    renderer = Render(
        Config.RENDER_PATH,
        "FFMPEG",
        1,
        Config.TOTAL_FRAMES,
    )
    renderer.run()
    # Export the armature as FBX
    export_fbx = Exporter(
        "idle", Config.RENDER_PATH + '\\', "idle.fbx"
    )
    export_fbx.run()
    # Saving the main file (not needed for now)
    # bpy.ops.wm.save_mainfile(
    #     filepath="C:\\Users\\User\\Desktop\\FYP\\blender-utils\\Xbot.blend"
    # )


if __name__ == "__main__":
    main()