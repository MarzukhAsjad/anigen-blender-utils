import bpy


class MakeInvisible:
    """
    A class to make armature objects invisible in the outliner other than "idle"
    """

    def run(self):
        """
        Makes armature objects invisible in the outliner.
        """
        # Get all armature objects in the scene
        armature_objects = [obj for obj in bpy.data.objects if obj.type == "ARMATURE"]

        # Make armature objects invisible in the outliner
        for obj in armature_objects:
            if obj.name == "idle":
                continue
            obj.hide_set(True)
            obj.hide_select = True


def main():
    # Create an instance of the MakeInvisible class
    make_invisible = MakeInvisible()
    make_invisible.run()


# Call the main function
if __name__ == "__main__":
    main()
