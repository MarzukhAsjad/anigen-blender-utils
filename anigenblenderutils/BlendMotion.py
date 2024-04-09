import bpy


class BlendMotion:
    """
    A class to push down the active action to the NLA tracks and adjust the time frames of the strips.

    ...

    Attributes
    ----------
    armature_name : str
        a formatted string to print out the name of the armature
    action_name : str
        a formatted string to print out the name of the action

    Methods
    -------
    __init__(self, armature_name, action_name):
        Initializes the BlendMotion object with the given armature name and action name
    select_armature(self, armature_name):
        Selects the armature object with the given name
    get_uppermost_nla_track(self, armature_obj):
        Retrieves the uppermost NLA track that contains actions for the given armature object
    get_last_frame(self, uppermost_track):
        Retrieves the last frame of the last strip in the given NLA track
    switch_to_nla_editor(self):
        Splits active editor to existing editor and the NLA Editor
    push_down_action(self, armature_obj, uppermost_track, action, last_frame):
        Pushes down the given action to the NLA tracks and adjusts the time frames
    fix_strips_timings(self, armature_obj):
        Iterates over all the strips in the NLA tracks of the armature and adjusts the start and end time frames of the strips
    run(self):
        Orchestrates the execution of the script
    """

    def __init__(self, armature_name, action_name):
        """
        Parameters
        ----------
        armature_name : str
            The name of the armature object to select
        action_name : str
            The name of the action to push down to the NLA tracks
        """
        self.armature_name = armature_name
        self.action_name = action_name

    def select_armature(self, armature_name):
        """
        Selects the armature object with the given name

        Parameters:
        - armature_name: The name of the armature object to select

        Returns:
        - The selected armature object if found, None otherwise
        """
        # Select the armature object with the armature name
        armature_obj = bpy.data.objects.get(armature_name)
        if armature_obj is None or armature_obj.type != "ARMATURE":
            print("Armature object not found.")
            return None
        else:
            # Set 'Idle' armature object as the active object
            bpy.context.view_layer.objects.active = armature_obj
            armature_obj.select_set(True)
            return armature_obj

    def get_uppermost_nla_track(self, armature_obj):
        """
        Retrieves the uppermost NLA track that contains actions for the given armature object

        Parameters:
        - armature_obj: The armature object to retrieve the uppermost NLA track from

        Returns:
        - The uppermost NLA track if found, None otherwise
        """
        # Get the NLA tracks
        nla_tracks = armature_obj.animation_data.nla_tracks

        # Get the uppermost NLA track that contains actions
        index = -1
        uppermost_track = nla_tracks[index]
        while len(uppermost_track.strips) == 0:
            index -= 1
        uppermost_track = nla_tracks[index]
        return uppermost_track

    def switch_to_nla_editor(self):
        """
        Splits active editor to existing editor and the NLA Editor

        Parameters:
        - None

        Returns:
        - None
        """
        # Switch to the NLA Editor
        # Get the active window
        window = bpy.context.window_manager.windows[0]

        # Find the desired area type
        area = None
        for a in window.screen.areas:
            if a.type == "TEXT_EDITOR":
                area = a
                break

        # Check if the area was found
        if area is not None:
            # Split the area vertically
            bpy.ops.screen.area_split(direction="VERTICAL", factor=0.5)

            # Find the newly created area
            new_area = None
            for a in window.screen.areas:
                if a != area:
                    new_area = a
                    break

            # Check if the new area was found
            if new_area is not None:
                # Set the new area type to "NLA_EDITOR"
                new_area.type = "NLA_EDITOR"
            else:
                print("New area not found.")
        else:
            print("TEXT_EDITOR area not found.")

    def push_down_action(self, armature_obj, uppermost_track, action):
        """
        Pushes down the given action to the NLA tracks and adjusts the time frames

        Parameters:
        - action: The action to push down to the NLA tracks
        - last_frame: The last frame of the uppermost NLA track

        Prints:
        - The name of the pushed-down strip if successful, or a message if the action was not pushed down
        """
        # Set the correct context for the operator
        # Push down the action to the NLA tracks
        if action is not None:
            track = armature_obj.animation_data.nla_tracks.new()
            track.strips.new(action.name, 0, action)
            armature_obj.animation_data.action = None
        # Update the uppermost_track to the newly created track
        uppermost_track = self.get_uppermost_nla_track(armature_obj)
        # Get the pushed-down strip
        pushed_down_strip = None
        for strip in uppermost_track.strips:
            if strip.action.name == action.name:
                pushed_down_strip = strip
                break

        if pushed_down_strip is not None:
            print("Push down SUCCESS of strip:", pushed_down_strip.name)
            pushed_down_strip.use_auto_blend = True
        else:
            print("Action not pushed down to NLA tracks.")

    def run(self):
        """
        The main function that orchestrates the execution of the script
        Calls other functions to select the armature, retrieve the uppermost NLA track,
        get the last frame, switch to the NLA Editor, and push down the action to the NLA tracks
        """
        armature_obj = self.select_armature(self.armature_name)
        if armature_obj is not None:
            print(armature_obj.name)
            uppermost_track = self.get_uppermost_nla_track(armature_obj)
            self.switch_to_nla_editor()
            action = bpy.data.actions.get(self.action_name)
            if action is not None:
                armature_obj.animation_data.action = action
                self.push_down_action(armature_obj, uppermost_track, action)
            else:
                print("Action not found:", self.action_name)


if __name__ == "__main__":
    blendMotion = BlendMotion("idle", "Jump Over")
    blendMotion.run()
