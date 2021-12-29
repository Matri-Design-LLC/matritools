set_scale
---------
Sets the x, y, and z axis of scale.

Parameters:

+------+-------------+-------+---------+
| Name | Description | Type  | Default |
+======+=============+=======+=========+
| x    | scale_x     | float | 0       |
+------+-------------+-------+---------+
| y    | scale_y     | float | 0       |
+------+-------------+-------+---------+
| z    | scale_z     | float | 0       |
+------+-------------+-------+---------+

Returns:
    self

Raises:
    TypeError

Example::

	from matritools import nodefile as nf

	# create node
	node = nf.Node()

	node.set_scale(1, 2, 3)

	# same as

	node.scale_x = 1
	node.scale_y = 2
	node.scale_z = 3

