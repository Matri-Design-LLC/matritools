`NodeFileRow <nodefilerow.html>`_
=================================
set_color
---------
Sets the x, y, and z axis of color.

Parameters:

+------+-------------+------+---------+
| Name | Description | Type | Default |
+======+=============+======+=========+
| r    | color_r     | int  | 0       |
+------+-------------+------+---------+
| g    | color_g     | int  | 0       |
+------+-------------+------+---------+
| b    | color_b     | int  | 0       |
+------+-------------+------+---------+
| a    | color_a     | int  | 255     |
+------+-------------+------+---------+

Returns: None

Raises: TypeError

Example::

	from matritools import nodefile as nf

	# create node file with 6 default node file rows

	my_node_file = nf.NodeFile("My Node File")

	my_node_file.properties.set_color(1, 2, 3, 4)

	# same as

	my_node_file.properties.color_r = 1
	my_node_file.properties.color_g = 2
	my_node_file.properties.color_b = 3
	my_node_file.properties.color_a = 4

