import pandas as pd
from ast import literal_eval
import json

def create_df_from_json(json_file_name):
    with open(json_file_name) as json_data:
        return pd.DataFrame(json.load(json_data))


def create_df_from_json_string(json_string):
    return pd.DataFrame(json.load(json_string))


def interpolate_df_column(df, column, obj_scale_min, obj_scale_max, column_tail):
    """
    Scales the values of a data frame column between obj_scale_min and obj_scale_max.
    Adds the interpolated data into a new column labeled (original column name) + (column_tail) and preserves original
    un-interpolated data.

    :param df:
    :param column:
    :param obj_scale_min:
    :param obj_scale_max:
    :param column_tail:
    :return:
    """
    col_min = df[column].min()
    col_max = df[column].max()
    col_list = df[column].tolist()
    scalar = make_interpolater(col_min + .0002, col_max, obj_scale_min, obj_scale_max)
    col_interp = [scalar(x) for x in col_list]
    df[(column + column_tail)] = col_interp


def make_interpolator(old_min, old_max, new_min, new_max):
    """
    Creates a reusable interpolation function to scale a value in between a new min and new max

    :param old_min:
    :param old_max:
    :param new_min:
    :param new_max:
    :return: interpolation function
    """

    # Figure out how 'wide' each range is
    old_span = old_max - old_min
    new_span = new_max - new_min

    # Compute the scale factor between old and new values
    scale_factor = float(new_span) / float(old_span)

    # create interpolation function using pre-calculated scaleFactor
    def interp_fn(value):
        """
        Scale a value in between a set min and  max
        :param value: value to be interpolated
        :return: float
        """
        return new_min + (value - old_min) * scale_factor

    return interp_fn

def separate_compound_dataframe(df, evaluate_df=True, name_template=""):
    """
    Use to create a list of data frames from a dataframe with embedded lists.

    :param df: a data frame that has lists of data contained in individual cells
    :param evaluate_df: set True to apply literal_eval (default True)
    :param name_template: individual data frame columns = lambda x: (name_template + "{}").format(x + 1) (default "")
    :return: list of data frames


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
    if evaluate_df:
        for column in df.columns:
            df[column] = df[column].apply(literal_eval)

    df_list = []

    l = lambda x: (name_template + "{}").format(x + 1)
    for column in df.columns:
        df_list.append(pd.DataFrame(df[column].values.tolist(), df.index, dtype=object).fillna(17).rename(columns=l))

    return df_list

def find_index_in_set(value_set, value):
    """
    returns the index of a value in a set as if it were a list
    :param value_set: target set
    :param value: target value
    :return: (int) index of value in value_set, returns -1 if value is not in value_set
    """
    index = 0
    for i in value_set:
        if value == i:
            return index
        index += 1
    return -1

def set_to_list(value_set):
    """
    Converts a set to a list
    :param value_set: target set
    :return: list
    """
    result = []
    for value in value_set:
        result.append(value)
    return result