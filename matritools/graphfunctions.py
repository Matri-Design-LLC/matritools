from matritools import utils as mu
import math

def sine_function(amplitude: float = 1,
                  frequency: float = 1,
                  increments: float = 12,
                  x_offset: float = 0,
                  y_offset: float = 0,
                  decimal_place: int = 2):
    """
    Creates a sine function with pre set parameters.
    Y = round({sin([x + x_offset] * [pi / increments] * frequency) * amplitude} + y_offset, decimal_place)
    Parameters:
        amplitude (float: 1) - effects the min and max output of the function.
        frequency (float : 1) - effect how frequently the value rises and falls over time.
        increments (float : 12) - effects how many increments a wave is measured at.
        x_offset (float : 0) - the amount x is offset before being transformed by the function
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
    mu.check_type(increments, float)
    mu.check_type(x_offset, float)
    mu.check_type(y_offset, float)
    mu.check_type(decimal_place, int)

    def sin(x: float):
        mu.check_type(x, float)
        new_x = (float(x) + float(x_offset))
        sin_result = math.sin(new_x * (math.pi / float(increments)) * float(frequency)) * float(amplitude)
        return round(sin_result + float(y_offset), int(decimal_place))

    return sin


def cosine_function(amplitude: float = 1,
                    frequency: float = 1,
                    increments: float = 12,
                    x_offset: float = 0,
                    y_offset: float = 0,
                    decimal_place: int = 2):
    """
    Creates a cosine function with pre set parameters.
    Y = round({cos([x + x_offset] * [pi / increments] * frequency) * amplitude} + y_offset, decimal_place)
    Parameters:
        amplitude (float: 1) - effects the min and max output of the function.
        frequency (float : 1) - effect how frequently the value rises and falls over time.
        increments (float : 12) - effects how many increments a wave is measured at.
        x_offset (float : 0) - the amount x is offset before being transformed by the function
        y_offset (float : 0) - the amount the final result is offset by.
        decimal_place (int: 2) - the number of decimal places the function is rounded by.

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
    mu.check_type(increments, float)
    mu.check_type(x_offset, float)
    mu.check_type(y_offset, float)
    mu.check_type(decimal_place, int)

    def cos(x: float):
        mu.check_type(x, float)
        new_x = (float(x) + float(x_offset))
        cos_result = math.cos(new_x * (math.pi / float(increments)) * float(frequency)) * float(amplitude)
        return round(cos_result + float(y_offset), int(decimal_place))

    return cos


def line_function(slope: float = 1, x_offset: float = 0, y_offset: float = 0, decimal_place: int = 2):
    """
    Creates a line function with pre set parameters
    Y = ((x + x_offset) * slope) + y_offset
    Parameters:
        slope (float : 1) - slope of line.
        x_offset (float : 0) - offset of x pre function.
        y_offset (float : 0) - offset of x post function.

    Returns:
        line function

        Parameters:
            x (float) - input value

        returns:
            float

        raises:
            TypeError

    Raises:
        TypeError
    """
    mu.check_type(slope, float)
    mu.check_type(x_offset, float)
    mu.check_type(y_offset, float)
    mu.check_type(decimal_place, int)

    def line(x: float):
        mu.check_type(float(x), float)
        return round(((float(x) + float(x_offset)) * float(slope)) + float(y_offset), int(decimal_place))

    return line

def triangle_function(slope: float = 1,
                    period: int = 10,
                    x_offset: float = 0,
                    y_offset: float = 0,
                    decimal_place: int = 2):
    mu.check_type(slope, float)
    mu.check_type(period, int)
    mu.check_type(x_offset, float)
    mu.check_type(y_offset, float)
    mu.check_type(decimal_place, int)

    def triangle(x: float):
        mu.check_type(x, float)
        x += x_offset
        x %= period
        if x < period / 2:
            return round((float(x * float(slope)) + float(y_offset)), int(decimal_place))
        else:
            return round((((int(period) - float(x)) * float(slope)) + float(y_offset)), int(decimal_place))

    return triangle