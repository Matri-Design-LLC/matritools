`Node <node.html>`_
===================
set_u_scale
-----------
Sets the x, y, and z axis of scale uniformly.

Parameters:

+-------+-------------------+-------+---------+
| Name  | Description       | Type  | Default |
+=======+===================+=======+=========+
| scale | scale_x, y, and z | float | 1       |
+-------+-------------------+-------+---------+

Returns:
    self

Raises:
    TypeError

Example::

	from matritools import nodefile as nf

	# create node
	node = nf.Node()

	node.set_u_scale(5)

	# same as

	node.scale_x = 5
	node.scale_y = 5
	node.scale_z = 5

