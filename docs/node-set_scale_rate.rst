`NodeFileRow <nodefilerow.html>`_
=================================
set_scale_rate
--------------
Sets the x, y, and z axis of scale_rate.

Parameters:

+------+--------------+------+---------+
| Name | Description  | Type | Default |
+======+==============+======+=========+
| x    | scale_rate_x | int  | 0       |
+------+--------------+------+---------+
| y    | scale_rate_y | int  | 0       |
+------+--------------+------+---------+
| z    | scale_rate_z | int  | 0       |
+------+--------------+------+---------+

Returns:
    self

Raises:
    TypeError

Example::

	from matritools import nodefile as nf

	# create node
	node = nf.Node()

	node.set_scale_rate(1, 2, 3)

	# same as

	node.scale_rate_x = 1
	node.scale_rate_y = 2
	node.scale_rate_z = 3

