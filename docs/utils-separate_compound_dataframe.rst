`utils <utils.html>`_
=====================
set_to_list
-----------
Use to create a list of data frames from a dataframe with embedded lists.

Parameters:

+---------------+------------------------------------------------+------------------+----------------+
| Name          | Description                                    | Type             | Default        |
+===============+================================================+==================+================+
| df            | target DataFrame                               | pandas.DataFrame | None           |
+---------------+------------------------------------------------+------------------+----------------+
| name_template | individual data frame columns =                |                  |                |
|               | lambda x: (name_template + "{}").format(x + 1) | str              | ""             |
+---------------+------------------------------------------------+------------------+----------------+

Returns: List[pandas.DataFrame]

Example::

    from matritools import utils as mu
    import pandas as pd

    df = pd.read_csv("example.csv)

    df_list = mu.separate_compound_dataframe(df)

    I.E when a data frame is in the form of :

    [ [ 11, 12, 13], [ 14, 15, 16 ], [ 17, 18, 19 ] ]
    [ [ 21, 22, 23], [ 24, 25, 26 ], [ 27, 28, 29 ] ]
    [ [ 31, 32, 33], [ 34, 35, 36 ], [ 37, 38, 39 ] ]

    returns

    df1 [ 11, 12, 13]  df2 [ 14, 15, 16 ]  df3 [ 17, 18, 19 ]
        [ 21, 22, 23]      [ 24, 25, 26 ]      [ 27, 28, 29 ]
        [ 31, 32, 33]      [ 34, 35, 36 ]      [ 37, 38, 39 ]

