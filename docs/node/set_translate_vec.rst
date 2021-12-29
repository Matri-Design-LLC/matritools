set_translate_vec
-----------------
Sets the x, y, and z axis of translate_vec.

Parameters:

+------+-----------------+------+---------+
| Name | Description     | Type | Default |
+======+=================+======+=========+
| x    | translate_vec_x | int  | 0       |
+------+-----------------+------+---------+
| y    | translate_vec_y | int  | 0       |
+------+-----------------+------+---------+
| z    | translate_vec_z | int  | 0       |
+------+-----------------+------+---------+

Returns:
    self

Raises:
    TypeError

Example::

	# create node
	node = nf.Node()

	node.set_translate_vec(1, 2, 3)

	# same as

	node.translate_vec_x = 1
	node.translate_vec_y = 2
	node.translate_vec_z = 3

