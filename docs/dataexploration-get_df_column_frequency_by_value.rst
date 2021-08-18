`dataexploration <dataexploration.html>`_
=========================================
get_df_column_frequency_by_value
--------------------------------
Prints number of all unique values of a dataframe column. Optionally prints out all values.

Parameters:

+---------------+------------------------------------------------+------------------+----------------+
| Name          | Description                                    | Type             | Default        |
+===============+================================================+==================+================+
| column_series | target series from a data frame column         | pandas.Series    | None           |
+---------------+------------------------------------------------+------------------+----------------+

Returns: Dict

Example::

    from matritools import dataexploration as dex
    from matritools import utils as mu
    import pandas as pd

    # example.csv
    # | A  | B  | C  |
    # ----------------
    # | a1 | b1 | c1 |
    # | a2 | b2 | c2 |
    # | a2 | b2 | c2 |
    # | a3 | b3 | c3 |
    df = pandas.read_csv("example.csv")

    frequencies = dex.get_df_column_frequency_by_value(df["A"]

    print(mu.dict_to_mulilined_str(frequencies))

    # output:
    # a1 : 1
    # a2 : 2
    # a3 : 1

