set_color_by_hex
-----------------
Sets the r, g, b, and a axis of color.

Parameters:

+----------+------------------------------------------------------------------------+------+---------+
| Name     | Description                                                            | Type | Default |
+==========+========================================================================+======+=========+
| hex_code | hex_code of a color i.e '#FF0000', Can contain '#' but doesn't have to | str  | N/A     |
+----------+------------------------------------------------------------------------+------+---------+

Returns:
    self

Raises:
    TypeError,
    ValueError

Example::

	from matritools import nodefile as nf

	# create node
	node = nf.Node()

	node.set_color_by_hex('#FF0000')

	# same as

	node.color_r = 255
	node.color_g = 0
	node.color_b = 0
	node.color_a = 255
