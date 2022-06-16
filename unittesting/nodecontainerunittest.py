import matritools as mt
import pytest

# region constructor
def test_empty_constructor():
	try:
		mt.NodeContainer()
	except Exception as exec:
		assert False, 'Constructor raised exception.\n' + exec
# endregion

# region length
def test_length():
	node_container = mt.NodeContainer()
	node_container2 = mt.NodeContainer()
	node_container2.create_node()
	assert node_container.length() == 0 and node_container2.length() == 1
# endregion

# region get_last_node
def test_get_last_node_when_empty():
	node_container = mt.NodeContainer()
	assert node_container.get_last_node() == None, node_container.get_last_node()

def test_get_last_node():
	node_container = mt.NodeContainer()
	node_container.create_node()
	assert node_container.get_last_node().id == mt.main_grid_id + 1
# endregion

# region get_next_id
def test_get_next_id():
	node_container = mt.NodeContainer()
	node_container2 = mt.NodeContainer()
	node = node_container2.create_node()
	assert node_container.get_next_id() == mt.main_grid_id + 1 and node_container2.get_next_id() == mt.main_grid_id + 2
# endregion

# region get_node_by_id
def test_get_node_by_id_when_empty():
	node_container = mt.NodeContainer()
	assert node_container.get_node_by_id(1) == None

def test_get_node_by_id():
	node_container = mt.NodeContainer()
	node = node_container.create_node()
	assert node_container.get_node_by_id(node.id).id == node.id

def test_get_node_by_id_bad_input():
	with pytest.raises(TypeError):
		node_container = mt.NodeContainer()
		node_container.get_node_by_id('a')

def test_get_node_by_id_casted_input():
	try:
		node_container = mt.NodeContainer()
		node_container.get_node_by_id('1')
	except Exception as exc:
		assert False, exc
# endregion

# region get_nodes_by_parent_id
def test_get_nodes_by_parent_id_when_empty():
	node_container = mt.NodeContainer()
	assert len(node_container.get_nodes_by_parent_id(1)) == 0

def test_get_node_by_parent_id():
	node_container = mt.NodeContainer()
	node = node_container.create_node()
	node_container.create_node(node)
	assert len(node_container.get_nodes_by_parent_id(node.id)) == 1

def test_get_node_by_parent_id_bad_input():
	with pytest.raises(TypeError):
		node_container = mt.NodeContainer()
		node = node_container.create_node()
		node_container.create_node(node)
		node_container.get_nodes_by_parent_id('a')

def test_get_node_by_parent_id_casted_input():
	try:
		node_container = mt.NodeContainer()
		node = node_container.create_node()
		node_container.create_node(node)
		assert len(node_container.get_nodes_by_parent_id(str(node.id))) == 1
	except Exception as exc:
		assert False, exc
# endregion

# region get nodes of branch level
def test_get_nodes_of_branch_level():
	test_glyph = mt.Glyph("Test4.csv", False, False)
	node_container = mt.NodeContainer()
	for node in test_glyph.nodes:
		node_container.nodes.append(node)
	nodes = node_container.get_nodes_of_branch_level(3)
	
	results = []
	
	for node in nodes:
		results.append(node.id)
	
	assert results == [10, 11, 14, 15]
# endregion

# region unselect all
def test_unselect_all():
	node_container = mt.NodeContainer()
	for i in range(5):
		node_container.create_node().selected = 1
	
	node_container.unselect_all()
	
	for node in node_container.nodes:
		if node.selected == 1:
			assert node.selected == 0
	
	assert True
# endregion

# region untag all
def test_untag_all():
	node_container = mt.NodeContainer()
	for i in range(5):
		node_container.create_node(tag_mode=1)
	
	node_container.untag_all()
	
	for node in node_container.nodes:
		if node.tag_mode == 1:
			assert node.tag_mode == 0
	
	assert True
# endregion

# region match record ids and data to ids
def test_match_record_ids_and_data_to_ids_record_id():
	test_glyph = mt.Glyph("Test1.csv", False, False)
	node_container = mt.NodeContainer()
	for node in test_glyph.nodes:
		node_container.nodes.append(node)
	node_container.match_record_ids_and_data_to_ids()
	results = []
	for node in node_container.nodes:
		results.append(node.record_id)
	assert results == [8, 9]

def test_match_record_ids_and_data_to_ids_data():
	test_glyph = mt.Glyph("Test1.csv", False, False)
	node_container = mt.NodeContainer()
	for node in test_glyph.nodes:
		node_container.nodes.append(node)
	node_container.match_record_ids_and_data_to_ids()
	results = []
	for node in node_container.nodes:
		results.append(node.data)
	assert results == [8, 9]
# endregion

# region make link

def test_make_link_correct_input_ints():
	ntf = mt.NodeFile("Test")
	node1 = ntf.create_node()
	node2 = ntf.create_node()
	original_length = ntf.length()
	last_id = node2.id
	link = ntf.make_link(node1, node2)
	assert link.parent_id == node1.id and \
		   link.child_id ==node2.id and \
		   original_length + 1 == ntf.length() and \
		   last_id + 1 == link.id

def test_make_link_correct_input_a_b_are_same():
	ntf = mt.NodeFile("Test")
	node1 = ntf.create_node()
	with pytest.raises(RuntimeError):
		ntf.make_link(node1, node1)

def test_make_link_id1_not_in_nodes():
	ntf = mt.NodeFile("Test")
	node1 = ntf.create_node()
	node2 = mt.Node()
	node2.id = 50

	with pytest.raises(RuntimeError):
		ntf.make_link(node1, node2)

def test_make_link_id2_not_in_nodes():
	ntf = mt.NodeFile("Test")
	node1 = ntf.create_node()
	node2 = mt.Node()
	with pytest.raises(RuntimeError):
		ntf.make_link(node2, node1)

# endregion

# region add glyph
def test_add_glyph_ids():
	glyph = mt.Glyph()
	glyph.create_node(glyph.create_node())
	
	node_container = mt.NodeContainer()
	node_container.add_glyph(glyph)
	assert node_container.get_last_node().id == mt.main_grid_id + 2

def test_add_glyph_parent_ids():
	glyph = mt.Glyph()
	glyph.create_node(glyph.create_node())
	
	node_container = mt.NodeContainer()
	node_container.add_glyph(glyph)
	assert node_container.get_last_node().parent_id == mt.main_grid_id + 1

def test_add_glyph_increment_ids():
	glyph = mt.Glyph()
	glyph.create_node(glyph.create_node())
	
	node_container = mt.NodeContainer()
	node_container.add_glyph(glyph)
	node_container.add_glyph(glyph)
	assert glyph.get_last_node().id == mt.main_grid_id + 4

def test_add_glyph_increment_parent_ids():
	glyph = mt.Glyph()
	glyph.create_node(glyph.create_node())
	
	node_container = mt.NodeContainer()
	node_container.add_glyph(glyph)
	node_container.add_glyph(glyph)
	assert glyph.get_last_node().parent_id == mt.main_grid_id + 3

def test_add_glyph_branch():
	glyph = mt.Glyph()
	glyph.create_node(glyph.create_node())
	
	glyph2 = mt.Glyph()
	glyph2.create_node(glyph2.create_node())
	
	node_container = mt.NodeContainer()
	node_container.add_glyph(glyph)
	node_container.add_glyph(glyph2, node_container.get_last_node().id)
	
	assert glyph2.get_last_node().branch_level == 4

def test_add_glyph_bad_parent_id():
	with pytest.raises(RuntimeError):
		glyph = mt.Glyph()
		glyph.create_node(glyph.create_node())
		
		glyph2 = mt.Glyph()
		glyph2.create_node(glyph.create_node())
		
		node_container = mt.NodeContainer()
		node_container.add_glyph(glyph)
		node_container.add_glyph(glyph2, 50)

def test_add_glyph_copy():
	glyph = mt.Glyph()
	glyph.create_node(glyph.create_node())
	
	node_container = mt.NodeContainer()
	node_container.add_glyph(glyph)
	assert glyph.get_last_node() != node_container.get_last_node()

def test_add_glyph_not_copy():
	glyph = mt.Glyph()
	glyph.create_node(glyph.create_node())
	
	node_container = mt.NodeContainer()
	node_container.add_glyph(glyph, copy_glyph=False)
	assert glyph.get_last_node() == node_container.get_last_node()

def test_add_glyph_bad_input_glyph():
	with pytest.raises(TypeError):
		
		node_container = mt.NodeContainer()
		node_container.add_glyph(10)

def test_add_glyph_bad_input_parent_idh():
	with pytest.raises(TypeError):
		glyph = mt.Glyph()
		node_container = mt.NodeContainer()
		node_container.add_glyph(glyph, 'a')

def test_add_glyph_bad_input_copy_glyph():
	with pytest.raises(TypeError):
		glyph = mt.Glyph()
		node_container = mt.NodeContainer()
		node_container.add_glyph(glyph, '0', 'a')
# endregion

# region create_node
def test_create_node():
	node_container = mt.NodeContainer()
	node1 = node_container.create_node()
	node2 = node_container.create_node()
	assert node1.id == mt.main_grid_id + 1 and node2.id == mt.main_grid_id + 2

def test_create_node_with_tag():
	node_container = mt.NodeContainer()
	node1 = node_container.create_node()
	node2 = node_container.create_node(None, 'tag', 1)
	assert node1.tag_text == "" and node1.tag_mode == 0 and node2.tag_text == 'tag' and node2.tag_mode == 1

def test_create_node_with_parent():
	node_container = mt.NodeContainer()
	node1 = node_container.create_node()
	node2 = node_container.create_node(node1)
	assert node2.parent_id == mt.main_grid_id + 1 and node2.branch_level == 2

def test_create_node_with_template():
	node_container = mt.NodeContainer()
	node1 = node_container.create_node()
	node1.scale_x = 6
	node2 = node_container.create_node(template=node1)
	assert node2.id != node1.id and node1.scale_x == node2.scale_x

def test_create_node_bad_input_parent_node():
	with pytest.raises(TypeError):
		node_container = mt.NodeContainer()
		node1 = node_container.create_node()
		node2 = node_container.create_node('a', 'tag', 1)

def test_create_node_bad_input_tag_mode():
	with pytest.raises(TypeError):
		node_container = mt.NodeContainer()
		node1 = node_container.create_node()
		node2 = node_container.create_node(node1, 'tag', 'a')

def test_create_node_bad_input_template():
	with pytest.raises(TypeError):
		node_container = mt.NodeContainer()
		node1 = node_container.create_node()
		node2 = node_container.create_node(node1, 'tag', 'a', 'a')

def test_create_node_parent_node_not_in_nodes():
	with pytest.raises(RuntimeError):
		node_container = mt.NodeContainer()
		node1 = node_container.create_node()
		fake_node = mt.Node()
		node2 = node_container.create_node(fake_node)
# endregion

# region create_grid
def test_create_grid_no_handle_no_():
	node_container = mt.NodeContainer()
	node_tuple = node_container.create_grid()
	assert type(node_tuple) == tuple

def test_create_grid_no_handle():
	node_container = mt.NodeContainer()
	grid = node_container.create_grid(create_handle=False)
	assert type(grid) == mt.Node

def test_create_grid_parent_id():
	node_container = mt.NodeContainer()
	grid_handle, grid = node_container.create_grid()
	assert grid_handle.id == grid.parent_id

def test_create_grid_grid_properties():
	node_container = mt.NodeContainer()
	grid_handle, grid = node_container.create_grid()
	assert grid.type == 6 and grid.topo == mt.topos['plane'] and grid.geometry == mt.geos['plane']

def test_create_grid_templates():
	node_container = mt.NodeContainer()
	grid_handle, grid = node_container.create_grid()
	
	grid.set_segments(500)
	grid_handle.color_a = 100
	
	new_grid_handle, new_grid = node_container.create_grid(grid_template=grid, handle_template=grid_handle)
	assert new_grid_handle.color_a == grid_handle.color_a and grid.segments_x == new_grid.segments_x

def test_create_grid_template_not_equal():
	node_container = mt.NodeContainer()
	grid_handle, grid = node_container.create_grid()
	
	grid.set_segments(500)
	grid_handle.color_a = 100
	
	new_grid_handle, new_grid = node_container.create_grid(grid_template=grid, handle_template=grid_handle)
	assert grid_handle.id != new_grid_handle.id and grid.id != new_grid.id
# endregion

