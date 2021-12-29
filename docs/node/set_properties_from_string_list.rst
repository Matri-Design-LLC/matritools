set_properties_from_string_list
-------------------------------
Set properties of the NodeFile from a list of strings.

Parameters:

+------------+-----------------------------------------------+------------------+---------+
| Name       | Description                                   | Type             | Default |
+============+===============================================+==================+=========+
| values     | list of strings that can be cast as integrals | List[str]        | None    |
+------------+-----------------------------------------------+------------------+---------+

Returns:
    self

Raises:
    RuntimeError

Example::

    from matritools import nodefile as nf

    # create node
	node = nf.Node()

    comma_string = "6,6,6,1,0," + \
                   "0,0,1,0,0," + \
                   "0,0,0,1,360," + \
                   "220,0,0,0,0," + \
                   "0,0,0,0,0," + \
                   "1,1,1,0,0," + \
                   "0,0,0,1,0," + \
                   "0,0,0,0,0," + \
                   "0,0,0,0,0," + \
                   "0,0,0,0,0," + \
                   "0,1,0,0.1,3," + \
                   "0,0,255,150,0," + \
                   "0,0,0,0,0," + \
                   "0,0,0,0,0," + \
                   "0,0,0,0,0," + \
                   "0,0,0,0,0," + \
                   "0,0,0,0,0," + \
                   "0,1,1,0,0," + \
                   "0,0,0,420"

    values = comma_string.split(",")
        if len(values) != 94:

    node.set_properties_from_string_list(values)

