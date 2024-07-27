import bpy

class MakeInvisible:
    """
    A class to make armature objects and their children invisible in the 
    viewport and rendering, other than "idle".

    ...
    Methods
    -------
    run(self):
        Makes armature objects and their children invisible in the viewport and rendering.
    make_invisible_recursive(self, obj):
        Recursively makes the object and its children invisible in the viewport and rendering.
    """

    def make_invisible_recursive(self, obj):
        """
        Recursively makes the object and its children invisible in the viewport and rendering.
        """
        obj.hide_set(True)
        obj.hide_select = True
        obj.hide_viewport = True
        obj.hide_render = True
        for child in obj.children:
            self.make_invisible_recursive(child)

    def run(self):
        """
        Makes armature objects and their children invisible in the viewport and rendering.
        """
        # Get all armature objects in the scene
        armature_objects = [obj for obj in bpy.data.objects if obj.type == "ARMATURE"]

        # Make armature objects and their children invisible in the viewport and rendering
        for obj in armature_objects:
            if obj.name == "idle":
                continue
            self.make_invisible_recursive(obj)

def main():
    # Create an instance of the MakeInvisible class
    make_invisible = MakeInvisible()
    make_invisible.run()

# Call the main function
if __name__ == "__main__":
    main()