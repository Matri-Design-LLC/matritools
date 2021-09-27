`NodeFileRow <nodefilerow.html>`_
=================================
set_aux_b
---------
Sets the x, y, and z axis of aux_b.

Parameters:

+------+-------------+------+---------+
| Name | Description | Type | Default |
+======+=============+======+=========+
| x    | aux_b_x     | int  | 30      |
+------+-------------+------+---------+
| y    | aux_b_y     | int  | 30      |
+------+-------------+------+---------+
| z    | aux_b_z     | int  | 30      |
+------+-------------+------+---------+

Returns: None

Raises: TypeError

Example::

	from matritools import nodefile as nf

	# create node file with 6 default node file rows

	my_node_file = nf.NodeFile("My Node File")

	my_node_file.properties[0].set_aux_b(1, 2, 3)

	# same as

	my_node_file.properties[0].aux_b_x = 1
	my_node_file.properties[0].aux_b_x = 2
	my_node_file.properties[0].aux_b_x = 3

