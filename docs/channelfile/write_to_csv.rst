write_to_csv
------------
Writes two csv files (antzch0001.csv and antzchmap0001.csv) formatted for Antz to use for animations.

Parameters:

+---------------+------------------------------------------------------------------+-------+---------+
| Name          | Description                                                      | Type  | Default |
+===============+==================================================================+=======+=========+
| path          | Path to desired save directory.                                  | str   | ""      |
+---------------+------------------------------------------------------------------+-------+---------+

Returns:
    none

Raises:
    RuntimeError

    NotADirectoryError

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

    channel_file.subscribe_attribute('translate_x', 1)

    # you can specify the path to an antz folder.
    channel_file.write_to_csv('antz-xr_2021-06-22_app/usr/csv')
