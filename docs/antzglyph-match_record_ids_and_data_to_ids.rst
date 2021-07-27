`AntzGlyph <antzglyph>`_
========================
match_record_ids_and_data_to_ids
--------------------------------
Iterates over each NodeFileRow in the glyph and matches its record ID and data to its ID

Returns: None

Example::

    from matritools import nodefile as nf

    my_glyph = nf.AntzGlyph("example.csv")

    # Iterate over each NodeFileRow in the glyph and matches its record ID and data to its ID
    my_glyph.match_record_ids_and_data_to_ids()

