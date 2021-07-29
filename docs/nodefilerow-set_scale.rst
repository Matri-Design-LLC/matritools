`NodeFileRow <nodefilerow.html>`_
=================================
set_scale
---------
Sets the x, y, and z axis of scale.

Parameters:

+------+-------------+-------+---------+
| Name | Description | Type  | Default |
+======+=============+=======+=========+
| x    | scale_x     | float | 0       |
+------+-------------+-------+---------+
| y    | scale_y     | float | 0       |
+------+-------------+-------+---------+
| z    | scale_z     | float | 0       |
+------+-------------+-------+---------+

Returns: None

Example::

	from matritools import nodefile as nf

	# create node file with 6 default node file rows

	my_node_file = nf.NodeFile("My Node File")

	my_node_file.properties[0].set_scale(1, 2, 3)

	# same as

	my_node_file.properties[0].scale_x = 1
	my_node_file.properties[0].scale_x = 2
	my_node_file.properties[0].scale_x = 3

