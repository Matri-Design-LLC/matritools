`Node <node.html>`_
===================
set_rotate
----------
Sets the x, y, and z axis of rotate.

Parameters:

+------+-------------+-------+---------+
| Name | Description | Type  | Default |
+======+=============+=======+=========+
| x    | rotate_x    | float | 0       |
+------+-------------+-------+---------+
| y    | rotate_y    | float | 0       |
+------+-------------+-------+---------+
| z    | rotate_z    | float | 0       |
+------+-------------+-------+---------+

Returns:
    self

Raises:
    TypeError

Example::

	from matritools import nodefile as nf

	# create node
	node = nf.Node()

	node.set_rotate(1, 2, 3)

	# same as

	node.rotate_x = 1
	node.rotate_y = 2
	node.rotate_z = 3

