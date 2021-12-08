`NodeContainer <nodecontainer.html>`_
=====================================
match_record_ids_and_data_to_ids
--------------------------------
Iterates over each Node in the NodeContainer and matches its record id and data to its id.
Upon construction of a Glyph, this happens by default.
The uses of this function are primarily for internal purposes.

Parameters:
    None

Returns:
    None

Raises:
    self

Example::

    from matritools import nodefile as nf

    # Create Node Container
    my_glyph = nf.NodeContainer()

    # Iterate over each NodeFileRow in the glyph and matches its record ID and data to its ID
    my_glyph.match_record_ids_and_data_to_ids()

