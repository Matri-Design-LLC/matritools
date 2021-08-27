`NodeFileRow <nodefilerow.html>`_
=================================
set_translate
-------------
Sets the x, y, and z axis of translate.

Parameters:

+------+-------------+-------+---------+
| Name | Description | Type  | Default |
+======+=============+=======+=========+
| x    | translate_x | float | 0       |
+------+-------------+-------+---------+
| y    | translate_y | float | 0       |
+------+-------------+-------+---------+
| z    | translate_z | float | 0       |
+------+-------------+-------+---------+

Returns: None

Raises: TypeError

Example::

	from matritools import nodefile as nf

	# create node file with 6 default node file rows

	my_node_file = nf.NodeFile("My Node File")

	my_node_file.properties[0].set_translate(1, 2, 3)

	# same as

	my_node_file.properties[0].translate_x = 1
	my_node_file.properties[0].translate_x = 2
	my_node_file.properties[0].translate_x = 3

