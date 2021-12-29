make_interpolator
-----------------
Creates a reusable interpolation function to scale a value in between a new min and new max.

Parameters:

+---------------+--------------------------------------+------------------+----------------+
| Name          | Description                          | Type             | Default        |
+===============+======================================+==================+================+
| old_min       | old minimum value                    | float            | None           |
+---------------+--------------------------------------+------------------+----------------+
| old_max       | old maximum value                    | float            | None           |
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

    from matritools import utils as mu

    nums = [10, 20, 30]

    interpolator = mu.make_interpolator(10, 30, 1, 3)

    nums[0] = interpolator(nums[0])
    nums[1] = interpolator(nums[1])
    nums[2] = interpolator(nums[2])

    print(nums)
    # output
    # [1,2,3]

