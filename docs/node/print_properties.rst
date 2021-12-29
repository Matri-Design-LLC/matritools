print_properties
----------------
Prints the label and value of each property.

Parameters:
    None

Returns:
    self

Raises:
    None

Example::

    from matritools import nodefile as nf

    # create node file with 6 default node file rows
    my_node_file = nf.NodeFile("My Node File")

    # print camera view 1 properties
    camera_view = my_node_file.get_node_by_id(2).print_properties()
    # output:
    # id: 2
    # type: 1
    # data: 2
    # ...
    # table_id: 0
    # record_id: 0
    # size: 420

