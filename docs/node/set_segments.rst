set_segments
------------
Sets the x, y, and z axis of segments.

Parameters:

+------+-------------+------+---------+
| Name | Description | Type | Default |
+======+=============+======+=========+
| x    | segments_x  | int  | 20      |
+------+-------------+------+---------+
| y    | segments_y  | int  | 12      |
+------+-------------+------+---------+
| z    | segments_z  | int  | 0       |
+------+-------------+------+---------+

Returns:
    self

Raises:
    TypeError

Example::

	from matritools import nodefile as nf

	# create node
	node = nf.Node()

	node.set_segments(1, 2, 3)

	# same as

	node.segments_x = 1
	node.segments_y = 2
	node.segments_z = 3

