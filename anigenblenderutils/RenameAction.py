import bpy


class RenameAction:
    """
    A class to rename the active action in the Action Editor to the name of the armature object.

    ...

    Attributes
    ----------
    armature_name : str
        a formatted string to print out the name of the armature

    Methods
    -------
    select_armature_object():
        Selects the armature object with the given name
    switch_to_action_editor():
        Switches to the Action Editor
    rename_active_action(armature_obj):
        Renames the active action in the Action Editor to the name of the given armature object
    run():
        The main function that orchestrates the execution of the script
    """

    def __init__(self, armature_name):
        """
        Parameters
        ----------
        armature_name : str
            The name of the armature object to select
        """
        self.armature_name = armature_name

    def select_armature_object(self):
        """
        Selects the armature object with the name armature_name and sets it as the active object.

        Returns:
        The selected armature object, or None if it is not found or not of type "ARMATURE".
        """
        # Select the armature object
        armature_obj = bpy.data.objects.get(self.armature_name)
        if armature_obj is None or armature_obj.type != "ARMATURE":
            print("Armature object not found [Rename Action].")
            return None
        else:
            # Set armature object as the active object
            print("Armature found")
            bpy.context.view_layer.objects.active = armature_obj
            armature_obj.select_set(True)
            return armature_obj

    # TODO: Instead of switching the whole editor, create a partition for the action editor
    def switch_to_action_editor(self):
        # Get the active area
        area = None
        for window in bpy.context.window_manager.windows:
            for area in window.screen.areas:
                if area.type == "DOPESHEET_EDITOR":
                    break
            if area is not None:
                break

        # Set the area type and the UI mode
        area.type = "DOPESHEET_EDITOR"

        # Find the active space in the Dope Sheet Editor
        space = area.spaces.active
        if space is not None:
            # Set the UI mode to 'ACTION'
            print("Switching to the Action Editor")
            space.mode = "ACTION"

    def rename_active_action(self, armature_obj):
        """
        Renames the active action in the Action Editor to the name of the given armature object.

        Parameters:
        - armature_obj: The armature object whose name will be used to rename the active action.
        """
        # Get the active action in the Action Editor
        active_action = bpy.context.object.animation_data.action
        if active_action is not None:
            print("Active action name before renaming:", active_action.name)
            active_action.name = armature_obj.name
            print("Active action name after renaming:", active_action.name)
        else:
            print("No active action in the Action Editor.")

    def run(self):
        """
        The main function of the script.
        It selects the 'Jump Over' armature object, switches to the Action Editor,
        and renames the active action to the name of the armature object.
        """
        armature_obj = self.select_armature_object()
        if armature_obj is not None:
            self.switch_to_action_editor()
            self.rename_active_action(armature_obj)


if __name__ == "__main__":
    renameAction = RenameAction("Jump Over")
    renameAction.run()
