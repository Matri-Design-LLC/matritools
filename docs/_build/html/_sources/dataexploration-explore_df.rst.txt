`dataexploration <dataexploration.html>`_
=========================================
explore_df
----------
Returns the result of df.describe() with an added row describe the number of unique values per parameter.

Parameters:

    +------------+-------------------+------------------+---------+
    | Name       | Description       | Type             | Default |
    +============+===================+==================+=========+
    | df         | target dataframe  | pandas.DataFrame | None    |
    +--------------+-----------------+------------------+---------+

Returns: pandas.DataFrame

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

