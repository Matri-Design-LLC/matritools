`NodeFileRow <nodefilerow.html>`_
=================================
make_link
---------
Creates a visible link between link_id_a, and link_id_b using this NodeFileRow's properties

Parameters:

+------------+---------------------------------------------+------------------+---------+
| Name       | Description                                 | Type             | Default |
+============+=============================================+==================+=========+
| link_id_a  | id of a NodeFileRow to be linked from       | int              | None    |
+------------+---------------------------------------------+------------------+---------+
| link_id_b  | id of a NodeFileRow to be linked to         | int              | None    |
+------------+---------------------------------------------+------------------+---------+

Returns: None

Example::

    from matritools import nodefile as nf

    # create node file with 6 default node file rows
    my_node_file = nf.NodeFile("My Node File")

    # create sphere barbell

    # sphere 1
    my_node_file.properties.topo = nf.NodeFileRow.topos["sphere"]
    sphere_1 = my_node_file.create_node_row("Sphere 1")

    # sphere 2
    my_node_file.properties.set_translate(10, 0, 0)
    sphere_2 = my_node_file.create_node_row("Sphere 2")

    # create bar
    bar = my_node_file.create_node_row("Bar")
    bar.make_link(sphere_1.id, sphere_2.id)

