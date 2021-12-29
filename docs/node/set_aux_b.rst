set_aux_b
---------
Sets the x, y, and z axis of aux_b.

Parameters:

+------+-------------+------+---------+
| Name | Description | Type | Default |
+======+=============+======+=========+
| x    | aux_b_x     | int  | 30      |
+------+-------------+------+---------+
| y    | aux_b_y     | int  | 30      |
+------+-------------+------+---------+
| z    | aux_b_z     | int  | 30      |
+------+-------------+------+---------+

Returns:
    self

Raises:
    TypeError

Example::

	from matritools import nodefile as nf

	# create node
	node = nf.Node()

	node.set_aux_b(1, 2, 3)

	# same as

	node.aux_b_x = 1
	node.aux_b_y = 2
	node.aux_b_z = 3

