`NodeFileRow <nodefilerow.html>`_
=================================
set_trigger_hi
--------------
Sets the x, y, and z axis of trigger_hi.

Parameters:

+------+--------------+------+---------+
| Name | Description  | Type | Default |
+======+==============+======+=========+
| x    | trigger_hi_x | int  | 0       |
+------+--------------+------+---------+
| y    | trigger_hi_y | int  | 0       |
+------+--------------+------+---------+
| z    | trigger_hi_z | int  | 0       |
+------+--------------+------+---------+

Returns: None

Raises: TypeError

Example::

	from matritools import nodefile as nf

	# create node file with 6 default node file rows

	my_node_file = nf.NodeFile("My Node File")

	my_node_file.properties[0].set_trigger_hi(1, 2, 3)

	# same as

	my_node_file.properties[0].trigger_hi_x = 1
	my_node_file.properties[0].trigger_hi_x = 2
	my_node_file.properties[0].trigger_hi_x = 3

