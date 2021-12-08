`Node <node.html>`_
===================
to_string
---------
Returns a string of all Node properties seperated by commas.

Parameters:

+------------+---------------------------------------------+------------------+---------+
| Name       | Description                                 | Type             | Default |
+============+=============================================+==================+=========+
| node_id    | target ID                                   | int              | None    |
+------------+---------------------------------------------+------------------+---------+

Returns:
    str

Raises:
    None

Example::

    from matritools import nodefile as nf

    # create node file with 6 default node file rows
    my_node_file = nf.NodeFile("My Node File")

    # print first camera view properties
    print(my_node_file.get_row_by_id(2))
    # output:
    # 2,1,2,0,0,0,2,2,3,0,0,0,0,1,0,0,0,0,0,0,0,0,0.008645,0.825266,-0.564678,1,1,1,...,0,0,0,420


