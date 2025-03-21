import pyvista as pv

# method to plot map in a 3D view
def plot_3d_map(map_path, map_header_info, output_path):

    # Get parameters from map header info
    map_header = list(np.array(map_header_info.split(',')).astype(int))
    skip_row = map_header[0]
    x_col = map_header[1]-1
    y_col = map_header[2]-1
    z_col = map_header[3]-1

    # Read data from the text file
    self.map = np.loadtxt(map_path, skiprows = skip_row, usecols=[x_col, y_col, z_col],dtype=(float))
    X = self.map[:, 0] 
    Y = self.map[:, 1]  
    Z = self.map[:, 2]

    # For consistency the elevation is plotted with (-) sign
    if statistics.mean(Z) > 0:
        Z = -Z 

    # Convert data points to PyVista structured grid
    geological_grid = pv.StructuredGrid(X, Y, Z)
    print(geological_grid)

    # Create a colormap
    colormap = 'jet'  
    # geological_grid_scaled = geological_grid.scale([1,1,1])
    plotter.add_mesh(geological_grid, scalars = Z, cmap = colormap, show_scalar_bar = True, style = 'points')
    plotter.show_axes()
    plotter.show_bounds()
    plotter.show(interactive=True)
    
    # Export the plot to an HTML file
    plotter.export_html(output_path)
    plotter.close()

    return output_path
