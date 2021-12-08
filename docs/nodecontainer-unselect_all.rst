`NodeContainer <nodecontainer.html>`_
=====================================
unselect_all
------------
Changes the selected property of all NodeContainer's Nodes to 0.

Parameters:
    None

Returns:
    self

Example::

    from matritools import nodefile as nf

    # Create NodeContainer
    node_container = nf.NodeContainer()

    # create 5 Nodes and change selected to 1
    for i in range(5):
        node_container.create_node().selected = 1

    for node in node_container.nodes:
        print(node.selected)

    # output:
    # 1
    # 1
    # 1
    # 1
    # 1

    node_container.unselect_all()

    for node in node_container.nodes:
        print(node.selected)

    # output:
    # 0
    # 0
    # 0
    # 0
    # 0



