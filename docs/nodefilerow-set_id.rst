`NodeFileRow <nodefilerow.html>`_
=================================
set_id
------
Sets id, record_id, and data to row_id.

Parameters:

+------------+---------------------------------------------+------------------+---------+
| Name       | Description                                 | Type             | Default |
+============+=============================================+==================+=========+
| row_id     | target ID                                   | int              | None    |
+------------+---------------------------------------------+------------------+---------+

Returns: None

Example::

    from matritools import nodefile as nf

    # create node file with 6 default node file rows
    my_node_file = nf.NodeFile("My Node File")

    row = my_node_file.create_node_row()

    # set id, data and record id
    row.set_id(10)

    # same as

    row.id = 10
    row.data = 10
    row.record_id = 10

