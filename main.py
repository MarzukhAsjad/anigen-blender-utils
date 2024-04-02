import os, sys, bpy

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)
from anigenblenderutils.RenameAction import RenameAction
from anigenblenderutils.FindAndImport import FindAndImport
from anigenblenderutils.BlendMotion import BlendMotion
from anigenblenderutils.AdjustFrames import AdjustFrames


# TODO: Readjust the main function to properly connect the classes
def main():
    # Create instances of the classes
    rename_action = RenameAction("Jump Over")
    find_and_import = FindAndImport("C:\\Users\\User\\Desktop\\FYP\\Motions")
    blend_motion = BlendMotion("idle", "Jump Over")
    adjust_frames = AdjustFrames(
        "idle", offset=10
    )  # Create an instance of AdjustFrames

    # Call the run method of each instance
    rename_action.run()
    find_and_import.run()
    blend_motion.run()
    adjust_frames.fix_strips_timings()  # Call the fix_strips_timings method of the AdjustFrames instance


if __name__ == "__main__":
    main()
