from __future__ import annotations
import math
from typing import List, Tuple, Callable
import pandas as pd
from matritools import utils as mu, node as nd, nodefileglobals as nfg, nodefile as nf

# region global variables
__x_column_min__: float = None
__x_column_max__: float = None
__clamp_x__: bool = False

def set_scatter_x_column(min: float=None, max: float=None, clamp: bool=False):
	"""
	Sets old min and max of x axis interpolator.
	
	Parameters:
		min (float: None) - Old min number used to build x axis interpolator.
		If None, this value will be set by min data value.
		max (float: None) - Old max number used to build x axis interpolator.
		If None, this value will be set by max data value.
		clamp (bool: False) - Should x axis interpolator clamp?

	Returns:
	 None

	Raises:
		TypeError
	"""
	global __x_column_min__, __x_column_max__, __clamp_x__
	__check_setter_type__
	
	__x_column_min__ = min
	__x_column_max__ = max
	__clamp_x__ = clamp

__y_column_min__: float = None
__y_column_max__: float = None
__clamp_y__: bool = False

def set_scatter_y_column(min: float = None, max: float = None, clamp: bool = False):
	"""
	Sets old min and max of y axis interpolator.

	Parameters:
		min (float: None) - Old min number used to build y axis interpolator.
		If None, this value will be set by min data value.
		max (float: None) - Old max number used to build y axis interpolator.
		If None, this value will be set by max data value.
		clamp (bool: False) - Should y axis interpolator clamp?

	Returns:
	 None

	Raises:
		TypeError
	"""
	global __y_column_min__, __y_column_max__, __clamp_y__
	__check_setter_type__(min, max, clamp)
	
	__y_column_min__ = min
	__y_column_max__ = max
	__clamp_y__ = clamp

__z_column_min__: float = None
__z_column_max__: float = None
__clamp_z__: bool = False

def set_scatter_z_column(min: float = None, max: float = None, clamp: bool = False):
	"""
	Sets old min and max of z axis interpolator.

	Parameters:
		min (float: None) - Old min number used to build z axis interpolator.
		If None, this value will be set by min data value.
		max (float: None) - Old max number used to build z axis interpolator.
		If None, this value will be set by max data value.
		clamp (bool: False) - Should z axis interpolator clamp?

	Returns:
	 None

	Raises:
		TypeError
	"""
	global __z_column_min__, __z_column_max__, __clamp_z__
	__check_setter_type__(min, max, clamp)
	
	__z_column_min__ = min
	__z_column_max__ = max
	__clamp_z__ = clamp

__color_column_min__: float = None
__color_column_max__: float = None
__clamp_color__: bool = False


def set_scatter_color_column(min: float = None, max: float = None, clamp: bool = False):
	"""
	Sets old min and max of color_id interpolator.

	Parameters:
		min (float: None) - Old min number used to build color_id interpolator.
		If None, this value will be set by min data value.
		max (float: None) - Old max number used to build color_id interpolator.
		If None, this value will be set by max data value.
		clamp (bool: False) - Should color_id interpolator clamp?

	Returns:
	 None

	Raises:
		TypeError
	"""
	global __color_column_min__, __color_column_max__, __clamp_color__
	__check_setter_type__(min, max, clamp)
	
	__color_column_min__ = min
	__color_column_max__ = max
	__clamp_color__ = clamp

__color_id_min__: int = 127
__color_id_max__: int = 0
__palette_id__: int = 6

def set_scatter_color_info(min: int=127, max: int=0, palette_id_in: int = 6):
	"""
	Sets pallete_id for plots and new min and max of color_id interpolator
	
	Parameters:
		min (int: 127) - new min number used to build color_id interpolator. This value should be set to max or min
			color_id of the selected pallete_id and should be oposite end of the spectrum from color_id_max.
		max (int: 127) - new min number used to build color_id interpolator. This value should be set to max or min
			color_id of the selected pallete_id and should be oposite end of the spectrum from color_id_min.
		palette_id_in (int: 6) - pallete_id used to color plots.

	Returns:
		None
		
	Raises:
		TypeError
	"""
	global __color_id_min__, __color_id_max__, __palette_id__
	
	mu.check_type(min, int)
	mu.check_type(max, int)
	mu.check_type(palette_id_in, int)
	
	__color_id_min__ = min
	__color_id_max__ = max
	__palette_id__ = palette_id_in
	
__grid_size__: float = 25

def set_scatter_grid_size(size):
	"""
	Sets size of grid.
	Parameters:
		size (float: 25) - number used to size grid and interpolate plot points.

	Returns:
		None
		
	Raises:
		TypeError
	"""
	global __grid_size__
	mu.check_type(size, float)
	__grid_size__ = size

__plot_size__: float = 0.5

def set_scatter_plot_size(size):
	"""
	Sets size of grid.
	Parameters:
		size (float: 0.5) - scale of plots.

	Returns:
		None

	Raises:
		TypeError
	"""
	global __plot_size__
	mu.check_type(size, float)
	__plot_size__ = size

scatter_plot_template: nd.Node = nd.Node()
"""
	(Node: new Node()) - template used when creating plots. All properties are default except geometry is set to sphere.
"""
scatter_plot_template.geometry = nfg.geos['sphere']

scatter_corner_node_template: nd.Node = nd.Node()
"""
	(Node: new Node() - template used for nodes placed at corners of scatter plots. All properties are default except
	for geometry is set to cube.
"""
scatter_corner_node_template.geometry = nfg.geos['cube']

__z_column_min__: float = None
""" (float: None) - old min for z axis interpolator. Declared globally so helper functions can set them. """
__color_column__: float = None
""" (float: None) - old min for color_id interpolator. Declared globally so helper functions can set them. """

__grid_row__: int = 0
""" (int: 0) - index for how many grids have been placed in the current row. """

__grid_column__: int = 0
""" (int: 0) - index for how many grids have been placed in the current column. """

__x_range__: float = 300
""" (float: 300) - range that grids will be placed along the x axis. """

__grid_max_rows__: None
""" (int : None) - max number of rows in grid formation. """

grid_distance: float = None
""" (float: None) - distance grids will be placed from one another."""

grid_offset: float = None
""" (float: None) - offset of first grid on the x and y axis. """

# endregion



def scatter_plot_merge_plots(df: pd.DataFrame, ntf: nf.NodeFile, grid_color: str, key_column: str,
				x_column: str, y_column: str, z_column: str=None, common_tag:str="")-> Tuple[nd.Node, nd.Node]:
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
									key_column + ", " + common_tag + '(' + x_column + ", " + y_column + ") " + number
									of merged points
			node_function (function(Node, Series): None) - a user implemented function that takes in a Node.
													   If the function is not None, it will be called after each plot
													   is plotted and merged. The function will be passed the plotted Node.

		 Returns:
			 (Node, Node)

		Raises:
			TypeError
	"""
	
	__check_scatter_plot_input__(df, ntf, grid_color, key_column, x_column, y_column, z_column, None, common_tag, None)
	
	grid_handle, grid = __create_grid__(ntf, grid_color)
	pos_x_scalar, pos_y_scalar, pos_z_scalar, color_scalar = __make_scalars__(__z_column__, None)
	
	__create_cube_corners__(ntf, grid, grid_color, __z_column__, common_tag)
	
	plots = {}
	for index, row in df.iterrows():
		if __bad_scatter_plot_input__(x_column, y_column, __z_column__, None, row):
			continue
		__plot_point_merge__(grid, row, ntf, grid_color, key_column, x_column, y_column, __z_column__,
					   common_tag, pos_x_scalar, pos_y_scalar, pos_z_scalar, plots)
		
	old_min, old_max = __get_min_max_from_plots__(plots)
	color_scalar = mu.make_interpolator(old_min, old_max, 0, 127)
	
	for key in plots:
		plots[key][0].set_color_by_id(color_scalar(plots[key][1]), __palette_id__)
		plots[key][0].tag_text += " " + str(plots[key][1])
	
	__reset_default_values__()
	
	return grid_handle, grid


def add_cameras_to_grid(ntf:nf.NodeFile, grid_handle: nd.Node):
	"""
	Places cameras around a scatter plot. Should be called after grid handle has its final position set. Camera offsets
	are static will most likley not line up with scatter plots that have custom sizes.
	
	Parameters:
		ntf (NodeFile) - NodeFile to add cameras too
		grid_handle (Node) - Node to position cameras around

	Returns:
		None
		
	Raises:
		TypeError
	"""
	mu.check_type(ntf, nf.NodeFile, False)
	mu.check_type(grid_handle, nd.Node, False)
	
	camera1 = ntf.create_camera().set_rotate(90)
	camera1.set_translate(grid_handle.translate_x + 25, grid_handle.translate_y - 50, grid_handle.translate_z + 18)
	
	camera2 = ntf.create_camera().set_rotate(90, -90)
	camera2.set_translate(grid_handle.translate_x + 100, grid_handle.translate_y + 25, grid_handle.translate_z + 18)
	
	camera3 = ntf.create_camera().set_rotate()
	camera3.set_translate(grid_handle.translate_x + 25, grid_handle.translate_y + 25, grid_handle.translate_z + 120)


def scatter_plot(df: pd.DataFrame, ntf: nf.NodeFile, grid_color: str, key_column: str, x_column: str, y_column: str,
				 z_column: str=None, color_column: str=None, common_tag: str="",
				 node_function: Callable[[nd.Node, pd.Series], None]=None)-> Tuple[nd.Node, nd.Node]:
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
	
	__check_scatter_plot_input__(df, ntf, grid_color, key_column, x_column, y_column, z_column, color_column,
								 common_tag, node_function)
	grid_handle, grid = __create_grid__(ntf, grid_color)
	pos_x_scalar, pos_y_scalar, pos_z_scalar, color_scalar = __make_scalars__(__z_column__, __color_column__)
	
	__create_cube_corners__(ntf, grid, grid_color, __z_column__, common_tag)

	for index, row in df.iterrows():
		if __bad_scatter_plot_input__(x_column, y_column, __z_column__, __color_column__, row):
			continue
		__plot_point__(grid, row, ntf, grid_color, key_column, x_column, y_column, __z_column__,
				 	__color_column__, common_tag, node_function, pos_x_scalar, pos_y_scalar,
				   	pos_z_scalar, color_scalar)
		
	__reset_default_values__()
	
	return grid_handle, grid


def multi_scatter_plot_merge_plots(data_df: pd.DataFrame, input_df: pd.DataFrame, ntf: nf.NodeFile, key_column: str) \
		-> List[Tuple(Node, Node)]:
	"""
	Adds a scatter plot with merged plots to a NodeFile per row in an input_df. input_df should contain most of the
	parameters to call scatter_plot_merge_plots. input_df must contain column names of data_df.
	Translates grids to form a grid pattern. Returns a list of tuples containg grid_handles and grids.
	
	Paremeters:
		data_df (DataFrame) - DataFrame to plot points from.
		input_df (DataFrame) - DataFrame containing rows with column names from data_df and parameters for
		scatter_plot_merge_plots. DataFrame should have the following column names:
			grid_color,
			x_column,
			y_column,
			z_column,
			color_column,
			common_tag,
			x_min,
			x_max,
			y_min,
			y_max,
			z_min,
			z_max,
			color_min,
			color_max
			
		Use generate_multi_scatter_plot_input_csv to generate a template csv
		ntf (NodeFile) - NodeFile to add grid and plots too.
		key_column(str) - Column name used to uniquley identify each row. The data in this column will be used
							in tags. Can be None.

	Returns:
		List[Tuple(Node, Node)]
		
	Raises:
		TypeError
	"""
	global __grid_row__, __grid_column__
	
	__check_multi_scatter_plot_input(data_df, input_df, ntf, key_column)
	__set_grid_variables__(input_df)
	
	result = []
	
	for index, row in input_df.iterrows():
		__set_interpolator_min_and_max_from_series__(row)
		
		grid_handle, grid = scatter_plot_merge_plots(data_df, ntf, row['grid_color'], key_column, row['x_column'], row['y_column'],
										 row['z_column'], row['common_tag'])
		
		__place_multi_grid__(grid_handle)
		__increment_grid_indices()
	
		result.append((grid_handle, grid))
	
	return result

def multi_scatter_plot(data_df: pd.DataFrame, input_df: pd.DataFrame, ntf: nf.NodeFile, key_column: str,
					   node_function: Callable[[nd.Node, pd.Series], None]=None)-> List[Tuple(Node, Node)]:
	"""
	Adds a scatter plot to a NodeFile per row in an input_df. input_df should contain most of the
	parameters to call scatter_plot. input_df must contain column names of data_df.
	Translates grids to form a grid pattern. Returns a list of tuples containg grid_handles and grids.

	Paremeters:
		data_df (DataFrame) - DataFrame to plot points from.
		input_df (DataFrame) - DataFrame containing rows with column names from data_df and parameters for
		scatter_plot_merge_plots. DataFrame should have the following column names:
			grid_color,
			x_column,
			y_column,
			z_column,
			color_column,
			common_tag,
			x_min,
			x_max,
			y_min,
			y_max,
			z_min,
			z_max,
			color_min,
			color_max

		Use generate_multi_scatter_plot_input_csv to generate a template csv
		ntf (NodeFile) - NodeFile to add grid and plots too.
		key_column(str) - Column name used to uniquley identify each row. The data in this column will be used
							in tags. Can be None.
		node_function (function(Node, Series): None) - a user implemented function that takes in a Node and Series.
													   If the function is not None, it will be called after each plot
													   is plotted. The function will be passed the plotted Node and the
													   DataFrame.iterrows() series for that DataFrame iteration loop.

	Returns:
		List[Tuple(Node, Node)]

	Raises:
		TypeError
	"""
	
	__check_multi_scatter_plot_input(data_df, input_df, ntf, key_column)
	__set_grid_variables__(input_df)
	
	result = []
	
	for index, row in input_df.iterrows():
		__set_interpolator_min_and_max_from_series__(row)
		
		grid_handle, grid = scatter_plot(data_df, ntf, row['grid_color'], key_column, row['x_column'], row['y_column'],
											row['z_column'], row['color_column'], row['common_tag'], node_function)
		
		__place_multi_grid__(grid_handle)
		__increment_grid_indices()
			
		result.append((grid_handle, grid))
		
	return result

def generate_multi_scatter_plot_input_csv(file_path: str='multi_scatter_plot_input_template'):
	"""
	Creates a csv file template to store parameters used to make multiple scatter plots on the same data frame.
	
	Parameters:
		file_path (str: 'multi_scatter_plot_input_template') - name of output file.

	Returns:
		List[Tuple(Node, Node)]
	"""
	mu.check_type(file_path, str)
	file_path = str(file_path)
	if not file_path.endswith('.csv'):
		file_path += '.csv'
		
	columns = ['grid_color','x_column','y_column','z_column','color_column','common_tag','x_min','x_max','y_min',
			   'y_max','z_min','z_max','color_min','color_max']
	
	csv_dict = {}
	
	for column in columns:
		csv_dict[column] = ['']
		
	pd.DataFrame(csv_dict).to_csv(file_path, index=None)

# region helper functions

# region error checking and sanitation.
def __sanitize_input_df__(input_df: pd.DataFrame):
	""" ensures input_df columns that should be numeric are numeric """
	columns = ['x_min', 'x_max', 'y_min', 'y_max', 'z_min', 'z_max', 'color_min', 'color_max']
	
	for column in columns:
		input_df[column] = pd.to_numeric(df[column])
	
	
def __check_setter_type__(min: float, max: float, clamp: bool):
	""" Checks the types for min, max and clamp setter function input"""
	if min is not None:
		mu.check_type(min, float)
	if max is not None:
		mu.check_type(max, float)
	mu.check_type(clamp, bool)
	

def __check_multi_scatter_plot_input(data_df: pd.DataFrame, input_df: pd.DataFrame, ntf: nf.NodeFile, key_column: str):
	""" Checks the types of multi scatter plot function parameters. """
	mu.check_type(data_df, pd.DataFrame)
	mu.check_type(input_df, pd.DataFrame)
	__sanitize_input_df__(input_df)
	mu.check_type(ntf, nf.NodeFile)
	mu.check_type(key_column, str)


def __check_scatter_plot_input__(df, ntf, grid_color, key_column, x_column, y_column,
								 z_column, color_column, common_tag, node_function):
	""" Checks the type of scatter plot parameters and santizies them. """
	global __z_column__, __color_column__
	
	mu.check_type(df, pd.DataFrame, False)
	mu.check_type(ntf, nf.NodeFile, False)
	mu.check_type(grid_color, str)
	mu.check_type(key_column, str)
	mu.check_type(x_column, str)
	mu.check_type(y_column, str)
	
	__z_column__ = z_column
	__color_column__ = color_column
	
	if (__z_column__ is not None):
		if str(__z_column__) == 'nan' or str(__z_column__) == '':
			__z_column__ = None
		else:
			mu.check_type(__z_column__, str)
	if (__color_column__ is not None):
		if str(__color_column__) == 'nan' or str(__color_column__) == '':
			__color_column__ = None
		else:
			mu.check_type(__color_column__, str)
	
	mu.check_type(common_tag, str)
	if node_function is not None:
		mu.check_type(node_function, type(__check_scatter_plot_input__), False)
	
	if str(__z_column__) == 'nan' or str(__z_column__) == '':
		__z_column__ = None
	if str(__color_column__) == 'nan' or str(__color_column__) == '':
		__color_column__ = None
	__sanitize_interpolator_input__(df, x_column, y_column, __z_column__, __color_column__)


def __sanitize_interpolator_input__(df, x_column, y_column, z_column, color_column):
	global __x_column_min__, __x_column_max__, __y_column_min__, __y_column_max__, __z_column_max__, __z_column_min__, \
		__color_column_min__, __color_column_max__
	if str(__x_column_min__) == 'nan' or str(__x_column_min__) == '':
		__x_column_min__ = None
	if str(__x_column_max__) == 'nan' or str(__x_column_max__) == '':
		__x_column_max__ = None
	if str(__y_column_min__) == 'nan' or str(__y_column_min__) == '':
		__y_column_min__ = None
	if str(__y_column_max__) == 'nan' or str(__y_column_max__) == '':
		__y_column_max__ = None
	if str(__z_column_min__) == 'nan' or str(__z_column_min__) == '':
		__z_column_min__ = None
	if str(__z_column_max__) == 'nan' or str(__z_column_max__) == '':
		__z_column_max__ = None
	if str(__color_column_min__) == 'nan' or str(__color_column_min__) == '':
		__color_column_min__ = None
	if str(__color_column_max__) == 'nan' or str(__color_column_max__) == '':
		__color_column_max__ = None
	
	if __x_column_min__ is None:
		__x_column_min__ = df[x_column].min()
	if __x_column_max__ is None:
		__x_column_max__ = df[x_column].max()
	if __y_column_min__ is None:
		__y_column_min__ = df[y_column].min()
	if __y_column_max__ is None:
		__y_column_max__ = df[y_column].max()
	if z_column is not None:
		if __z_column_min__ is None:
			__z_column_min__ = df[z_column].min()
		if __z_column_max__ is None:
			__z_column_max__ = df[z_column].max()
	if color_column is not None:
		if __color_column_min__ is None:
			__color_column_min__ = df[color_column].min()
		if __color_column_max__ is None:
			__color_column_max__ = df[color_column].max()


def __bad_input__(value, is_clamped, value_min, value_max):
	""" Returns True or False if value is out of range or is nan or None"""
	if str(value) == 'nan' or value is None or (not is_clamped and (value > value_max or value < value_min)):
		return True
	else:
		return False


def __bad_scatter_plot_input__(x_column, y_column, z_column, color_column, row):
	""" Returns True or False if any column data is out of range or is nan or None. """
	if __bad_input__(row[x_column], __clamp_x__, __x_column_min__, __x_column_max__) or \
			__bad_input__(row[y_column], __clamp_y__, __y_column_min__, __y_column_max__):
		return True
	
	if z_column is not None:
		if __bad_input__(row[z_column], __clamp_z__, __z_column_min__, __z_column_max__):
			return True
	
	if color_column is not None:
		if __bad_input__(row[color_column], __clamp_color__, __color_column_min__, __color_column_max__):
			return True

# endregion

# region setters

def __set_interpolator_min_and_max_from_series__(row):
	global __x_column_min__, __x_column_max__, __y_column_min__, __y_column_max__, __z_column_max__, __z_column_min__, \
		__color_column_min__, __color_column_max__
	__x_column_min__ = row['x_min']
	__x_column_max__ = row['x_max']
	
	__y_column_min__ = row['y_min']
	__y_column_max__ = row['y_max']
	
	__z_column_min__ = row['z_min']
	__z_column_max__ = row['z_max']
	
	__color_column_min__ = row['color_min']
	__color_column_max__ = row['color_max']


def __reset_default_values__():
	set_scatter_x_column()
	set_scatter_y_column()
	set_scatter_z_column()
	set_scatter_color_column()


def __set_grid_variables__(input_df):
	global __x_range__, __grid_max_rows__, __grid_distance__, __grid_offset__, __grid_row__, __grid_column__
	
	__x_range__ = 300
	
	__grid_max_rows__ = round(len(input_df) ** 0.5)
	__grid_distance__ = __x_range__ / __grid_max_rows__
	__grid_offset__ = (__x_range__ / 2) * -1
	
	__grid_row__ = 0
	__grid_column__ = 0
	
	
def __increment_grid_indices():
	global __grid_row__, __grid_column__
	__grid_row__ += 1
	if __grid_row__ == __grid_max_rows__:
		__grid_row__ = 0
		__grid_column__ += 1

# endregion

# region node manipulation

def __create_grid__(ntf, grid_color):
	grid_handle, grid = ntf.create_grid(ntf.main_grid, grid_template=ntf.main_grid)
	
	grid_handle.set_color_by_name(grid_color)
	
	grid.set_aux_a(__grid_size__, __grid_size__, __grid_size__)
	grid.set_color_by_name(grid_color)
	grid.set_segments(2, 2, 0)
	grid.set_translate(25, 25, 5)
	
	grid_handle.topo = nfg.topos['plane']
	
	return grid_handle, grid


def __create_cube_corner__(ntf, grid, grid_color, x, y, z, tag):
	node = ntf.create_node(grid, template=scatter_corner_node_template)
	node.set_translate(x, y, z)
	node.set_tag(tag, 0)
	node.set_color_by_name(grid_color)
	return node


def __create_cube_corners__(ntf, grid, grid_color, z_column, common_tag):
	__create_cube_corner__(ntf, grid, grid_color, 0, __grid_size__ + 1, 0, "")
	
	if z_column is not None:
		c1 = __create_cube_corner__(ntf, grid, grid_color, -__grid_size__ - 1, -__grid_size__ - 1, 0,
									common_tag + '(' + str(__x_column_min__) + ', ' + str(
										round(__y_column_min__, 2)) + ', '
									+ str(round(__z_column_min__, 2)) + ')')
		c2 = __create_cube_corner__(ntf, grid, grid_color, __grid_size__ + 1, -__grid_size__ - 1, 0,
									common_tag + '(' + str(__x_column_max__) + ',' + str(
										round(__y_column_min__, 2)) + ' , '
									+ str(round(__z_column_min__, 2)) + ')')
		c3 = __create_cube_corner__(ntf, grid, grid_color, -__grid_size__ - 1, __grid_size__ + 1, 0,
									common_tag + '(' + str(__x_column_min__) + ',' + str(
										round(__y_column_max__, 2)) + ', ' +
									str(round(__z_column_min__, 2)) + ')')
		c4 = __create_cube_corner__(ntf, grid, grid_color, __grid_size__ + 1, __grid_size__ + 1, 0,
									common_tag + '(' + str(__x_column_max__) + ', ' + str(
										round(__y_column_max__, 2)) + ', '
									+ str(round(__z_column_min__, 2)) + ')')
		c5 = __create_cube_corner__(ntf, grid, grid_color, -__grid_size__ - 1, -__grid_size__ - 1, __grid_size__,
									common_tag + '(' + str(__x_column_min__) + ', ' + str(
										round(__y_column_min__, 2)) + ','
									+ str(round(__z_column_max__, 2)) + ')')
		c6 = __create_cube_corner__(ntf, grid, grid_color, __grid_size__ + 1, -__grid_size__ - 1, __grid_size__,
									common_tag + '(' + str(__x_column_max__) + ', ' + str(
										round(__y_column_min__, 2)) + ', '
									+ str(round(__z_column_max__, 2)) + ')')
		c7 = __create_cube_corner__(ntf, grid, grid_color, -__grid_size__ - 1, __grid_size__ + 1, __grid_size__,
									common_tag + '(' + str(__x_column_min__) + ', ' + str(
										round(__y_column_max__, 2)) + ', '
									+ str(round(__z_column_max__, 2)) + ')')
		c8 = __create_cube_corner__(ntf, grid, grid_color, __grid_size__ + 1, __grid_size__ + 1, __grid_size__,
									common_tag + '(' + str(__x_column_max__) + ', ' + str(
										round(__y_column_max__, 2)) + ', '
									+ str(round(__z_column_max__, 2)) + ')')
		__link_corner_cubes__(ntf, grid_color, c1, c2, c3, c4, c5, c6, c7, c8)
	else:
		__create_cube_corner__(ntf, grid, grid_color, -__grid_size__ - 1, -__grid_size__ - 1, 0,
							   common_tag + '(' + str(__x_column_min__) + ', ' + str(round(__y_column_min__, 2)) + ')')
		__create_cube_corner__(ntf, grid, grid_color, __grid_size__ + 1, -__grid_size__ - 1, 0,
							   common_tag + '(' + str(__x_column_max__) + ',' + str(round(__y_column_min__, 2)) + ')')
		__create_cube_corner__(ntf, grid, grid_color, -__grid_size__ - 1, __grid_size__ + 1, 0,
							   common_tag + '(' + str(__x_column_min__) + ',' + str(round(__y_column_max__, 2)) + ')')
		__create_cube_corner__(ntf, grid, grid_color, __grid_size__ + 1, __grid_size__ + 1, 0,
							   common_tag + '(' + str(__x_column_max__) + ', ' + str(round(__y_column_max__, 2)) + ')')


def __plot_point_merge__(grid, row, ntf, grid_color, key_column, x_column, y_column, z_column,
						 common_tag, pos_x_scalar, pos_y_scalar, pos_z_scalar, plots):
	x = pos_x_scalar(row[x_column])
	y = pos_y_scalar(row[y_column])
	if z_column is not None:
		z = pos_z_scalar(row[z_column])
	else:
		z = 0
	
	if (x, y, z) in plots:
		plots[(x, y, z)][1] += 1
		return
	
	node = ntf.create_node(grid, template=scatter_plot_template)
	node.set_translate(x, y, z)
	node.set_u_scale(__plot_size__)
	
	__add_tag_to_node__(node, row, key_column, x_column, y_column, z_column, None, common_tag)
	
	plots[(x, y, z)] = [node, 1]


def __plot_point__(grid, row, ntf, grid_color, key_column, x_column, y_column, z_column,
				   color_column, common_tag, node_function,
				   pos_x_scalar, pos_y_scalar, pos_z_scalar, color_scalar):
	node = ntf.create_node(grid, template=scatter_plot_template)
	
	if color_column is not None:
		node.set_color_by_id(color_scalar(row[color_column]), __palette_id__)
	
	x = pos_x_scalar(row[x_column])
	y = pos_y_scalar(row[y_column])
	if z_column is not None:
		z = pos_z_scalar(row[z_column])
	else:
		z = 0
	node.set_translate(x, y, z)
	node.set_u_scale(__plot_size__)
	
	__add_tag_to_node__(node, row, key_column, x_column, y_column, z_column, color_column, common_tag)
	
	if node_function is not None:
		node_function(node, row)


def __place_multi_grid__(grid_handle):
	x = (__grid_row__ * __grid_distance__) + __grid_offset__
	y = (__grid_column__ * __grid_distance__) + __grid_offset__
	grid_handle.set_translate(x, y)
	
def __add_tag_to_node__(node, row, key_column, x_column, y_column, z_column, color_column, common_tag):
	if key_column is None:
		node.set_tag(common_tag + '(' + str(row[x_column]) + ", " + str(round(row[y_column], 2)))
	else:
		node.set_tag(
			str(row[key_column]) + ", " + common_tag + '(' + str(row[x_column]) + ", " + str(
				round(row[y_column], 2)))
	
	if z_column is not None:
		node.tag_text += ', ' + str(round(row[z_column], 2))
	if color_column is not None:
		node.tag_text += ', ' + str(round(row[color_column], 2))
	
	node.tag_text += ")"


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

# endregion

# region getters

def __get_min_max_from_plots__(plots):
	min = math.inf
	max = -math.inf
	for key in plots:
		if plots[key][1] < min:
			min = plots[key][1]
		if plots[key][1] > max:
			max = plots[key][1]
			
	return min, max

	
def __make_scalars__(z_column, color_column):
	pos_x_scalar = mu.make_interpolator(__x_column_min__, __x_column_max__, -__grid_size__, __grid_size__, __clamp_x__,
										True, __x_column_min__)
	pos_y_scalar = mu.make_interpolator(__y_column_min__, __y_column_max__, -__grid_size__, __grid_size__, __clamp_y__,
										True, __y_column_min__)
	pos_z_scalar = None
	color_scalar = None
	if z_column is not None:
		pos_z_scalar = mu.make_interpolator(__z_column_min__, __z_column_max__, 0, __grid_size__, __clamp_z__, True,
											__z_column_min__)
	if color_column is not None:
		color_scalar = mu.make_interpolator(__color_column_min__, __color_column_max__, __color_id_min__,
											__color_id_max__, __clamp_color__, True, __color_id_min__)
		
	return pos_x_scalar, pos_y_scalar, pos_z_scalar, color_scalar

# endregion

# endregion