`AntzGlyph <antzglyph.html>`_
=============================
length
------
Returns the number of NodeFileRows in this file.

Parameters: None

Returns: int

Raises: None

Example::

    from matritools import nodefile as nf

    # template.csv
    # contains 3 rows

    # create a node file
    glyph = nf.AntzGlyph("template.csv")

    length = my_node_file.length()

    print(length)

    # output:
    # 3