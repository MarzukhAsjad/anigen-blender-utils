import bpy


class AdjustFrames:
    """
    A class used to adjust the timings of the strips in the NLA tracks of an armature object.

    ...

    Attributes
    ----------
    armature_obj : obj
        an armature object whose NLA tracks' timings are to be adjusted
    offset : int
        the offset to be used to adjust the start and end time frames of the strips

    Methods
    -------
    fix_strips_timings():
        Adjusts the start and end time frames of the strips in the NLA tracks of the armature object.
    """

    def __init__(self, armature_obj, offset):
        """
        Constructs all the necessary attributes for the AdjustFrames object.

        Parameters
        ----------
            armature_obj : obj
                an armature object whose NLA tracks' timings are to be adjusted
        """
        self.armature_obj = bpy.data.objects.get(armature_obj)
        self.offset = offset

    def fix_strips_timings(self):
        """
        This function iterates over all the strips in the
        NLA tracks of the armature and adjusts the start and
        end time frames of the strips.

        The frame start is initialised as the last frame of the previous strip - offset.
        The frame end is set as the frame start + duration of the strip.
        If auto blend is not turned on, it is turned on.
        The last frame of the last strip of the current NLA track is recorded for next iteration use.
        """

        # Variable init
        last_frame = 0
        nla_tracks = self.armature_obj.animation_data.nla_tracks
        current_strip = None
        # Iterate through the NLA tracks (assuming each track has one strip)
        for track in nla_tracks:
            current_strip = track.strips[0]
            # Extract the action from the strip
            action = current_strip.action
            # Delete the current strip
            if current_strip.name != "idle":
                track.strips.remove(current_strip)
                # Initialise the frame start as last frame of previous strip - offset
                frame_start = max(0, last_frame - self.offset)
                # Paste it to the desired time frame start within the NLA track
                new_strip = track.strips.new(
                    name=action.name, action=action, start=int(frame_start)
                )
                # DEBUGGING
                print("frame_start:", new_strip.frame_start)
                # Set the frame end as frame start + duration of the strip
                # Get the action's frame duration
                duration = action.frame_range[1] - action.frame_range[0]
                frame_end = frame_start + duration
                print("frame_end:", new_strip.frame_end)
                new_strip.use_auto_blend = True
                # Record the last frame of the last strip of the current NLA track for next iteration use
                last_frame = frame_end
            else:
                last_frame = current_strip.frame_end


if __name__ == "__main__":
    blendMotion = AdjustFrames("Idle", offset=10)
    blendMotion.run()
