get_node_indexes
----------------
Prints out the indexes of a glyph templates NodeFileRows with their corresponding template tags

Parameters:

+---------------+--------------------------------------+------------------+----------------+
| Name          | Description                          | Type             | Default        |
+===============+======================================+==================+================+
| node_file     | name of node file location           | str              | N/A            |
+---------------+--------------------------------------+------------------+----------------+
| tag_file      | name of tag file location            | str              | N/A            |
+---------------+--------------------------------------+------------------+----------------+

Returns:
    None

Raises:
    FileNotFoundError

    TypeError

    RuntimeError

Example::

    from matritools import utils as mu

    mu.get_node_indexes('Example_2_Template.csv', 'Example_2_Template_tag.csv')

    # output:
    # 0 : root
    # 1 : record id: 21
    # 2 : weight rod
    # 3 : height_rod
    # 4 : bank_rod
    # 5 : age_rod

