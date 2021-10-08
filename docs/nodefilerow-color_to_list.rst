`NodeFileRow <nodefilerow.html>`_
=================================
color_to_list
-------------
Returns a list with rgba values of the nodes current color

Parameters: None

Returns: list

Raises: TypeError

Example::

	from matritools import nodefile as nf

	# create node file with 6 default node file rows

	my_node_file = nf.NodeFile("My Node File")

	my_node_file.properties.set_color(1, 2, 3, 4)

	# same as

	my_node_file.properties.color_r = 1
	my_node_file.properties.color_g = 2
	my_node_file.properties.color_b = 3
	my_node_file.properties.color_a = 4

	print(my_node_file.properties.color_to_list())

	# output:
	# [1,2,3,4]

