`utils <utils.html>`_
=====================
dict_to_multilined_str
----------------------
Converts a dict into a formatted string with a line for each key value pair

Parameters:

+--------------+--------------------------------------------------------------------------+------+---------+
| Name         | Description                                                              | Type | Default |
+==============+==========================================================================+======+=========+
| dictionary   | dict to be converted to string                                           | dict | None    |
+--------------+--------------------------------------------------------------------------+------+---------+
| indent_level | used for recursion for formatting the string in the case of nested dicts | int  | 0       |
+--------------+--------------------------------------------------------------------------+------+---------+

Returns: str

Example::

    from matritools import utils as mu

    letter_nums = {
        "A": 1,
        "B": 2,
        "C": 3
    }

    print(mu.dict_to_multilined_str(letter_nums))

    # output
    # A : 1
    # B : 2
    # C : 3

