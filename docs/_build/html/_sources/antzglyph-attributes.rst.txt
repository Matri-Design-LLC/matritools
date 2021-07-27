`AntzGlyph <antzglyph.html>`_
=============================
Attributes
----------

+----------------------+----------------------------------------------+-----------+---------+
| Name                 | Description                                  | Type      | Default |
+======================+==============================================+===========+=========+
| node_file_rows       | list of NodeFileRows that make up the glyph  | List[str] | ""      |
+----------------------+----------------------------------------------+-----------+---------+

Returns: List[NodeFileRow]

Example::

    from matritools import nodefile as nf
    import copy

    glyph = nf.AntzGlyph("example.csv")

    # change position of root object
    glyph.node_file_rows[0].set_translate(10, 0, 0)

    # new NodeFileRow to glyph template
    new_row = nf.NodeFileRow()
    glyph.node_file_rows.append(new_row)

    # remove object from glyph
    glyph.node_file_rows.remove(glyph.node_file_rows[1])

    # duplicate object and change position
    duplicated_row = copy.deepcopy(glyph.node_file_rows[5])
    duplicated_row.set_translate(40, 10, 0)
    glyph.node_file_rows.append(duplicated_row)

