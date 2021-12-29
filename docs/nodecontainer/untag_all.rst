untag_all
---------
Sets tag_mode of all Nodes in a NodeContainer to 0.

Parameters:
    None

Returns:
    None

Raises:
    self

Example::

    from matritools import nodefile as nf

    # Create NodeContainer
    node_container = nf.NodeContainer()

    # create 5 Nodes and change selected to 1
    for i in range(5):
        node_container.create_node().tag_mode = 1

    for node in node_container.nodes:
        print(node.tag_mode)

    # output:
    # 1
    # 1
    # 1
    # 1
    # 1

    node_container.untag_all()

    for node in node_container.nodes:
        print(node.tag_mode)

    # output:
    # 0
    # 0
    # 0
    # 0
    # 0

