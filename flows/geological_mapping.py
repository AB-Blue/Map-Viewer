import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
import statistics


def plot_2d_map(map_path, map_header_info, point_no=100, output_path="output_map.png"):
    """
    Plots a 2D elevation contour map from an input file.

    Args:
        map_path (str): Path to the input map file.
        map_header_info (str): Header info as a comma-separated string (skip_row,x_col,y_col,z_col).
        point_no (int): Number of grid points for interpolation.
        output_path (str): Path to save the output map image.
    """
    # Parse map header
    map_header = list(np.array(map_header_info.split(',')).astype(int))
    skip_row = map_header[0]
    x_col = map_header[1] - 1
    y_col = map_header[2] - 1
    z_col = map_header[3] - 1

    # Read data
    data = np.loadtxt(map_path, skiprows=skip_row, usecols=[x_col, y_col, z_col], dtype=float)
    X, Y, Z = data[:, 0], data[:, 1], data[:, 2]

    # Ensure elevation consistency
    if statistics.mean(Z) > 0:
        Z = -Z

    # Grid definition
    x_min, x_max = X.min(), X.max()
    y_min, y_max = Y.min(), Y.max()

    xi = np.linspace(x_min, x_max, int(point_no))
    yi = np.linspace(y_min, y_max, int(point_no))
    xi, yi = np.meshgrid(xi, yi)

    # Interpolation
    zi = griddata((X, Y), Z, (xi, yi), method="linear")

    # Plotting
    plt.figure()
    plt.contour(xi, yi, zi, colors="black", levels=10)
    image = plt.contourf(xi, yi, zi, levels=50, cmap="jet")
    plt.colorbar(image, label="Elevation")

    map_name = os.path.splitext(os.path.basename(map_path))[0]
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(f"Elevation Contour Map\nMap Name: {map_name}")
    plt.grid(True)
    plt.show()
    
    # Save the output
    plt.savefig(output_path)
    plt.close()
    return output_path
