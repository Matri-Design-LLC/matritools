import pandas as pd
from matritools import utils as mu
import math

def sine_function(amplitude: float = 1,
                 frequency:float = 1,
                 increments:float = 12,
                 x_offset:float = 0,
                 y_offset:float = 0,
                 decimal_place: int = 2):
    """
    Creates a sine function with pre set parameters.
    Y = round({sin([x + x_offset] * [pi / increments] * frequency) * amplitude} + y_offset, decimal_place)
    Parameters:
        amplitude (float: 1) - effects the min and max output of the function.
        frequency (float : 1) - effect how frequently the value rises and falls over time.
        increments (float : 12) - effects how many increments a wave is measured at.
        x_offset (float : 0) - the amount x is offset before being transformed by the fucntion
        y_offset (float : 0) - the amount the final result is offset by.
        decimal_place (int: 2) - the number of decimal places the function is rounded by.

    Returns:
        sine function

        Parameters:
            x (float) - input value

        returns:
            float

        raises:
            TypeError

    Raises:
        TypeError
    """
    mu.check_type(amplitude, float)
    mu.check_type(frequency, float)
    mu.check_type(increments)
    mu.check_type(x_offset, float)
    mu.check_type(y_offset, float)
    mu.check_type(decimal_place, int)
    def sin(x: float):
        mu.check_type(x, float)
        new_x = (float(x) + float(x_offset))
        sin_result = math.sin(new_x * (math.pi / float(increments)) * float(frequency)) * float(amplitude)
        return round(sin_result, int(decimal_place)) + float(y_offset)
    return sin


def cosine_function(amplitude: float = 1,
                 frequency: float = 1,
                 increments: float = 12,
                 offset: float = 0,
                 decimal_place: int = 2):
    """
    Creates a cosine function with pre set parameters
    Parameters:
        amplitude:
        frequency:
        increments:
        offset:
        decimal_place:

    Returns:
        cosine function

        Parameters:
            x (float) - input value

        returns:
            float

        raises:
            TypeError

    Raises:
        TypeError
    """
    mu.check_type(amplitude, float)
    mu.check_type(frequency, float)
    mu.check_type(increments)
    mu.check_type(offset, float)
    mu.check_type(decimal_place, int)

    def sin(x: float):
        mu.check_type(x, float)
        sin_result = math.cos(float(x) * (math.pi / float(increments)) * float(frequency)) * float(amplitude)
        return round(sin_result, int(decimal_place)) + float(offset)

    return sin

class ChannelFile:
    """

    """
    def __init__(self, cycle_count):
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

        mu.check_type(cycle_count, int)
        self.cycle_count = int(cycle_count)

        self.current_id =0
        self.map = {
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
        mu.check_type(attribute, str, False)
        mu.check_type(channel_id, int)
        mu.check_type(track_id, int)
        mu.check_type(track_table_id, int)
        mu.check_type(ch_map_table_id, int)
        mu.check_type(record_id, int)

        self.map['id'].append(self.current_id)
        self.current_id += 1
        self.map['channel_id'].append(int(channel_id))
        if track_id == 0:
            track_id = channel_id
        self.map['track_id'].append(int(track_id))
        self.map['attribute'].append(attribute)
        self.map['track_table_id'].append(int(track_table_id))
        self.map['ch_map_table_id'].append(int(ch_map_table_id))
        self.map['record_id'].append(int(record_id))

    def write_to_csv(self, path: str = ''):
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
        pd.DataFrame(self.map).to_csv(path + 'antzchmap0001.csv', index=False)

    def __populate_channel(self, channel, key):
        if len(self.channel_data[key]) > 0:
            if len(self.channel_data[key]) != self.cycle_count:
                raise RuntimeError(f'{key} number of values does not match cycle_count. Number of values must be {self.cycle_count}')
        else:
            for i in range(1, self.cycle_count + 1):
                self.channel_data[key].append(channel(i))
