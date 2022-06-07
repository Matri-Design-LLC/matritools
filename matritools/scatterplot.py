from __future__ import annotations

import math
from typing import Tuple
import pandas as pd
from matritools import utils as mu, node, nodefileglobals as globals, nodefile as nf

x_column_min = None
x_column_max = None
clamp_x = False

y_column_min = None
y_column_max = None
clamp_y = False

z_column_min = None
z_column_max = None
clamp_z = False

color_column_min = None
color_column_max = None
clamp_color = False

color_id_min = 127
color_id_max = 0
palette_id = 6

grid_size = 25
dot_size = 0.5
default_sphere_color = None

corner_cube_template = node.Node()
corner_cube_template.geometry = globals.geos['cube']
corner_cube_template.set_color_by_name('cyan')

def set_mins(x, y, z, color):
    global x_column_min, y_column_min, z_column_min, color_column_min
    x_column_min = x
    y_column_min = y
    z_column_min = z
    color_column_min = color
	
def scatter_plot_merge_plots(df: pd.DataFrame, ntf: nf.NodeFile, grid_color: str, key_column: str,
				x_column: str, y_column: str, z_column: str=None, common_tag:str="")-> Tuple[node.Node, node.Node]:
	"""
		Adds a grid with a grid handle with points plotted from a DataFrame to a NodeFile

		 Parameters:
			 df (DataFrame) - DataFrame to plot points from.
			 ntf (NodeFile) - NodeFile to add grid and plots too.
			 grid_color (str) - Color of grid lines.
			 key_column (str) - Column name used to uniquley identify each row. The data in this column will be used
								in tags. Can be None.
			x_column (str) - Column name for data that is interpolated to place a plot along the x axis.
			y_column (str) - Column name for data that is interpolated to place a plot along the y axis.
			z_column (str: None) - Column name for data that is interpolated to place a plot along the z axis.
			common_tag (str: "") - A string that will be added to every plots tag.
									Tag for each plot will be formmated as
									key_column + ", " + common_tag + '(' + x_column + ", " + y_column

		 Returns:
			 (Node, Node)

		Raises:
			TypeError
	"""
	__check_scatter_plot_input__(df, ntf, grid_color, key_column, x_column, y_column, z_column,
								 None, common_tag, None)
	grid_handle, grid = __create_grid__(ntf, grid_color)
	pos_x_scalar, pos_y_scalar, pos_z_scalar, color_scalar = __make_scalars__(z_column, None)
	__create_cube_corners__(ntf, grid, grid_color, z_column, common_tag)
	
	plots = {}
	for index, row in df.iterrows():
		if __bad_scatter_plot_input__(x_column, y_column, z_column, None, row):
			continue
		__plot_point_merge__(grid, row, ntf, grid_color, key_column, x_column, y_column, z_column,
					   common_tag, pos_x_scalar, pos_y_scalar, pos_z_scalar, plots)
		
	old_min, old_max = __get_min_max_from_plots__(plots)
	color_scalar = mu.make_interpolator(old_min, old_max, 0, 127)
	
	for key in plots:
		plots[key][0].set_color_by_id(color_scalar(plots[key][1]), palette_id)
		plots[key][0].tag_text += " " + str(plots[key][1])
	
	return grid_handle, grid

def scatter_plot(df: pd.DataFrame, ntf: nf.NodeFile, grid_color: str, key_column: str, x_column: str, y_column: str,
				 z_column: str=None, color_column: str=None, common_tag: str="", node_function: function=None)\
		-> Tuple[node.Node, node.Node]:
	"""
	Adds a grid with a grid handle with points plotted from a DataFrame to a NodeFile

	 Parameters:
		 df (DataFrame) - DataFrame to plot points from.
		 ntf (NodeFile) - NodeFile to add grid and plots too.
		 grid_color (str) - Color of grid lines.
		 key_column (str) - Column name used to uniquley identify each row. The data in this column will be used
							in tags. Can be None.
		x_column (str) - Column name for data that is interpolated to place a plot along the x axis.
		y_column (str) - Column name for data that is interpolated to place a plot along the y axis.
		z_column (str: None) - Column name for data that is interpolated to place a plot along the z axis.
		color_column (str: None) - Column name for data that is interpolated between the min and max color or
									the globally specified pallete_id to color a plot.
		common_tag (str: "") - A string that will be added to every plots tag.
								Tag for each plot will be formmated as
								key_column + ", " + common_tag + '(' + x_column + ", " + y_column
		node_function (function(Node, Series): None) - a user implemented function that takes in a Node and Series.
													   If the function is not None, it will be called after each plot
													   is plotted. The function will be passed the plotted Node and the
													   DataFrame.iterrows() series for that DataFrame iteration loop.

	 Returns:
		 (Node, Node)

	Raises:
		TypeError
	"""
	
	__check_scatter_plot_input__(df, ntf, grid_color, key_column, x_column, y_column, z_column,
								 color_column, common_tag, node_function)
	grid_handle, grid = __create_grid__(ntf, grid_color)
	pos_x_scalar, pos_y_scalar, pos_z_scalar, color_scalar = __make_scalars__(z_column, color_column)
	__create_cube_corners__(ntf, grid, grid_color, z_column, common_tag)
	
	for index, row in df.iterrows():
		if __bad_scatter_plot_input__(x_column, y_column, z_column, color_column, row):
			continue
		__plot_point__(grid, row, ntf, grid_color, key_column, x_column, y_column, z_column,
				 	color_column, common_tag, node_function, pos_x_scalar, pos_y_scalar,
				   	pos_z_scalar, color_scalar)
	
	return grid_handle, grid


def __get_min_max_from_plots__(plots):
	min = math.inf
	max = -math.inf
	for key in plots:
		if plots[key][1] < min:
			min = plots[key][1]
		if plots[key][1] > max:
			max = plots[key][1]
			
	return min, max


def __plot_point_merge__(grid, row, ntf, grid_color, key_column, x_column, y_column, z_column,
					common_tag, pos_x_scalar, pos_y_scalar, pos_z_scalar, plots):
	x = pos_x_scalar(row[x_column])
	y = pos_y_scalar(row[y_column])
	if z_column is not None:
		z = pos_z_scalar(row[z_column])
	else:
		z = 0
		
	if (x,y,z) in plots:
		plots[(x,y,z)][1] += 1
		return
	
	node = ntf.create_node(grid)
	
	node.geometry = globals.geos['sphere']
	node.set_translate(x, y, z)
	node.set_u_scale(dot_size)
	
	__add_tag_to_node__(node, row, key_column, x_column, y_column, z_column, None, common_tag)
	
	plots[(x, y, z)] = [node, 1]
	
def __plot_point__(grid, row, ntf, grid_color, key_column, x_column, y_column, z_column,
				 	color_column, common_tag, node_function,
					pos_x_scalar, pos_y_scalar, pos_z_scalar, color_scalar):
	node = ntf.create_node(grid)
	
	if color_column is not None:
		node.set_color_by_id(color_scalar(row[color_column]), palette_id)
	node.geometry = globals.geos['sphere']
	
	x = pos_x_scalar(row[x_column])
	y = pos_y_scalar(row[y_column])
	if z_column is not None:
		z = pos_z_scalar(row[z_column])
	else:
		z = 0
	node.set_translate(x, y, z)
	node.set_u_scale(dot_size)
	if color_column is None and default_sphere_color is not None:
		node.set_color_by_name(default_sphere_color)
	
	__add_tag_to_node__(node, row, key_column, x_column, y_column, z_column, color_column, common_tag)
	
	if node_function is not None:
		node_function(node, row)
	
	
def __add_tag_to_node__(node, row, key_column, x_column, y_column, z_column, color_column, common_tag):
	if key_column is None:
		node.set_tag(common_tag + '(' + str(row[x_column]) + ", " + str(round(row[y_column], 2)))
	else:
		node.set_tag(
			str(row[key_column]) + ", " + common_tag + '(' + str(row[x_column]) + ", " + str(round(row[y_column], 2)))
	
	if z_column is not None:
		node.tag_text += ', ' + str(round(row[z_column], 2))
	if color_column is not None:
		node.tag_text += ', ' + str(round(row[color_column], 2))
		
		
def __check_scatter_plot_input__(df, ntf, grid_color, key_column, x_column, y_column,
				 z_column, color_column, common_tag, node_function):
	mu.check_type(df, pd.DataFrame, False)
	mu.check_type(ntf, nf.NodeFile, False)
	mu.check_type(grid_color, str)
	mu.check_type(key_column, str)
	mu.check_type(x_column, str)
	mu.check_type(y_column, str)
	
	if (z_column is not None):
		mu.check_type(z_column, str)
	if (color_column is not None):
		mu.check_type(color_column, str)
	
	mu.check_type(common_tag, str)
	if node_function is not None:
		mu.check_type(node_function, type(__check_scatter_plot_input__), False)
		
	if str(z_column) == 'nan' or str(z_column) == '':
		z_column = None
	if str(color_column) == 'nan' or str(color_column) == '':
		color_column = None
	__sanitize_interpolator_input__(df, x_column, y_column, z_column, color_column)
	
	
def __sanitize_interpolator_input__(df, x_column, y_column, z_column, color_column):
	global x_column_min, x_column_max, y_column_min, y_column_max, z_column_min, z_column_max, \
		color_column_min, color_column_max
	
	if str(x_column_min) == 'nan' or str(x_column_min) == '':
		x_column_min = None
	if str(x_column_max) == 'nan' or str(x_column_max) == '':
		x_column_max = None
	if str(y_column_min) == 'nan' or str(y_column_min) == '':
		y_column_min = None
	if str(y_column_max) == 'nan' or str(y_column_max) == '':
		y_column_max = None
	if str(z_column_min) == 'nan' or str(z_column_min) == '':
		z_column_min = None
	if str(z_column_max) == 'nan' or str(z_column_max) == '':
		z_column_max = None
	if str(color_column_min) == 'nan' or str(color_column_min) == '':
		color_column_min = None
	if str(color_column_max) == 'nan' or str(color_column_max) == '':
		color_column_max = None
	
	if x_column_min is None:
		x_column_min = df[x_column].min()
	if x_column_max is None:
		x_column_max = df[x_column].max()
	if y_column_min is None:
		y_column_min = df[y_column].min()
	if y_column_max is None:
		y_column_max = df[y_column].max()
	if z_column is not None:
		if z_column_min is None:
			z_column_min = df[z_column].min()
		if z_column_max is None:
			z_column_max = df[z_column].max()
	if color_column is not None:
		if color_column_min is None:
			color_column_min = df[color_column].min()
		if color_column_max is None:
			color_column_max = df[color_column].max()
		
			
def __bad_input__(value, is_clamped, value_min, value_max):
	if str(value) == 'nan' or value is None or (not is_clamped and (value > value_max or value < value_min)):
		return True
	else:
		return False
	
	
def __bad_scatter_plot_input__(x_column, y_column, z_column, color_column, row):
	if __bad_input__(row[x_column], clamp_x, x_column_min, x_column_max) or __bad_input__(row[y_column], clamp_y,
																						  y_column_min, y_column_max):
		return True
	
	if z_column is not None:
		if __bad_input__(row[z_column], clamp_z, z_column_min, z_column_max):
			return True
	
	if color_column is not None:
		if __bad_input__(row[color_column], clamp_color, color_column_min, color_column_max):
			return True
	
	
def __create_grid__(ntf, grid_color):
	grid_handle, grid = ntf.create_grid(ntf.main_grid, grid_template=ntf.main_grid)
	
	grid_handle.set_color_by_name(grid_color)
	
	grid.set_aux_a(grid_size, grid_size, grid_size)
	grid.set_color_by_name(grid_color)
	grid.set_segments(2, 2, 0)
	
	return grid_handle, grid
	
	
def __create_cube_corner__(ntf, grid, grid_color, x, y, z, tag):
	node = ntf.create_node(grid, template=corner_cube_template)
	node.set_translate(x,y,z)
	node.set_tag(tag, 0)
	node.set_color_by_name(grid_color)
	return node
	
	
def __create_cube_corners__(ntf, grid, grid_color, z_column, common_tag):
	__create_cube_corner__(ntf, grid, grid_color, 0, grid_size + 1, 0, "")
	
	if z_column is not None:
		c1 = __create_cube_corner__(ntf, grid, grid_color, -grid_size - 1, -grid_size - 1, 0,
							   common_tag + '(' + str(x_column_min) + ', ' + str(round(y_column_min, 2)) + ', ' + str(
								   round(z_column_min, 2)) + ')')
		c2 = __create_cube_corner__(ntf, grid, grid_color, grid_size + 1, -grid_size - 1, 0,
							   common_tag + '(' + str(x_column_max) + ',' + str(round(y_column_min, 2)) + ' , ' + str(
								   round(z_column_min, 2)) + ')')
		c3 = __create_cube_corner__(ntf, grid, grid_color, -grid_size - 1, grid_size + 1, 0,
							   common_tag + '(' + str(x_column_min) + ',' + str(round(y_column_max, 2)) + ', ' + str(
								   round(z_column_min, 2)) + ')')
		c4 = __create_cube_corner__(ntf, grid, grid_color, grid_size + 1, grid_size + 1, 0,
							   common_tag + '(' + str(x_column_max) + ', ' + str(round(y_column_max, 2)) + ', ' + str(
								   round(z_column_min, 2)) + ')')
		c5 = __create_cube_corner__(ntf, grid, grid_color, -grid_size - 1, -grid_size - 1, grid_size,
							   common_tag + '(' + str(x_column_min) + ', ' + str(round(y_column_min, 2)) + ',' + str(
								   round(z_column_max, 2)) + ')')
		c6 = __create_cube_corner__(ntf, grid, grid_color, grid_size + 1, -grid_size - 1, grid_size,
							   common_tag + '(' + str(x_column_max) + ', ' + str(round(y_column_min, 2)) + ', ' + str(
								   round(z_column_max, 2)) + ')')
		c7 = __create_cube_corner__(ntf, grid, grid_color, -grid_size - 1, grid_size + 1, grid_size,
							   common_tag + '(' + str(x_column_min) + ', ' + str(round(y_column_max, 2)) + ', ' + str(
								   round(z_column_max, 2)) + ')')
		c8 = __create_cube_corner__(ntf, grid, grid_color, grid_size + 1, grid_size + 1, grid_size,
							   common_tag + '(' + str(x_column_max) + ', ' + str(round(y_column_max, 2)) + ', ' + str(
								   round(z_column_max, 2)) + ')')
		__link_corner_cubes__(ntf, grid_color, c1, c2, c3, c4, c5, c6, c7, c8)
	else:
		__create_cube_corner__(ntf, grid, grid_color, -grid_size - 1, -grid_size - 1, 0,
							   common_tag + '(' + str(x_column_min) + ', ' + str(round(y_column_min, 2)) + ')')
		__create_cube_corner__(ntf, grid, grid_color, grid_size + 1, -grid_size - 1, 0,
							   common_tag + '(' + str(x_column_max) + ',' + str(round(y_column_min, 2)) + ')')
		__create_cube_corner__(ntf, grid, grid_color, -grid_size - 1, grid_size + 1, 0,
							   common_tag + '(' + str(x_column_min) + ',' + str(round(y_column_max, 2)) + ')')
		__create_cube_corner__(ntf, grid, grid_color, grid_size + 1, grid_size + 1, 0,
							   common_tag + '(' + str(x_column_max) + ', ' + str(round(y_column_max, 2)) + ')')
	

def __link_corner_cubes__(ntf, grid_color, c1, c2, c3, c4, c5, c6, c7, c8):
	ntf.make_link(c1, c2).set_color_by_name(grid_color)
	ntf.make_link(c1, c3).set_color_by_name(grid_color)
	
	ntf.make_link(c2, c4).set_color_by_name(grid_color)
	ntf.make_link(c3, c4).set_color_by_name(grid_color)
	
	ntf.make_link(c5, c6).set_color_by_name(grid_color)
	ntf.make_link(c5, c7).set_color_by_name(grid_color)
	
	ntf.make_link(c6, c8).set_color_by_name(grid_color)
	ntf.make_link(c7, c8).set_color_by_name(grid_color)
	
	ntf.make_link(c1, c5).set_color_by_name(grid_color)
	ntf.make_link(c2, c6).set_color_by_name(grid_color)
	ntf.make_link(c3, c7).set_color_by_name(grid_color)
	ntf.make_link(c4, c8).set_color_by_name(grid_color)
	
		
def __make_scalars__(z_column, color_column):
	pos_x_scalar = mu.make_interpolator(x_column_min, x_column_max, -grid_size, grid_size, clamp_x, True, x_column_min)
	pos_y_scalar = mu.make_interpolator(y_column_min, y_column_max, -grid_size, grid_size, clamp_y, True, y_column_min)
	pos_z_scalar = None
	color_scalar = None
	if z_column is not None:
		pos_z_scalar = mu.make_interpolator(z_column_min, z_column_max, 0, grid_size, clamp_z, True, z_column_min)
	if color_column is not None:
		color_scalar = mu.make_interpolator(color_column_min, color_column_max, color_id_min, color_id_max, clamp_color,
											True, color_id_min)
		
	return pos_x_scalar, pos_y_scalar, pos_z_scalar, color_scalar