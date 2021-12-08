`utils <utils.html>`_
=====================
create_df_from_json_string
--------------------------
Crates a dataframe from a json formatted string.

Parameters:

+----------------+-----------------------+------+---------+
| Name           | Description           | Type | Default |
+================+=======================+======+=========+
| json_string    | json formatted string | str  | None    |
+----------------+-----------------------+------+---------+

Returns:
    pandas.DataFrame

Example::

    from matritools import utils as mu
    import pandas as pd

    df = mu.create_df_from_json_string("{"name":"John", "age":30, "car":null}")

    print(df.shape)
    # output
    # (1, 3)

