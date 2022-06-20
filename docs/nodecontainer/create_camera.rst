create_node
-----------
Adds a camera to the NodeFile.

Parameters:

+-------------+----------------------------------------------------------------------------+------+---------+
| Name        | Description                                                                | Type | Default |
+=============+============================================================================+======+=========+
| template    | Created node will be a copy of template if one is passed.                  | Node | None    |
+-------------+----------------------------------------------------------------------------+------+---------+

Returns:
    Node

Raises:
    TypeError

    RuntimeError

Example::

    from matritools import nodefile as nf

    # create node file with 6 default node file rows
    my_node_file = nf.NodeFile("My Node File")


    camera1 = my_node_file.create_camera()
    camera1.set_rotate(90, -45)

    camera2 = my_node_file.create_camera(camera1)
    camera2.set_translate(20)

    my_node_file.write_to_csv()

