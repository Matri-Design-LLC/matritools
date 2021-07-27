`dataexploration <dataexploration.html>`_
=========================================
print_df_column_set
-------------------
Prints number of all unique values of a dataframe column. Optionally prints out all values.

Parameters:

+------------+---------------------------------------------+------------------+---------+
| Name       | Description                                 | Type             | Default |
+============+=============================================+==================+=========+
| df         | target dataframe                            | pandas.DataFrame | None    |
+------------+---------------------------------------------+------------------+---------+
| column     | string value of the target column of df     | str              | None    |
+------------+---------------------------------------------+------------------+---------+
| print_sets | Should all of the unique values be printed? | bool             | False   |
+------------+---------------------------------------------+------------------+---------+

Returns: None

Example::

    from matritools import dataexploration as dex
    import pandas as pd

    # example.csv
    # | A  | B  | C  |
    # ----------------
    # | a1 | b1 | c1 |
    # | a2 | b2 | c2 |
    # | a2 | b2 | c2 |
    # | a3 | b3 | c3 |
    df = pandas.read_csv("example.csv")

    dex.print(df_column_set(df, "A")
    # output
    # A, Length: 3

    dex.print(df_column_set(df, "A", True)
    # output
    # A, Length: 3
    # a1
    # a2
    # a3

