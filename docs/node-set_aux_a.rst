`Node <node.html>`_
===================
set_aux_a
---------
Sets the x, y, and z axis of aux_a.

Parameters:

+------+-------------+------+---------+
| Name | Description | Type | Default |
+======+=============+======+=========+
| x    | aux_a_x     | int  | 30      |
+------+-------------+------+---------+
| y    | aux_a_y     | int  | 30      |
+------+-------------+------+---------+
| z    | aux_a_z     | int  | 30      |
+------+-------------+------+---------+

Returns:
    self

Raises:
    TypeError

Example::

	from matritools import nodefile as nf

	# create node
	node = nf.Node()

	node.set_aux_a(1, 2, 3)

	# same as

	node.aux_a_x = 1
	node.aux_a_y = 2
	node.aux_a_z = 3

