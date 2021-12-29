create_node
-----------
Creates and returns a Node inside of the NodeContainer.

Parameters:

+-------------+----------------------------------------------------------------------------+------+---------+
| Name        | Description                                                                | Type | Default |
+=============+============================================================================+======+=========+
| parent_node | Node that newly created Node will be associated with                       | Node | None    |
+-------------+----------------------------------------------------------------------------+------+---------+
| tag_text    | text that will be written in the tag file associated with the created Node | str  | ""      |
+-------------+----------------------------------------------------------------------------+------+---------+
| tag_mode    | int representing how the tag should be displayed by default                | int  | 0       |
+-------------+----------------------------------------------------------------------------+------+---------+
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


    # Do you wanna build a snow man?

    # create a root node, (parent_node=None, template=None)
    base_node = my_node_file.create_node(tag_text="Base", tag_mode=1)
    base_node.topo = nf.topo['sphere']
    base_node.geometry = nf.geos['sphere']
    base_node.set_translate(0,0,0)
    node.set_u_scale(3)

    # create object snow man body. By passing base_node as a template, body will have similar attributes.
    body = my_node_file.create_node(base_node, "Body", 1, base_node)
    my_node_file.properties.set_translate(0,0,3)
    my_node_file.properties.set_u_scale(2)

    # create object snow man head
    head = my_node_file.create_node(body, "Head", 1, body)
    my_node_file.properties.set_translate(0,0,5)
    my_node_file.properties.set_u_scale(1)

