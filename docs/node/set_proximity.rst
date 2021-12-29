set_proximity
-------------
Sets the x, y, and z axis of proximity.

Parameters:

+------+-------------+-------+---------+
| Name | Description | Type  | Default |
+======+=============+=======+=========+
| x    | proximity_x | float | 0       |
+------+-------------+-------+---------+
| y    | proximity_y | float | 0       |
+------+-------------+-------+---------+
| z    | proximity_z | float | 0       |
+------+-------------+-------+---------+

Returns:
    self

Raises:
    TypeError

Example::

	from matritools import nodefile as nf

	# create node
	node = nf.Node()

	node.set_proximity(1, 2, 3)

	# same as

	node.proximity_x = 1
	node.proximity_y = 2
	node.proximity_z = 3

