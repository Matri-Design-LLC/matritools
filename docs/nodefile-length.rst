`NodeFile <nodefile.html>`_
===========================
length
------
Returns the number of NodeFileRows in this file.

Parameters: None

Returns: int

Raises: None

Example::

    from matritools import nodefile as nf

    # create a node file
    my_node_file = nf.NodeFile("My Node File")

    length = my_node_file.length()

    print(length)

    # output:
    # 6 << default 6 NodeFileRows

