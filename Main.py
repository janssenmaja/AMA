import numpy as np
from bezier_surface import BezierSurface
from visualization import plot_bezier_surface
from ray import Ray
from equation_system import equation_system
from jacobian import jacobian
from newton_solver import newton_solver

#control_points = [
#    [[0, 0, 0], [0, 1, 0], [0, 2, 0]],
#    [[1, 0, 0], [1, 1, 1], [1, 2, 0]],
#    [[2, 0, 0], [2, 1, 0], [2, 2, 0]]
#]

control_points = [
    [[0, 0, 0], [0, 1, 1], [0, 2, 0]],
    [[1, 0, 1], [1, 1, 3], [1, 7, 1]],
    [[2, 0, 0], [2, -4, 1], [2, 2, 0]]
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

result = equation_system(surface, ray, 0.5, 0.5, 1.75)

print(result)


J = jacobian(surface, ray, 0.5, 0.5, 1.75)

print("Jacobian:")
print(J)

initial_guess = [0.4, 0.6, 1.5]

solution = newton_solver(
    surface,
    ray,
    initial_guess
)

print("Newton-Lösung:")
print(solution)

plot_bezier_surface(surface, ray)