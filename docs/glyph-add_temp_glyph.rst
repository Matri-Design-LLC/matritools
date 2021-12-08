`Glyph <glyph.html>`_
=====================
add_temp_glyph
--------------
Temporarily appends all Nodes of a glyph to nodes and manages it's ID's.
Temporary glyphs get removed on NodeFile.add_glyph.

Parameters:

+------------+-------------------------------------------------+-------------------------------+---------+
| Name       | Description                                     | Type                          | Default |
+============+=================================================+===============================+=========+
| glyph      | Glyph that has its Nodes copied and incremented | Glyph                         | N/A     |
+------------+-------------------------------------------------+-------------------------------+---------+
| parent_id  | id of node this glyph will be attached too      | int                           | N/A     |
+------------+-------------------------------------------------+-------------------------------+---------+

Returns:
    self

Raises:
    TypeError

Example::

    from matritools import nodefile as nf

    # build glyph
    glyph = nf.glyph()
    root = glyph.create_node(None, 'root')
    branch = glyph.create_node(root, 'branch')

    # build temp glyph
    temp_glyph = nf.glyph()
    temp_root = temp_glyph.create_node(None, 'Temp root')
    temp_leaf = temp_glyph.create_node(None, 'Temp leaf')

    glyph.add_temp_glyph(temp_glyph)


    # print glyph
    for node in glyph.nodes:
        print(node.tag_text)

    # output:
    # root
    # branch
    # temp root
    # temp leaf

    # declare node file
    ntf = nf.NodeFile('My Node File')

    # add glyph to node file
    ntf.add_glyph(glyph, branch.id)

    # print node file
    for node in glyph.nodes:
        print(node.tag_text)

    # output:
    #
    #
    #
    #
    #
    #
    # root
    # branch
    # temp root
    # temp leaf

    # print glyph
    for node in glyph.nodes:
        print(node.tag_text)

    # output:
    # root
    # branch

