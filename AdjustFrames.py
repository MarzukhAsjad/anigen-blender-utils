class AdjustFrames:
    """
    A class used to adjust the timings of the strips in the NLA tracks of an armature object.

    ...

    Attributes
    ----------
    armature_obj : obj
        an armature object whose NLA tracks' timings are to be adjusted

    Methods
    -------
    fix_strips_timings():
        Adjusts the start and end time frames of the strips in the NLA tracks of the armature object.
    """

    def __init__(self, armature_obj):
        """
        Constructs all the necessary attributes for the AdjustFrames object.

        Parameters
        ----------
            armature_obj : obj
                an armature object whose NLA tracks' timings are to be adjusted
        """

        self.armature_obj = armature_obj

    def fix_strips_timings(self):
        """
        This function iterates over all the strips in the
        NLA tracks of the armature and adjusts the start and
        end time frames of the strips.

        The frame start is initialised as the last frame of the previous strip - 10.
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
            # Initialise the frame start as last frame of previous strip - 10
            frame_start = max(0, last_frame - 10)
            # Set the frame end as frame start + duration of the strip
            frame_end = frame_start + (
                current_strip.frame_end - current_strip.frame_start
            )
            # Print frame end and start
            print("Frame start:")
            print(frame_start)
            print("Frame end: ")
            print(frame_end)
            current_strip.frame_start = frame_start
            current_strip.frame_end = frame_end
            # Turn auto blend on if not turned on
            current_strip.use_auto_blend = True
            # Record the last frame of the last strip of the current NLA track for next iteration use
            last_frame = frame_end


if __name__ == "__main__":
    blendMotion = AdjustFrames("Idle")
    blendMotion.run()
