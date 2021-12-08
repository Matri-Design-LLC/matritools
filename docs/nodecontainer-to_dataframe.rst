`NodeContainer <nodecontainer.html>`_
=====================================
to_dataframe
------------
Returns a DataFrame of all of the Node properties

Parameters: None

Returns:
    DataFrame

Example::

    from matritools import nodefile as nf

    # create NodeContainer
    node_container = nf.NodeContainer()

    # create data frame out of node file
    node_container = my_node_file.to_df()

    print(node_df.head())

    # Output
    #   id type data selected parent_id  ... format_id table_id record_id size\n tag_text
    # 0  4    5    4        0         3  ...         0        0         4  420\n
    # 1  4    5    4        0         3  ...         0        0         4  420\n
    # 2  4    5    4        0         3  ...         0        0         4  420\n
    # 3  4    5    4        0         3  ...         0        0         4  420\n
    # [4 rows x 95 columns]


