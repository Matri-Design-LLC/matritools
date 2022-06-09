scatter plot globals
--------------------

.. toctree::
   :maxdepth: 2

   scatter_plot <scatterplot>
   scatter_plot_merge_plots <scatterplotmergeplots>

Global properties:

+------------------------------+---------------------------------------------------------------------+-------+---------+
| Name                         | Description                                                         | Type  | Default |
+==============================+=====================================================================+=======+=========+
| x_column_min (setter)        | Old min number used to build x axis interpolator.                   |       |         |
|                              | If None, this value will be set by min data value.                  | float | N/A     |
+------------------------------+---------------------------------------------------------------------+-------+---------+
| x_column_max (setter)        | Old max number used to build x axis interpolator.                   |       |         |
|                              | If None, this value will be set by max data value.                  | float | N/A     |
+------------------------------+---------------------------------------------------------------------+-------+---------+
| clamp_x (setter)             | Should x axis interpolator clamp?                                   | bool  | False   |
+------------------------------+---------------------------------------------------------------------+-------+---------+
| y_column_min (setter)        | Old min number used to build y axis interpolator.                   |       |         |
|                              | If None, this value will be set by min data value.                  | float | N/A     |
+------------------------------+---------------------------------------------------------------------+-------+---------+
| y_column_max (setter)        | Old max number used to build y axis interpolator.                   |       |         |
|                              | If None, this value will be set by max data value.                  | float | N/A     |
+------------------------------+---------------------------------------------------------------------+-------+---------+
| clamp_y (setter)             | Should y axis interpolator clamp?                                   | bool  | False   |
+------------------------------+---------------------------------------------------------------------+-------+---------+
| z_column_min (setter)        | Old min number used to build z axis interpolator.                   |       |         |
|                              | If None, this value will be set by min data value.                  | float | N/A     |
+------------------------------+---------------------------------------------------------------------+-------+---------+
| z_column_max (setter)        | Old max number used to build z axis interpolator.                   |       |         |
|                              | If None, this value will be set by max data value.                  | float | N/A     |
+------------------------------+---------------------------------------------------------------------+-------+---------+
| clamp_z (setter)             | Should z axis interpolator clamp?                                   | bool  | False   |
+------------------------------+---------------------------------------------------------------------+-------+---------+
| color_column_min (setter)    | Old min number used to build color_id interpolator.                 |       |         |
|                              | If None, this value will be set by min data value.                  | float | N/A     |
+------------------------------+---------------------------------------------------------------------+-------+---------+
| color_column_max (setter)    | Old max number used to build color_id interpolator.                 |       |         |
|                              | If None, this value will be set by max data value.                  | float | N/A     |
+------------------------------+---------------------------------------------------------------------+-------+---------+
| clamp_color (setter)         | Should color_id interpolator clamp?                                 | bool  | False   |
+------------------------------+---------------------------------------------------------------------+-------+---------+
| color_id_min (setter)        | new min number used to build color_id interpolator. This value      | int   | 127     |
|                              | should be set to max or min color_id of the selected pallete_id and |       |         |
|                              | should be oposite end of the spectrum from color_id_max.            |       |         |
+------------------------------+---------------------------------------------------------------------+-------+---------+
| color_id_max (setter)        | new max number used to build color_id interpolator. This value      | int   | 0       |
|                              | should be set to max or min color_id of the selected pallete_id     |       |         |
|                              | and should be opositeend of the spectrum from color_id_min.         |       |         |
+------------------------------+---------------------------------------------------------------------+-------+---------+
| palette_id (setter)          | pallete_id used to color plots.                                     | int   | 6       |
+------------------------------+---------------------------------------------------------------------+-------+---------+
| grid_size (setter)           | number used to size grid and interpolate plot points.               | float | 25      |
+------------------------------+---------------------------------------------------------------------+-------+---------+
| plot_size (setter)           | scale of plots.                                                     | float | 0.5     |
+------------------------------+---------------------------------------------------------------------+-------+---------+
| scatter_plot_template        | template used when creating plots.                                  | Node  | new     |
|                              | All properties are default except geometry is set to sphere         |       |         |
+------------------------------+---------------------------------------------------------------------+-------+---------+
| scatter_corner_node_template | template used for nodes placed at corners of scatter plots.         | Node  | new     |
|                              | All properties are default except for geometry is set to cube.      |       |         |
+------------------------------+---------------------------------------------------------------------+-------+---------+

Setters:

	set_scatter_x_column(x_column_min, x_column_max, clamp_x)

	set_scatter_y_column(y_column_min, y_column_max, clamp_y)

	set_scatter_z_column(z_column_min, z_column_max, clamp_z)

	set_scatter_color_column(color_column_min, color_column_max, clamp_color)

	set_scatter_color_info(color_id_min, color_id_max, pallete_id)

	set_scatter_grid_size(grid_size)

	set_scatter_plot_size(plot_size

