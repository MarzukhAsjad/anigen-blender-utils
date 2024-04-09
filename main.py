import os, sys, bpy

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)
from anigenblenderutils.RenameAction import RenameAction
from anigenblenderutils.FindAndImport import FindAndImport
from anigenblenderutils.BlendMotion import BlendMotion
from anigenblenderutils.AdjustFrames import AdjustFrames
from anigenblenderutils.MakeInvisible import MakeInvisible


# TODO: Readjust the main function to properly connect the classes
def main():
    # TODO: Make this dynamically take input from external sources
    motions = ["crouched_walking", "Swing_Dancing"]

    # Import the fbx files
    # TODO: Make the path dynamic or somehow configurable
    # TODO: Make the importing of the files dynamic as well (check inside code for the class)
    find_and_import = FindAndImport("C:\\Users\\User\\Desktop\\FYP\\Motions")
    find_and_import.run()

    # Rename the actions and blend the motions for each of the motions
    for motion in motions:
        rename_action = RenameAction(motion)
        rename_action.run()
    for motion in motions:
        print("BOOM")
        blend_motion = BlendMotion("idle", motion)
        blend_motion.run()

    # Fix the strips timings for all the NLA tracks
    adjust_frames = AdjustFrames("idle", offset=10)
    adjust_frames.fix_strips_timings()

    # Make the armature objects invisible in the outliner
    make_invisible = MakeInvisible()
    make_invisible.run()
    # TODO: uncomment the saving code once done
    # Save the main file
    bpy.ops.wm.save_mainfile(
        filepath="C:\\Users\\User\\Desktop\\FYP\\blender-utils\\inplacetest4.blend"
    )


if __name__ == "__main__":
    main()
