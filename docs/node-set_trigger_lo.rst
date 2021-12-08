`Node <node.html>`_
===================
set_trigger_lo
--------------
Sets the x, y, and z axis of trigger_lo.

Parameters:

+------+--------------+------+---------+
| Name | Description  | Type | Default |
+======+==============+======+=========+
| x    | trigger_lo_x | int  | 0       |
+------+--------------+------+---------+
| y    | trigger_lo_y | int  | 0       |
+------+--------------+------+---------+
| z    | trigger_lo_z | int  | 0       |
+------+--------------+------+---------+

Returns:
    self

Raises:
    TypeError

Example::

	from matritools import nodefile as nf

	# create node
	node = nf.Node()

	node.set_trigger_lo(1, 2, 3)

	# same as

	node.trigger_lo_x = 1
	node.trigger_lo_y = 2
	node.trigger_lo_z = 3

