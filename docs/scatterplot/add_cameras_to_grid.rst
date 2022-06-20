add_cameras_to_grid
-------------------
Places cameras around a scatter plot. Should be called after grid handle has its final position set. Camera offsets
are static will most likley not line up with scatter plots that have custom sizes.

Parameters:

+---------------+------------------------------------------------------+----------+------------------------------------+
| Name          | Description                                          | Type     |  Default                           |
+===============+======================================================+==========+====================================+
| ntf           | NodeFile to add cameras too                          | NodeFile | N/A                                |
+---------------+------------------------------------------------------+----------+------------------------------------+
| grid_handle   | Node to position cameras around                      | Node     | N/A                                |
+---------------+------------------------------------------------------+----------+------------------------------------+

Returns:
    None

Raises:
    TypeError

Example::

	import matritools as mt
	import pandas as pd

	data = {"Name": ["Plot 1", "Plot 2", "Plot 3", "Plot 4", "Plot 5", "Plot 6", "Plot 7", "Plot 8", "Plot 9", "Plot 10", "Plot 11"],
			"A": [1, 1, 6, 6, 6, 2, 6, 7, 7, 2, 6],
			"B": [4, 4, 7, 7, 7, 2, 8, 8, 8, 2, 0],
			"C": [8, 8, 2, 2, 2, 5, 9, 9, 9, 2, 4],
			"D": [8, 8, 6, 6, 6, 3, 1, 2, 2, 5, 0]}

	data_df = pd.DataFrame(data)

	input_data = {'grid_color': ['red', 'blue', 'green'],
				  'x_column': ["A", "A", "A"],
				  'y_column': ["B", "B", "B"],
				  'z_column': ["C", "C", ""],
				  'color_column': ["D", "", ""],
				  'common_tag': ['A/B/C/D', 'A/B/C/D', 'A/B'],
				  'x_min': ['', '-5', ''],
				  'x_max': ['', '15', ''],
				  'y_min': ['', '-5', ''],
				  'y_max': ['', '15', ''],
				  'z_min': ['', '-5', ''],
				  'z_max': ['', '15', ''],
				  'color_min': ['', '-5', ''],
				  'color_max': ['', '15', '']}

	input_df = pd.DataFrame(input_data)

	file_name = "my_file_name"

	ntf = mt.NodeFile(file_name)
	#ntf.main_grid.hide = 1

	mt.scatter_plot_template.geometry = mt.geos['cube']
	mt.set_scatter_color_info(palette_id_in=7)

	grid_handle, grid = mt.scatter_plot_merge_plots(data_df, ntf, 'Blue', "Name", "A", "B", "C")
	mt.add_cameras_to_grid(ntf, grid_handle)

	ntf.write_to_csv()
