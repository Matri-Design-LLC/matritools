make_link
---------
Creates a visible link between link_node_a and link_node_b.
Returns the created Node.

Parameters:

+-----------------+---------------------------------------------------------------------+------+---------+
| Name            | Description                                                         | Type | Default |
+=================+=====================================================================+======+=========+
| link_node_a     | Node to be linked from                                              | Node | N/A     |
+-----------------+---------------------------------------------------------------------+------+---------+
| link_node_b     | Node to be linked to                                                | Node | N/A     |
+-----------------+---------------------------------------------------------------------+------+---------+

Returns:
    Node

Raises:
    TypeError

    RuntimeError

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
    bar = my_node_file.make_link(sphere_1.id, sphere_2.id)

    print(bar.id)

