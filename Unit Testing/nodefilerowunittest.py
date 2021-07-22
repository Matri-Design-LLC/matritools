import matritools.nodefile as nf

print("Testing NodeFileRow")

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

tests = []

#region constructor

try:
    test_nfr = nf.NodeFileRow()
    tests.append("Pass: Empty Constructor")
except:
    tests.append("Fail: Empty Constructor")

try:
    test_nfr = nf.NodeFileRow('0')
    tests.append("Fail: Construct with less than 94 values")
except RuntimeError:
    tests.append("Pass: Construct with less than 94 values")

try:
    test_nfr = nf.NodeFileRow(test_property_string + ',95')
    tests.append("Fail: Construct with more than 94 values")
except RuntimeError:
    tests.append("Pass: Construct with more than 94 values")

try:
    test_nfr = nf.NodeFileRow(test_property_string)
    tests.append("Pass: Construct with 94 values")
except:
    tests.append("Fail: Construct with 94 values")

test_nfr = nf.NodeFileRow(test_property_string)
test_values = test_property_string.split(',')
test_floats = [float(value) for value in test_values]

result_values = test_nfr.to_string().split(',')
result_floats = [float(value)for value in result_values]

result = True
for i in range(len(test_floats)):
    if test_floats[i] != result_floats[i]:
        tests.append("Fail: To string")
        result = False
        break

if result:
    tests.append("Pass: To string")

#endregion

#region make link

test_nfr.make_link(100, 200)
if test_nfr.parent_id == 100 and test_nfr.child_id == 200:
    tests.append("Pass: make link correct input (ints)")
else:
    tests.append("Fail: make link correct input (ints)")

test_nfr.make_link("300", "400")
if test_nfr.parent_id == 300 and test_nfr.child_id == 400:
    tests.append("Pass: make link correct input (int castable strings)")
else:
    tests.append("Fail: make link correct input (int castable strings)")

test_nfr.make_link(500.0, 600.0)
if test_nfr.parent_id == 500 and test_nfr.child_id == 600:
    tests.append("Pass: make link correct input (int castable floats)")
else:
    tests.append("Fail: make link correct input (int castable floats)")

try:
    test_nfr.make_link("a", "b")
    tests.append("Fail: make link with bad input (strings)")
except:
    tests.append("Pass: make link with bad input (strings)")

try:
    test_nfr.make_link(1.1, 2.1)
    tests.append("Fail: make link with bad input (floats)")
except:
    tests.append("Pass: make link with bad input (floats)")

try:
    test_nfr.make_link(1,1)
    tests.append("Fail: make link with equal parameters")
except:
    tests.append("Pass: make link with equal parameters")

try:
    test_nfr.id = 1000
    test_nfr.make_link(1000, 2000)
    tests.append("Fail: make link with parameters equal to id 1")
except:
    tests.append("Pass: make link with parameters equal to id 1")

try:
    test_nfr.id = 2000
    test_nfr.make_link(1000, 2000)
    tests.append("Fail: make link with parameters equal to id 2")
except:
    tests.append("Pass: make link with parameters equal to id 2")

#endregion

#region set id

test_nfr.set_id(100)
if test_nfr.id == test_nfr.data == test_nfr.record_id == 100:
    tests.append("Pass: set id correct input int")
else:
    tests.append("Fail: set id correct input int")

test_nfr.set_id("600")
if test_nfr.id == test_nfr.data == test_nfr.record_id == 600:
    tests.append("Pass: set id correct input castable string")
else:
    tests.append("Fail: set id correct input castable string")

test_nfr.set_id(300.0)
if test_nfr.id == test_nfr.data == test_nfr.record_id == 300:
    tests.append("Pass: set id correct input castable float")
else:
    tests.append("Fail: set id correct input castable float")

test_nfr.set_id(100)
if test_nfr.id == test_nfr.data == test_nfr.record_id == 100:
    tests.append("Pass: set id bad input")
else:
    tests.append("Fail: set id bad input")

#endregion

#region set tag

test_nfr.set_tag("Test", 1)
if test_nfr.tag_text == "Test" and test_nfr.tag_mode == 1:
    tests.append("Pass: set tag")
else:
    tests.append("Fail: set tag")

test_nfr.set_tag("Test", "3")
if test_nfr.tag_text == "Test" and test_nfr.tag_mode == 3:
    tests.append("Pass: set tag")
else:
    tests.append("Fail: set tag")

test_nfr.set_tag("Test", 5.0)
if test_nfr.tag_text == "Test" and test_nfr.tag_mode == 5:
    tests.append("Pass: set tag")
else:
    tests.append("Fail: set tag")

#endregion

#region set aux a
test_nfr.set_aux_a(100, 200, 300)
if test_nfr.aux_a_x == 100 and test_nfr.aux_a_y == 200 and test_nfr.aux_a_z == 300:
    tests.append("Pass: set aux acorrect input ints")
else:
    tests.append("Fail: set aux acorrect input ints")

test_nfr.set_aux_a("400", "500", "600")
if test_nfr.aux_a_x == 400 and test_nfr.aux_a_y == 500 and test_nfr.aux_a_z == 600:
    tests.append("Pass: set aux acorrect input castable strings")
else:
    tests.append("Fail: set aux acorrect input castable strings")

test_nfr.set_aux_a(700.0, 800.0, 900.0)
if test_nfr.aux_a_x == 700 and test_nfr.aux_a_y == 800 and test_nfr.aux_a_z == 900:
    tests.append("Pass: set aux a orrect input castable floats")
else:
    tests.append("Fail: set aux a correct input castable floats")

#endregion

#region set aux b

test_nfr.set_aux_b(100, 200, 300)
if test_nfr.aux_b_x == 100 and test_nfr.aux_b_y == 200 and test_nfr.aux_b_z == 300:
    tests.append("Pass: set aux b correct input ints")
else:
    tests.append("Fail: set aux b correct input ints")

test_nfr.set_aux_b("400", "500", "600")
if test_nfr.aux_b_x == 400 and test_nfr.aux_b_y == 500 and test_nfr.aux_b_z == 600:
    tests.append("Pass: set aux b correct input castable strings")
else:
    tests.append("Fail: set aux b correct input castable strings")

test_nfr.set_aux_b(700.0, 800.0, 900.0)
if test_nfr.aux_b_x == 700 and test_nfr.aux_b_y == 800 and test_nfr.aux_b_z == 900:
    tests.append("Pass: set aux b correct input castable floats")
else:
    tests.append("Fail: set aux b correct input castable floats")

#endregion

# region set rotate vec

test_nfr.set_rotate_vec(100, 200, 300, 110)
if test_nfr.rotate_vec_x == 100 and \
        test_nfr.rotate_vec_y == 200 and \
        test_nfr.rotate_vec_z == 300 and \
        test_nfr.rotate_vec_s == 110:
    tests.append("Pass: set_rotate_vec correct input ints")
else:
    tests.append("Fail: set_rotate_vec correct input ints")

test_nfr.set_rotate_vec("400", "500", "600", "120")
if test_nfr.rotate_vec_x == 400 and \
        test_nfr.rotate_vec_y == 500 and \
        test_nfr.rotate_vec_z == 600 and \
        test_nfr.rotate_vec_s == 120:
    tests.append("Pass: set_rotate_vec correct input castable strings")
else:
    tests.append("Fail:et set_rotate_vec correct input castable strings")

test_nfr.set_rotate_vec(700.0, 800.0, 900.0, 130.0)
if test_nfr.rotate_vec_x == 700 and test_nfr.rotate_vec_y == 800 and test_nfr.rotate_vec_z == 900:
    tests.append("Pass: set_rotate_vec correct input castable floats")
else:
    tests.append("Fail: set_rotate_vec correct input castable floats")

# endregion vec

#region set scale

test_nfr.set_scale(100.1, 200.2, 300.3)
if test_nfr.scale_x == 100.1 and test_nfr.scale_y == 200.2 and test_nfr.scale_z == 300.3:
    tests.append("Pass: set scale correct input integrals")
else:
    tests.append("Fail: set scale correct input integrals")

test_nfr.set_scale("400.4", "500.5", "600.6")
if test_nfr.scale_x == 400.4 and test_nfr.scale_y == 500.5 and test_nfr.scale_z == 600.6:
    tests.append("Pass: set scale correct input castable strings")
else:
    tests.append("Fail: set scale correct input castable strings")

#endregion
# region set translate

test_nfr.set_translate(100.1, 200.2, 300.3)
if test_nfr.translate_x == 100.1 and test_nfr.translate_y == 200.2 and test_nfr.translate_z == 300.3:
    tests.append("Pass: set translate correct input integrals")
else:
    tests.append("Fail: set translate correct input integrals")

test_nfr.set_translate("400.4", "500.5", "600.6")
if test_nfr.translate_x == 400.4 and test_nfr.translate_y == 500.5 and test_nfr.translate_z == 600.6:
    tests.append("Pass: set translate correct input castable strings")
else:
    tests.append("Fail: set translate correct input castable strings")

# endregion

# region set tag offset

test_nfr.set_tag_offset(100, 200, 300)
if test_nfr.tag_offset_x == 100 and test_nfr.tag_offset_y == 200 and test_nfr.tag_offset_z == 300:
    tests.append("Pass: set tag offset correct input ints")
else:
    tests.append("Fail: set tag offset correct input ints")

test_nfr.set_tag_offset("400", "500", "600")
if test_nfr.tag_offset_x == 400 and test_nfr.tag_offset_y == 500 and test_nfr.tag_offset_z == 600:
    tests.append("Pass: set tag offset correct input castable strings")
else:
    tests.append("Fail: set tag offset correct input castable strings")

# endregion

# region set rotate

test_nfr.set_rotate(100.1, 200.2, 300.3)
if test_nfr.rotate_x == 100.1 and test_nfr.rotate_y == 200.2 and test_nfr.rotate_z == 300.3:
    tests.append("Pass: set rotate correct input integrals")
else:
    tests.append("Fail: set rotate correct input integrals")

test_nfr.set_rotate("400.4", "500.5", "600.6")
if test_nfr.rotate_x == 400.4 and test_nfr.rotate_y == 500.5 and test_nfr.rotate_z == 600.6:
    tests.append("Pass: set rotate correct input castable strings")
else:
    tests.append("Fail: set rotate correct input castable strings")

# endregion

# region set rotate rate

test_nfr.set_rotate_rate(100, 200, 300)
if test_nfr.rotate_rate_x == 100 and test_nfr.rotate_rate_y == 200 and test_nfr.rotate_rate_z == 300:
    tests.append("Pass: set rotate_rate correct input ints")
else:
    tests.append("Fail: set rotate_rate correct input ints")

test_nfr.set_rotate_rate("400", "500", "600")
if test_nfr.rotate_rate_x == 400 and test_nfr.rotate_rate_y == 500 and test_nfr.rotate_rate_z == 600:
    tests.append("Pass: set rotate_rate correct input castable strings")
else:
    tests.append("Fail: set rotate_rate correct input castable strings")

test_nfr.set_rotate_rate(700.0, 800.0, 900.0)
if test_nfr.rotate_rate_x == 700 and test_nfr.rotate_rate_y == 800 and test_nfr.rotate_rate_z == 900:
    tests.append("Pass: set rotate_rate correct input castable floats")
else:
    tests.append("Fail: set rotate_rate correct input castable floats")

# endregion

# region set scale rate

test_nfr.set_scale_rate(100, 200, 300)
if test_nfr.scale_rate_x == 100 and test_nfr.scale_rate_y == 200 and test_nfr.scale_rate_z == 300:
    tests.append("Pass: set scale rate correct input ints")
else:
    tests.append("Fail: set scale rate correct input ints")

test_nfr.set_scale_rate("400", "500", "600")
if test_nfr.scale_rate_x == 400 and test_nfr.scale_rate_y == 500 and test_nfr.scale_rate_z == 600:
    tests.append("Pass: set scale rate correct input castable strings")
else:
    tests.append("Fail: set scale rate correct input castable strings")

test_nfr.set_scale_rate(700.0, 800.0, 900.0)
if test_nfr.scale_rate_x == 700 and test_nfr.scale_rate_y == 800 and test_nfr.scale_rate_z == 900:
    tests.append("Pass: set scale rate correct input castable floats")
else:
    tests.append("Fail: set scale rate correct input castable floats")

# endregion

# region set translate rate

test_nfr.set_translate_rate(100, 200, 300)
if test_nfr.translate_rate_x == 100 and test_nfr.translate_rate_y == 200 and test_nfr.translate_rate_z == 300:
    tests.append("Pass: set translate rate correct input ints")
else:
    tests.append("Fail: set translate rate correct input ints")

test_nfr.set_translate_rate("400", "500", "600")
if test_nfr.translate_rate_x == 400 and test_nfr.translate_rate_y == 500 and test_nfr.translate_rate_z == 600:
    tests.append("Pass: set translate rate correct input castable strings")
else:
    tests.append("Fail: set translate rate correct input castable strings")

test_nfr.set_translate_rate(700.0, 800.0, 900.0)
if test_nfr.translate_rate_x == 700 and test_nfr.translate_rate_y == 800 and test_nfr.translate_rate_z == 900:
    tests.append("Pass: set translate rate correct input castable floats")
else:
    tests.append("Fail: set translate rate correct input castable floats")

# endregion

# region set translate vec

test_nfr.set_translate_vec(100, 200, 300)
if test_nfr.translate_vec_x == 100 and test_nfr.translate_vec_y == 200 and test_nfr.translate_vec_z == 300:
    tests.append("Pass: set translate vec correct input ints")
else:
    tests.append("Fail: set translate vec correct input ints")

test_nfr.set_translate_vec("400", "500", "600")
if test_nfr.translate_vec_x == 400 and test_nfr.translate_vec_y == 500 and test_nfr.translate_vec_z == 600:
    tests.append("Pass: set translate vec correct input castable strings")
else:
    tests.append("Fail: set translate vec correct input castable strings")

test_nfr.set_translate_vec(700.0, 800.0, 900.0)
if test_nfr.translate_vec_x == 700 and test_nfr.translate_vec_y == 800 and test_nfr.translate_vec_z == 900:
    tests.append("Pass: set translate vec correct input castable floats")
else:
    tests.append("Fail: set translate vec correct input castable floats")

# endregion

# region set auto zoom

test_nfr.set_auto_zoom(100, 200, 300)
if test_nfr.auto_zoom_x == 100 and test_nfr.auto_zoom_y == 200 and test_nfr.auto_zoom_z == 300:
    tests.append("Pass: set auto zoom correct input ints")
else:
    tests.append("Fail: set auto zoom correct input ints")

test_nfr.set_auto_zoom("400", "500", "600")
if test_nfr.auto_zoom_x == 400 and test_nfr.auto_zoom_y == 500 and test_nfr.auto_zoom_z == 600:
    tests.append("Pass: set auto zoom correct input castable strings")
else:
    tests.append("Fail: set auto zoom correct input castable strings")

test_nfr.set_auto_zoom(700.0, 800.0, 900.0)
if test_nfr.auto_zoom_x == 700 and test_nfr.auto_zoom_y == 800 and test_nfr.auto_zoom_z == 900:
    tests.append("Pass: set auto zoom correct input castable floats")
else:
    tests.append("Fail: set auto zoom correct input castable floats")

# endregion

# region set trigger hi

test_nfr.set_auto_zoom(100, 200, 300)
if test_nfr.auto_zoom_x == 100 and test_nfr.auto_zoom_y == 200 and test_nfr.auto_zoom_z == 300:
    tests.append("Pass: set auto zoom correct input ints")
else:
    tests.append("Fail: set auto zoom correct input ints")

test_nfr.set_auto_zoom("400", "500", "600")
if test_nfr.auto_zoom_x == 400 and test_nfr.auto_zoom_y == 500 and test_nfr.auto_zoom_z == 600:
    tests.append("Pass: set auto zoom correct input castable strings")
else:
    tests.append("Fail: set auto zoom correct input castable strings")

test_nfr.set_auto_zoom(700.0, 800.0, 900.0)
if test_nfr.auto_zoom_x == 700 and test_nfr.auto_zoom_y == 800 and test_nfr.auto_zoom_z == 900:
    tests.append("Pass: set auto zoom correct input castable floats")
else:
    tests.append("Fail: set auto zoom correct input castable floats")

# endregion

# region set trigger_hi

test_nfr.set_trigger_hi(100, 200, 300)
if test_nfr.trigger_hi_x == 100 and test_nfr.trigger_hi_y == 200 and test_nfr.trigger_hi_z == 300:
	tests.append("Pass: set trigger_hi correct input ints")
else:
	tests.append("Fail: set trigger_hi correct input ints")

test_nfr.set_trigger_hi("400", "500", "600")
if test_nfr.trigger_hi_x == 400 and test_nfr.trigger_hi_y == 500 and test_nfr.trigger_hi_z == 600:
	tests.append("Pass: set trigger_hi correct input castable strings")
else:
	tests.append("Fail: set trigger_hi correct input castable strings")

test_nfr.set_trigger_hi(700.0, 800.0, 900.0)
if test_nfr.trigger_hi_x == 700 and test_nfr.trigger_hi_y == 800 and test_nfr.trigger_hi_z == 900:
	tests.append("Pass: set trigger_hi correct input castable floats")
else:
	tests.append("Fail: set trigger_hi correct input castable floats")

# endregion

# region set trigger_lo

test_nfr.set_trigger_lo(100, 200, 300)
if test_nfr.trigger_lo_x == 100 and test_nfr.trigger_lo_y == 200 and test_nfr.trigger_lo_z == 300:
	tests.append("Pass: set trigger_lo correct input ints")
else:
	tests.append("Fail: set trigger_lo correct input ints")

test_nfr.set_trigger_lo("400", "500", "600")
if test_nfr.trigger_lo_x == 400 and test_nfr.trigger_lo_y == 500 and test_nfr.trigger_lo_z == 600:
	tests.append("Pass: set trigger_lo correct input castable strings")
else:
	tests.append("Fail: set trigger_lo correct input castable strings")

test_nfr.set_trigger_lo(700.0, 800.0, 900.0)
if test_nfr.trigger_lo_x == 700 and test_nfr.trigger_lo_y == 800 and test_nfr.trigger_lo_z == 900:
	tests.append("Pass: set trigger_lo correct input castable floats")
else:
	tests.append("Fail: set trigger_lo correct input castable floats")

# endregion

# region set hi

test_nfr.set_hi(100, 200, 300)
if test_nfr.set_hi_x == 100 and test_nfr.set_hi_y == 200 and test_nfr.set_hi_z == 300:
	tests.append("Pass: set hi correct input ints")
else:
	tests.append("Fail: set hi correct input ints")

test_nfr.set_hi("400", "500", "600")
if test_nfr.set_hi_x == 400 and test_nfr.set_hi_y == 500 and test_nfr.set_hi_z == 600:
	tests.append("Pass: set hi correct input castable strings")
else:
	tests.append("Fail: set hi correct input castable strings")

test_nfr.set_hi(700.0, 800.0, 900.0)
if test_nfr.set_hi_x == 700 and test_nfr.set_hi_y == 800 and test_nfr.set_hi_z == 900:
	tests.append("Pass: set hi correct input castable floats")
else:
	tests.append("Fail: set hi correct input castable floats")

# endregion

# region set lo

test_nfr.set_lo(100, 200, 300)
if test_nfr.set_lo_x == 100 and test_nfr.set_lo_y == 200 and test_nfr.set_lo_z == 300:
	tests.append("Pass: set lo correct input ints")
else:
	tests.append("Fail: set lo correct input ints")

test_nfr.set_lo("400", "500", "600")
if test_nfr.set_lo_x == 400 and test_nfr.set_lo_y == 500 and test_nfr.set_lo_z == 600:
	tests.append("Pass: set lo correct input castable strings")
else:
	tests.append("Fail: set lo correct input castable strings")

test_nfr.set_lo(700.0, 800.0, 900.0)
if test_nfr.set_lo_x == 700 and test_nfr.set_lo_y == 800 and test_nfr.set_lo_z == 900:
	tests.append("Pass: set lo correct input castable floats")
else:
	tests.append("Fail: set lo correct input castable floats")

# endregion

# region set proximity

test_nfr.set_proximity(100.1, 200.2, 300.3)
if test_nfr.proximity_x == 100.1 and test_nfr.proximity_y == 200.2 and test_nfr.proximity_z == 300.3:
	tests.append("Pass: set proximity correct input integrals")
else:
	tests.append("Fail: set proximity correct input integrals")

test_nfr.set_proximity("400", "500", "600")
if test_nfr.proximity_x == 400 and test_nfr.proximity_y == 500 and test_nfr.proximity_z == 600:
	tests.append("Pass: set proximity correct input castable strings")
else:
	tests.append("Fail: set proximity correct input castable strings")

# endregion

# region set proximity_mode

test_nfr.set_proximity_mode(100, 200, 300)
if test_nfr.proximity_mode_x == 100 and test_nfr.proximity_mode_y == 200 and test_nfr.proximity_mode_z == 300:
	tests.append("Pass: set proximity_mode correct input ints")
else:
	tests.append("Fail: set proximity_mode correct input ints")

test_nfr.set_proximity_mode("400", "500", "600")
if test_nfr.proximity_mode_x == 400 and test_nfr.proximity_mode_y == 500 and test_nfr.proximity_mode_z == 600:
	tests.append("Pass: set proximity_mode correct input castable strings")
else:
	tests.append("Fail: set proximity_mode correct input castable strings")

test_nfr.set_proximity_mode(700.0, 800.0, 900.0)
if test_nfr.proximity_mode_x == 700 and test_nfr.proximity_mode_y == 800 and test_nfr.proximity_mode_z == 900:
	tests.append("Pass: set proximity_mode correct input castable floats")
else:
	tests.append("Fail: set proximity_mode correct input castable floats")

# endregion

# region set segments

test_nfr.set_segments(100, 200, 300)
if test_nfr.segments_x == 100 and test_nfr.segments_y == 200 and test_nfr.segments_z == 300:
	tests.append("Pass: set segments correct input ints")
else:
	tests.append("Fail: set segments correct input ints")

test_nfr.set_segments("400", "500", "600")
if test_nfr.segments_x == 400 and test_nfr.segments_y == 500 and test_nfr.segments_z == 600:
	tests.append("Pass: set segments correct input castable strings")
else:
	tests.append("Fail: set segments correct input castable strings")

test_nfr.set_segments(700.0, 800.0, 900.0)
if test_nfr.segments_x == 700 and test_nfr.segments_y == 800 and test_nfr.segments_z == 900:
	tests.append("Pass: set segments correct input castable floats")
else:
	tests.append("Fail: set segments correct input castable floats")

# endregion



print("\n******************Results***************")
for test in tests:
    print(test)

