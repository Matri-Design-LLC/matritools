set_rotate_vec
--------------
Sets the x, y, and z axis of rotate_vec.

Parameters:

+------+--------------+------+---------+
| Name | Description  | Type | Default |
+======+==============+======+=========+
| x    | rotate_vec_x | int  | 0       |
+------+--------------+------+---------+
| y    | rotate_vec_y | int  | 0       |
+------+--------------+------+---------+
| z    | rotate_vec_z | int  | 0       |
+------+--------------+------+---------+
| s    | rotate_vec_s | int  | 0       |
+------+--------------+------+---------+

Returns:
    self

Raises:
    TypeError

Example::

	from matritools import nodefile as nf

	# create node
	node = nf.Node()

	node.set_rotate_vec(1, 2, 3, 4)

	# same as

	node.rotate_vec_x = 1
	node.rotate_vec_y = 2
	node.rotate_vec_z = 3
	node.rotate_vec_s = 4

