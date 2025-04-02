import onecode
import os
from .geological_mapping_2d import plot_2d_map
from .geological_mapping_3d import plot_3d_map
from onecode import Project, dropdown, file_input, text_input, file_output, Logger

def run():

    # Dropdown to select map display mode
    display_mode = dropdown(
        key="display_mode",
        options=["2D", "3D"],
        value="2D",  # Default value
        label="Select Map Display Mode"
    )

    map_file = file_input(
        "map_file",
        value="",  # Start blank
        label="Path to Map File"
    )
  
    # Validate the file actually exists
    if not os.path.exists(map_file):
        raise FileNotFoundError(f"[map_file] File not found: {map_file}")

    Logger.info(f"Using map file: {map_file}")
    
    map_header = text_input(
        "map_header",
        value="0,3,4,5",
        label="Skip lines, X column, Y column, Z column"
    )

    grid_points = text_input(
        "grid_points",
        value="100",
        label="Number of Grid Points"
    )
    
    # File output to save the generated map
    output_file = file_output("output_map", "output_map.png" if display_mode == "2D" else "output_map.html")

    # Log the input parameters
    Logger.info(f"Map File: {map_file}, Header: {map_header}, Grid Points: {grid_points}, Visualization Mode: {display_mode}")

    
    # Convert grid_points from text to int
    try:
        point_no = int(grid_points)
    except ValueError:
        Logger.error("Invalid input for grid points. Please enter a valid integer.")
        return

    # Call the appropriate function based on display mode
    try:
        if display_mode == "2D":
            result = plot_2d_map(map_file, map_header, point_no=point_no, output_path=output_file)
        elif display_mode == "3D":
            result = plot_3d_map(map_file, map_header, output_path=output_file)
        Logger.info(f"Map generated and saved to: {result}")
        
    except ValueError:
        Logger.error("Invalid map_header_info format. Please check 'skip_row,x_col,y_col,z_col' values again.")
        return
