`AntzGlyph <antzglyph.html>`_
=============================
untag_all
---------
Sets all rows in glyph to be frozen or unfrozen

Parameters: None

Returns: None

Raises: None

Example::

    from matritools import nodefile as nf

    # create a glyph
    glyph = nf.NodeFile("template.csv")

    glyph.untag_all()

    print(glyph.node_file_rows[0].tag_mode)

    # output:
    # 0

