import pandas as pd

def print_df_column_set(column_series, print_set: bool = False):
    """
    Prints every out the number unique values in a dataframe column

    Parameters:
        column_series (Series: None) - target series from a data frame column
        print_sets: Set True to print out each of the unique values

    Returns: None
    """
    col_list = column_series.tolist()
    col_set = set(col_list)

    if print_set:
        print("\n\t" + column_series.name + ", \tLength: " + str(len(col_set)) + "\n")
        for value in col_set:
            print("\t\t" + str(value))
    else:
        print("\t" + column_series.name + ", \tLength: " + str(len(col_set)))

def get_df_column_frequency_by_value(column_series):
    """
    Prints number of all unique values of a dataframe column. Optionally prints out all values.

    Parameters:
        column_series (Series: None) - target series from a data frame column

    Returns: Dict

    """
    result = {}
    for value in column_series.tolist():
        if value in result.keys():
            result[value] += 1
        else:
            result[value] = 1
    return result

def explore_df(df):
    """
    Returns the result of df.describe() with an added row describe the number of unique values per parameter.

    Parameters:
        df: target dataframe

    Returns: DataFrame

    """
    result = df.describe()
    set_lengths = []
    for column in result.columns:
        set_lengths.append(len(set(df[column].tolist())))

    result.loc["set lengths"] = set_lengths
    return result