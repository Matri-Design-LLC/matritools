`NodeFile <nodefile.html>`_
===========================
write_to_csv
------------
Writes all the parameters of each NodeFileRow into a node csv file as well as
creates a corresponding tag file.

Parameters: None

Returns: None

Raises: RuntimeError

Example::

    from matritools import nodefile as nf

    # create a glyph
    my_glyph = nf.AntzGlyph("example.csv")

    # create a node file
    my_node_file = nf.NodeFile("My Node File")

    # add glyph to node file
    my_node_file.add_glyph(my_glyph)

    # write node file to csv
    my_node_file.write_to_csv()

