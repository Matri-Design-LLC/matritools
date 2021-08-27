`NodeFileRow <nodefilerow.html>`_
=================================
set_set_lo
---------
Sets the x, y, and z axis of set_lo.

Parameters:

+------+-------------+------+---------+
| Name | Description | Type | Default |
+======+=============+======+=========+
| x    | set_lo_x    | int  | 0       |
+------+-------------+------+---------+
| y    | set_lo_y    | int  | 0       |
+------+-------------+------+---------+
| z    | set_lo_z    | int  | 0       |
+------+-------------+------+---------+

Returns: None

Raises: TypeError

Example::

	from matritools import nodefile as nf

	# create node file with 6 default node file rows

	my_node_file = nf.NodeFile("My Node File")

	my_node_file.properties[0].set_set_lo(1, 2, 3)

	# same as

	my_node_file.properties[0].set_lo_x = 1
	my_node_file.properties[0].set_lo_x = 2
	my_node_file.properties[0].set_lo_x = 3

