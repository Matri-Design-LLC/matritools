`Node <node.html>`_
===================
set_set_lo
----------
Sets the x, y, and z axis of set_lo.

Parameters:

+------+-------------+------+---------+
| Name | Description | Type | Default |
+======+=============+======+=========+
| x    | set_lo_x    | int  | 0       |
+------+-------------+------+---------+
| y    | set_lo_y    | int  | 0       |
+------+-------------+------+---------+
| z    | set_lo_z    | int  | 0       |
+------+-------------+------+---------+

Returns:
    self

Raises:
    TypeError

Example::

	from matritools import nodefile as nf

	# create node
	node = nf.Node()

	node.set_set_low(1, 2, 3)

	# same as

	node.set_lo_x = 1
	node.set_lo_y = 2
	node.set_lo_z = 3

