`NodeFile <nodefile.html>`_
===========================
Constructor
-----------

Parameters:

+------------+-----------------------------------------------------+------------------+---------+
| Name       | Description                                         | Type             | Default |
+============+=====================================================+==================+=========+
| file_name  | name of node and tag file created on write_to_csv() | str              | N/A     |
+------------+-----------------------------------------------------+------------------+---------+

Raises:
    TypeError

    RuntimeError

Example::

    from matritools import nodefile as nf

    # create node file with 6 default node file rows
    my_node_file = nf.NodeFile("my_file_name")

    my_node_file.write_to_csv()
    # my_file_name_node.csv and my_file_name_tag.csv will be created

