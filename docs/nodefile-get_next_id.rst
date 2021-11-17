`NodeFile <nodefile.html>`_
===========================
get_next_id
-----------
Returns the last NodeFileRow of the file.

Parameters: None

Returns: int

Raises: None

Example::

    from matritools import nodefile as nf

    # create a node file
    my_node_file = nf.NodeFile("My Node File")

    last_id = my_node_file.get_next_id()

    print(last_id)

    # output:
    # 6

