from RenamingAction import RenameAction
from FindAndImport import FindAndImport
from BlendMotion import BlendMotion
from AdjustFrames import AdjustFrames


# TODO: Readjust the main function to properly connect the classes
def main():
    # Create instances of the classes
    rename_action = RenameAction("Jump Over")
    find_and_import = FindAndImport("C:\\Users\\User\\Desktop\\FYP\\Motions")
    blend_motion = BlendMotion("idle", "Jump Over")
    adjust_frames = AdjustFrames("idle")  # Create an instance of AdjustFrames

    # Call the run method of each instance
    rename_action.run()
    find_and_import.run()
    blend_motion.run()
    adjust_frames.fix_strips_timings()  # Call the fix_strips_timings method of the AdjustFrames instance


if __name__ == "__main__":
    main()
