#beschreibt an unserem aktuellen Punkt, wie sich die Bézier-Fläche und der Strahl lokal verändern.
import numpy as np

def jacobian(surface, ray, u, v, t): #J(u,v,t)
    du = surface.derivative_u(u, v) #du = [dx, dy, dz] - erste Spalte unserer Jacobi-Matrix.
    dv = surface.derivative_v(u, v) # ableitung nach v - zweite spalte
    d = ray.direction #dritte spalte -D  (t

    J = np.column_stack((du, dv, -d)) #Setze diese Vektoren nebeneinander als Spalten.
    return J
