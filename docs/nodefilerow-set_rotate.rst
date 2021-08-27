`NodeFileRow <nodefilerow.html>`_
=================================
set_rotate
----------
Sets the x, y, and z axis of rotate.

Parameters:

+------+-------------+-------+---------+
| Name | Description | Type  | Default |
+======+=============+=======+=========+
| x    | rotate_x    | float | 0       |
+------+-------------+-------+---------+
| y    | rotate_y    | float | 0       |
+------+-------------+-------+---------+
| z    | rotate_z    | float | 0       |
+------+-------------+-------+---------+

Returns: None

Raises: TypeError

Example::

	from matritools import nodefile as nf

	# create node file with 6 default node file rows

	my_node_file = nf.NodeFile("My Node File")

	my_node_file.properties[0].set_rotate(1, 2, 3)

	# same as

	my_node_file.properties[0].rotate_x = 1
	my_node_file.properties[0].rotate_x = 2
	my_node_file.properties[0].rotate_x = 3

