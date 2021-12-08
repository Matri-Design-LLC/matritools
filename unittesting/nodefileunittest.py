import matritools.nodefile as nf
import pytest

# region constructor
def test_empty_constructor():
    with pytest.raises(TypeError):
        nf.NodeFile()

def test_constructor_row_count():
    ntf = nf.NodeFile("Test")
    assert len(ntf.nodes) == 6

def test_constructor_initial_row_ids():
    ntf = nf.NodeFile("Test")

    results = []

    for row in ntf.nodes:
        results.append(row.id)

    assert results == [1,2,3,4,5,6]
# endregion

# region add glyph
def test_add_glyph():
    glyph = nf.Glyph()
    glyph.create_node(glyph.create_node())
    glyph.create_temp_node(glyph.get_last_node())

    glyph2 = nf.Glyph()
    glyph2.create_node(glyph2.create_node())

    glyph.add_temp_glyph(glyph2, glyph.nodes[0].id)

    ntf = nf.NodeFile('test')
    ntf.add_glyph(glyph)
    assert glyph.length() == 2

def test_add_glyph_ids():
    glyph = nf.Glyph()
    glyph.create_node(glyph.create_node())

    node_container = nf.NodeContainer()
    node_container.add_glyph(glyph)
    assert node_container.get_last_node().id == 2

def test_add_glyph_parent_ids():
    glyph = nf.Glyph()
    glyph.create_node(glyph.create_node())

    node_container = nf.NodeContainer()
    node_container.add_glyph(glyph)
    assert node_container.get_last_node().parent_id == 1

def test_add_glyph_increment_ids():
    glyph = nf.Glyph()
    glyph.create_node(glyph.create_node())

    node_container = nf.NodeContainer()
    node_container.add_glyph(glyph)
    node_container.add_glyph(glyph)
    assert glyph.get_last_node().id == 4

def test_add_glyph_increment_parent_ids():
    glyph = nf.Glyph()
    glyph.create_node(glyph.create_node())

    node_container = nf.NodeContainer()
    node_container.add_glyph(glyph)
    node_container.add_glyph(glyph)
    assert glyph.get_last_node().parent_id == 3

def test_add_glyph_branch():
    glyph = nf.Glyph()
    glyph.create_node(glyph.create_node())

    glyph2 = nf.Glyph()
    glyph2.create_node(glyph2.create_node())

    node_container = nf.NodeContainer()
    node_container.add_glyph(glyph)
    node_container.add_glyph(glyph2, node_container.get_last_node().id)

    assert glyph2.get_last_node().branch_level == 4

def test_add_glyph_bad_parent_id():
    with pytest.raises(RuntimeError):
        glyph = nf.Glyph()
        glyph.create_node(glyph.create_node())

        glyph2 = nf.Glyph()
        glyph2.create_node(glyph.create_node())

        node_container = nf.NodeContainer()
        node_container.add_glyph(glyph)
        node_container.add_glyph(glyph2, 50)

def test_add_glyph_copy():
    glyph = nf.Glyph()
    glyph.create_node(glyph.create_node())

    node_container = nf.NodeContainer()
    node_container.add_glyph(glyph)
    assert glyph.get_last_node() != node_container.get_last_node()

def test_add_glyph_not_copy():
    glyph = nf.Glyph()
    glyph.create_node(glyph.create_node())

    node_container = nf.NodeContainer()
    node_container.add_glyph(glyph, copy_glyph=False)
    assert glyph.get_last_node() == node_container.get_last_node()

def test_add_glyph_bad_input_glyph():
    with pytest.raises(TypeError):
        node_container = nf.NodeContainer()
        node_container.add_glyph(10)

def test_add_glyph_bad_input_parent_idh():
    with pytest.raises(TypeError):
        glyph = nf.Glyph()
        node_container = nf.NodeContainer()
        node_container.add_glyph(glyph, 'a')

def test_add_glyph_bad_input_copy_glyph():
    with pytest.raises(TypeError):
        glyph = nf.Glyph()
        node_container = nf.NodeContainer()
        node_container.add_glyph(glyph, '0', 'a')
# endregion
