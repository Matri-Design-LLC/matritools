add_glyph
---------
Appends all Nodes of a glyph to Nodes and manages the glyph's IDs.
Returns passed glyph (Glyph).

Parameters:

+------------+-------------------------------------------------+-------------------------------+---------+
| Name       | Description                                     | Type                          | Default |
+============+=================================================+===============================+=========+
| glyph      | Glyph that has its Nodes copied and incremented | Glyph                         | N/A     |
+------------+-------------------------------------------------+-------------------------------+---------+
| parent_id  | id of node this glyph will be attached too      | int                           | 0       |
+------------+-------------------------------------------------+-------------------------------+---------+
| copy_glyph | Should the glyph nodes be stored as copies?     |                               |         |
|            | Mark false if you if want to add the glyph only |                               |         |
|            | once and maintain node references.              | bool                          | True    |
+------------+-------------------------------------------------+-------------------------------+---------+

Returns:
    Glyph

Raises:
    TypeError

    RuntimeError

Example::

    from matritools import nodefile as nf

    # function to print selected properties of the Nodes in a NodeContainer
    def print_node_container(node_container):
        for node in node_container.nodes:
            print('ID: ' + str(node.id) + ', P_ID: ' + str(node.parent_id) + ', ' + node.tag_text)

    # declare node file
    ntf = nf.NodeFile('test')

    # declare base glyph template
    glyph = nf.Glyph()
    root = glyph.create_node(None, 'root')
    leaf = glyph.create_node(root, 'leaf')

    # declare a modication to append to the base glyph
    glyph_mod = nf.Glyph()
    mod_root = glyph_mod.create_node(None, 'mod_root')
    mod_leaf = glyph_mod.create_node(mod_root, 'mod_leaf')

    # marking copy_glyph as False because we are adding glyph_mod only once and mod_root and mod_leaf
    # will still be valid references to nodes in the base glyph.
    glyph.add_glyph(glyph_mod, root.id, False)

    ntf.add_glyph(glyph)
    ntf.add_glyph(glyph)
    ntf.add_glyph(glyph)

    print_node_container(ntf)

    # Output:
    # ID: 1, P_ID: 0,
    # ID: 2, P_ID: 0,
    # ID: 3, P_ID: 2,
    # ID: 4, P_ID: 2,
    # ID: 5, P_ID: 2,
    # ID: 6, P_ID: 0,
    # ID: 7, P_ID: 0, root
    # ID: 8, P_ID: 7, leaf
    # ID: 9, P_ID: 7, mod_root
    # ID: 10, P_ID: 9, mod_leaf
    # ID: 11, P_ID: 0, root
    # ID: 12, P_ID: 11, leaf
    # ID: 13, P_ID: 11, mod_root
    # ID: 14, P_ID: 13, mod_leaf
    # ID: 15, P_ID: 0, root
    # ID: 16, P_ID: 15, leaf
    # ID: 17, P_ID: 15, mod_root
    # ID: 18, P_ID: 17, mod_leaf


