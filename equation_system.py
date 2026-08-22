import numpy as np
from bezier_surface import BezierSurface
from ray import Ray
#sagt uns, wie weit wir von einer Lösung entfernt sind.


def equation_system(surface, ray, u, v, t):
    surface_point = surface.evaluate(u, v) #Berechne den Punkt auf der Bézier-Fläche für die Parameter u und v
    ray_point = ray.evaluate(t) #macht daselbe für den Strahl 

    difference = surface_point - ray_point #Wie weit sind diese beiden Punkte voneinander entfernt? 
    #3D Vektor - difference = [x-Differenz, y-Differenz, z-Differenz]
    return np.array([
        difference[0],
        difference[1],
        difference[2]
    ])
    # wenn alle zusammen 0 sind, dann getroffen 

