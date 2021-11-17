`NodeFileRow <nodefilerow.html>`_
=================================
set_color_by_name
-----------------
Sets the r, g, b, and a axis of color.

Parameters:

+----------+------------------------------------------------------------------------+------+---------+
| Name     | Description                                                            | Type | Default |
+==========+========================================================================+======+=========+
| hex_code | hex_code of a color i.e '#FF0000', Can contain '#' but doesn't have to | str  | None    |
+----------+------------------------------------------------------------------------+------+---------+

Returns: None

Raises: TypeError, ValueError

Example::

	from matritools import nodefile as nf

	# create node file with 6 default node file rows

	my_node = nf.NodeFileRow()

	my_node.set_color_by_hex('#FF0000')

	# same as

	my_node.properties[0].color_r = 255
	my_node.properties[0].color_g = 0
	my_node_file.properties[0].color_b = 0
	my_node.properties[0].color_a = 255
