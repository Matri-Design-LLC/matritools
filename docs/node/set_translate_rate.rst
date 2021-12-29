set_translate_rate
------------------
Sets the x, y, and z axis of translate_rate.

Parameters:

+------+------------------+------+---------+
| Name | Description      | Type | Default |
+======+==================+======+=========+
| x    | translate_rate_x | int  | 0       |
+------+------------------+------+---------+
| y    | translate_rate_y | int  | 0       |
+------+------------------+------+---------+
| z    | translate_rate_z | int  | 0       |
+------+------------------+------+---------+

Returns:
    self

Raises:
    TypeError

Example::

	from matritools import nodefile as nf

	# create node
	node = nf.Node()

	node.set_translate_rate(1, 2, 3)

	# same as

	node.translate_rate_x = 1
	node.translate_rate_y = 2
	node.translate_rate_z = 3

