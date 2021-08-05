`NodeFileRow <nodefilerow.html>`_
=================================
set_proximity_mode
------------------
Sets the x, y, and z axis of proximity_mode.

Parameters:

+------+------------------+------+---------+
| Name | Description      | Type | Default |
+======+==================+======+=========+
| x    | proximity_mode_x | int  | 0       |
+------+------------------+------+---------+
| y    | proximity_mode_y | int  | 0       |
+------+------------------+------+---------+
| z    | proximity_mode_z | int  | 0       |
+------+------------------+------+---------+

Returns: None

Example::

	from matritools import nodefile as nf

	# create node file with 6 default node file rows

	my_node_file = nf.NodeFile("My Node File")

	my_node_file.properties[0].set_proximity_mode(1, 2, 3)

	# same as

	my_node_file.properties[0].proximity_mode_x = 1
	my_node_file.properties[0].proximity_mode_x = 2
	my_node_file.properties[0].proximity_mode_x = 3

