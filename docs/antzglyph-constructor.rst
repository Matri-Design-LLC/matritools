`AntzGlyph <antzglyph>`_
========================
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
    |                      | (IDs 1-6) be removed                         | bool | True    |
    +----------------------+----------------------------------------------+------+---------+
    | make_ids_consecutive | Should the IDs of the glyph template file be |      |         |
    |                      | changed to be consecutive?                   | bool | True    |
    +----------------------+----------------------------------------------+------+---------+

Returns: List[NodeFileRow]

Example::

    from matritools import nodefile as nf

    # "example.csv" Glyph template Node file
    # | ID | parent ID | child ID
    # | 1  | <<< Global Parameter
    # | 2  | <<< Global Parameter
    # | 3  | <<< Global Parameter
    # | 4  | <<< Global Parameter
    # | 5  | <<< Global Parameter
    # | 6  | <<< Global Parameter
    # | 20 | 0         | 0
    # | 21 | 20        | 0
    # | 56 | 20        | 0
    # | 70 | 21        | 56


    unchanged_glyph = nf.AntzGlyph("example.csv", False, False)

    # unchanged_glyph
    # | ID | parent ID | child ID
    # | 1  | <<< Global Parameter
    # | 2  | <<< Global Parameter
    # | 3  | <<< Global Parameter
    # | 4  | <<< Global Parameter
    # | 5  | <<< Global Parameter
    # | 6  | <<< Global Parameter
    # | 20 | 0         | 0
    # | 21 | 20        | 0
    # | 56 | 20        | 0
    # | 70 | 21        | 56

    removed_params_glyph = nf.AntzGlyph("example.csv, True, False)

    # Example Glyph template Node file
    # | ID | parent ID | child ID
    # | 20 | 0         | 0
    # | 21 | 20        | 0
    # | 56 | 20        | 0
    # | 70 | 21        | 56

    consecutive_removed_params_glyph = nf.AntzGlyph("example.csv)

    # Example Glyph template Node file
    # | ID | parent ID | child ID
    # | 8  | 0         | 0
    # | 9  | 8         | 0
    # | 10 | 8         | 0
    # | 11 | 9         | 10

