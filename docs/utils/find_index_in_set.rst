find_index_in_set
-----------------
Converts returns the index of a value in a set as if it were a list
Returns -1 if value was not in the set

Parameters:

+-----------+--------------+------+---------+
| Name      | Description  | Type | Default |
+===========+==============+======+=========+
| value_set | target set   | set  | None    |
+-----------+--------------+------+---------+
| value     | target value | any  | None    |
+-----------+--------------+------+---------+

Returns:
    int

Example::

    from matritools import utils as mu

    values = [1, 1, 2, 2, 3, 3 ]

    index = find_index-in_set(set(values), 1)

    if index != -1:
        print("Index of 1 is " + str(index)
        # output
        # Index of 1 is 0
    else :
        print("1 is not in the set")

