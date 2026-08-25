import numpy as np
from equation_system import equation_system
from jacobian import jacobian


def broyden_solver(surface, ray, initial_guess):

    x = np.array(initial_guess, dtype=float)

    J = jacobian( #nur am Anfang und nicht innerhalb jeder iteration !!
        surface,
        ray,
        x[0],
        x[1],
        x[2]
    )

    max_iterations = 20

    for iteration in range(max_iterations):

        F = equation_system(
            surface,
            ray,
            x[0],
            x[1],
            x[2]
        )

        delta_x = np.linalg.solve(J, -F)

        x = x + delta_x

        F_new = equation_system(
            surface,
            ray,
            x[0],
            x[1],
            x[2]
        )

        delta_F = F_new - F

        J = J + np.outer(
            (delta_F - J @ delta_x),
            delta_x
        ) / (delta_x @ delta_x)

        error = np.linalg.norm(F_new)

        if error < 1e-6:
            break
        print(f"Iteration {iteration + 1}: x = {x}")

    return x, iteration + 1