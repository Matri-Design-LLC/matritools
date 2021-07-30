import matritools.nodefile as nf
import pytest


# region constructor

def test_empty_constructor():
    with pytest.raises(RuntimeError):
        nf.AntzGlyph()


def test_construct_without_file_extension():
    with pytest.raises(RuntimeError):
        nf.AntzGlyph("no file ext")


def test_proper_construction():
    try:
        nf.AntzGlyph("Test1.csv")
    except Exception as exc:
        assert False, exc


def test_improperly_formatted_csv_construction():
    with pytest.raises(Exception):
        nf.AntzGlyph("Test2.csv")


def test_construct_with_reservered_rows_without_removal():
    with pytest.raises(Exception):
        nf.AntzGlyph("Test3.csv", False)


def test_construct_with_reservered_rows_with_removal():
    try:
        nf.AntzGlyph("Test3.csv")
    except Exception as exc:
        assert False, exc


# endregion

# region increment_node_file_rows()
test_glyph4 = nf.AntzGlyph("Test4.csv")
test_glyph4.increment_ids()


def test_id_properly_incremented():
    i = 0
    results = []
    for row in test_glyph4.node_file_rows:
        results.append(row.id)
        i += 1
    assert results == [16, 17, 18, 19, 20, 21, 22, 23]


def test_parent_id_properly_incremented():
    i = 0
    results = []
    for row in test_glyph4.node_file_rows:
        results.append(row.parent_id)
        i += 1
    assert results == [0, 16, 17, 17, 0, 20, 21, 20]


def test_child_id_properly_incremented():
    i = 0
    results = []
    for row in test_glyph4.node_file_rows:
        results.append(row.child_id)
        i += 1
    assert results == [0, 0, 0, 0, 0, 0, 0, 16]

# endregion

def test_unselect_all():
    for row in test_glyph4.node_file_rows:
        row.selected = 1

    test_glyph4.unselect_all()

    for row in test_glyph4.node_file_rows:
        if row.selected == 1:
            assert row.selected == 0

    assert True

def test_match_record_ids_and_data_to_ids_record_id():
    test_glyph = nf.AntzGlyph("Test1.csv", False, False)
    test_glyph.match_record_ids_and_data_to_ids()
    results = []
    for row in test_glyph.node_file_rows:
        results.append(row.record_id)
    assert results == [38, 39]

def test_match_record_ids_and_data_to_ids_data():
    test_glyph = nf.AntzGlyph("Test1.csv", False, False)
    test_glyph.match_record_ids_and_data_to_ids()
    results = []
    for row in test_glyph.node_file_rows:
        results.append(row.data)
    assert results == [38, 39]

def test_get_rows_of_branch_level():
    test_glyph = nf.AntzGlyph("Test4.csv", False, False)
    rows = test_glyph.get_rows_of_branch_level(3)

    results = []

    for row in rows:
        results.append(row.id)

    assert results == [40, 41, 44, 45]

def test_remove_rows_of_branch_level():
    test_glyph = nf.AntzGlyph("Test4.csv", False, False)
    test_glyph.remove_rows_of_branch_level(3)
    rows = test_glyph.get_rows_of_branch_level(3)

    results = []

    for row in rows:
        results.append(row.id)

    assert results == []
