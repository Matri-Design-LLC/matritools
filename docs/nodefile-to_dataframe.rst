`NodeFile <nodefile.html>`_
===========================
to_dataframe
------------
Returns a pandas.DataFrame of all of the NodeFileRow properties

Parameters: None

Returns: pandas.DataFrame

Example::

    from matritools import nodefile as nf

    # create a glyph
    my_glyph = nf.AntzGlyph("example.csv")

    # create a node file
    my_node_file = nf.NodeFile("My Node File")

    # add glyph to node file
    my_node_file.add_glyph(my_glyph)

    # create data frame out of node file
    node_df = my_node_file.to_df()

    print(node_df.head())

