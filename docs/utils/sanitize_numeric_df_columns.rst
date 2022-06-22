sanitize_numeric_df_columns
---------------------------
Removes characters such as commas, dollar signs, and percent signs from a DataFrame with numeric columns that are
being interpreted as strings and recasts them to an appropriate numeric type.

Parameters:

+-----------------------+------------------------------------------------------------+-----------+----------------+
| Name                  | Description                                                | Type      | Default        |
+=======================+============================================================+===========+================+
| df                    | DataFrame to be operated on.                               | DataFrame | None           |
+-----------------------+------------------------------------------------------------+-----------+----------------+
| columns               | list of column names that are numeric                      |           |                |
|                       | but pandas interprests as strings.                         | List[str] | None           |
+-----------------------+------------------------------------------------------------+-----------+----------------+
| strings_to_be_removed | list of strings or characters                              |           |                |
|                       | to be removed from values.                                 | List[str] | None           |
+-----------------------+------------------------------------------------------------+-----------+----------------+
| errors                | If ‘raise’, then invalid parsing will raise an exception.  |           |                |
|                       | If ‘coerce’, then invalid parsing will be set as NaN.      |           |                |
|                       | If ‘ignore’, then invalid parsing will return the input.   | str       | None           |
+-----------------------+------------------------------------------------------------+-----------+----------------+

Returns:
    interpolation function
            Returns a float that was mapped to the value passed.

            Parameters:
                value: (any: None) A value that belongs to the column_series the function was built with.

            Returns:
                (float) the value that was mapped to value.

            Raises:
                KeyError

Example::

	import pandas as pd
	import matritools as mt

	# data to build DataFrame with
	my_data = {
	'Name'                     : ['Kevin', 'Lisa', 'Ranir', 'Abigale', 'Robert', 'Fran'],
	'Height'                   : [71, 64, 75, 59, 55, 50],
	'Weight'                   : [184, 142, 209, 119, 220, 158],
	'Age'                      : [26, 43, 31, 56, 29, 30],
	'Bank Balance'             : ['$1.06', '$3,567.40', '$300.00', '$536.37', '$126.57', '$-35.00'],
	'Books Started / Finished' : ['50%', "60%", "10%", "35.6%", "47.5%", "100%"],
	'hypothetical value'       : ['50-7', '60-8', '20-2', '35-8', '12-3', '25-8']
	}

	df = pd.DataFrame(my_data)

	# print data types of each column before sanitization.
	for column in df.columns:
		print(column, '::', df[column].dtype)

	numeric_columns_that_are_strings = ['Bank Balance', 'Books Started / Finished']

	# sanitize with default parameters
	mt.sanitize_numeric_df_columns(df, numeric_columns_that_are_strings)

	# print data types of each column after sanitization.
	print('Data Types:\n')
	for column in df.columns:
		print(column, '::', df[column].dtype)

	print('\n')
	print(df.head())
	print('\n')

	numeric_columns_that_are_strings.append('hypothetical value')

	# sanitize with custom parameters
	mt.sanitize_numeric_df_columns(df, numeric_columns_that_are_strings, ['$', '%', ',', '-'])

	# print data types of each column after sanitization.
	print('Data Types:\n')
	for column in df.columns:
		print(column, '::', df[column].dtype)

	print('\n')
	print(df.head())
	print('\n')

	df = pd.DataFrame(my_data)

	# print data types of each column before sanitization.
	print('Data Types:\n')
	for column in df.columns:
		print(column, '::', df[column].dtype)

	mt.sanitize_numeric_df_columns(df, numeric_columns_that_are_strings, errors='ignore')

	print('Data Types:\n')
	for column in df.columns:
		print(column, '::', df[column].dtype)

	print('\n')
	print(df.head())

Output::

	Data Types:

	Name :: object
	Height :: int64
	Weight :: int64
	Age :: int64
	Bank Balance :: object
	Books Started / Finished :: object
	hypothetical value :: object
	Data Types:

	Name :: object
	Height :: int64
	Weight :: int64
	Age :: int64
	Bank Balance :: float64
	Books Started / Finished :: float64
	hypothetical value :: object


		  Name  Height  ...  Books Started / Finished  hypothetical value
	0    Kevin      71  ...                      50.0                50-7
	1     Lisa      64  ...                      60.0                60-8
	2    Ranir      75  ...                      10.0                20-2
	3  Abigale      59  ...                      35.6                35-8
	4   Robert      55  ...                      47.5                12-3

	[5 rows x 7 columns]


	Data Types:

	Name :: object
	Height :: int64
	Weight :: int64
	Age :: int64
	Bank Balance :: float64
	Books Started / Finished :: float64
	hypothetical value :: int64


		  Name  Height  ...  Books Started / Finished  hypothetical value
	0    Kevin      71  ...                      50.0                 507
	1     Lisa      64  ...                      60.0                 608
	2    Ranir      75  ...                      10.0                 202
	3  Abigale      59  ...                      35.6                 358
	4   Robert      55  ...                      47.5                 123

	[5 rows x 7 columns]


	Data Types:

	Name :: object
	Height :: int64
	Weight :: int64
	Age :: int64
	Bank Balance :: object
	Books Started / Finished :: object
	hypothetical value :: object
	Data Types:

	Name :: object
	Height :: int64
	Weight :: int64
	Age :: int64
	Bank Balance :: float64
	Books Started / Finished :: float64
	hypothetical value :: object


		  Name  Height  ...  Books Started / Finished  hypothetical value
	0    Kevin      71  ...                      50.0                50-7
	1     Lisa      64  ...                      60.0                60-8
	2    Ranir      75  ...                      10.0                20-2
	3  Abigale      59  ...                      35.6                35-8
	4   Robert      55  ...                      47.5                12-3

	[5 rows x 7 columns]
