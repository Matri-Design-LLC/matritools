`NodeContainer <nodecontainer.html>`_
=====================================
length
------
Returns the number of Nodes in this file.

Parameters:
    None

Returns:
    int

Raises:
    None

Example::

    from matritools import nodefile as nf

    # create a NodeContainer
    node_container = nf.NodeContainer()

    length = node_container.length()

    print(length)

    # output:
    # 0

    node_container.create_node()

    length = node_container.length()

    print(length)

    # output:
    # 1

