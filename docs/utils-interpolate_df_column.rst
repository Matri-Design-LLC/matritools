`utils <utils.html>`_
=====================
interpolate_df_column
---------------------
Scales the values of a data frame column between new_min and new_max.
Adds the interpolated data into a new column labeled (original column name) + (column_tail) and preserves original
un-interpolated data.

Parameters:

+---------------+--------------------------------------+------------------+----------------+
| Name          | Description                          | Type             | Default        |
+=============+======================================+==================+================+
| df            | target DataFrame                     | pandas.DataFrame | None           |
+---------------+--------------------------------------+------------------+----------------+
| column        | string column to be interpolated     | str              | None           |
+---------------+--------------------------------------+------------------+----------------+
| new_min       | new minimum value                    | float            | None           |
+---------------+--------------------------------------+------------------+----------------+
| new_max       | new maximum value                    | float            | None           |
+---------------+--------------------------------------+------------------+----------------+
| column_tail   | string to be appended to column name | str              | "_interpolated |
+---------------+--------------------------------------+------------------+----------------+
| handle_error  | new maximum value                    | float            | None           |
+---------------+--------------------------------------+------------------+----------------+
| default_value | new maximum value                    | float            | None           |
+---------------+--------------------------------------+------------------+----------------+

Returns: pandas.DataFrame

Example::

    from matritools import utils as mu
    import pandas as pd

    df = pandas.read_csv("example.csv")

    # df before
    # | A  |
    # ------
    # | 10 |
    # | 20 |
    # | 30 |

    # added column of interpolated values
    mu.interpolate_df_column(df, "A", 1, 3, "_interpolated")

    # df after
    # | A  | A_interpolated |
    # -----------------------
    # | 10 | 1              |
    # | 20 | 2              |
    # | 30 | 3              |

