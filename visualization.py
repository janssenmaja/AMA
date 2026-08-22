#Kommentare 
import numpy as np
import matplotlib.pyplot as plt
from ray import Ray



def plot_bezier_surface(surface, ray):
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

        ax.plot_surface(X, Y, Z)

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
        intersection = ray.evaluate(1.75) #momentan vorgegeben aber muss er eig selbst berechnen können - nur als test

        ax.scatter(
            intersection[0],
            intersection[1],
            intersection[2],
            color="black",
            s=50,
            label="Intersection"
    )

        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")

        ax.legend()
        plt.show()