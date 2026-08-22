import numpy as np
from bezier_surface import BezierSurface
from visualization import plot_bezier_surface
from ray import Ray

control_points = [
    [[0, 0, 0], [0, 1, 0], [0, 2, 0]],
    [[1, 0, 0], [1, 1, 1], [1, 2, 0]],
    [[2, 0, 0], [2, 1, 0], [2, 2, 0]]
]


surface = BezierSurface(control_points)
#erstellt die Bézier-Fläche aus deinen 9 Kontrollpunkten.

point = surface.evaluate(0.5, 0.5)
#berechnet den Punkt bzw.  die Stelle auf der Fläche, bei der sowohl u als auch v in der Mitte liegen.

print(point)
#gibt die berechneten x,y,z-Koordinaten aus


ray = Ray([1, 1, 2], [0, 0, -1])

print(ray.evaluate(0))
print(ray.evaluate(1))
print(ray.evaluate(2))


plot_bezier_surface(surface, ray)