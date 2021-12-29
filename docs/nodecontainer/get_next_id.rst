get_next_id
-----------
Returns the the last id + 1, Returns 1 if empty.

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

    next_id = node_container.get_next_id()

    print(last_id)

    # output:
    # 1

    node_container.create_node()

    next_id = node_container.get_next_id()

    print(last_id)

    # output:
    # 2

    node_container.create_node()

    next_id = node_container.get_next_id()

    # output:
    # 3

