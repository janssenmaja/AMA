import numpy as np
from equation_system import equation_system
from jacobian import jacobian

def newton_solver(surface, ray, initial_guess): #initial_guess = Startschätzung für (u, v, t)
    x = np.array(initial_guess, dtype=float) #vektor x mit 3 werten 
    max_iterations = 20
    for iteration in range(max_iterations): 
        F = equation_system(surface, ray, x[0], x[1], x[2]) #Wenn wir am Schnittpunkt sind, dann ist F = 0, sonst enthällt F den Fehler 

        J = jacobian( #Wie müssen wir u,v,t verändern, um näher zum Schnittpunkt zu kommen?
            surface,
            ray,
            x[0],
            x[1],
            x[2]
        )
        delta_x = np.linalg.solve(J, -F) #löst das Gleichungssystem J * delta_x = -F, um die Änderung in den Parametern zu finden
        x = x + delta_x #aktualisiert die Parameter u, v, t - neuer Punkt 
        print(f"Iteration {iteration + 1}: x = {x}")        
        F_new = equation_system(
            surface,
            ray,
            x[0],
            x[1],
            x[2]
        )
        error = np.linalg.norm(F_new) #berechnet die Größe des Fehlers, um zu sehen, wie nah wir am Schnittpunkt sind

        if error < 1e-6: #Wenn der Fehler kleiner als 0.000001 ist, betrachten wir die Lösung als genau genug und beenden die Schleife.
            break
    return x