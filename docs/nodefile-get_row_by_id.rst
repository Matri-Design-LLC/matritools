`NodeFile <nodefile.html>`_
===========================
get_row_by_id
-------------
Returns a NodeFileRow at the requested ID.

Parameters:

+------------+---------------------------------------------------------+------------------+---------+
| Name       | Description                                             | Type             | Default |
+============+=========================================================+==================+=========+
| row_id     | Returns the row with the given ID, None if no row found | int              | None    |
+------------+---------------------------------------------------------+------------------+---------+

Returns: NodeFileRow, None

Example::

    from matritools import nodefile as nf

    # create node file with 6 default node file rows
    my_node_file = nf.NodeFile("My Node File")

    # edit first camera view position
    camera_view = my_node_file.get_row_by_id(2)
    camera_view.set_translate(0, 0, 0)

