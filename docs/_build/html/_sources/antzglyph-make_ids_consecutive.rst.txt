`AntzGlyph <antzglyph.html>`_
=============================
make_ids_consecutive
--------------------
Changes the IDs, parent IDs and child IDs to appear sequentially with no gaps between ID number.



Parameters:

    +--------------------------------+---------------------------------------+------+---------+
    | Name                           | Description                           | Type | Default |
    +================================+=======================================+======+=========+
    | starting_id                    | First ID in the sequence.             | int  | 8       |
    +--------------------------------+---------------------------------------+------+---------+
    | match_data_and_record_id_to_id | Should the rows update their          | bool | True    |
    |                                | record ID and data to match their ID? |      |         |
    +--------------------------------+---------------------------------------+------+---------+

Returns: None

Example::

    from matritools import nodefile as nf


    glyph = nf.AntzGlyph("example.csv",  make_ids_consecutive=False)

    # unchanged_glyph
    # | ID | parent ID | child ID
    # | 20 | 0         | 0
    # | 21 | 20        | 0
    # | 56 | 20        | 0
    # | 70 | 21        | 56

    # make IDs consecutive and start from 10
    glyph.make_ids_consecutive(10)

    # Example Glyph template Node file
    # | ID | parent ID | child ID
    # | 10 | 0         | 0
    # | 11 | 10        | 0
    # | 12 | 10        | 0
    # | 13 | 11        | 12

    # make IDs consecutive and start from 20
    glyph.make_ids_consecutive(20)

    # Example Glyph template Node file
    # | ID | parent ID | child ID
    # | 20 | 0         | 0
    # | 21 | 20        | 0
    # | 22 | 20        | 0
    # | 23 | 21        | 22

    # make IDs consecutive staring from default value (8)
    glyph.make_ids_consecutive()

    # Example Glyph template Node file
    # | ID | parent ID | child ID
    # | 8  | 0         | 0
    # | 9  | 8         | 0
    # | 10 | 8         | 0
    # | 11 | 9         | 10

