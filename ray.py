import numpy as np

class Ray:

    def __init__(self, origin, direction):
        self.origin = np.array(origin, dtype=float) #o / ursprung des Strahls speichern
        self.direction = np.array(direction, dtype=float) #d / richtung  speichern

    def evaluate(self, t): #wenn es evaluate(1) ist, dann wird origin + 1 * directen gerechnet 
        return self.origin + t * self.direction