check_type
----------
Prints out the indexes of a glyph templates NodeFileRows with their corresponding template tags

Parameters:

+---------------+--------------------------------------+------------------+----------------+
| Name          | Description                          | Type             | Default        |
+===============+======================================+==================+================+
| obj           | name of node file location           | str              | N/A            |
+---------------+--------------------------------------+------------------+----------------+
| tag_file      | name of tag file location            | str              | N/A            |
+---------------+--------------------------------------+------------------+----------------+

Returns:
    None

Raises:
    TypeError

Example::

    from matritools import utils as mu

    my_int = 1

    # No error
    check(my_int, int)

    my_int = '1'

    try:
        check(my_int, int, False)
    except TypeError:
        print('error')

    # output error

    # since '1' is castable to int, no error
    check(my_int, int)

