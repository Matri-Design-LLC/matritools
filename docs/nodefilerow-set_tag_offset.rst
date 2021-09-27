`NodeFileRow <nodefilerow.html>`_
=================================
set_tag_offset
--------------
Sets the x, y, and z axis of tag_offset.

Parameters:

+------+--------------+-------+---------+
| Name | Description  | Type  | Default |
+======+==============+=======+=========+
| x    | tag_offset_x | float | 0       |
+------+--------------+-------+---------+
| y    | tag_offset_y | float | 0       |
+------+--------------+-------+---------+
| z    | tag_offset_z | float | 0       |
+------+--------------+-------+---------+

Returns: None

Raises: TypeError

Example::

	from matritools import nodefile as nf

	# create node file with 6 default node file rows

	my_node_file = nf.NodeFile("My Node File")

	my_node_file.properties[0].set_tag_offset(1, 2, 3)

	# same as

	my_node_file.properties[0].tag_offset_x = 1
	my_node_file.properties[0].tag_offset_x = 2
	my_node_file.properties[0].tag_offset_x = 3

