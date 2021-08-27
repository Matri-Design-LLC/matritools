`AntzGlyph <antzglyph.html>`_
=============================
remove_rows_of_branch_level
---------------------------
Removes gaps in ids. i.e IDs 1,2,4 become 1,2,3.
Can also be used to change the ID's of the glyph to start from a specified index

Parameters:

+--------------+------------------------------------+------+---------+
| Name         | Description                        | Type | Default |
+==============+====================================+======+=========+
| branch_level | branch level of all removed items  | int  | None    |
+--------------+------------------------------------+------+---------+

Returns: None

Example::

    from matritools import nodefile as nf

    my_glyph = nf.AntzGlyph("example.csv")

    # Remove all rows with the branch level of 3
    my_glyph.unselect_all(3)

