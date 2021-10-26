import pandas as pd
from matritools import nodefile as nf
from ast import literal_eval
import json

def create_df_from_json(json_file_name: str):
    """
    Crates a dataframe from a json file name.

    Parameters:
        json_file_name (str: None) - file name of .json file

    Returns: DataFrame

    """
    with open(json_file_name) as json_data:
        return pd.DataFrame(json.load(json_data))

def create_df_from_json_string(json_string):
    """
    Crates a dataframe from a json formatted string.

    Parameters:
        json_string (str: None) - string in json format

    Returns: Dataframe

    """
    return pd.DataFrame(json.load(json_string))

def interpolate_df_column(df, column: str, new_min: float, new_max: float, column_tail: str = "_interpolated", handle_error: bool = False, default_value: float = None):
    """
    Scales the values of a data frame column between obj_scale_min and obj_scale_max.
    Adds the interpolated data into a new column labeled (original column name) + (column_tail) and preserves original
    un-interpolated data.

    Parameters:
        df (DataFrame: None) - target DataFrame
        column (str: None) - string column to be interpolated
        obj_scale_min (float: None) - new minimum value
        obj_scale_max (float: None) -  new maximum value
        column_tail (str: "_interpolated") - string to be appended to column name
        handle_error (bool: False) - if value passed in isn't a number, should the function return default_value instead of raising error?
        default_value (float: None) - value that gets returned if non number is passed and handle_error == True

    Returns: None
    """
    col_min = df[column].min()
    col_max = df[column].max()
    col_list = df[column].tolist()
    scalar = make_interpolator(col_min + .0002, col_max, float(new_min), float(new_max), handle_error, default_value)
    col_interp = [scalar(x) for x in col_list]
    df[(str(column) + str(column_tail))] = col_interp

def make_interpolator(old_min: float, old_max: float, new_min: float, new_max: float, handle_error: bool = False, default_value: float = None):
    """
    Creates a reusable interpolation function to scale a value in between a new min and new max.

    Parameters:
        old_min (float: None) - old minimum value
        old_max (float: None) - old maximum value
        new_min (float: None) - new minimum value
        new_max (float: None) - new maximum value
        handle_error (bool: False) - if value passed in isn't a number, should the function return default_value instead of raising error?
        default_value (float: None) - value that gets returned if non number is passed and handle_error == True

    Returns: interpolation function
        Scale a value in between a set min and  max

        Paramaters:
            value (float: None) - value to be interpolated

        Returns: float
    """

    # Figure out how 'wide' each range is
    old_span = float(old_max) - float(old_min)
    new_span = float(new_max) - float(new_min)

    # Compute the scale factor between old and new values
    if old_span == 0:
        scale_factor = 1
    else:
        scale_factor = float(new_span) / float(old_span)

    # create interpolation function using pre-calculated scaleFactor
    def interp_fn(value: float):
        """
        Scale a value in between a set min and  max

        Paramaters:
            value (float: None) - value to be interpolated

        Returns: float
        """
        result = value
        if handle_error:
            try:
                result = float(value)
            except:
                return default_value
        return new_min + (result - old_min) * scale_factor

    return interp_fn

def make_df_column_interpolator(column_series, new_min: float, new_max: float, handle_error: bool = False, default_value: float = None):
    """
        Creates a reusable interpolation function to scale a value in between a new min and new max.

        Parameters:
            column_series (Series: None) - column_series that you want to derive old_min and old_max from
            new_min (float: None) - new minimum value
            new_max (float: None) - new maximum value
            handle_error (bool: False) - if value passed in isn't a number, should the function return default_value instead of raising error?
            default_value (float: None) - value that gets returned if non number is passed and handle_error == True

        Returns: interpolation function
            Scale a value in between a set min and  max

            Paramaters:
                value (float: None) - value to be interpolated

            Returns: float
    """
    return make_interpolator(column_series.min(), column_series.max(), new_min, new_max, handle_error, default_value)

def make_default_scalar(returned_value):
    """
    Creates a reusable place holder interpolation function that takes in a value and returns min_value
    (the value the function was built with).
    Paramaters:
        min_value: the value that will be returned when calling the returned function

    Returns:
        interpolation function
            Function that returns what ever value it was built with (min_value)

            Parameters:
                value: (any: None) doesn't matter

            Returns:
                what ever value it was built with (min_value)
    """
    def scalar(value):
        return returned_value

    return scalar

def make_set_scalar(column_series, min_value: float, max_value: float):
    """
    Creates a resabule psudo-interpolation function to scale non numeric values. This function essentially creates a
    dictionary, using each unique value in the column_series and assigns numeric values at equal increments between
    min_value and max_value.
    Parameters:
        column_series: (Series : None) column series whos values you want the function to interpolate
        min_value: (float : None) The smallest value you want mapped to the column_series values
        max_value: (float : None) The largest value you want mapped to the column_series values

    Returns:
        interpolation function
            Returns a float that was mapped to the value passed.

            Parameters:
                value: (any: None) A value that belongs to the column_series the function was built with.

            Returns:
                (float) the value that was mapped to value.

            Raises:
                KeyError
    """
    value_dict = {}
    for value in set(column_series):
        value_dict[value] = 0

    value_range = max_value - min_value
    increments = value_range / len(value_dict.keys())
    i = 0
    for key in value_dict.keys():
        value_dict[key] = (i * increments) + min_value

    def position_scalar(value):
        return value_dict[value]

    return position_scalar


def separate_compound_dataframe(df,  name_template=""):
    """
    Use to create a list of data frames from a dataframe with embedded lists.

    Parameters:
        df (DataFrame) - a data frame that has lists of data contained in individual cells
        name_template: individual data frame columns = lambda x: (name_template + "{}").format(x + 1) (default "")

    Returns: list of data frames


    I.E when a data frame is in the form of :

    [ [ 11, 12, 13], [ 14, 15, 16 ], [ 17, 18, 19 ] ]
    [ [ 21, 22, 23], [ 24, 25, 26 ], [ 27, 28, 29 ] ]
    [ [ 31, 32, 33], [ 34, 35, 36 ], [ 37, 38, 39 ] ]

    returns

    df1 [ 11, 12, 13]  df2 [ 14, 15, 16 ]  df3 [ 17, 18, 19 ]
        [ 21, 22, 23]      [ 24, 25, 26 ]      [ 27, 28, 29 ]
        [ 31, 32, 33]      [ 34, 35, 36 ]      [ 37, 38, 39 ]
    """
    # Expand evaluate tupled data into lists
    for column in df.columns:
        try:
            df[column] = df[column].apply(literal_eval)
        except:
            pass

    df_list = []

    l = lambda x: (name_template + "{}").format(x + 1)
    for column in df.columns:
        df_list.append(pd.DataFrame(df[column].values.tolist(), df.index, dtype=object).fillna(17).rename(columns=l))

    return df_list

def find_index_in_set(value_set, value):
    """
    Returns the index of a value in a set as if it were a list

    Parameters:
        value_set (set: None) - target set
        value (any: None) target value

    Returns: (int) index of value in value_set, returns -1 if value is not in value_set
    """
    index = 0
    for i in value_set:
        if value == i:
            return index
        index += 1
    return -1

def set_to_list(value_set):
    """
    Converts a set to a list.

    Parameters:
        value_set (set: None) target set

    Returns: list
    """
    result = []
    for value in value_set:
        result.append(value)
    return result

def dict_to_multilined_str(dictionary: dict, indent_level = 0):
    """
    Converts a dict into a formatted string with a line for each key value pair

    Parameters:
        dictionary (dict: None) - dict to be converted to string
        indent_level (int: 0) - used for recursion for formatting the string in the case of nested dicts

    Returns: str

    """
    result = ""
    for key in dictionary.keys():
        result += ('\t' * indent_level) + str(key) + " : "
        if isinstance(dictionary[key], dict):
            result += "\n" + dict_to_multilined_str(dictionary[key], indent_level + 1)
        else:
            result += str(dictionary[key]) + '\n'
    return result

def create_column_value_color_legend(column_series):
    """
    Creates a dictionary mapping values of a data frame column to names of colors. Used to set NodeFileRow colors by name.

    Parameters:
        column_series (Series: None) - target series from a data frame column

    Returns: Dict[any, str]

    """
    color_keys = []

    for color in nf.NodeFileRow.colors.keys():
        color_keys.append(color)

    result = {}
    i = 0
    for value in set(column_series):
        if i == len(color_keys):
            i = 0
        result[value] = color_keys[i]
        i += 1
    return result

def split_df_by_value(df, column):
    """
    Seperates all the rows of a dataframe by unique value and returns them as a list of dataframes.

    Parametes:
        df (Dataframe: None) - dataframe to be extracted from
        column (str: None) - column name to be extracted from.
    """

    values = set(df[column].tolist())
    result = []
    for value in values:
        result.append(df.loc[df[column] == value])

    return result