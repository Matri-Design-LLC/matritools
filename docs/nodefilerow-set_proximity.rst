`NodeFileRow <nodefilerow.html>`_
=================================
set_proximity
-------------
Sets the x, y, and z axis of proximity.

Parameters:

+------+-------------+-------+---------+
| Name | Description | Type  | Default |
+======+=============+=======+=========+
| x    | proximity_x | float | 0       |
+------+-------------+-------+---------+
| y    | proximity_y | float | 0       |
+------+-------------+-------+---------+
| z    | proximity_z | float | 0       |
+------+-------------+-------+---------+

Returns: None

Raises: TypeError

Example::

	from matritools import nodefile as nf

	# create node file with 6 default node file rows

	my_node_file = nf.NodeFile("My Node File")

	my_node_file.properties[0].set_proximity(1, 2, 3)

	# same as

	my_node_file.properties[0].proximity_x = 1
	my_node_file.properties[0].proximity_x = 2
	my_node_file.properties[0].proximity_x = 3

