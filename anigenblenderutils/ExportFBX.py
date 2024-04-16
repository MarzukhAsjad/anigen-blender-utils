import bpy


class FBXExporter:
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

    def run(self):
        """
        Runs the export process.

        Prints "Armature not found!" if the specified armature is not found.
        Otherwise, sets the active object to the armature, selects the armature,
        and exports it as an FBX file.

        Prints "Export complete!" when the export process is finished.
        """
        # Find the specified armature
        armature = bpy.data.objects.get(self.armature_name)
        if armature is None:
            print("Armature not found!")
        else:
            # Set the active object to the armature
            bpy.context.view_layer.objects.active = armature

            # Select the armature
            armature.select_set(True)

            # Export the armature as FBX
            bpy.ops.export_scene.fbx(
                filepath=self.export_path + self.export_filename, use_selection=True
            )

            print("Export complete!")


if __name__ == "__main__":
    # Create an instance of the FBXExporter class
    exporter = FBXExporter(
        "idle", "C:\\Users\\User\\Desktop\\FYP\\Renders\\", "idle.fbx"
    )

    # Run the export process
    exporter.run()
