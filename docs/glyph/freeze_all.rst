freeze_all
----------
Sets all Nodes in glyph to be frozen or unfrozen

Parameters:

+--------------+---------------------------------------+------+---------+
| Name         | Description                           | Type | Default |
+==============+=======================================+======+=========+
| freeze       | Should all rows in glyph be frozen    | bool | True    |
+--------------+---------------------------------------+------+---------+

Returns:
    self

Raises:
    None

Example::

    from matritools import nodefile as nf

    # Create NodeContainer
    node_container = nf.NodeContainer()

    # create 5 Nodes and change selected to 1
    for i in range(5):
        node_container.create_node().freeze = 1

    for node in node_container.nodes:
        print(node.freeze)

    # output:
    # 1
    # 1
    # 1
    # 1
    # 1

    node_container.freeze_all(False)

    for node in node_container.nodes:
        print(node.freeze)

    # output:
    # 0
    # 0
    # 0
    # 0
    # 0

    node_container.freeze_all()

    for node in node_container.nodes:
        print(node.freeze)

    # output:
    # 1
    # 1
    # 1
    # 1
    # 1

