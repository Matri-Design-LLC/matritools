set_rotate_rate
------------------
Sets the x, y, and z axis of rotate_rate.

Parameters:

+------+------------------+------+---------+
| Name | Description      | Type | Default |
+======+==================+======+=========+
| x    | rotate_rate_x    | int  | 0       |
+------+------------------+------+---------+
| y    | rotate_rate_y    | int  | 0       |
+------+------------------+------+---------+
| z    | rotate_rate_z    | int  | 0       |
+------+------------------+------+---------+

Returns:
    self

Raises:
    TypeError

Example::

	from matritools import nodefile as nf

	# create node
	node = nf.Node()

	node.set_rotate_rate(1, 2, 3)

	# same as

	node.rotate_rate_x = 1
	node.rotate_rate_y = 2
	node.rotate_rate_z = 3

