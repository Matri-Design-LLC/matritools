`utils <utils.html>`_
=====================
create_df_from_json
-------------------
Crates a dataframe from a json file name.

Parameters:

+----------------+---------------------------------------------+------+---------+
| Name           | Description                                 | Type | Default |
+================+=============================================+======+=========+
| json_file_name | string name of json file (including ".json" | str  | None    |
+----------------+---------------------------------------------+------+---------+

Returns:
    pandas.DataFrame

Example::

    from matritools import utils as mu
    import pandas as pd

    df = mu.create_df_from_json("example.json")

    print(df.shape)

