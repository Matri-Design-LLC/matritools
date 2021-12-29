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

Returns:
    self

Raises:
    TypeError

Example::

	from matritools import nodefile as nf

	# create node
	node = nf.Node()

	node.set_tag_offset(1, 2, 3)

	# same as

	node.tag_offset_x = 1
	node.tag_offset_y = 2
	node.tag_offset_z = 3

