`NodeContainer <nodecontainer.html>`_
=====================================
get_nodes_of_branch_level
-------------------------
Returns a list of Nodes with a given branch level

Parameters:

+--------------+---------------------------------------+------+---------+
| Name         | Description                           | Type | Default |
+==============+=======================================+======+=========+
| branch_level | Level of Nodes to be returned         | int  | N/A     |
+--------------+---------------------------------------+------+---------+

Returns:
    List[Node]

Raises:
    TypeError

Example::

    from matritools import nodefile as nf

    # create NodeContainer
    node_container = nf.NodeContainer()

    # create Nodes with parent Nodes
    root = node_container.create_node(None, "Root")

    branch_1 = node_container.create_node(root, "branch_1")
    branch_1_child_1 = node_container.create_node(branch_1, "Branch 1, Child 1")
    branch_1_child_2 = node_container.create_node(branch_1, "Branch 1, Child 2")

    branch_2 = node_container.create_node(root, "branch_1")
    branch_2_child_1 = node_container.create_node(branch_2, "Branch 2, Child 1")
    branch_2_child_2 = node_container.create_node(branch_2, "Branch 2, Child 2")

    nodes_of_level_3 = node_container.get_nodes_of_branch_level(3)

    for node in nodes_of_level_3:
        print(node.tag_text)

    # output
    # Branch 1, Child 1
    # Branch 1, Child 2
    # Branch 2, Child 1
    # Branch 2, Child 2

