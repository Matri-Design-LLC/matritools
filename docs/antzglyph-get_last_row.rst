`AntzGlyph <antzglyph.html>`_
=============================
get_last_row
------------
Returns the last NodeFileRow of the file.

Parameters: None

Returns: NodeFileRow

Raises: None

Example::

    from matritools import nodefile as nf

    # create a glyph
    glyph = nf.NodeFile("template.csv")

    last_id = glyph.get_last_row().id

    print(last_id)

    # output:
    # 6

