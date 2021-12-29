Attributes
----------

+----------------+-------------------------------------------------------------+-------------------+---------+
| Name           | Description                                                 | Type              | Default |
+================+=============================================================+===================+=========+
| cycle_count    | Maximum number of animation cycles.                         | int               | N/A     |
+----------------+-------------------------------------------------------------+-------------------+---------+
| channel_data   | Dictionary of animation channel values.                     | dict              | N/A     |
+----------------+-------------------------------------------------------------+-------------------+---------+
| ch1            | Y = f(x) like function that will populate animation channel | int function(int) | N/A     |
+----------------+-------------------------------------------------------------+-------------------+---------+
| ch2            | Y = f(x) like function that will populate animation channel | int function(int) | N/A     |
+----------------+-------------------------------------------------------------+-------------------+---------+
| ch3            | Y = f(x) like function that will populate animation channel | int function(int) | N/A     |
+----------------+-------------------------------------------------------------+-------------------+---------+
| ch4            | Y = f(x) like function that will populate animation channel | int function(int) | N/A     |
+----------------+-------------------------------------------------------------+-------------------+---------+
| ch5            | Y = f(x) like function that will populate animation channel | int function(int) | N/A     |
+----------------+-------------------------------------------------------------+-------------------+---------+
| ch6            | Y = f(x) like function that will populate animation channel | int function(int) | N/A     |
+----------------+-------------------------------------------------------------+-------------------+---------+
| ch6            | Y = f(x) like function that will populate animation channel | int function(int) | N/A     |
+----------------+-------------------------------------------------------------+-------------------+---------+
| ch7            | Y = f(x) like function that will populate animation channel | int function(int) | N/A     |
+----------------+-------------------------------------------------------------+-------------------+---------+
| ch8            | Y = f(x) like function that will populate animation channel | int function(int) | N/A     |
+----------------+-------------------------------------------------------------+-------------------+---------+
| ch9            | Y = f(x) like function that will populate animation channel | int function(int) | N/A     |
+----------------+-------------------------------------------------------------+-------------------+---------+
| ch10           | Y = f(x) like function that will populate animation channel | int function(int) | N/A     |
+----------------+-------------------------------------------------------------+-------------------+---------+
| ch11           | Y = f(x) like function that will populate animation channel | int function(int) | N/A     |
+----------------+-------------------------------------------------------------+-------------------+---------+
| ch12           | Y = f(x) like function that will populate animation channel | int function(int) | N/A     |
+----------------+-------------------------------------------------------------+-------------------+---------+
| ch13           | Y = f(x) like function that will populate animation channel | int function(int) | N/A     |
+----------------+-------------------------------------------------------------+-------------------+---------+
| ch14           | Y = f(x) like function that will populate animation channel | int function(int) | N/A     |
+----------------+-------------------------------------------------------------+-------------------+---------+
| ch15           | Y = f(x) like function that will populate animation channel | int function(int) | N/A     |
+----------------+-------------------------------------------------------------+-------------------+---------+

channel_data = {

"cyclecount": [],

"ch1": [],

"ch2": [],

"ch3": [],

"ch4": [],

"ch5": [],

"ch6": [],

"ch7": [],

"ch8": [],

"ch9": [],

"ch10": [],

"ch11": [],

"ch12": [],

"ch13": [],

"ch14": [],

"ch15": []

}

Example::

    from matritools animations as ani

    # graph function
    def x_equal_y(x):
        return x + x_offset

    # channel file creation
    channel_file = ani.ChannelFile(5)

    # two ways to do the same thing.
    # 1. On write_to_csv, channel file will loop through 1 - cycle_count appending the result of ch1 function
    channel_file.ch1 = x_equal_y
    # 2. On write_to_csv, channel file will detect values have already been assigned and just use those values
    channel_file.channel_data['ch1'] = [1,2,3,4,5]

    channel_file.subscribe_attribute('translate_x', 1)

    # you can specify the path to an antz folder.
    channel_file.write_to_csv('antz-xr_2021-06-22_app/usr/csv')
