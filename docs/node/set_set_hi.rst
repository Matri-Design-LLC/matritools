set_set_hi
----------
Sets the x, y, and z axis of set_hi.

Parameters:

+------+-------------+------+---------+
| Name | Description | Type | Default |
+======+=============+======+=========+
| x    | set_hi_x    | int  | 0       |
+------+-------------+------+---------+
| y    | set_hi_y    | int  | 0       |
+------+-------------+------+---------+
| z    | set_hi_z    | int  | 0       |
+------+-------------+------+---------+

Returns:
    self

Raises:
    TypeError

Example::

	from matritools import nodefile as nf

	# create node
	node = nf.Node()

	node.set_set_hi(1, 2, 3)

	# same as

	node.set_hi_x = 1
	node.set_hi_y = 2
	node.set_hi_z = 3

