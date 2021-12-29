set_translate
-------------
Sets the x, y, and z axis of translate.

Parameters:

+------+-------------+-------+---------+
| Name | Description | Type  | Default |
+======+=============+=======+=========+
| x    | translate_x | float | 0       |
+------+-------------+-------+---------+
| y    | translate_y | float | 0       |
+------+-------------+-------+---------+
| z    | translate_z | float | 0       |
+------+-------------+-------+---------+

Returns:
    self

Raises:
    TypeError

Example::

	from matritools import nodefile as nf

	# create node
	node = nf.Node()

	node.set_translate(1, 2, 3)

	# same as

	node.translate_x = 1
	node.translate_y = 2
	node.translate_z = 3

