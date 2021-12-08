`utils <utils.html>`_
=====================
make_df_column_interpolator
-----------------
Creates a reusable interpolation function to scale a value in between a new min and new max.

Parameters:

+---------------+--------------------------------------+------------------+----------------+
| Name          | Description                          | Type             | Default        |
+===============+======================================+==================+================+
| column_series | column_series that you want to       |                  |                |
|               | derive old_min and old_max from      | Series           | None           |
+---------------+--------------------------------------+------------------+----------------+
| new_min       | new minimum value                    | float            | None           |
+---------------+--------------------------------------+------------------+----------------+
| new_max       | new maximum value                    | float            | None           |
+---------------+--------------------------------------+------------------+----------------+
| handle_error  | if value passed in isn't a number,   |                  |                |
|               | should the function return           |                  |                |
|               | default_value instead of raising     |                  |                |
|               | error?                               | bool             | False          |
+---------------+--------------------------------------+------------------+----------------+
| default_value | value that gets returned if non      |                  |                |
|               | number is passed and handle_error    |                  |                |
|               | == True                              | float            | None           |
+---------------+--------------------------------------+------------------+----------------+

Returns:
    Function (interpolates a value based on predefined scale factors:
        Parameters:
            value (float: None)
        Returns:
            Float


Example::

    import pandas as pd
    from matritools import utils as mu

    my_data = {
    'Name'         : ['Kevin', 'Lisa', 'Ranir', 'Abigale', 'Robert', 'Fran'],
    'Height'       : [71, 64, 75, 59, 55, 50],
    'Weight'       : [184, 142, 209, 119, 220, 158],
    'Age'          : [26, 43, 31, 56, 29, 30],
    'Bank Balance' : [1.06, 3567.40, 300.00, 536.37, 126.57, -35.00]
    }

    df = pd.DataFrame(my_data)

    interpolator = mu.make_df_column_interpolator(df['Height'], 1, 3)

    for index, row in df.iterrows():
        print(interpolator(row['Height']))


    # output
    # 2.6799999999999997
    # 2.12
    # 3.0
    # 1.72
    # 1.4
    # 1.0

