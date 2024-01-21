import numpy as np
import matplotlib.pyplot as plt
import math

class LinearTransformations:
    def __init__(self):
        self.xmin, self.xmax, self.ymin, self.ymax = -8, 8, -8, 8

    def cartesian_plane(self):
        ticks_frequency = 1
        fig, ax = plt.subplots(figsize=(10, 10))

        ax.set(xlim=(self.xmin-1, self.xmax+1), ylim=(self.ymin-1, self.ymax+1), aspect='equal')

        ax.spines['bottom'].set_position('zero')
        ax.spines['left'].set_position('zero')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        ax.set_xlabel('x', size=14, labelpad=-24, x=1.03)
        ax.set_ylabel('y', size=14, labelpad=-21, y=1.02, rotation=0)

        x_ticks = np.arange(self.xmin, self.xmax+1, ticks_frequency)
        y_ticks = np.arange(self.ymin, self.ymax+1, ticks_frequency)
        ax.set_xticks(x_ticks[x_ticks != 0])
        ax.set_yticks(y_ticks[y_ticks != 0])

        ax.set_xticks(np.arange(self.xmin, self.xmax+1), minor=True)
        ax.set_yticks(np.arange(self.ymin, self.ymax+1), minor=True)

        ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

        arrow_fmt = dict(markersize=4, color='black', clip_on=False)
        ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
        ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)

        for x in range(-8, 9):
            ax.plot([x, x], [self.ymin, self.ymax], color='grey', linestyle='-', linewidth=1, alpha=0.2)
        for y in range(-8, 9):
            ax.plot([self.xmin, self.xmax], [y, y], color='grey', linestyle='-', linewidth=1, alpha=0.2)

        return ax

    def new_vector(self, grid, x:float, y:float, scaled: bool, scalar: float):
        if scaled == True:
            grid.arrow(0, 0, x*scalar, y*scalar, width=0.05)
            return [x*scalar, y*scalar]
        else:
            grid.arrow(0, 0, x, y, width=0.05)
            return [x, y]

    def matrix(self, grid, m):
        x_val, y_val = np.meshgrid(np.linspace(self.xmin, self.xmax, 10), np.linspace(self.ymin, self.ymax, 10))
        transformed_points = np.dot(m, np.vstack([x_val.flatten(), y_val.flatten()]))

        tx = transformed_points[0, :].reshape(x_val.shape)
        ty = transformed_points[1, :].reshape(y_val.shape)

        grid.streamplot(x_val[0, :], y_val[:, 0], tx, ty, color='grey', linewidth=1, density=0.4)
        return [m[0][0], m[1][0]], [m[0][1], m[1][1]]
    
    def determinant(self, M):
        plt.text(9, 9, f"Determinant = {(M[0][0] * M[1][1]) - (M[1][0] * M[0][1])}")
        return (M[0][0] * M[1][1]) - (M[1][0] * M[0][1])

    def eigenvalues(self, M):
        mean = (M[0][0] + M[1][1]) / 2
        product = self.determinant(M)
        e = mean + math.sqrt(mean**2 - product), mean - math.sqrt(mean**2 - product)
        plt.text(-9, 9, f"Eigenvalues = {e}")

    def matrix_multiplication(self, M1, M2):
        new_matrix = [[0, 0], [0, 0]]
        new_matrix[0][0], new_matrix[0][1] = (M1[0][0] * M2[0][0]) + (M1[1][0] * M2[0][1]), (M1[0][1] * M2[0][0]) + (M1[1][1] * M2[0][1])
        new_matrix[1][0], new_matrix[1][1] = (M1[0][0] * M2[1][0]) + (M1[1][0] * M2[1][1]), (M1[0][1] * M2[0][1]) + (M1[1][1] * M2[1][1])  
        return new_matrix
    
    def dot_product_and_angle(self, v1:list, v2:list):
        def dot_product(v1, v2):
            dot = v1[0] * v2[0] + v1[1] * v2[1]
            plt.text(-9,-9, f"Dot product of these 2 vectors are: {dot}")
            return dot
        magnitude_v1 = math.sqrt(dot_product(v1, v1))
        magnitude_v2 = math.sqrt(dot_product(v2, v2))

        dot = dot_product(v1, v2)
        vectors = dot / math.sqrt(magnitude_v1 * magnitude_v2)
        cos = max(-1, min(1, vectors))

        angle = math.acos(cos)
        plt.text(v1[0], v2[0], f"Angle between the 2 vectors are: {round(math.degrees(angle), 2)}")
        return dot_product
    
    def cross_product(self, v1:list, v2:list):
        matrix = [v1, v2]
        plt.text(v1[1], v2[1], f"Cross product of the 2 vectors are: {self.determinant(matrix)}")
        
c = LinearTransformations()
plane = c.cartesian_plane()
# Functions are to be used in this file, and executed on the main.py file.
