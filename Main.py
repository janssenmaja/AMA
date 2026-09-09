import numpy as np
from bezier_surface import BezierSurface
from visualization import plot_bezier_surface
from ray import Ray
from equation_system import equation_system
from jacobian import jacobian
from newton_solver import newton_solver
from broyden_solver import broyden_solver
import time

#control_points = [
#    [[0, 0, 0], [0, 1, 1], [0, 2, 0]],
#    [[1, 0, 1], [1, 1, 3], [1, 2, 1]],
#    [[2, 0, 0], [2, 1, 1], [2, 2, 0]]
#]

#control_points = [
#    [[0, 0, 0], [0, 1, 0], [0, 2, 0]],
#    [[1, 0, 0], [1, 1, 1], [1, 2, 0]],
#    [[2, 0, 0], [2, 1, 0], [2, 2, 0]]
#]

#control_points = [
#    [[0, 0, 0], [0, 1, 1], [0, 2, 0]],
#    [[1, 0, 1], [1, 1, 3], [1, 7, 1]],
#    [[2, 0, 0], [2, -4, 1], [2, 2, 0]]
#]

control_points = [
    [[0, 0, 0], [0, 0.67, 0.8], [0, 1.33, 0.8], [0, 2, 0]],
    [[0.67, 0, 0.8], [0.67, 0.67, 1.8], [0.67, 1.33, 1.8], [0.67, 2, 0.8]],
    [[1.33, 0, 0.8], [1.33, 0.67, 1.8], [1.33, 1.33, 1.8], [1.33, 2, 0.8]],
    [[2, 0, 0], [2, 0.67, 0.8], [2, 1.33, 0.8], [2, 2, 0]]
]

surface = BezierSurface(control_points)
#erstellt die Bézier-Fläche aus deinen 9 Kontrollpunkten.

point = surface.evaluate(0.5, 0.5)
#berechnet den Punkt bzw. die Stelle auf der Fläche, bei der sowohl u als auch v in der Mitte liegen.

print(point)
#gibt die berechneten x,y,z-Koordinaten aus


# Einfacher Fall: senkrechter Schnitt durch die Fläche
# ray = Ray([1, 1, 2], [0, 0, -1])

# Schräger Schnitt durch die Fläche
# ray = Ray([0.7, 1.2, 2], [0, 0, -1])
# ray = Ray([0.7, 1.2, -1.2], [0.25, 0.15, 1])

#ray für Tangential-/schwierigen Fall - hier keine gültigen Schnittpunkte 
ray = Ray([0.35, 0.6, 0.8], [0.2, 0, -0.1]) 


#außerhalb des gültigen Bézier-Parameterbereichs [0,1] - dh evtl. Solver-Konvergenz ≠ automatisch gültiger Ray-Surface-Intersection. - prüfen wir hier *
print(ray.evaluate(0))
print(ray.evaluate(1))
print(ray.evaluate(2))

result = equation_system(surface, ray, 0.5, 0.5, 1.75)

print(result)


J = jacobian(surface, ray, 0.5, 0.5, 1.75)

print("Jacobian:")
print(J)

#initial_guess = [0.2, 0.7, 1.0]
#initial_guess = [0.8, 0.2, 1.2] #schlechterer Startwert, um die Robustheit der Solver zu testen

initial_guesses = [ #testen mehrere Startwerte, um die Robustheit der Solver zu überprüfen
    [0.5, 0.5, 1.0],
    [0.8, 0.2, 1.2],
    [0.2, 0.8, 2.0],
]


# Ergebnisse speichern, damit wir später nicht nur den letzten Startwert betrachten
results = []


for initial_guess in initial_guesses:

    print("\nStartwert:", initial_guess)

    # Newton-Zeit messen
    start = time.perf_counter()

    newton_solution, newton_iterations = newton_solver(
        surface,
        ray,
        initial_guess
    )

    newton_time = time.perf_counter() - start

    # Broyden-Zeit messen
    start = time.perf_counter()

    broyden_solution, broyden_iterations = broyden_solver(
        surface,
        ray,
        initial_guess
    )

    broyden_time = time.perf_counter() - start

    print("Newton:", newton_solution, newton_iterations)
    print("Broyden:", broyden_solution, broyden_iterations)

    print("Newton-Zeit:", newton_time)
    print("Broyden-Zeit:", broyden_time)



#Für die Ausgabe der Residuen der beiden Solver 
    newton_residual = np.linalg.norm(
        equation_system(surface, ray, newton_solution[0], newton_solution[1], newton_solution[2])
    )
    broyden_residual = np.linalg.norm(
        equation_system(surface, ray, broyden_solution[0], broyden_solution[1], broyden_solution[2])
    )




    print("Newton Residual:", newton_residual)
    print("Broyden Residual:", broyden_residual)

    #gültige Lösung überprüfen, ob sie innerhalb des gültigen Bereichs liegt *
    if (newton_solution is not None
            and 0 <= newton_solution[0] <= 1
            and 0 <= newton_solution[1] <= 1
            and newton_solution[2] >= 0):

        print("Newton: gültiger Schnittpunkt")
        print(newton_solution)

    else:

        print("Newton: Kein gültiger Schnittpunkt")


    if (broyden_solution is not None
            and 0 <= broyden_solution[0] <= 1
            and 0 <= broyden_solution[1] <= 1
            and broyden_solution[2] >= 0):

        print("Broyden: gültiger Schnittpunkt")
        print(broyden_solution)

    else:

        print("Broyden: Kein gültiger Schnittpunkt")


    results.append({
        "initial_guess": initial_guess,
        "newton_solution": newton_solution,
        "newton_iterations": newton_iterations,
        "newton_time": newton_time,
        "newton_residual": newton_residual,
        "broyden_solution": broyden_solution,
        "broyden_iterations": broyden_iterations,
        "broyden_time": broyden_time,
        "broyden_residual": broyden_residual
    })



# Übersichtliche Zusammenfassung der Ergebnisse
print("\n" + "=" * 100)
print("ERGEBNISSE")
print("=" * 100)

print(
    f"{'Startwert':<20}"
    f"{'Newton It.':<12}"
    f"{'Broyden It.':<13}"
    f"{'Newton Zeit':<15}"
    f"{'Broyden Zeit':<15}"
    f"{'Newton Res.':<15}"
    f"{'Broyden Res.':<15}"
    f"{'Newton':<12}"
    f"{'Broyden':<12}"
)

print("-" * 100)

for result in results:

    newton_valid = (
        result["newton_solution"] is not None
        and 0 <= result["newton_solution"][0] <= 1
        and 0 <= result["newton_solution"][1] <= 1
        and result["newton_solution"][2] >= 0
    )

    broyden_valid = (
        result["broyden_solution"] is not None
        and 0 <= result["broyden_solution"][0] <= 1
        and 0 <= result["broyden_solution"][1] <= 1
        and result["broyden_solution"][2] >= 0
    )

    print(
        f"{str(result['initial_guess']):<20}"
        f"{result['newton_iterations']:<12}"
        f"{result['broyden_iterations']:<13}"
        f"{result['newton_time']:<15.6f}"
        f"{result['broyden_time']:<15.6f}"
        f"{result['newton_residual']:<15.2e}"
        f"{result['broyden_residual']:<15.2e}"
        f"{'gültig' if newton_valid else 'ungültig':<12}"
        f"{'gültig' if broyden_valid else 'ungültig':<12}"
    )

# gültige Newton-Lösung für die Visualisierung auswählen
solution = None

for result in results:

    newton_solution = result["newton_solution"]

    if (newton_solution is not None
            and 0 <= newton_solution[0] <= 1
            and 0 <= newton_solution[1] <= 1
            and newton_solution[2] >= 0):

        solution = newton_solution
        break


plot_bezier_surface(surface, ray, solution)