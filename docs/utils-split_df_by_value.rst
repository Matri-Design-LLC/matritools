`utils <utils.html>`_
=====================
create_df_from_json_string
--------------------------
Crates a dataframe from a json formatted string.

Parameters:

+------- +----------------------------------+------------------+---------+
| Name   | Description                      | Type             | Default |
+========+==================================+==================+=========+
| df     | dataframe to be extracted from   | pandas.DataFrame | None    |
+------- +----------------------------------+------------------+---------+
| column | column name to be extracted from | pandas.DataFrame | None    |
+------- +----------------------------------+------------------+---------+

Returns: pandas.DataFrame

Example::

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

    list_of_dfs = mu.dfs_by_value(df, 'B')

    print(len(list_of_dfs)) << 3

    print(list_of_dfs[0])
    # output:
    # | A  | B  | C  |
    # ----------------
    # | a1 | b1 | c1 |

    print(list_of_dfs[1])
    # output:
    # | A  | B  | C  |
    # ----------------
    # | a2 | b2 | c2 |
    # | a2 | b2 | c2 |

    print(list_of_dfs[2])
    # output:
    # | A  | B  | C  |
    # ----------------
    # | a3 | b3 | c3 |

