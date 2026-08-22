import math
import numpy as np


class BezierSurface:

    def __init__(self, control_points):
        self.control_points = np.array(control_points, dtype=float)
    #speichert die Kontrollpunkte 

    def bernstein(self, i, n, t):
        #berechnet die Bernsteinformel
        return (
            math.comb(n, i)
            * t**i
            * (1 - t)**(n - i)
        )
    def evaluate(self, u, v):
        #berechnet die Punkte auf der Bezierfläche
        n = self.control_points.shape[0] - 1
        m = self.control_points.shape[1] - 1

        point = np.zeros(3)

        for i in range(n + 1):
            for j in range(m + 1):
                weight_u = self.bernstein(i, n, u)
                weight_v = self.bernstein(j, m, v)

                point += (
                    weight_u
                    * weight_v
                    * self.control_points[i, j]
                )

        return point