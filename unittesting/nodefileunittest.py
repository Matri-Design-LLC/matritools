import matritools as mt
import os
import pytest

# region constructor
def test_empty_constructor():
    with pytest.raises(TypeError):
        mt.NodeFile()

def test_constructor_row_count():
    ntf = mt.NodeFile("Test")
    assert len(ntf.nodes) == 6

def test_constructor_initial_row_ids():
    ntf = mt.NodeFile("Test")

    results = []

    for row in ntf.nodes:
        results.append(row.id)

    assert results == [1,2,3,4,5,mt.main_grid_id]
# endregion

# region add glyph
def test_add_glyph():
    glyph = mt.Glyph()
    glyph.create_node(glyph.create_node())
    glyph.create_temp_node(glyph.get_last_node())

    glyph2 = mt.Glyph()
    glyph2.create_node(glyph2.create_node())

    glyph.add_temp_glyph(glyph2, glyph.nodes[0].id)

    ntf = mt.NodeFile('test')
    ntf.add_glyph(glyph)
    assert glyph.length() == 2

def test_add_glyph_ids():
    glyph = mt.Glyph()
    glyph.create_node(glyph.create_node())

    ntf = mt.NodeFile('test')
    ntf.add_glyph(glyph)
    assert ntf.get_last_node().id == mt.main_grid_id + 2

def test_add_glyph_parent_ids():
    glyph = mt.Glyph()
    glyph.create_node(glyph.create_node())

    ntf = mt.NodeFile('test')
    ntf.add_glyph(glyph)
    assert ntf.get_last_node().parent_id == mt.main_grid_id + 1

def test_add_glyph_increment_ids():
    glyph = mt.Glyph()
    glyph.create_node(glyph.create_node())

    ntf = mt.NodeFile('test')
    ntf.add_glyph(glyph)
    ntf.add_glyph(glyph)
    assert glyph.get_last_node().id == mt.main_grid_id + 4

def test_add_glyph_increment_parent_ids():
    glyph = mt.Glyph()
    glyph.create_node(glyph.create_node())

    ntf = mt.NodeFile('test')
    ntf.add_glyph(glyph)
    ntf.add_glyph(glyph)
    assert glyph.get_last_node().parent_id == mt.main_grid_id + 3

def test_add_glyph_branch():
    glyph = mt.Glyph()
    glyph.create_node(glyph.create_node())

    glyph2 = mt.Glyph()
    glyph2.create_node(glyph2.create_node())

    ntf = mt.NodeFile('test')
    ntf.add_glyph(glyph)
    ntf.add_glyph(glyph2, ntf.get_last_node().id)

    assert glyph2.get_last_node().branch_level == 4

def test_add_glyph_bad_parent_id():
    with pytest.raises(RuntimeError):
        glyph = mt.Glyph()
        glyph.create_node(glyph.create_node())

        glyph2 = mt.Glyph()
        glyph2.create_node(glyph.create_node())

        ntf = mt.NodeFile('test')
        ntf.add_glyph(glyph)
        ntf.add_glyph(glyph2, 50)

def test_add_glyph_copy():
    glyph = mt.Glyph()
    glyph.create_node(glyph.create_node())

    ntf = mt.NodeFile('test')
    ntf.add_glyph(glyph)
    assert glyph.get_last_node() != ntf.get_last_node()

def test_add_glyph_not_copy():
    glyph = mt.Glyph()
    glyph.create_node(glyph.create_node())

    ntf = mt.NodeFile('test')
    ntf.add_glyph(glyph, copy_glyph=False)
    assert glyph.get_last_node() == ntf.get_last_node()

def test_add_glyph_bad_input_glyph():
    with pytest.raises(TypeError):
        ntf = mt.NodeFile('test')
        ntf.add_glyph(10)

def test_add_glyph_bad_input_parent_idh():
    with pytest.raises(TypeError):
        glyph = mt.Glyph()
        ntf = mt.NodeFile('test')
        ntf.add_glyph(glyph, 'a')

def test_add_glyph_bad_input_copy_glyph():
    with pytest.raises(TypeError):
        glyph = mt.Glyph()
        ntf = mt.NodeFile('test')
        ntf.add_glyph(glyph, '0', 'a')
# endregion

# region create_node
def test_create_node_no_parent_node():
    ntf = mt.NodeFile('test')
    node = ntf.create_node()
    assert node.parent_id == ntf.main_grid.id

def test_create_node_with_parent_node():
    ntf = mt.NodeFile('test')
    parent_node = ntf.create_node()
    node = ntf.create_node(parent_node)
    assert node.parent_id == parent_node.id
# endregion

# region write_to_csv

def test_write_to_csv_file_was_written():
	file_name = 'unittest'
	ntf = mt.NodeFile(file_name)
	ntf.write_to_csv()
	
	assert os.path.exists(f'{file_name}_node.csv')
	os.remove(f'{file_name}_node.csv')
	assert os.path.exists(f'{file_name}_tag.csv')
	os.remove(f'{file_name}_tag.csv')
	
def test_write_to_csv_duplicate_IDs():
	file_name = 'unittest'
	ntf = mt.NodeFile(file_name)
	node1 = ntf.create_node()
	node2 = ntf.create_node()
	node2.id = node1.id
	
	with pytest.raises(RuntimeError):
		ntf.write_to_csv()
		
	assert os.path.exists('debug_node.csv')
	os.remove('debug_node.csv')
	
	if os.path.exists(f'{file_name}_node.csv'):
		os.remove(f'{file_name}_node.csv')
	if os.path.exists(f'{file_name}_tag.csv'):
		os.remove(f'{file_name}_tag.csv')
	
# endregion