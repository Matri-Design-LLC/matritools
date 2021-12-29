import pandas as pd
from matritools import utils as mu

class ChannelFile:
    """
    Class that builds and writes Antz channel file and channel map file used for animations within Antz.

    Attributes:
        cycle_count (int) - Maximum number of animation cycles.
        channel_data (dict) - Dictionary of animation channel values.
        ch1 (int function(int)) - Y = f(x) like function that will populate animation channel.
        ch2 (int function(int)) - Y = f(x) like function that will populate animation channel.
        ch3 (int function(int)) - Y = f(x) like function that will populate animation channel.
        ch4 (int function(int)) - Y = f(x) like function that will populate animation channel.
        ch5 (int function(int)) - Y = f(x) like function that will populate animation channel.
        ch6 (int function(int)) - Y = f(x) like function that will populate animation channel.
        ch7 (int function(int)) - Y = f(x) like function that will populate animation channel.
        ch8 (int function(int)) - Y = f(x) like function that will populate animation channel.
        ch9 (int function(int)) - Y = f(x) like function that will populate animation channel.
        ch10 (int function(int)) - Y = f(x) like function that will populate animation channel.
        ch11 (int function(int)) - Y = f(x) like function that will populate animation channel.
        ch12 (int function(int)) - Y = f(x) like function that will populate animation channel.
        ch13 (int function(int)) - Y = f(x) like function that will populate animation channel.
        ch14 (int function(int)) - Y = f(x) like function that will populate animation channel.
        ch15 (int function(int)) - Y = f(x) like function that will populate animation channel.
    """

    def __init__(self, cycle_count: int):
        """
        Parameters:
            cycle_count (int) - Maximum number of animation cycles.

        Raises:
            TypeError
        """
        mu.check_type(cycle_count, int)
        def default_equation(x):
            return 0
        self.ch1 = default_equation
        self.ch2 = default_equation
        self.ch3 = default_equation
        self.ch4 = default_equation
        self.ch5 = default_equation
        self.ch6 = default_equation
        self.ch7 = default_equation
        self.ch8 = default_equation
        self.ch9 = default_equation
        self.ch10 = default_equation
        self.ch11 = default_equation
        self.ch12 = default_equation
        self.ch13 = default_equation
        self.ch14 = default_equation
        self.ch15 = default_equation

        self.cycle_count = int(cycle_count)

        self.__current_id__ = 0
        self.__map__ = {
            "id": [],
            "channel_id": [],
            "track_id": [],
            "attribute": [],
            "track_table_id": [],
            "ch_map_table_id": [],
            "record_id": []
        }

        self.channel_data = {
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

    def subscribe_attribute(self, attribute: str,
                            channel_id: int,
                            track_id: int = 0,
                            track_table_id: int = 0,
                            ch_map_table_id: int = 0,
                            record_id: int = 1):
        """
        Subscribes an attribute to an animation channel
        Parameters:
            attribute (str) - name of attribute such as x_translate or x_scale
            channel_id (int) - id of channel (1-15)
            track_id (int: 0) - no antz documentation
            track_table_id (int: 0)  - no antz documentation
            ch_map_table_id (int: 0)  - no antz documentation
            record_id (int: 1) - no antz documentation

        Returns:
            None

        Raises:
            TypeError
        """
        mu.check_type(attribute, str, False)
        mu.check_type(channel_id, int)
        mu.check_type(track_id, int)
        mu.check_type(track_table_id, int)
        mu.check_type(ch_map_table_id, int)
        mu.check_type(record_id, int)

        self.__map__['id'].append(self.__current_id__)
        self.__current_id__ += 1
        self.__map__['channel_id'].append(int(channel_id))
        if track_id == 0:
            track_id = channel_id
        self.__map__['track_id'].append(int(track_id))
        self.__map__['attribute'].append(attribute)
        self.__map__['track_table_id'].append(int(track_table_id))
        self.__map__['ch_map_table_id'].append(int(ch_map_table_id))
        self.__map__['record_id'].append(int(record_id))

    def write_to_csv(self, path: str = ''):
        """
        Writes two csv files (antzch0001.csv and antzchmap0001.csv) formatted for Antz to use for animations.

        Parameters:
            path (str: "") - Path to desired save directory.

        Returns:
            None

        Raises:
            TypeError
            NotADirectoryError

        """
        mu.check_type(path, str, False)

        for i in range(1, self.cycle_count + 1):
            self.channel_data['cyclecount'].append(i)

        self.__populate_channel(self.ch1, 'ch1')
        self.__populate_channel(self.ch2, 'ch2')
        self.__populate_channel(self.ch3, 'ch3')
        self.__populate_channel(self.ch4, 'ch4')
        self.__populate_channel(self.ch5, 'ch5')
        self.__populate_channel(self.ch6, 'ch6')
        self.__populate_channel(self.ch7, 'ch7')
        self.__populate_channel(self.ch8, 'ch8')
        self.__populate_channel(self.ch9, 'ch9')
        self.__populate_channel(self.ch10, 'ch10')
        self.__populate_channel(self.ch11, 'ch11')
        self.__populate_channel(self.ch12, 'ch12')
        self.__populate_channel(self.ch13, 'ch13')
        self.__populate_channel(self.ch14, 'ch14')
        self.__populate_channel(self.ch15, 'ch15')


        if path != '':
            if not path.endswith('/'):
                path = path + '/'

        pd.DataFrame(self.channel_data).to_csv(path + 'antzch0001.csv', index=False)
        pd.DataFrame(self.__map__).to_csv(path + 'antzchmap0001.csv', index=False)

    def __populate_channel(self, channel, key):
        if len(self.channel_data[key]) > 0:
            if len(self.channel_data[key]) != self.cycle_count:
                raise RuntimeError(f'{key} number of values does not match cycle_count. Number of values must be {self.cycle_count}')
        else:
            for i in range(1, self.cycle_count + 1):
                self.channel_data[key].append(channel(i))
