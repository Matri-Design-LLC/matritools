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

Returns:
    self

Raises:
    TypeError

Example::

	from matritools import nodefile as nf

	# create node
	node = nf.Node()

	node.set_trigger_hi(1, 2, 3)

	# same as

	node.trigger_hi_x = 1
	node.trigger_hi_y = 2
	node.trigger_hi_z = 3

