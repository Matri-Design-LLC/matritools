`Node <node.html>`_
===================
set_color_by_id
---------------
Sets r,g,b to 0 and sets color by color_id, palette_id and color_a.

Parameters:

+------------+------------------------------------------------------------------------+------+---------+
| Name       | Description                                                            | Type | Default |
+============+========================================================================+======+=========+
| color_id   | color_id of a color in a given palette                                 | int  | N/A     |
+------------+------------------------------------------------------------------------+------+---------+
| palette_id | ID of a palette that effects what color color_id represents            | int  | None    |
+------------+------------------------------------------------------------------------+------+---------+
| color_a    | int between 0 - 255 that effects the transparency of the color         | int  | 255     |
+------------+------------------------------------------------------------------------+------+---------+

Returns:
    self

Raises:
    TypeError

Example::

	from matritools import nodefile as nf

	# create node
	node = nf.Node()

	node.set_color(255, 128, 128, 255)
	print(node.color_to_list())

	# output:
	# [255, 128, 128, 255]

	node.set_color_by_id(2, 0, 255)

	print(node.color_to_list())

	# output:
	# [0, 0, 0, 255]

	print(node.color_id)
	print(node.palette_id)

	# output:
	# 2
	# 0

