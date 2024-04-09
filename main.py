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


def main():
    # TODO: Make this dynamically take input from external sources
    motions = [
        "backward_happy_walk",
        "backwards_running",
        "boxing_left_side_step_walk",
        "careful_walk",
        "crouched_walking",
        "male_brutal_walk",
    ]

    # Import the fbx files
    # TODO: Make the path dynamic or somehow configurable
    # TODO: Make the importing of the files dynamic as well (check inside code for the class)
    find_and_import = FindAndImport(
        "C:\\Users\\User\\Desktop\\FYP\\Motions\\0409-first20"
    )
    find_and_import.run()

    # Rename the actions and blend the motions for each of the motions
    for motion in motions:
        rename_action = RenameAction(motion)
        rename_action.run()
    for motion in motions:
        blend_motion = BlendMotion("idle", motion)
        blend_motion.run()

    # Fix the strips timings for all the NLA tracks
    adjust_frames = AdjustFrames("idle", offset=10)
    adjust_frames.fix_strips_timings()

    # Make the armature objects invisible in the outliner
    make_invisible = MakeInvisible()
    make_invisible.run()
    # Render the animation
    # TODO: Change the path to a dynamic one
    renderer = Render(
        "C:\\Users\\User\\Desktop\\FYP\\Renders",
        "FFMPEG",
        1,
        bpy.context.scene.frame_end,
    )
    renderer.run()
    # Saving the main file (not needed for now)
    # bpy.ops.wm.save_mainfile(
    #     filepath="C:\\Users\\User\\Desktop\\FYP\\blender-utils\\inplacetest4.blend"
    # )


if __name__ == "__main__":
    main()
