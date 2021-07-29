def template_int(name):

    return '#region ' + name + '\n\n' + \
    'def test_set_' + name + '_correct_input_ints():\n' + \
        '\ttest_nfr.set_' + name + '(100, 200, 300)\n' + \
        '\tassert test_nfr.' + name + '_x == 100 and test_nfr.' + name + '_y == 200 and test_nfr.' + name + '_z == 300\n\n' + \
    'def test_set_' + name + '_correct_input_strings():\n' + \
        '\ttest_nfr.set_' + name + '("400", "500", "600")\n' + \
        '\tassert test_nfr.' + name + '_x == 400 and test_nfr.' + name + '_y == 500 and test_nfr.' + name + '_z == 600\n\n' + \
    'def test_set_' + name + '_correct_input_floats():\n' + \
        '\ttest_nfr.set_' + name + '(700.0, 800.0, 900.0)\n' + \
        '\tassert test_nfr.' + name + '_x == 700 and test_nfr.' + name + '_y == 800 and test_nfr.' + name + '_z == 900\n\n' + \
    'def test_set_' + name + '_bad_input():\n' + \
       '\twith pytest.raises(Exception):\n' + \
           '\t\ttest_nfr.set_' + name + '("a", "b", "C")\n\n' + \
     '#endregion\n'

def template_float(name):

    return '#region ' + name + '\n\n' + \
    'def test_set_' + name + '_correct_input_integrals():\n' + \
        '\ttest_nfr.set_' + name + '(100.1, 200.2, 300.3)\n' + \
        '\tassert test_nfr.' + name + '_x == 100.1 and test_nfr.' + name + '_y == 200.2 and test_nfr.' + name + '_z == 300.3\n\n' + \
    'def test_set_' + name + '_correct_input_strings():\n' + \
        '\ttest_nfr.set_' + name + '("400.4", "500.5", "600.6")\n' + \
        '\tassert test_nfr.' + name + '_x == 400.4 and test_nfr.' + name + '_y == 500.5 and test_nfr.' + name + '_z == 600.6\n\n' + \
    'def test_set_' + name + '_bad_input():\n' + \
        '\twith pytest.raises(Exception):\n' + \
            '\t\ttest_nfr.set_' + name + '("a", "b", "C")\n\n' + \
    '#endregion\n'

def template_doc_int(name):
    return '`NodeFileRow <nodefilerow.html>`_\n' + \
            '=================================\n' + \
            '' + name + '\n' + \
            '---------\n' + \
            'Sets the x, y, and z axis of ' + name + '.\n\n' + \
            'Parameters:\n\n' + \
            '+------+----------------------------+------------------+---------+\n' + \
            '| Name | Description | Type | Default |\n' + \
            '+======+============================+==================+=========+\n' + \
            '| x    | ' + name + '_x | int | 0 |\n' + \
            '+------+----------------------------+------------------+---------+\n' + \
            '| y    | ' + name + '_y | int | 0 |\n' + \
            '+------+----------------------------+------------------+---------+\n' + \
            '| z    | ' + name + '_z | int | 0 |\n' + \
            '+------+----------------------------+------------------+---------+\n\n' + \
            'Returns: None\n\n' + \
            'Example::\n\n' + \
            '\tfrom matritools import nodefile as nf\n\n' + \
            '\t# create node file with 6 default node file rows\n\n' + \
            '\tmy_node_file = nf.NodeFile("My Node File")\n\n' + \
            '\tmy_node_file.properties[0].set_' + name + '(1, 2, 3)\n\n' + \
            '\t# same as\n\n' + \
            '\tmy_node_file.properties[0].' + name + '_x = 1\n' + \
            '\tmy_node_file.properties[0].' + name + '_x = 2\n' + \
            '\tmy_node_file.properties[0].' + name + '_x = 3\n\n\n'


def template_doc_float(name):
    return '`NodeFileRow <nodefilerow.html>`_\n' + \
            '=================================\n' + \
            '' + name + '\n' + \
            '---------\n' + \
            'Sets the x, y, and z axis of ' + name + '.\n\n' + \
           'Parameters:\n\n' + \
           '+------+----------------------------+------------------+---------+\n' + \
           '| Name | Description | Type | Default |\n' + \
           '+======+============================+==================+=========+\n' + \
           '| x    | ' + name + '_x | float | 0 |\n' + \
           '+------+----------------------------+------------------+---------+\n' + \
           '| y    | ' + name + '_y | float | 0 |\n' + \
           '+------+----------------------------+------------------+---------+\n' + \
           '| z    | ' + name + '_z | float | 0 |\n' + \
           '+------+----------------------------+------------------+---------+\n\n' + \
           'Returns: None\n\n' + \
           'Example::\n\n' + \
           '\tfrom matritools import nodefile as nf\n\n' + \
           '\t# create node file with 6 default node file rows\n\n' + \
           '\tmy_node_file = nf.NodeFile("My Node File")\n\n' + \
           '\tmy_node_file.properties[0].set_' + name + '(1, 2, 3)\n\n' + \
           '\t# same as\n\n' + \
           '\tmy_node_file.properties[0].' + name + '_x = 1\n' + \
           '\tmy_node_file.properties[0].' + name + '_x = 2\n' + \
           '\tmy_node_file.properties[0].' + name + '_x = 3\n\n\n'

print(template_doc_int("aux_b"))
print(template_doc_int("rotate_rate"))
print(template_doc_int("scale_rate"))
print(template_doc_int("rotate_vec"))
print(template_doc_float("scale"))
print(template_doc_float("translate"))
print(template_doc_float("tag_offset"))
print(template_doc_float("rotate"))
print(template_doc_int("translate_rate"))
print(template_doc_int("translate_vec"))
print(template_doc_int("color"))
print(template_doc_int("auto_zoom"))
print(template_doc_int("trigger_hi"))
print(template_doc_int("trigger_lo"))
print(template_doc_int("set_hi"))
print(template_doc_int("set_lo"))
print(template_doc_int("proximity_mode"))
print(template_doc_int("segments"))

#print(template_int("aux_b"))
#print(template_int("rotate_rate"))
#print(template_int("scale_rate"))
#print(template_int("rotate_vec"))
#print(template_float("scale"))
#print(template_float("translate"))
#print(template_float("tag_offset"))
#print(template_float("rotate"))
#print(template_int("translate_rate"))
#print(template_int("translate_vec"))
#print(template_int("color"))
#print(template_int("auto_zoom"))
#print(template_int("trigger_hi"))
#print(template_int("trigger_lo"))
#print(template_int("set_hi"))
#print(template_int("set_lo"))
#print(template_int("proximity_mode"))
#print(template_int("segments"))