import matritools.nodefile as nf
import pytest

def test_empty_constructor():
    with pytest.raises(RuntimeError):
        nf.NodeFile()

def test_constructor_row_count():
    ntf = nf.NodeFile("Test")
    assert len(ntf.node_file_rows) == 6

def test_constructor_initial_row_ids():
    ntf = nf.NodeFile("Test")

    results = []

    for row in ntf.node_file_rows:
        results.append(row.id)

    assert results == [1,2,3,4,5,6]

def test_get_row_by_index():
    ntf = nf.NodeFile("Test")
    assert ntf.get_row_by_index(0).id == 1

def test_get_row_by_id():
    ntf = nf.NodeFile("Test")
    assert ntf.get_row_by_id(1).id == 1

def test_duplicate_ids_and_add_glyph():
    ntf = nf.NodeFile("Test")
    ntf.add_glyph_to_node_file_rows(nf.AntzGlyph('Test5.csv', False, False))
    with pytest.raises(RuntimeError):
        ntf.check_for_duplicate_id()

def test_to_string():
    test_property_string = '1,2,3,4,5,6,7,8,9,10,' \
                           '11,12,13,14,15,16,17,18,19,20,' \
                           '21,22,23,24,25,26,27,28,29,30,' \
                           '31,32,33,34,35,36,37,38,39,40,' \
                           '41,42,43,44,45,46,47,48,49,50,' \
                           '51,52,53,54,55,56,57,58,59,60,' \
                           '61,62,63,64,65,66,67,68,69,70,' \
                           '71,72,73,74,75,76,77,78,79,80,' \
                           '81,82,83,84,85,86,87,88,89,90,' \
                           '91,92,93,94'

    ntf = nf.NodeFile("Test")

    # region set properties

    ntf.properties.id = 1
    ntf.properties._type = 2
    ntf.properties.data = 3
    ntf.properties.selected = 4
    ntf.properties.parent_id = 5
    ntf.properties.branch_level = 6
    ntf.properties.child_id = 7
    ntf.properties.child_index = 8
    ntf.properties.palette_id = 9
    ntf.properties.ch_input_id = 10
    ntf.properties.ch_output_id = 11
    ntf.properties.ch_last_updated = 12
    ntf.properties.average = 13
    ntf.properties.samples = 14
    ntf.properties.aux_a_x = 15
    ntf.properties.aux_a_y = 16
    ntf.properties.aux_a_z = 17
    ntf.properties.aux_b_x = 18
    ntf.properties.aux_b_y = 19
    ntf.properties.aux_b_z = 20
    ntf.properties.color_shift = 21
    ntf.properties.rotate_vec_x = 22
    ntf.properties.rotate_vec_y = 23
    ntf.properties.rotate_vec_z = 24
    ntf.properties.rotate_vec_s = 25
    ntf.properties.scale_x = 26
    ntf.properties.scale_y = 27
    ntf.properties.scale_z = 28
    ntf.properties.translate_x = 29
    ntf.properties.translate_y = 30
    ntf.properties.translate_z = 31
    ntf.properties.tag_offset_x = 32
    ntf.properties.tag_offset_y = 33
    ntf.properties.tag_offset_z = 34
    ntf.properties.rotate_rate_x = 35
    ntf.properties.rotate_rate_y = 36
    ntf.properties.rotate_rate_z = 37
    ntf.properties.rotate_x = 38
    ntf.properties.rotate_y = 39
    ntf.properties.rotate_z = 40
    ntf.properties.scale_rate_x = 41
    ntf.properties.scale_rate_y = 42
    ntf.properties.scale_rate_z = 43
    ntf.properties.translate_rate_x = 44
    ntf.properties.translate_rate_y = 45
    ntf.properties.translate_rate_z = 46
    ntf.properties.translate_vec_x = 47
    ntf.properties.translate_vec_y = 48
    ntf.properties.translate_vec_z = 49
    ntf.properties.shader = 50
    ntf.properties.geometry = 51
    ntf.properties.line_width = 52
    ntf.properties.point_size = 53
    ntf.properties.ratio = 54
    ntf.properties.color_index = 55
    ntf.properties.color_r = 56
    ntf.properties.color_g = 57
    ntf.properties.color_b = 58
    ntf.properties.color_a = 59
    ntf.properties.color_fade = 60
    ntf.properties.texture_id = 61
    ntf.properties.hide = 62
    ntf.properties.freeze = 63
    ntf.properties.topo = 64
    ntf.properties.facet = 65
    ntf.properties.auto_zoom_x = 66
    ntf.properties.auto_zoom_y = 67
    ntf.properties.auto_zoom_z = 68
    ntf.properties.trigger_hi_x = 69
    ntf.properties.trigger_hi_y = 70
    ntf.properties.trigger_hi_z = 71
    ntf.properties.trigger_lo_x = 72
    ntf.properties.trigger_lo_y = 73
    ntf.properties.trigger_lo_z = 74
    ntf.properties.set_hi_x = 75
    ntf.properties.set_hi_y = 76
    ntf.properties.set_hi_z = 77
    ntf.properties.set_lo_x = 78
    ntf.properties.set_lo_y = 79
    ntf.properties.set_lo_z = 80
    ntf.properties.proximity_x = 81
    ntf.properties.proximity_y = 82
    ntf.properties.proximity_z = 83
    ntf.properties.proximity_mode_x = 84
    ntf.properties.proximity_mode_y = 85
    ntf.properties.proximity_mode_z = 86
    ntf.properties.segments_x = 87
    ntf.properties.segments_y = 88
    ntf.properties.segments_z = 89
    ntf.properties.tag_mode = 90
    ntf.properties.format_id = 91
    ntf.properties.table_id = 92
    ntf.properties.record_id = 93
    ntf.properties.size = 94

    # endregion

    ntf.create_node_row()
    test_values = test_property_string.split(',')
    result_values = ntf.get_row_by_index(6).to_string().split(',')
    ntf.get_row_by_index(6).print_properties()
    assert [float(value) for value in test_values] == [float(value) for value in result_values]