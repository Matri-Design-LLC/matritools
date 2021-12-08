`NodeContainer <nodecontainer.html>`_
=====================================
get_last_node
-------------
Returns the last Node of the NodeContainer. Returns None if nodes is empty.

Parameters:
    None

Returns:
    Node

    None

Raises:
    None

Example::

    from matritools import nodefile as nf

    # create a NodeContainer
    node_container = nf.NodeContainer()
    node_container.create_node()

    last_id = node_container.get_last_node().id

    print(last_id)

    # output:
    # 1

    node_container.create_node()

    last_id = node_container.get_last_node().id

    # output:
    # 2

