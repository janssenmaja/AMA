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
    
#ABLEITUNG !! JACOBI
    def derivative_u(self, u, v):
        n = self.control_points.shape[0] - 1 #Damit bestimmen wir den Grad in u-Richtung (3 Kontrollpunkte in u-Richtung -> n = 3-1 = 2)
        result = np.zeros(3) #vektor mit 3 nullen - befüllt man mit Kontrollpunkten 
        m = self.control_points.shape[1] - 1 #m ist der Grad in v-Richtung.

        for i in range(n):
            for j in range(len(self.control_points[0])): #„Gehe jeden benötigten Kontrollpunkt durch.“

                difference = (self.control_points[i + 1][j] - self.control_points[i][j] )#Wir nehmen zwei benachbarte Kontrollpunkte
                #Das ist ein Vektor, der beschreibt, wie sich der Kontrollpunkt in dieser Richtung verändert.

                weight_u = self.bernstein(i, n - 1, u) #durch die Ableitung sinkt der Grad um 1, daher n-1

                
                weight_v = self.bernstein(j, m, v)

                result += n * difference * weight_u * weight_v
                #entspricht der formel 
                # += Weil jeder Kontrollpunkt einen kleinen Beitrag zur gesamten Ableitung liefert. Wir sammeln diese Beiträge auf.
        return result

    def derivative_v(self, u, v):
        n = self.control_points.shape[0] - 1
        m = self.control_points.shape[1] - 1
        result = np.zeros(3)

        for i in range(n + 1):
            for j in range(m):

                difference = (
                    self.control_points[i][j + 1]
                    - self.control_points[i][j]
                )

                weight_u = self.bernstein(i, n, u)
                weight_v = self.bernstein(j, m - 1, v)

                result += m * difference * weight_u * weight_v

        return result