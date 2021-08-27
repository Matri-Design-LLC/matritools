`NodeFileRow <nodefilerow.html>`_
=================================
set_translate_rate
-----------------
Sets the x, y, and z axis of translate_vec.

Parameters:

+------+------------------+------+---------+
| Name | Description      | Type | Default |
+======+==================+======+=========+
| x    | translate_rate_x | int  | 0       |
+------+------------------+------+---------+
| y    | translate_rate_y | int  | 0       |
+------+------------------+------+---------+
| z    | translate_rate_z | int  | 0       |
+------+------------------+------+---------+

Returns: None

Raises: TypeError

Example::

	from matritools import nodefile as nf

	# create node file with 6 default node file rows

	my_node_file = nf.NodeFile("My Node File")

	my_node_file.properties[0].set_translate_rate(1, 2, 3)

	# same as

	my_node_file.properties[0].translate_rate_x = 1
	my_node_file.properties[0].translate_rate_x = 2
	my_node_file.properties[0].translate_rate_x = 3

