import pandas as pd
from matritools import utils as mu, node, nodefileglobals as globals

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

def scatter_plot(df, ntf, grid_color, key_column, x_column, y_column, z_column, color_column, common_tag, target_keys=None):
	global x_column_min, x_column_max, y_column_min, y_column_max, z_column_min, z_column_max, \
		color_column_min, color_column_max
	
	target_nodes = {}
	
	if target_keys is not None:
		for key in target_keys:
			target_nodes[key] = []
	
	if str(z_column) == 'nan' or str(z_column) == '':
		z_column = None
	if str(color_column) == 'nan' or str(color_column) == '':
		color_column = None
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
	
	grid_handle, grid = ntf.create_grid(ntf.main_grid, grid_template=ntf.main_grid)
	
	grid_handle.set_color_by_name(grid_color)
	
	grid.set_aux_a(grid_size, grid_size, grid_size)
	grid.set_color_by_name(grid_color)
	grid.set_segments(2,2,0)
	
	# variables that affect viz layout=
	
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
	
	pos_x_scalar = mu.make_interpolator(x_column_min, x_column_max, -grid_size, grid_size, clamp_x, True, x_column_min)
	pos_y_scalar = mu.make_interpolator(y_column_min, y_column_max, -grid_size, grid_size, clamp_y, True, y_column_min)
	if z_column is not None:
		pos_z_scalar = mu.make_interpolator(z_column_min, z_column_max, 0, grid_size, clamp_z, True, z_column_min)
	if color_column is not None:
		color_scalar = mu.make_interpolator(color_column_min, color_column_max, color_id_min, color_id_max, clamp_color, True, color_id_min)
	
	def create_cube_corner(x, y, z, tag):
		node = ntf.create_node(grid, template=corner_cube_template)
		node.set_translate(x,y,z)
		node.set_tag(tag, 0)
	
	create_cube_corner(0, grid_size+1, 0, "")
	
	if z_column is not None:
		create_cube_corner(-grid_size-1, -grid_size-1, 0, common_tag + '(' + str(x_column_min) + ', ' + str(round(y_column_min, 2)) + ', ' + str(round(z_column_min, 2)) + ')')
		create_cube_corner(grid_size+1, -grid_size-1, 0, common_tag + '(' + str(x_column_max) + ',' + str(round(y_column_min, 2)) + ' , ' + str(round(z_column_min, 2)) + ')')
		create_cube_corner(-grid_size-1, grid_size+1, 0, common_tag + '(' + str(x_column_min) + ',' + str(round(y_column_max, 2)) + ', ' + str(round(z_column_min, 2)) + ')')
		create_cube_corner(grid_size+1, grid_size+1, 0, common_tag + '(' + str(x_column_max) + ', ' + str(round(y_column_max, 2)) + ', ' + str(round(z_column_min, 2)) + ')')
		create_cube_corner(-grid_size-1, -grid_size-1, grid_size, common_tag + '(' + str(x_column_min) + ', ' + str(round(y_column_min, 2)) + ',' + str(round(z_column_max, 2)) + ')')
		create_cube_corner(grid_size+1, -grid_size-1, grid_size, common_tag + '(' + str(x_column_max) + ', ' + str(round(y_column_min, 2)) + ', ' + str(round(z_column_max, 2)) + ')')
		create_cube_corner(-grid_size-1, grid_size+1, grid_size, common_tag + '(' + str(x_column_min) + ', ' + str(round(y_column_max, 2)) + ', ' + str(round(z_column_max, 2)) + ')')
		create_cube_corner(grid_size+1, grid_size+1, grid_size, common_tag + '(' + str(x_column_max) + ', ' + str(round(y_column_max, 2)) + ', ' + str(round(z_column_max, 2)) + ')')
	else:
		create_cube_corner(-grid_size-1, -grid_size-1, 0, common_tag + '(' + str(x_column_min) + ', ' + str(round(y_column_min, 2)) + ')')
		create_cube_corner(grid_size+1, -grid_size-1, 0, common_tag + '(' + str(x_column_max) + ',' + str(round(y_column_min, 2)) + ')')
		create_cube_corner(-grid_size-1, grid_size+1, 0, common_tag + '(' + str(x_column_min) + ',' + str(round(y_column_max, 2)) + ')')
		create_cube_corner(grid_size+1, grid_size+1, 0, common_tag + '(' + str(x_column_max) + ', ' + str(round(y_column_max, 2)) + ')')
	
	
	def bad_input(value, is_clamped, value_min, value_max):
		if str(value) == 'nan' or value is None or (not is_clamped and (value > value_max or value < value_min)):
			return True
		else:
			return False
	
	
	# main loop
	for index, row in df.iterrows():
		if bad_input(row[x_column], clamp_x, x_column_min, x_column_max) or bad_input(row[y_column], clamp_y, y_column_min, y_column_max):
			continue
		
		if z_column is not None:
			if bad_input(row[z_column], clamp_z, z_column_min, z_column_max):
				continue
		
		if color_column is not None:
			if bad_input(row[color_column], clamp_color, color_column_min, color_column_max):
				continue
		
		node = ntf.create_node(grid)
		
		if target_keys is not None:
			if row[key_column] in target_keys:
				target_nodes[row[key_column]].append(node)
		if color_column is not None:
			node.set_color_by_id(color_scalar(row[color_column]), palette_id)
		node.geometry = globals.geos['sphere']
		
		x = pos_x_scalar(row[x_column])
		y = pos_y_scalar(row[y_column])
		if z_column is not None:
			z = pos_z_scalar(row[z_column])
		else:
			z = 0
		node.set_translate(x,y,z)
		node.set_u_scale(dot_size)
		if color_column is None and default_sphere_color is not None:
			node.set_color_by_name(default_sphere_color)
		
		if key_column is None:
			node.set_tag(common_tag + '(' + str(row[x_column]) + ", " + str(round(row[y_column], 2)))
		else:
			node.set_tag(str(row[key_column]) + ", " + common_tag + '(' + str(row[x_column]) + ", " + str(round(row[y_column], 2)))
		
		if z_column is not None:
			node.tag_text += ', ' + str(round(row[z_column], 2))
		if color_column is not None:
			node.tag_text += ', ' + str(round(row[color_column], 2))
	
	if target_keys is None:
		return grid_handle, grid
	else:
		return grid_handle, grid, target_nodes