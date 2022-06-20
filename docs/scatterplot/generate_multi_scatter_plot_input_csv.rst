generate_multi_scatter_plot_input_csv
-------------------------------------
Creates a csv file template to store parameters used to make multiple scatter plots on the same data frame.

Parameters:

+---------------+------------------------------------------------------+-------+-------------------------------------+
| Name          | Description                                          | Type  |  Default                            |
+===============+======================================================+=======+=====================================+
| file_path     | name of output file.                                 | str   | 'multi_scatter_plot_input_template' |
+---------------+------------------------------------------------------+-------+-------------------------------------+

Returns:
    None

Raises:
    TypeError

Example 1::

	import matritools as mt

	mt.generate_multi_scatter_plot_input_csv()

Example 2::

	import matritools as mt

	mt.generate_multi_scatter_plot_input_csv('my_file_name')

Example 3::

	import matritools as mt

	mt.generate_multi_scatter_plot_input_csv('my_file_name.csv')