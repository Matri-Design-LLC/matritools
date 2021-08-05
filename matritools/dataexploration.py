import pandas as pd

def print_df_column_set(column_series, print_set: bool = False):
    """
    Prints every out the number unique values in a dataframe column
    :param df: target data frame
    :param column: target column
    :param print_sets: Set True to print out each of the unique values
    :return: None
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
    result = {}
    for value in column_series.tolist():
        if value in result.keys():
            result[value] += 1
        else:
            result[value] = 1
    return result

def explore_df(df):
    result = df.describe()
    set_lengths = []
    for column in result.columns:
        set_lengths.append(len(set(df[column].tolist())))

    result.loc["set lengths"] = set_lengths
    return result