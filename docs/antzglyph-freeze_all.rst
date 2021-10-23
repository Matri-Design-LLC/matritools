`AntzGlyph <antzglyph.html>`_
=============================
freeze_all
----------
Sets all rows in glyph to be frozen or unfrozen

Parameters:

+--------------+---------------------------------------+------+---------+
| Name         | Description                           | Type | Default |
+==============+=======================================+======+=========+
| freeze       | Should all rows in glyph be frozen    | bool | True    |
+--------------+---------------------------------------+------+---------+

Returns: None

Raises: None

Example::

    from matritools import nodefile as nf

    # create a glyph
    glyph = nf.NodeFile("template.csv")

    glyph.freeze_all()

    print(glyph.node_file_rows[0].freeze)

    # output:
    # 1

    glyph.freeze_all(False)

    print(glyph.node_file_rows[0].freeze)

    # output:
    # 0

