`NodeFile <nodefile.html>`_
===========================
create_node_row
---------------
Creates a NodeFileRow out of the current NodeFile properties and appends them to the NodeFileRow list.
After the new NodeFileRow is added, id is incremented by one.

Parameters:

+------------+---------------------------------------------+------------------+---------+
| Name       | Description                                 | Type             | Default |
+============+=============================================+==================+=========+
| tag_text   | tag associated with created Node File Row   | str              | ""      |
+------------+---------------------------------------------+------------------+---------+

Returns: matritools.nodefile.NodeFileRow

Example::

    from matritools import nodefile as nf

    # create node file with 6 default node file rows
    my_node_file = nf.NodeFile("My Node File")

    my_node_file.properties.topo = nf.NodeFile.geos["sphere"]

    # Do you wanna build a snow man?

    # create snow man base
    my_node_file.properties.set_translate(0,0,0)
    my_node_file.properties.set_u_scale(3)
    row = my_node_file.create_node_row("Base")
    print(row.to_string())

    # create object snow man body
    my_node_file.properties.set_translate(0,0,3)
    my_node_file.properties.set_u_scale(2)
    row = my_node_file.create_node_row("Body")
    print(row.to_string())

    # create object snow man head
    my_node_file.properties.set_translate(0,0,5)
    my_node_file.properties.set_u_scale(1)
    row = my_node_file.create_node_row("Object 3")
    print(row.to_string())

