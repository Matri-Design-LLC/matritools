Constructor
-----------

Parameters:

+---------------+------------------------------------------+------+---------+
| Name          | Description                              | Type | Default |
+===============+==========================================+======+=========+
| comma_string  | a string with 94 comma seperated         | str  | ""      |
|               | values in the order of an antz node file |      |         |
+---------------+------------------------------------------+------+---------+

Raises:
    TypeError

    RuntimeError

Note:
    When specifying values, properties are assigned in the following order:

    id, type, data, selected, parent_id, branch_level, child_id, child_index, palette_id, ch_input_id,

    ch_output_id, ch_last_updated, average, samples, aux_a_x, aux_a_y, aux_a_z, aux_b_x, aux_b_y, aux_b_z,

    color_shift, rotate_vec_x, rotate_vec_y, rotate_vec_z, rotate_vec_s, scale_x, scale_y, scale_z,
    translate_x, translate_y,

    translate_z, tag_offset_x, tag_offset_y, tag_offset_z, rotate_rate_x, rotate_rate_y, rotate_rate_z,
    rotate_x, rotate_y, rotate_z,

    scale_rate_x, scale_rate_y, scale_rate_z, translate_rate_x, translate_rate_y, translate_rate_z,
    translate_vec_x, translate_vec_y, translate_vec_z, shader,

    geometry, line_width, point_size, ratio, color_id, color_r, color_g, color_b, color_a, color_fade,

    texture_id, hide, freeze, topo, facet, auto_zoom_x, auto_zoom_y, auto_zoom_z, trigger_hi_x, trigger_hi_y,

    trigger_hi_z, trigger_lo_x, trigger_lo_y, trigger_lo_z, set_hi_x, set_hi_y, set_hi_z, set_lo_x, set_lo_y,
    set_lo_z,

    proximity_x, proximity_y, proximity_z, proximity_mode_x, proximity_mode_y, proximity_mode_z, segments_x,
    segments_y, segments_z, tag_mode,

    format_id, table_id, record_id, size

Example::

    from matritools import nodefile as nf

    # create node file row with default values
    my_node1 = nf.NodeFileRow()

    # create node file row with specified values
    my_node2 = NodeFileRow( "6,6,6,1,0,"
                           "0,0,1,0,0,"
                           "0,0,0,1,360,"
                           "220,0,0,0,0,"
                           "0,0,0,0,0,"
                           "1,1,1,0,0,"
                           "0,0,0,1,0,"
                           "0,0,0,0,0,"
                           "0,0,0,0,0,"
                           "0,0,0,0,0,"
                           "0,1,0,0.1,3,"
                           "0,0,255,150,0,"
                           "0,0,0,0,0,"
                           "0,0,0,0,0,"
                           "0,0,0,0,0,"
                           "0,0,0,0,0,"
                           "0,0,0,0,0,"
                           "0,1,1,0,0,"
                           "0,0,0,420"))

