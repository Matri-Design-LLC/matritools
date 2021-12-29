set_proximity_mode
------------------
Sets the x, y, and z axis of proximity_mode.

Parameters:

+------+------------------+------+---------+
| Name | Description      | Type | Default |
+======+==================+======+=========+
| x    | proximity_mode_x | int  | 0       |
+------+------------------+------+---------+
| y    | proximity_mode_y | int  | 0       |
+------+------------------+------+---------+
| z    | proximity_mode_z | int  | 0       |
+------+------------------+------+---------+

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

	node.proximity_mode_x = 1
	node.proximity_mode_y = 2
	node.proximity_mode_z = 3

