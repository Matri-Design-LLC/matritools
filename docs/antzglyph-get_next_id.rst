`AntzGlyph <antzglyph.html>`_
===========================
get_next_id
-----------
Returns the last NodeFileRow of the file.

Parameters: None

Returns: int

Raises: None

Example::

    from matritools import nodefile as nf

    # create a node file
    glyph = nf.AntzGlyph("My Node File.csv")

    last_id = glyph.get_next_id()

    print(last_id)

    # output:
    # 6

