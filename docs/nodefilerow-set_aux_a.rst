`NodeFileRow <nodefilerow.html>`_
=================================
set_aux_a
---------
Sets the x, y, and z axis of aux_a.

Parameters:

+------+-------------+------+---------+
| Name | Description | Type | Default |
+======+=============+======+=========+
| x    | aux_a_x     | int  | 30      |
+------+-------------+------+---------+
| y    | aux_a_y     | int  | 30      |
+------+-------------+------+---------+
| z    | aux_a_z     | int  | 30      |
+------+-------------+------+---------+

Returns: None

Example::

	from matritools import nodefile as nf

	# create node file with 6 default node file rows

	my_node_file = nf.NodeFile("My Node File")

	my_node_file.properties[0].set_aux_a(1, 2, 3)

	# same as

	my_node_file.properties[0].aux_a_x = 1
	my_node_file.properties[0].aux_a_x = 2
	my_node_file.properties[0].aux_a_x = 3

