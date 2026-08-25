#Kommentare 
import numpy as np
import matplotlib.pyplot as plt
from ray import Ray



def plot_bezier_surface(surface, ray, solution, control_points):
        resolution = 30 #Anzahl von Punkten bestimmmen 30x30 

        u_values = np.linspace(0, 1, resolution) #– also gleichmäßig verteilte Werte zwischen 0 und 1
        v_values = np.linspace(0, 1, resolution)

        X = np.zeros((resolution, resolution)) #leeres Zahlenfeld, das mit 0 gefüllt ist
        Y = np.zeros((resolution, resolution))
        Z = np.zeros((resolution, resolution))

        for i, u in enumerate(u_values):
            for j, v in enumerate(v_values):
                point = surface.evaluate(u, v) #aktuelle Kombination aus u und v

                X[i, j] = point[0] #array füllen mit zeile und spalte 
                Y[i, j] = point[1]
                Z[i, j] = point[2]

        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")

        # Bézier-Fläche zeichnen
        ax.plot_surface(X, Y, Z, alpha=0.7)

        # ---------------------------------------------------------
        # Kontrollpunkte und Kontrollnetz
        # ---------------------------------------------------------

        control_points = np.array(control_points)

        # Kontrollpunkte darstellen
        ax.scatter(
            control_points[:, :, 0],
            control_points[:, :, 1],
            control_points[:, :, 2],
            color="red",
            alpha=0.5,
            s=40,
            label="Control Points"
        )

        # Kontrollnetz in u-Richtung
        for i in range(control_points.shape[0]):
            ax.plot(
                control_points[i, :, 0],
                control_points[i, :, 1],
                control_points[i, :, 2],
                color="black",
                linewidth=1,
                alpha=0.4
            )

        # Kontrollnetz in v-Richtung
        for j in range(control_points.shape[1]):
            ax.plot(
                control_points[:, j, 0],
                control_points[:, j, 1],
                control_points[:, j, 2],
                color="black",
                linewidth=1
            )

        # ---------------------------------------------------------
        # Ray zeichnen
        # ---------------------------------------------------------

        t_values = np.linspace(0, 2.5, 50)

        ray_points = np.array([
            ray.evaluate(t) for t in t_values
        ])

        ax.plot(
            ray_points[:, 0],
            ray_points[:, 1],
            ray_points[:, 2],
            color="purple",
            linewidth=3,
            label="Ray"
        )

        # Ursprung des Rays markieren
        ray_origin = ray.evaluate(0)

        ax.scatter(
            ray_origin[0],
            ray_origin[1],
            ray_origin[2],
            color="black",
            s=25,
            label="Ray Origin"
        )

        # ---------------------------------------------------------
        # Schnittpunkt aus der berechneten Lösung
        # ---------------------------------------------------------

        if solution is not None:

            u = solution[0]
            v = solution[1]
            t = solution[2]

            intersection = ray.evaluate(t)

            ax.scatter(
                intersection[0],
                intersection[1],
                intersection[2],
                color="orange",
                s=120,
                label="Intersection"
            )

            # Schnittpunkt mit den Parametern beschriften
            ax.text(
                intersection[0],
                intersection[1],
                intersection[2],
                r"$P=S(u^*,v^*)$",
                fontsize=8
            )

            # Senkrechte Hilfslinie vom Schnittpunkt zur xy-Ebene
            ax.plot(
                [intersection[0], intersection[0]],
                [intersection[1], intersection[1]],
                [0, intersection[2]],
                linestyle="--",
                color="gray",
                linewidth=1
            )

        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")

        ax.legend()
        plt.show()