`Glyph <glyph.html>`_
=====================
create_temp_node
----------------
Creates and returns a node inside of the NodeFile.
Temporary glyphs get removed on NodeFile.add_glyph.

Parameters:

+-------------+----------------------------------------------------------------------------+------+---------+
| Name        | Description                                                                | Type | Default |
+=============+============================================================================+======+=========+
| parent_node | Node that newly created Node will be associated with                       | Node | None    |
+-------------+----------------------------------------------------------------------------+------+---------+
| tag_text    | text that will be written in the tag file associated with the created Node | str  | ""      |
+-------------+----------------------------------------------------------------------------+------+---------+
| tag_mode    | int representing how the tag should be displayed by default                | int  | 0       |
+-------------+----------------------------------------------------------------------------+------+---------+
| template    | Created node will be a copy of template if one is passed.                  | Node | None    |
+-------------+----------------------------------------------------------------------------+------+---------+

Returns:
    Node

Raises:
    TypeError

For a practical example, refer to `Example 3 <example3.html>`

Example::

    from matritools import nodefile as nf

    # build glyph
    glyph = nf.glyph()
    root = glyph.create_node(None, 'root')
    branch = glyph.create_node(root, 'branch')

    # add temp nodes
    for i in range(3):
        glyph.create_temp_node(branch, 'temp leaf')

    # print glyph
    for node in glyph.nodes:
        print(node.tag_text)

    # output:
    # root
    # branch
    # temp leaf
    # temp leaf
    # temp leaf

    # declare node file
    ntf = nf.NodeFile('My Node File')

    # add glyph to node file
    ntf.add_glyph(glyph)

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
    # temp leaf
    # temp leaf
    # temp leaf

    # print glyph
    for node in glyph.nodes:
        print(node.tag_text)

    # output:
    # root
    # branch

