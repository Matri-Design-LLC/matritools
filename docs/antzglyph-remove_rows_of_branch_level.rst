`AntzGlyph <antzglyph.html>`_
=============================
remove_rows_of_branch_level
---------------------------
Removes all NodeFileRow's of a given branch level

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

