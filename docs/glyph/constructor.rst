Constructor
-----------

Parameters:

+----------------------+----------------------------------------------+------+---------+
| Name                 | Description                                  | Type | Default |
+======================+==============================================+======+=========+
| csv_file_name        | string name of glyph template file generated |      |         |
|                      | in OpenANTz including ".csv"                 | str  | ""      |
+----------------------+----------------------------------------------+------+---------+
| remove_global_params | Should global parameter rows                 |      |         |
|                      | (IDs 1-7) be removed                         | bool | True    |
+----------------------+----------------------------------------------+------+---------+
| make_ids_consecutive | remove gaps in between row IDs.              |      |         |
|                      | i.e 1,2,4 becomes 1,2,3                      | bool | True    |
+----------------------+----------------------------------------------+------+---------+
| unselect all         | sets all NodeFileRows selected mode to 0     | bool | True    |
+----------------------+----------------------------------------------+------+---------+
| untag all            | sets all NodeFileRows tag mode to 0          | bool | True    |
+----------------------+----------------------------------------------+------+---------+

Raises: RuntimeError

Example::

    from matritools import nodefile as nf

    # "example.csv" Glyph template Node file
    # | ID | parent ID | child ID | selected | tag_mode
    # | 1  | <<< Global Parameter
    # | 2  | <<< Global Parameter
    # | 3  | <<< Global Parameter
    # | 4  | <<< Global Parameter
    # | 5  | <<< Global Parameter
    # | 6  | <<< Global Parameter
    # | 20 | 0         | 0        | 1        | 1
    # | 21 | 20        | 0        | 1        | 2
    # | 56 | 20        | 0        | 1        | 3
    # | 70 | 21        | 56       | 1        | 4


    unchanged_glyph = nf.AntzGlyph("example.csv", False, False, False, False)

    # unchanged_glyph
    # | ID | parent ID | child ID | selected | tag_mode
    # | 1  | <<< Global Parameter
    # | 2  | <<< Global Parameter
    # | 3  | <<< Global Parameter
    # | 4  | <<< Global Parameter
    # | 5  | <<< Global Parameter
    # | 6  | <<< Global Parameter
    # | 20 | 0         | 0        | 1        | 1
    # | 21 | 20        | 0        | 1        | 2
    # | 56 | 20        | 0        | 1        | 3
    # | 70 | 21        | 56       | 1        | 4

    removed_params_glyph = nf.AntzGlyph("example.csv, True, False, False, False)

    # Example Glyph template Node file
    # | ID | parent ID | child ID | selected | tag_mode
    # | 20 | 0         | 0        | 1        | 1
    # | 21 | 20        | 0        | 1        | 2
    # | 56 | 20        | 0        | 1        | 3
    # | 70 | 21        | 56       | 1        | 4

    consecutive_removed_params_glyph = nf.AntzGlyph("example.csv, True, True, False, False)

    # Example Glyph template Node file
    # | ID | parent ID | child ID | selected | tag_mode
    # | 8  | 0         | 0        | 1        | 1
    # | 9  | 8         | 0        | 1        | 2
    # | 10 | 8         | 0        | 1        | 3
    # | 11 | 9         | 10       | 1        | 4

    consecutive_removed_params_unselected_glyph = nf.AntzGlyph("example.csv, True, True, True, False)

    # Example Glyph template Node file
    # | ID | parent ID | child ID | selected | tag_mode
    # | 8  | 0         | 0        | 0        | 1
    # | 9  | 8         | 0        | 0        | 2
    # | 10 | 8         | 0        | 0        | 3
    # | 11 | 9         | 10       | 0        | 4

    consecutive_removed_params_unselected_untagged_glyph = nf.AntzGlyph("example.csv, True, True, True, True)
    # or
    consecutive_removed_params_unselected_untagged_glyph = nf.AntzGlyph("example.csv)

    # Example Glyph template Node file
    # | ID | parent ID | child ID | selected | tag_mode
    # | 8  | 0         | 0        | 0        | 0
    # | 9  | 8         | 0        | 0        | 0
    # | 10 | 8         | 0        | 0        | 0
    # | 11 | 9         | 10       | 0        | 0

