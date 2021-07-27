`AntzGlyph <antzglyph.html>`_
=============================
increment_ids
-------------
Iterates over each NodeFileRow in the glyph and updates its ID, parent ID, and child ID reflect as a new glyph in a node
file starting with the highest ID + 1. This is called automatically when adding glyph to NodeFile

i.e. a glyph with such as

| id | parent_id | child_id
| 1--| 0-----------| 0
| 2--| 1-----------| 0
| 3--| 1-----------| 2

will become

| id | parent_id | child_id
| 4--| 0-----------| 0
| 5--| 4-----------| 0
| 6--| 4-----------| 5


Parameters:

    +--------------------------------+---------------------------------------+------+---------+
    | Name                           | Description                           | Type | Default |
    +================================+=======================================+======+=========+
    | match_data_and_record_id_to_id | Should the rows update their          | bool | True    |
    |                                | record ID and data to match their ID? |      |         |
    +--------------------------------+---------------------------------------+------+---------+

Returns: None

Example::

    from matritools import nodefile as nf

    my_glyph = nf.AntzGlyph("example.csv")

    # Iterate over each NodeFileRow in the glyph and matches its record id and data to its id
    my_glyph.increment_ids()

