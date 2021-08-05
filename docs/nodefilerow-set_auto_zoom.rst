`NodeFileRow <nodefilerow.html>`_
=================================
set_auto_zoom
-------------
Sets the x, y, and z axis of auto zoom.

Parameters:

+------+----------------------------+------------------+---------+
| Name | Description                | Type             | Default |
+======+============================+==================+=========+
| x    | auto_zoom_x                | int              | 0       |
+------+----------------------------+------------------+---------+
| y    | auto_zoom_y                | int              | 0       |
+------+----------------------------+------------------+---------+
| z    | auto_zoom_z                | int              | 0       |
+------+----------------------------+------------------+---------+

Returns: None

Example::

    from matritools import nodefile as nf

    # create node file with 6 default node file rows
    my_node_file = nf.NodeFile("My Node File")

    my_node_file.properties[0].set_auto_zoom(1,2,3)

    # same as

    my_node_file.properties[0].auto_zoom_x = 1
    my_node_file.properties[0].auto_zoom_x = 2
    my_node_file.properties[0].auto_zoom_x = 3

