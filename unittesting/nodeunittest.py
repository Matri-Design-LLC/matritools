import matritools.nodefile as nf
import pytest

test_property_string = '1,2,3,4,5,6,7,8,9,10,' \
                       '11,12,13,14,15,16,17,18,19,20,' \
                       '21,22,23,24,25,26,27,28,29,30,' \
                       '31,32,33,34,35,36,37,38,39,40,' \
                       '41,42,43,44,45,46,47,48,49,50,' \
                       '51,52,53,54,55,56,57,58,59,60,' \
                       '61,62,63,64,65,66,67,68,69,70,' \
                       '71,72,73,74,75,76,77,78,79,80,' \
                       '81,82,83,84,85,86,87,88,89,90,' \
                       '91,92,93,94' \

# region constructor

def test_empty_construction():
    try:
        nf.Node()
    except Exception as exc:
        assert False, exc


def test_construct_with_less_than_94_values():
    with pytest.raises(RuntimeError):
        nf.Node('0')


def test_construct_with_more_than_94_values():
    with pytest.raises(RuntimeError):
        nf.Node(test_property_string + ',95')


def test_proper_construction():
    try:
        nf.Node(test_property_string)
    except Exception as exc:
        assert False, exc


test_nfr = nf.Node(test_property_string)


def test_to_string():
    test_values = test_property_string.split(',')
    result_values = test_nfr.to_string().split(',')
    assert [float(value) for value in test_values] == [float(value) for value in result_values]


# endregion

# region setters

# region set id

def test_set_id_correct_input_int():
    test_nfr.set_id(100)
    assert test_nfr.id == test_nfr.data == test_nfr.record_id == 100


def test_set_id_correct_input_string():
    test_nfr.set_id("600")
    assert test_nfr.id == test_nfr.data == test_nfr.record_id == 600


def test_set_id_correct_input_float():
    test_nfr.set_id(300.0)
    assert test_nfr.id == test_nfr.data == test_nfr.record_id == 300


def test_set_id_bad_input():
    test_nfr.set_id(100)
    assert test_nfr.id == test_nfr.data == test_nfr.record_id == 100

def test_set_id_return_self():
    assert test_nfr.set_id(100) == test_nfr


# endregion

# region set tag

def test_set_tag_correct_input_int():
    test_nfr.set_tag("Test", 1)
    assert test_nfr.tag_text == "Test" and test_nfr.tag_mode == 1


def test_set_tag_correct_input_string():
    test_nfr.set_tag("Test", "3")
    assert test_nfr.tag_text == "Test" and test_nfr.tag_mode == 3


def test_set_tag_correct_input_float():
    test_nfr.set_tag("Test", 5.0)
    assert test_nfr.tag_text == "Test" and test_nfr.tag_mode == 5

def test_set_tag_return_self():
    assert test_nfr.set_tag("Test", 5.0) == test_nfr


# endregion

# region set aux a

def test_set_aux_a_correct_input_ints():
    test_nfr.set_aux_a(100, 200, 300)
    assert test_nfr.aux_a_x == 100 and test_nfr.aux_a_y == 200 and test_nfr.aux_a_z == 300


def test_set_aux_a_correct_input_strings():
    test_nfr.set_aux_a("400", "500", "600")
    assert test_nfr.aux_a_x == 400 and test_nfr.aux_a_y == 500 and test_nfr.aux_a_z == 600


def test_set_aux_a_correct_input_floats():
    test_nfr.set_aux_a(700.0, 800.0, 900.0)
    assert test_nfr.aux_a_x == 700 and test_nfr.aux_a_y == 800 and test_nfr.aux_a_z == 900


def test_set_aux_a_bad_input():
    with pytest.raises(Exception):
        test_nfr.set_aux_a("a", "b", "C")

def test_set_aux_a_return_self():
    assert test_nfr.set_aux_a(700.0, 800.0, 900.0) == test_nfr

# endregion

# region aux_b

def test_set_aux_b_correct_input_ints():
    test_nfr.set_aux_b(100, 200, 300)
    assert test_nfr.aux_b_x == 100 and test_nfr.aux_b_y == 200 and test_nfr.aux_b_z == 300


def test_set_aux_b_correct_input_strings():
    test_nfr.set_aux_b("400", "500", "600")
    assert test_nfr.aux_b_x == 400 and test_nfr.aux_b_y == 500 and test_nfr.aux_b_z == 600


def test_set_aux_b_correct_input_floats():
    test_nfr.set_aux_b(700.0, 800.0, 900.0)
    assert test_nfr.aux_b_x == 700 and test_nfr.aux_b_y == 800 and test_nfr.aux_b_z == 900


def test_set_aux_b_bad_input():
    with pytest.raises(Exception):
        test_nfr.set_aux_b("a", "b", "C")

def test_set_aux_b_return_self():
    assert test_nfr.set_aux_b(700.0, 800.0, 900.0) == test_nfr

# endregion

# region rotate_rate

def test_set_rotate_rate_correct_input_ints():
    test_nfr.set_rotate_rate(100, 200, 300)
    assert test_nfr.rotate_rate_x == 100 and test_nfr.rotate_rate_y == 200 and test_nfr.rotate_rate_z == 300


def test_set_rotate_rate_correct_input_strings():
    test_nfr.set_rotate_rate("400", "500", "600")
    assert test_nfr.rotate_rate_x == 400 and test_nfr.rotate_rate_y == 500 and test_nfr.rotate_rate_z == 600


def test_set_rotate_rate_correct_input_floats():
    test_nfr.set_rotate_rate(700.0, 800.0, 900.0)
    assert test_nfr.rotate_rate_x == 700 and test_nfr.rotate_rate_y == 800 and test_nfr.rotate_rate_z == 900


def test_set_rotate_rate_bad_input():
    with pytest.raises(Exception):
        test_nfr.set_rotate_rate("a", "b", "C")

def test_set_rotate_rate_return_self():
    assert test_nfr.set_rotate_rate(700.0, 800.0, 900.0) == test_nfr

# endregion

# region scale_rate

def test_set_scale_rate_correct_input_ints():
    test_nfr.set_scale_rate(100, 200, 300)
    assert test_nfr.scale_rate_x == 100 and test_nfr.scale_rate_y == 200 and test_nfr.scale_rate_z == 300


def test_set_scale_rate_correct_input_strings():
    test_nfr.set_scale_rate("400", "500", "600")
    assert test_nfr.scale_rate_x == 400 and test_nfr.scale_rate_y == 500 and test_nfr.scale_rate_z == 600


def test_set_scale_rate_correct_input_floats():
    test_nfr.set_scale_rate(700.0, 800.0, 900.0)
    assert test_nfr.scale_rate_x == 700 and test_nfr.scale_rate_y == 800 and test_nfr.scale_rate_z == 900


def test_set_scale_rate_bad_input():
    with pytest.raises(Exception):
        test_nfr.set_scale_rate("a", "b", "C")

def test_set_scale_rate_return_self():
    assert test_nfr.set_scale_rate(700.0, 800.0, 900.0) == test_nfr
# endregion

# region rotate_vec

def test_set_rotate_vec_correct_input_ints():
    test_nfr.set_rotate_vec(100, 200, 300, 110)
    assert test_nfr.rotate_vec_x == 100 and \
           test_nfr.rotate_vec_y == 200 and \
           test_nfr.rotate_vec_z == 300 and \
           test_nfr.rotate_vec_s == 110


def test_set_rotate_vec_correct_input_strings():
    test_nfr.set_rotate_vec("400", "500", "600", "120")
    assert test_nfr.rotate_vec_x == 400 and \
           test_nfr.rotate_vec_y == 500 and \
           test_nfr.rotate_vec_z == 600 and \
           test_nfr.rotate_vec_s == 120


def test_set_rotate_vec_correct_input_floats():
    test_nfr.set_rotate_vec(700.0, 800.0, 900.0, 130.0)
    assert test_nfr.rotate_vec_x == 700 \
           and test_nfr.rotate_vec_y == 800 \
           and test_nfr.rotate_vec_z == 900 \
           and test_nfr.rotate_vec_s == 130


def test_set_rotate_vec_bad_input():
    with pytest.raises(Exception):
        test_nfr.set_rotate_vec("a", "b", "C", "D")

def test_set_rotate_vec_return_self():
    assert test_nfr.set_rotate_vec(700.0, 800.0, 900.0, 130.0) == test_nfr
# endregion

# region scale

def test_set_scale_correct_input_integrals():
    test_nfr.set_scale(100.1, 200.2, 300.3)
    assert test_nfr.scale_x == 100.1 and test_nfr.scale_y == 200.2 and test_nfr.scale_z == 300.3


def test_set_scale_correct_input_strings():
    test_nfr.set_scale("400.4", "500.5", "600.6")
    assert test_nfr.scale_x == 400.4 and test_nfr.scale_y == 500.5 and test_nfr.scale_z == 600.6


def test_set_scale_bad_input():
    with pytest.raises(Exception):
        test_nfr.set_scale("a", "b", "C")

def test_set_scale_return_self():
    assert test_nfr.set_scale(100.1, 200.2, 300.3) == test_nfr

# endregion

# region u scale

def test_set_u_scale_correct_input_integrals():
    test_nfr.set_u_scale(100.1)
    assert test_nfr.scale_x == 100.1 and test_nfr.scale_y == 100.1 and test_nfr.scale_z == 100.1


def test_set_u_scale_correct_input_strings():
    test_nfr.set_u_scale("400.4")
    assert test_nfr.scale_x == 400.4 and test_nfr.scale_y == 400.4 and test_nfr.scale_z == 400.4


def test_set_u_scale_bad_input():
    with pytest.raises(Exception):
        test_nfr.set_u_scale("a")

def test_set_u_scale_return_self():
    assert test_nfr.set_u_scale(100.1) == test_nfr

# endregion

# region translate

def test_set_translate_correct_input_integrals():
    test_nfr.set_translate(100.1, 200.2, 300.3)
    assert test_nfr.translate_x == 100.1 and test_nfr.translate_y == 200.2 and test_nfr.translate_z == 300.3


def test_set_translate_correct_input_strings():
    test_nfr.set_translate("400.4", "500.5", "600.6")
    assert test_nfr.translate_x == 400.4 and test_nfr.translate_y == 500.5 and test_nfr.translate_z == 600.6


def test_set_translate_bad_input():
    with pytest.raises(Exception):
        test_nfr.set_translate("a", "b", "C")

def test_set_translate_return_self():
    assert test_nfr.set_translate(100.1, 200.2, 300.3) == test_nfr

# endregion

# region tag_offset

def test_set_tag_offset_correct_input_integrals():
    test_nfr.set_tag_offset(100.1, 200.2, 300.3)
    assert test_nfr.tag_offset_x == 100.1 and test_nfr.tag_offset_y == 200.2 and test_nfr.tag_offset_z == 300.3


def test_set_tag_offset_correct_input_strings():
    test_nfr.set_tag_offset("400.4", "500.5", "600.6")
    assert test_nfr.tag_offset_x == 400.4 and test_nfr.tag_offset_y == 500.5 and test_nfr.tag_offset_z == 600.6


def test_set_tag_offset_bad_input():
    with pytest.raises(Exception):
        test_nfr.set_tag_offset("a", "b", "C")

def test_set_tag_offset_return_self():
    assert test_nfr.set_tag_offset(100.1, 200.2, 300.3) == test_nfr

# endregion

# region rotate

def test_set_rotate_correct_input_integrals():
    test_nfr.set_rotate(100.1, 200.2, 300.3)
    assert test_nfr.rotate_x == 100.1 and test_nfr.rotate_y == 200.2 and test_nfr.rotate_z == 300.3


def test_set_rotate_correct_input_strings():
    test_nfr.set_rotate("400.4", "500.5", "600.6")
    assert test_nfr.rotate_x == 400.4 and test_nfr.rotate_y == 500.5 and test_nfr.rotate_z == 600.6


def test_set_rotate_bad_input():
    with pytest.raises(Exception):
        test_nfr.set_rotate("a", "b", "C")

def test_set_rotate_return_self():
    assert test_nfr.set_rotate(100.1, 200.2, 300.3) == test_nfr

# endregion

# region translate_rate

def test_set_translate_rate_correct_input_ints():
    test_nfr.set_translate_rate(100, 200, 300)
    assert test_nfr.translate_rate_x == 100 and test_nfr.translate_rate_y == 200 and test_nfr.translate_rate_z == 300


def test_set_translate_rate_correct_input_strings():
    test_nfr.set_translate_rate("400", "500", "600")
    assert test_nfr.translate_rate_x == 400 and test_nfr.translate_rate_y == 500 and test_nfr.translate_rate_z == 600


def test_set_translate_rate_correct_input_floats():
    test_nfr.set_translate_rate(700.0, 800.0, 900.0)
    assert test_nfr.translate_rate_x == 700 and test_nfr.translate_rate_y == 800 and test_nfr.translate_rate_z == 900


def test_set_translate_rate_bad_input():
    with pytest.raises(Exception):
        test_nfr.set_translate_rate("a", "b", "C")

def test_set_translate_rate_return_self():
    assert test_nfr.set_translate_rate(100, 200, 300) == test_nfr

# endregion

# region translate_vec

def test_set_translate_vec_correct_input_ints():
    test_nfr.set_translate_vec(100, 200, 300)
    assert test_nfr.translate_vec_x == 100 and test_nfr.translate_vec_y == 200 and test_nfr.translate_vec_z == 300


def test_set_translate_vec_correct_input_strings():
    test_nfr.set_translate_vec("400", "500", "600")
    assert test_nfr.translate_vec_x == 400 and test_nfr.translate_vec_y == 500 and test_nfr.translate_vec_z == 600


def test_set_translate_vec_correct_input_floats():
    test_nfr.set_translate_vec(700.0, 800.0, 900.0)
    assert test_nfr.translate_vec_x == 700 and test_nfr.translate_vec_y == 800 and test_nfr.translate_vec_z == 900


def test_set_translate_vec_bad_input():
    with pytest.raises(Exception):
        test_nfr.set_translate_vec("a", "b", "C")

def test_set_translate_vec_return_self():
    assert test_nfr.set_translate_vec(100, 200, 300) == test_nfr

# endregion

# region color

def test_set_color_correct_input_ints():
    test_nfr.set_color(100, 200, 300, 430)
    assert test_nfr.color_r == 100 and test_nfr.color_g == 200 and test_nfr.color_b == 300 and test_nfr.color_a == 430


def test_set_color_correct_input_strings():
    test_nfr.set_color("400", "500", "600", "770")
    assert test_nfr.color_r == 400 and test_nfr.color_g == 500 and test_nfr.color_b == 600 and test_nfr.color_a == 770


def test_set_color_correct_input_floats():
    test_nfr.set_color(700.0, 800.0, 900.0, 1050)
    assert test_nfr.color_r == 700 and test_nfr.color_g == 800 and test_nfr.color_b == 900 and test_nfr.color_a == 1050


def test_set_color_bad_input():
    with pytest.raises(Exception):
        test_nfr.set_color("a", "b", "C", "D")

def test_set_color_return_self():
    assert test_nfr.set_color(100, 200, 300, 430) == test_nfr

# endregion

# region color by name

def test_set_color_by_name_correct_input():
    test_nfr.set_color_by_name("red")
    assert test_nfr.color_r == 255 and test_nfr.color_g == 0 and test_nfr.color_b == 0 and test_nfr.color_a == 255

def test_set_color_by_name_bad_input_none():
    with pytest.raises(TypeError):
        test_nfr.set_color_by_name()

def test_set_color_by_name_bad_input_not_str():
    with pytest.raises(TypeError):
        test_nfr.set_color_by_name(5)

def test_set_color_by_name_bad_input_invalid_color():
    with pytest.raises(KeyError):
        test_nfr.set_color_by_name("Some super specific color")

def test_set_color_by_name_return_self():
    assert test_nfr.set_color_by_name("red") == test_nfr
# endregion

# region color by hex

def test_set_color_by_hex_correct_input_1():
    test_nfr.set_color_by_hex("#FF0000")
    assert test_nfr.color_r == 255 and test_nfr.color_g == 0 and test_nfr.color_b == 0 and test_nfr.color_a == 255

def test_set_color_by_hex_correct_input_2():
    test_nfr.set_color_by_hex("FF0000")
    assert test_nfr.color_r == 255 and test_nfr.color_g == 0 and test_nfr.color_b == 0 and test_nfr.color_a == 255

def test_set_color_by_hex_correct_input_3():
    test_nfr.set_color_by_hex("#7DD0D7")
    assert test_nfr.color_r == 125 and test_nfr.color_g == 208 and test_nfr.color_b == 215 and test_nfr.color_a == 255

def test_set_color_by_hex_bad_input_none():
    with pytest.raises(TypeError):
        test_nfr.set_color_by_hex()

def test_set_color_by_hex_bad_input_not_str():
    with pytest.raises(TypeError):
        test_nfr.set_color_by_hex(5)

def test_set_color_by_hex_bad_input_invalid_digits():
    with pytest.raises(ValueError):
        test_nfr.set_color_by_hex("#FG0000")

def test_set_color_by_hex_bad_input_too_many_digits():
    with pytest.raises(ValueError):
        test_nfr.set_color_by_hex("#FF00000")

def test_set_color_by_hex_return_self():
    assert test_nfr.set_color_by_hex("#FF0000") == test_nfr
# endregion

# region color by id
def test_set_color_by_id_palette_id_no_change():
    palette_id = test_nfr.palette_id
    test_nfr.set_color_by_id(1)
    assert palette_id == test_nfr.palette_id

def test_set_color_by_id_palette_id_change():
    test_nfr.palette_id = 1
    test_nfr.set_color_by_id(1, 2)
    assert test_nfr.palette_id == 2

def test_set_color_by_id_color_id():
    test_nfr.color_id = 1
    test_nfr.set_color_by_id(2)
    assert test_nfr.color_id == 2

def test_set_color_by_id_color_a():
    test_nfr.color_a = 1
    test_nfr.set_color_by_id(2, 2, 5)
    assert test_nfr.color_a == 5

def test_set_color_by_id_bad_input_color_id():
    with pytest.raises(TypeError):
        test_nfr.set_color_by_id('a')

def test_set_color_by_id_bad_input_palette_id():
    with pytest.raises(TypeError):
        test_nfr.set_color_by_id(1, 'a')

def test_set_color_by_id_palette_id_no_change_cast():
    palette_id = test_nfr.palette_id
    test_nfr.set_color_by_id('1')
    assert palette_id == test_nfr.palette_id

def test_set_color_by_id_palette_id_change_cast():
    test_nfr.palette_id = 1
    test_nfr.set_color_by_id(1, '2')
    assert test_nfr.palette_id == 2

def test_set_color_by_id_color_id_cast():
    test_nfr.color_id = 1
    test_nfr.set_color_by_id('2')
    assert test_nfr.color_id == 2

def test_set_color_by_id_color_a_cast():
    test_nfr.color_a = 1
    test_nfr.set_color_by_id(2, 2, '5')
    assert test_nfr.color_a == 5
# endregion

# region auto_zoom

def test_set_auto_zoom_correct_input_ints():
    test_nfr.set_auto_zoom(100, 200, 300)
    assert test_nfr.auto_zoom_x == 100 and test_nfr.auto_zoom_y == 200 and test_nfr.auto_zoom_z == 300


def test_set_auto_zoom_correct_input_strings():
    test_nfr.set_auto_zoom("400", "500", "600")
    assert test_nfr.auto_zoom_x == 400 and test_nfr.auto_zoom_y == 500 and test_nfr.auto_zoom_z == 600


def test_set_auto_zoom_correct_input_floats():
    test_nfr.set_auto_zoom(700.0, 800.0, 900.0)
    assert test_nfr.auto_zoom_x == 700 and test_nfr.auto_zoom_y == 800 and test_nfr.auto_zoom_z == 900


def test_set_auto_zoom_bad_input():
    with pytest.raises(Exception):
        test_nfr.set_auto_zoom("a", "b", "C")

def test_set_auto_zoom_return_self():
    assert test_nfr.set_auto_zoom(700.0, 800.0, 900.0) == test_nfr

# endregion

# region trigger_hi

def test_set_trigger_hi_correct_input_ints():
    test_nfr.set_trigger_hi(100, 200, 300)
    assert test_nfr.trigger_hi_x == 100 and test_nfr.trigger_hi_y == 200 and test_nfr.trigger_hi_z == 300


def test_set_trigger_hi_correct_input_strings():
    test_nfr.set_trigger_hi("400", "500", "600")
    assert test_nfr.trigger_hi_x == 400 and test_nfr.trigger_hi_y == 500 and test_nfr.trigger_hi_z == 600


def test_set_trigger_hi_correct_input_floats():
    test_nfr.set_trigger_hi(700.0, 800.0, 900.0)
    assert test_nfr.trigger_hi_x == 700 and test_nfr.trigger_hi_y == 800 and test_nfr.trigger_hi_z == 900


def test_set_trigger_hi_bad_input():
    with pytest.raises(Exception):
        test_nfr.set_trigger_hi("a", "b", "C")

def test_set_trigger_hi_return_self():
    assert test_nfr.set_trigger_hi(700.0, 800.0, 900.0) == test_nfr

# endregion

# region trigger_lo

def test_set_trigger_lo_correct_input_ints():
    test_nfr.set_trigger_lo(100, 200, 300)
    assert test_nfr.trigger_lo_x == 100 and test_nfr.trigger_lo_y == 200 and test_nfr.trigger_lo_z == 300


def test_set_trigger_lo_correct_input_strings():
    test_nfr.set_trigger_lo("400", "500", "600")
    assert test_nfr.trigger_lo_x == 400 and test_nfr.trigger_lo_y == 500 and test_nfr.trigger_lo_z == 600


def test_set_trigger_lo_correct_input_floats():
    test_nfr.set_trigger_lo(700.0, 800.0, 900.0)
    assert test_nfr.trigger_lo_x == 700 and test_nfr.trigger_lo_y == 800 and test_nfr.trigger_lo_z == 900


def test_set_trigger_lo_bad_input():
    with pytest.raises(Exception):
        test_nfr.set_trigger_lo("a", "b", "C")

def test_set_trigger_lo_return_self():
    assert test_nfr.set_trigger_lo(700.0, 800.0, 900.0) == test_nfr

# endregion

# region set_hi

def test_set_set_hi_correct_input_ints():
    test_nfr.set_set_hi(100, 200, 300)
    assert test_nfr.set_hi_x == 100 and test_nfr.set_hi_y == 200 and test_nfr.set_hi_z == 300


def test_set_set_hi_correct_input_strings():
    test_nfr.set_set_hi("400", "500", "600")
    assert test_nfr.set_hi_x == 400 and test_nfr.set_hi_y == 500 and test_nfr.set_hi_z == 600


def test_set_set_hi_correct_input_floats():
    test_nfr.set_set_hi(700.0, 800.0, 900.0)
    assert test_nfr.set_hi_x == 700 and test_nfr.set_hi_y == 800 and test_nfr.set_hi_z == 900


def test_set_set_hi_bad_input():
    with pytest.raises(Exception):
        test_nfr.set_set_hi("a", "b", "C")

def test_set_set_hi_return_self():
    assert test_nfr.set_set_hi(700.0, 800.0, 900.0) == test_nfr

# endregion

# region set_lo

def test_set_set_lo_correct_input_ints():
    test_nfr.set_set_lo(100, 200, 300)
    assert test_nfr.set_lo_x == 100 and test_nfr.set_lo_y == 200 and test_nfr.set_lo_z == 300


def test_set_set_lo_correct_input_strings():
    test_nfr.set_set_lo("400", "500", "600")
    assert test_nfr.set_lo_x == 400 and test_nfr.set_lo_y == 500 and test_nfr.set_lo_z == 600


def test_set_set_lo_correct_input_floats():
    test_nfr.set_set_lo(700.0, 800.0, 900.0)
    assert test_nfr.set_lo_x == 700 and test_nfr.set_lo_y == 800 and test_nfr.set_lo_z == 900


def test_set_set_lo_bad_input():
    with pytest.raises(Exception):
        test_nfr.set_set_lo("a", "b", "C")

def test_set_set_lo_return_self():
    assert test_nfr.set_set_lo(700.0, 800.0, 900.0) == test_nfr

# endregion

# region proximity_mode

def test_set_proximity_mode_correct_input_ints():
    test_nfr.set_proximity_mode(100, 200, 300)
    assert test_nfr.proximity_mode_x == 100 and test_nfr.proximity_mode_y == 200 and test_nfr.proximity_mode_z == 300


def test_set_proximity_mode_correct_input_strings():
    test_nfr.set_proximity_mode("400", "500", "600")
    assert test_nfr.proximity_mode_x == 400 and test_nfr.proximity_mode_y == 500 and test_nfr.proximity_mode_z == 600


def test_set_proximity_mode_correct_input_floats():
    test_nfr.set_proximity_mode(700.0, 800.0, 900.0)
    assert test_nfr.proximity_mode_x == 700 and test_nfr.proximity_mode_y == 800 and test_nfr.proximity_mode_z == 900


def test_set_proximity_mode_bad_input():
    with pytest.raises(Exception):
        test_nfr.set_proximity_mode("a", "b", "C")

def test_set_proximity_mode_self():
    assert test_nfr.set_proximity_mode(700.0, 800.0, 900.0) == test_nfr

# endregion

# region segments

def test_set_segments_correct_input_ints():
    test_nfr.set_segments(100, 200, 300)
    assert test_nfr.segments_x == 100 and test_nfr.segments_y == 200 and test_nfr.segments_z == 300


def test_set_segments_correct_input_strings():
    test_nfr.set_segments("400", "500", "600")
    assert test_nfr.segments_x == 400 and test_nfr.segments_y == 500 and test_nfr.segments_z == 600


def test_set_segments_correct_input_floats():
    test_nfr.set_segments(700.0, 800.0, 900.0)
    assert test_nfr.segments_x == 700 and test_nfr.segments_y == 800 and test_nfr.segments_z == 900


def test_set_segments_bad_input():
    with pytest.raises(Exception):
        test_nfr.set_segments("a", "b", "C")

def test_set_segments_self():
    assert test_nfr.set_segments(700.0, 800.0, 900.0) == test_nfr
# endregion

# endregion