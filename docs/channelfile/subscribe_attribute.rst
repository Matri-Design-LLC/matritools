subscribe_attribute
-------------------

Parameters:

attribute (str) - name of attribute such as x_translate or x_scale
            channel_id (int) - id of channel (1-15)
            track_id (int: 0) - column within channel file to subscribe(ch1 == track_id 1)
            track_table_id (int: 0)  - no antz documentation
            ch_map_table_id (int: 0)  - no antz documentation
            record_id (int: 0) - no antz documentation

+-----------------+------------------------------------------------------------------+-------+---------+
| Name            | Description                                                      | Type  | Default |
+=================+==================================================================+=======+=========+
| attribute       | name of attribute such as x_translate or x_scale.                | str   | ""      |
+-----------------+------------------------------------------------------------------+-------+---------+
| channel_id      | id of channel (1-15)                                             | int   | N/A     |
+-----------------+------------------------------------------------------------------+-------+---------+
| track_id        | column within channel file                                       | int   | 0       |
+-----------------+------------------------------------------------------------------+-------+---------+
| track_table_id  | no antz documentation                                            | int   | 0       |
+-----------------+------------------------------------------------------------------+-------+---------+
| ch_map_table_id | no antz documentation                                            | int   | 0       |
+-----------------+------------------------------------------------------------------+-------+---------+
| record_id       | no antz documentation                                            | int   | 1       |
+-----------------+------------------------------------------------------------------+-------+---------+

Raises:
    TypeError

Example::

    from matritools channelfile as cf

    # graph function
    def x_equal_y(x):
        return x

    # channel file creation
    channel_file = cf.ChannelFile(5)

    # two ways to do the same thing.
    # 1. On write_to_csv, channel file will loop through 1 - cycle_count appending the result of ch1 function
    channel_file.ch1 = x_equal_y
    # 2. On write_to_csv, channel file will detect values have already been assigned and just use those values
    channel_file.channel_data['ch1'] = [1,2,3,4,5]

    channel_file.subscribe_attribute('translate_x', 1, 1)

    # you can specify the path to an antz folder.
    channel_file.write_to_csv('antz-xr_2021-06-22_app/usr/csv')
