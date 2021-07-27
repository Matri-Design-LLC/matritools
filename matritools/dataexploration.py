import pandas as pd

def print_df_column_set(df, column: str, print_set: bool = False):
    """
    Prints every out the number unique values in a dataframe column
    :param df: target data frame
    :param column: target column
    :param print_sets: Set True to print out each of the unique values
    :return: None
    """
    col_list = df[column].tolist()
    col_set = set(col_list)

    if print_set:
        print("\n\t" + column + ", \tLength: " + str(len(col_set)) + "\n")
        for value in col_set:
            print("\t\t" + str(value))
    else:
        print("\t" + column + ", \tLength: " + str(len(col_set)))

def explore_df(df):
    result = df.describe()
    set_lengths = []
    for column in result.columns:
        set_lengths.append(len(set(df[column].tolist())))

    print(len(set_lengths))
    print(len(result.columns))
    result.loc["set lengths"] = set_lengths
    return result