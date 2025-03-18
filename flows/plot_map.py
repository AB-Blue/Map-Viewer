import onecode
import os
from .geological_mapping import plot_2d_map
from onecode import Project, file_input, text_input, file_output, Mode

def run():

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
        value="0,1,2,3",
        label="Skip lines, X column, Y column, Z column"
    )

    grid_points = text_input(
        "grid_points",
        value="100",
        label="Number of Grid Points"
    )
    
    # File output to save generated map image
    output_file = file_output("output_map", "output_map.png")

    # Log the input parameters
    onecode.Logger.info(f"Map File: {map_file}, Header: {map_header}, Grid Points: {grid_points}")

    # Convert grid_points from text to int
    try:
        point_no = int(grid_points)
    except ValueError:
        onecode.Logger.error("Invalid input for grid points. Please enter a valid integer.")
        return

    # Call the function to generate the plot
    result = plot_2d_map(map_file, map_header, point_no=point_no, output_path=output_file)
    onecode.Logger.info(f"Map generated and saved to: {result}")
