import matritools.nodefile as nf
import pytest


# region constructor
def test_empty_constructor():
    try:
        nf.Glyph()
    except Exception as exc:
        assert False, exc


def test_construct_without_file_extension():
    with pytest.raises(RuntimeError):
        nf.Glyph("no file ext")


def test_proper_construction():
    try:
        nf.Glyph("Test1.csv")
    except Exception as exc:
        assert False, exc


def test_improperly_formatted_csv_construction():
    with pytest.raises(Exception):
        nf.Glyph("Test2.csv")


def test_construct_with_reserved_rows_without_removal():
    test_glyph3 = nf.Glyph("Test3.csv")
    assert test_glyph3.length() == 2


def test_construct_with_reserved_rows_with_removal():
    try:
        nf.Glyph("Test3.csv")
    except Exception as exc:
        assert False, exc
# endregion

# region create node
def test_create_node_non_temp_to_temp_parent():
    with pytest.raises(RuntimeError):
        glyph = nf.Glyph()
        node1 = glyph.create_temp_node()
        glyph.create_node(node1)
# endregion

# region add glyph
def test_add_glyph_node_non_temp_to_temp_parent():
    with pytest.raises(RuntimeError):
        glyph = nf.Glyph()
        node1 = glyph.create_temp_node()

        glyph2 = nf.Glyph()
        glyph2.create_node()

        glyph.add_glyph(glyph2, node1.id)
# endregion

# region create temp node
def test_create_temp_node():
    glyph = nf.Glyph()
    node1 = glyph.create_node()
    node2 = glyph.create_temp_node()
    assert node1.id == 1 and node2.id == 2 and len(glyph.__temp_nodes__) == 1 and len(glyph.nodes) == 2

def test_create_temp_node_with_tag():
    glyph = nf.Glyph()
    node1 = glyph.create_node()
    node2 = glyph.create_temp_node(None, 'tag', 1)
    assert node1.tag_text == "" and node1.tag_mode == 0 and node2.tag_text == 'tag' and node2.tag_mode == 1

def test_create_temp_node_with_parent():
    glyph = nf.Glyph()
    node1 = glyph.create_node()
    node2 = glyph.create_temp_node(node1)
    assert node2.parent_id == 1 and node2.branch_level == 2

def test_create_temp_node_with_template():
    glyph = nf.Glyph()
    node1 = glyph.create_node()
    node1.selected = 1
    node2 = glyph.create_temp_node(template=node1)
    assert node2.id != node1.id and node1.selected == node2.selected

def test_create_temp_node_bad_input_parent_node():
    with pytest.raises(TypeError):
        glyph = nf.Glyph()
        node1 = glyph.create_node()
        node2 = glyph.create_temp_node('a', 'tag', 1)

def test_create_temp_node_bad_input_tag_mode():
    with pytest.raises(TypeError):
        glyph = nf.Glyph()
        node1 = glyph.create_node()
        node2 = glyph.create_temp_node(node1, 'tag', 'a')

def test_create_temp_node_bad_input_template():
    with pytest.raises(TypeError):
        glyph = nf.Glyph()
        node1 = glyph.create_node()
        node2 = glyph.create_temp_node(node1, 'tag', 'a', 'a')

def test_create_temp_node_parent_node_not_in_nodes():
    with pytest.raises(RuntimeError):
        glyph = nf.Glyph()
        node1 = glyph.create_node()
        fake_node = nf.Node()
        node2 = glyph.create_temp_node(fake_node)

def test_create_temp_node_non_temp_to_temp_parent():
    with pytest.raises(RuntimeError):
        glyph = nf.Glyph()
        node1 = glyph.create_temp_node()
        glyph.create_node(node1)
# endregion

# region add temp glyph
def test_create_temp_glyph():
    glyph = nf.Glyph()
    node1 = glyph.create_node()

    temp_glyph = nf.Glyph()
    node2 = temp_glyph.create_node(temp_glyph.create_node())

    glyph.add_temp_glyph(temp_glyph, node1.id)
    assert node1.id == 1 and node2.id == 3 and len(glyph.__temp_nodes__) == 2 and len(glyph.nodes) == 3

# endregion

# region freeze all
def test_untag_all_true():
    glyph = nf.Glyph()
    for i in range(5):
        glyph.create_node().freeze = 1

    glyph.freeze_all()

    for node in glyph.nodes:
        if node.freeze == 0:
            assert node.freeze == 1

    assert True

def test_untag_all_false():
    glyph = nf.Glyph()
    for i in range(5):
        glyph.create_node()

    glyph.freeze_all(False)

    for node in glyph.nodes:
        if node.freeze == 1:
            assert node.freeze == 0

    assert True
# endregion
