import bpy, os, sys, re


class FindAndImport:
    """
    A class used to find and import fbx files from a directory.

    ...

    Attributes
    ----------
    directory : str
        a formatted string to print out the directory where the fbx files are located

    Methods
    -------
    find_file(filename)
        Returns the full path of the file if it exists in the directory.
    import_fbx(filepaths)
        Imports the fbx files located at the filepaths into the current Blender scene.
    run()
        The main method that finds and imports the fbx files.
    """

    def __init__(self, directory):
        """
        Constructs all the necessary attributes for the FindAndImport object.

        Parameters
        ----------
            directory : str
                directory where the fbx files are located
        """
        self.directory = directory

    def find_file(self, filename):
        """
        Finds a file in the directory.

        Parameters
        ----------
            filename : str
                name of the file to find

        Returns
        -------
            str
                full path of the file if it exists, otherwise None
        """
        file_path = os.path.join(self.directory, filename)
        if os.path.exists(file_path):
            return file_path
        else:
            print(f"File {filename} does not exist.")

    def import_fbx(self, filepaths):
        """
        Imports the fbx files into the current Blender scene.

        Parameters
        ----------
            filepaths : list
                list of filepaths where the fbx files are located
        """
        armature_name = "Armature"
        pattern = r"(?<=\\)[^\\]*(?=\.[^.]+$)"
        for filepath in filepaths:
            blend_dir = os.path.dirname(bpy.data.filepath)
            # Check if the directory is already in the path
            if blend_dir not in sys.path:
                sys.path.append(blend_dir)
            # Import the fbx file
            bpy.ops.import_scene.fbx(filepath=filepath)
            # Rename the armature object using regex and the filename
            armature_obj = bpy.data.objects["Armature"]
            match = re.search(pattern, filepath)
            if match:
                armature_name = match.group(0)
            print("Armature name [Find And Import]: ", armature_name)
            armature_obj.name = armature_name
            # Save the main file
            # bpy.ops.wm.save_mainfile(
            #     filepath="C:\\Users\\User\\Desktop\\FYP\\blender-utils\\inplacetest2.blend"
            # )
            # Rename the primary action for each of these imported fbxs
            # Also make them invisible

    def run(self):
        """
        The main method that finds and imports the fbx files.
        """
        # TODO: Make this dynamic
        files = [
            "male_strut_walk.fbx",
            "running_with_intention.fbx",
            "dodging_to_the_right_place.fbx",
            "hook_punch.fbx",
            "covering_face_in_shame_after_defeat.fbx",
        ]  # List of filenames to look up (usually fbx)
        filepaths = []  # Sequential list of filepaths stored
        for file_name in files:
            path = self.find_file(file_name)
            if path != None:
                filepaths.append(path)
            print(path)

        self.import_fbx(filepaths)


if __name__ == "__main__":
    finder = FindAndImport("C:\\Users\\User\\Desktop\\FYP\\Motions")
    finder.run()
