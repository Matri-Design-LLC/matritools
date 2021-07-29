`NodeFileRow <nodefilerow.html>`_
=================================
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

Returns: None

Example::

	from matritools import nodefile as nf

	# create node file with 6 default node file rows

	my_node_file = nf.NodeFile("My Node File")

	my_node_file.properties[0].set_rotate_vec(1, 2, 3, 4)

	# same as

	my_node_file.properties[0].rotate_vec_x = 1
	my_node_file.properties[0].rotate_vec_x = 2
	my_node_file.properties[0].rotate_vec_x = 3
	my_node_file.properties[0].rotate_vec_s = 4

