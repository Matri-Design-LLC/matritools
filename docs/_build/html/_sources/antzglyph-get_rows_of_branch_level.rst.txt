`AntzGlyph <antzglyph.html>`_
=============================
get_rows_of_branch_level
------------------------
Returns a list of NodeFileRows with a given branch level

Parameters:

+--------------+---------------------------------------+------+---------+
| Name         | Description                           | Type | Default |
+==============+=======================================+======+=========+
| branch_level | Level of NodeFileRow to be returned   | int  | None    |
+--------------+---------------------------------------+------+---------+

Returns: List[NodeFileRow]

Example::

    from matritools import nodefile as nf

    my_glyph = nf.AntzGlyph("example.csv")

    # Change color of level 3 objects to red
    rows = my_glyph.get_rows_of_branch_level(3)

    for row in rows:
        row.set_color(255, 0 , 0)

