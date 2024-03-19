class Section:
    def __init__(self, type, endvalue, intensity=1.0):
        self.type = type
        self.endvalue = endvalue
        if self.endvalue < 0:
            self.endvalue = 0
        elif self.endvalue > 1:
            self.endvalue = 1
        self.intensity = intensity
    
    def evaluate(self, time):
        # Evaluate the section at a given time (0-1)
        if self.type == "rising":
            return time**(3/self.intensity) 
        elif self.type == "sinking":
            return 1-(1-time)**(3/self.intensity)
        elif self.type == "linear":
            return time
        return 0