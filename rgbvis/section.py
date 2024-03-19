class Section:
    """
    Represents a section of a visualization with a specific type, end value, and intensity.

    Attributes:
        type (str): The type of the section ("rising", "sinking", or "linear").
        endvalue (float): The end value of the section (between 0 and 1).
        intensity (float): The intensity of the section (default is 1.0).

    Methods:
        evaluate(time): Evaluates the section at a given time (0-1).

    """

    def __init__(self, type, endvalue, intensity=1.0):
        self.type = type
        self.endvalue = endvalue
        if self.endvalue < 0:
            self.endvalue = 0
        elif self.endvalue > 1:
            self.endvalue = 1
        self.intensity = intensity
    
    def evaluate(self, time):
        """
        Evaluates the section at a given time.

        Args:
            time (float): The time value (between 0 and 1).

        Returns:
            float: The evaluated value of the section at the given time.

        """
        if self.type == "rising":
            return time**(3/self.intensity) 
        elif self.type == "sinking":
            return 1-(1-time)**(3/self.intensity)
        elif self.type == "linear":
            return time
        return 0