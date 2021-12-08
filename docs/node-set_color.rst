`Node <node.html>`_
===================
set_color
---------
Sets the x, y, and z axis of color.

Parameters:

+------+-------------+------+---------+
| Name | Description | Type | Default |
+======+=============+======+=========+
| r    | color_r     | int  | 0       |
+------+-------------+------+---------+
| g    | color_g     | int  | 0       |
+------+-------------+------+---------+
| b    | color_b     | int  | 0       |
+------+-------------+------+---------+
| a    | color_a     | int  | 255     |
+------+-------------+------+---------+

Returns:
    self

Raises:
    TypeError

Example::

	from matritools import nodefile as nf

	# create node
	node = nf.Node()

	node.set_color(1, 2, 3, 4)

	# same as

	node.color_r = 1
	node.color_g = 2
	node.color_b = 3
	node.color_a = 4

