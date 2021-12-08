`utils <utils.html>`_
=====================
create_column_value_color_legend
--------------------------------
Creates a dictionary mapping values of a data frame column to names of colors. Used to set NodeFileRow colors by name.

Parameters:

+---------------+------------------------------------------------+------------------+----------------+
| Name          | Description                                    | Type             | Default        |
+===============+================================================+==================+================+
| column_series | target series from a data frame column         | pandas.Series    | None           |
+---------------+------------------------------------------------+------------------+----------------+

Returns:
    Dict[any, str]

Example::

    from matritools import utils as mu
    import pandas as pd

    # example.csv
    # | A  | B  |
    # -----------
    # | A1 | B2 |
    # | A2 | B2 |
    # | C2 | C3 |
    df = pd.read_csv("example.csv)

    legend = mu.create_column_value_color_legend(df["A"])

    print(mu.dict_to_mulilined_string(legend))

    # output:
    # A1: red
    # A2: blue
    # A3: green

