`NodeFileRow <nodefilerow.html>`_
=================================
set_tag
-------
Sets tag text and tag mode.

Parameters:

+------------+---------------------------------------------+------------------+---------+
| Name       | Description                                 | Type             | Default |
+============+=============================================+==================+=========+
| tag_text   | sets NodeFile.tag_text                      | any              | None    |
+------------+---------------------------------------------+------------------+---------+
| tag_mode   | sets NodeFile.tag_mode                      | int              | None    |
+------------+---------------------------------------------+------------------+---------+

Returns: None

Raises: TypeError

Example::

    from matritools import nodefile as nf

    # create node file with 6 default node file rows
    my_node_file = nf.NodeFile("My Node File")

    row = my_node_file.create_node_row()

    # set tag and tag mode
    row.set_tag("my tag", 1)

    # same as

    row.tag_text = "my tag"
    row.tag_mode = 1

