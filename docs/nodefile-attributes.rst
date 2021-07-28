`NodeFile <nodefile.html>`_
===========================
Attributes
----------

+----------------+-----------------------------------------------+-------------------+---------+
| Name           | Description                                   | Type              | Default |
+================+===============================================+===================+=========+
| node_file_rows | list of NodeFileRows that make up a node file | List[NodeFileRow] | []      |
+----------------+-----------------------------------------------+-------------------+---------+

Example::

    from matritools import nodefile as nf
    import copy

    my_node_file = nf.NodeFile("filename")

    # change position of root object
    my_node_file.node_file_rows[0].set_translate(10, 0, 0)

    # new NodeFileRow to node file
    new_row = nf.NodeFileRow()
    my_node_file.node_file_rows.append(new_row)

    # remove object from node file
    my_node_file.node_file_rows.remove(my_node_file.node_file_rows[1])

    # duplicate object and change position
    duplicated_row = copy.deepcopy(my_node_file.node_file_rows[5])
    duplicated_row.set_translate(40, 10, 0)
    my_node_file.node_file_rows.append(duplicated_row)

