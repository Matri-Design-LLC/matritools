`NodeContainer <nodecontainer.html>`_
=====================================
get_node_by_id
--------------
Returns the Node with the given ID, None if no Node found.

Parameters:

+------------+---------------------------------------------------------+------------------+---------+
| Name       | Description                                             | Type             | Default |
+============+=========================================================+==================+=========+
| node_id    | ID of requested Node                                    | int              | N/A     |
+------------+---------------------------------------------------------+------------------+---------+

Returns:
    Node

    None

Raises:
    TypeError

Example::

    from matritools import nodefile as nf

    # create node file with 6 default node file rows
    my_node_file = nf.NodeFile("My Node File")

    # edit first camera view position
    camera_view = my_node_file.get_node_by_id(2)
    camera_view.set_translate(0, 0, 0)

