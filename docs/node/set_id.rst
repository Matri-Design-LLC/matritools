set_id
------
Sets id, record_id, and data to node_id.

Parameters:

+------------+---------------------------------------------+------------------+---------+
| Name       | Description                                 | Type             | Default |
+============+=============================================+==================+=========+
| node_id    | target ID                                   | int              | N/A     |
+------------+---------------------------------------------+------------------+---------+

Returns:
    self

Raises:
    TypeError

Example::

    from matritools import nodefile as nf

    # create node file with 6 default node file rows
    my_node_file = nf.NodeFile("My Node File")

    node = my_node_file.create_node()

    # set id, data and record id
    row.set_id(10)

    # same as

    row.id = 10
    row.data = 10
    row.record_id = 10

