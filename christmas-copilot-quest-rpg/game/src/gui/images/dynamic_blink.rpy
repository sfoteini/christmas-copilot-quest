init -1 python in dynamic_blink:

    class DynamicBlink(renpy.display.layout.DynamicDisplayable):
        """
        A dynamic displayable that alternates between two images at a random interval.
        It is used to create a blinking effect for character sprites.

        The code is based on Ruolin Zheng's implementation found at:
        https://gist.github.com/RuolinZheng08/b845f416ebda5b02ebc6b62379105564
        """

        def __init__(self, *args, **kwargs):
            """
            Initializes the dynamic displayable.

            :param args: The two images to alternate between.
            :param kwargs: Additional arguments.
            """
            self.current_image = args[1]
            self.blink_images = args
            self.blink_start_time = -1.0 # arbitrary number to force normal start

            # cache a random duration because calling random on each frame is too heavy
            # but we don't want multiple on-screen sprites to be always blinking at the same moment
            self.blink_interval = 2.0 + renpy.random.random() * 5.0
            self.blink_duration = 0.2

            kwargs.update({"_predict_function": self.blink_images})

            super().__init__(self.show_blink_image, *args, **kwargs)

        def show_blink_image(self, st, at, *args, **kwargs):
            """
            Determines which image to show based on the start time and the blink interval. The start time (st)
            represents the time (in seconds) since the displayable was first shown.
            """
            if self.current_image == args[1]:
                if st > self.blink_start_time:
                    self.blink_start_time = st + self.blink_interval
                    self.current_image = args[0]
            else:
                if st > self.blink_start_time:
                    self.blink_start_time = st + self.blink_duration
                    self.current_image = args[1]

            return self.current_image, 0
