from RenamingAction import RenameAction
from FindAndImport import FindAndImport
from BlendMotion import BlendMotion


def main():
    # Create instances of the classes
    rename_action = RenameAction("Jump Over")
    find_and_import = FindAndImport("C:\\Users\\User\\Desktop\\FYP\\Motions")
    blend_motion = BlendMotion("idle", "Jump Over")

    # Call the run method of each instance
    rename_action.run()
    find_and_import.run()
    blend_motion.run()


if __name__ == "__main__":
    main()
