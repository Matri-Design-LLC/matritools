`AntzGlyph <antzglyph.html>`_
=============================
get_row_by_id
-------------
Returns a NodeFileRow at the requested ID.

Parameters:

+------------+---------------------------------------------+------------------+---------+
| Name       | Description                                 | Type             | Default |
+============+=============================================+==================+=========+
| row_id     | target ID                                   | int              | None    |
+------------+---------------------------------------------+------------------+---------+

Returns: matritools.nodefile.NodeFileRow

Example::

    from matritools import nodefile as nf

    # create node file with 6 default node file rows
    my_glyph = nf.AntzGlyph"example.csv")

    # edit first camera view position
    camera_view = my_glyph.get_row_by_id(2)
    camera_view.set_translate(0, 0, 0)

