`NodeFileRow <nodefilerow.html>`_
=================================
set_scale_rate
--------------
Sets the x, y, and z axis of scale_rate.

Parameters:

+------+--------------+------+---------+
| Name | Description  | Type | Default |
+======+==============+======+=========+
| x    | scale_rate_x | int  | 0       |
+------+--------------+------+---------+
| y    | scale_rate_y | int  | 0       |
+------+--------------+------+---------+
| z    | scale_rate_z | int  | 0       |
+------+--------------+------+---------+

Returns: None

Raises: TypeError

Example::

	from matritools import nodefile as nf

	# create node file with 6 default node file rows

	my_node_file = nf.NodeFile("My Node File")

	my_node_file.properties[0].set_scale_rate(1, 2, 3)

	# same as

	my_node_file.properties[0].scale_rate_x = 1
	my_node_file.properties[0].scale_rate_x = 2
	my_node_file.properties[0].scale_rate_x = 3

