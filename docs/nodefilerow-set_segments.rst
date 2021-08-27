`NodeFileRow <nodefilerow.html>`_
=================================
set_segments
---------
Sets the x, y, and z axis of segments.

Parameters:

+------+-------------+------+---------+
| Name | Description | Type | Default |
+======+=============+======+=========+
| x    | segments_x  | int  | 20      |
+------+-------------+------+---------+
| y    | segments_y  | int  | 12      |
+------+-------------+------+---------+
| z    | segments_z  | int  | 0       |
+------+-------------+------+---------+

Returns: None

Raises: TypeError

Example::

	from matritools import nodefile as nf

	# create node file with 6 default node file rows

	my_node_file = nf.NodeFile("My Node File")

	my_node_file.properties[0].set_segments(1, 2, 3)

	# same as

	my_node_file.properties[0].segments_x = 1
	my_node_file.properties[0].segments_x = 2
	my_node_file.properties[0].segments_x = 3

