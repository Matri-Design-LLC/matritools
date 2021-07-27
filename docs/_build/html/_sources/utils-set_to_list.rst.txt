`utils <utils.html>`_
=====================
set_to_list
-----------
Converts a set to a list

Parameters:

+-----------+-------------+------+---------+
| Name      | Description | Type | Default |
+===========+=============+======+=========+
| value_set | target set  | set  | None    |
+-----------+-------------+------+---------+

Returns: list

Example::

    from matritools import utils as mu

    values = [1, 1, 2, 2, 3, 3 ]

    set_list = mu.set_to_list(set(values))

    print(set_list)
    # output
    # [1,2,3]

    print(set_list[0])
    # output
    # 1

