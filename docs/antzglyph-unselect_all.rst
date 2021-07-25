`AntzGlyph <https://matritools.readthedocs.io/en/main/antzglyph.html>`_
=========
unselect_all
------------
Changes the selected property of all glyph node file rows to 0. When glyph template files are saved via "save selected",
each row is marked selected, use this to reverse this effect

Parameters: None

Returns: None

Example::

    from matritools import nodefile as nf

    my_glyph = nf.AntzGlyph("example.csv")

    # this glyph will be unselected by default when rendered in OpenANTz
    my_glyph.unselect_all()

