`utils <utils.html>`_
=====================
make_set_scalar
---------------
Creates a resabule psudo-interpolation function to scale non numeric values. This function essentially creates a
dictionary, using each unique value in the column_series and assigns numeric values at equal increments between
min_value and max_value.

Parameters:

+---------------+--------------------------------------+------------------+----------------+
| Name          | Description                          | Type             | Default        |
+===============+======================================+==================+================+
| column_series | column series whos values you want   |                  |                |
|               | the function to interpolate          | Series           | None           |
+---------------+--------------------------------------+------------------+----------------+
| new_min       | The smallest value you want mapped   |                  |                |
|               | to the column_series values          | float            | None           |
+---------------+--------------------------------------+------------------+----------------+
| new_max       | The largest value you want mapped to |                  |                |
|               | the column_series values             | float            | None           |
+---------------+--------------------------------------+------------------+----------------+

Returns:
    interpolation function
            Returns a float that was mapped to the value passed.

            Parameters:
                value: (any: None) A value that belongs to the column_series the function was built with.

            Returns:
                (float) the value that was mapped to value.

            Raises:
                KeyError


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

    interpolator = mu.make_set_scalar(df['Name'], 0, 5)

    for index, row in df.iterrows():
        print(interpolator(row['Name']))


    # output
    # 0
    # 1
    # 2
    # 3
    # 4
    # 5

