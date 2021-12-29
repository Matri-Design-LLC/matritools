make_default_scalar
-------------------
Creates a reusable place holder interpolation function that takes in a value and returns min_value
    (the value the function was built with).

Parameters:

+----------------+--------------------------------------+------------------+----------------+
| Name           | Description                          | Type             | Default        |
+================+======================================+==================+================+
| returned_value | the value that will be returned      |                  |                |
|                | when calling the returned function   | float            | None           |
+----------------+--------------------------------------+------------------+----------------+

Returns:
    interpolation function
            Function that returns what ever value it was built with (min_value)

            Parameters:
                value: (any: None) doesn't matter

            Returns:
                what ever value it was built with (min_value)


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

    interpolator = mu.make_default_scalar(5)

    for index, row in df.iterrows():
        print(interpolator(row['Name']))


    # output
    # 5
    # 5
    # 5
    # 5
    # 5
    # 5

