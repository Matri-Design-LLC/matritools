`NodeFile <nodefile.html>`_
===========================
add_glyph
---------
Appends all rows of a glyph to node_file_rows and increments glyph template id,
parent_id, data, and record_id

Parameters:

+------------+---------------------------------------------+-------------------------------+---------+
| Name       | Description                                 | Type                          | Default |
+============+=============================================+===============================+=========+
| glyph      | glyph template to be added to node file     | AntzGlyph                     | None    |
+------------+---------------------------------------------+-------------------------------+---------+

Returns: None

Raises: TypeError

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

