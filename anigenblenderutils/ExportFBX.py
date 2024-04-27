import bpy


class FBXExporter:
    """
    A class for exporting an armature and its animations as an FBX file.

    ...

    Attributes:
    ----------
    armature_name : str
        The name of the armature object to export.
    export_path : str
        The path where the exported FBX file will be saved.
    export_filename : str
        The filename of the exported FBX file.

    Methods:
    -------
    __init__(self, armature_name, export_path, export_filename):
        Initializes the FBXExporter class with the given armature name, export path, and export filename.
    export_fbx(self):
        Runs the export process.
    run(self):
        The main method that runs the export process.
    """

    def __init__(self, armature_name, export_path, export_filename):
        """
        Initializes the FBXExporter class.

        Args:
            armature_name (str): The name of the armature object to export.
            export_path (str): The path where the exported FBX file will be saved.
            export_filename (str): The filename of the exported FBX file.
        """
        self.armature_name = armature_name
        self.export_path = export_path
        self.export_filename = export_filename

    def export_fbx(self):
        """
        Runs the export process.

        Recursively selects all objects under the specified armature, bakes all NLA tracks into a single animation,
        and exports it as an FBX file.

        Prints "Armature not found!" if the specified armature is not found.
        Prints "Export complete!" when the export process is finished.
        """
        # Find the specified armature
        armature = bpy.data.objects.get(self.armature_name)
        if armature is None:
            print("Armature not found!")
        else:
            # Clear the current selection
            bpy.ops.object.select_all(action="DESELECT")

            # Set the active object to the armature
            bpy.context.view_layer.objects.active = armature

            # Select the armature
            armature.select_set(True)

            # Select all objects recursively under the armature
            bpy.ops.object.select_hierarchy(direction="CHILD", extend=True)

            # Get all NLA tracks
            nla_tracks = armature.animation_data.nla_tracks

            # Create a new action to bake the NLA tracks into
            new_action = bpy.data.actions.new(name="Baked_Action")

            # Set the new action as the current action
            armature.animation_data.action = new_action

            # Bake all NLA tracks into the new action
            bpy.ops.nla.bake(
                frame_start=bpy.context.scene.frame_start,
                frame_end=bpy.context.scene.frame_end,
                step=1,
                only_selected=False,
                visual_keying=True,
                clear_constraints=False,
                use_current_action=True,
                bake_types={"OBJECT"},
            )

            # Export the selected objects as FBX
            bpy.ops.export_scene.fbx(
                filepath=self.export_path + self.export_filename,
                use_selection=True,
            )

            print("Export complete!")
            
    def run(self):
        """
        The main method that runs the export process.
        """
        self.export_fbx()


if __name__ == "__main__":
    # Create an instance of the FBXExporter class
    exporter = FBXExporter(
        "idle", "C:\\Users\\User\\Desktop\\FYP\\Renders\\", "idle.fbx"
    )

    # Run the export process
    exporter.run()
