`Node <node.html>`_
===================
color_to_list
-------------
Returns a list with rgba values of the nodes current color

Parameters:
    None

Returns:
    list[int]

Raises:
    TypeError

Example::

	from matritools import nodefile as nf

	# create node
	my_node = nf.Node()

	my_node.set_color(1, 2, 3, 4)

	# same as

	my_node.color_r = 1
	my_node.color_g = 2
	my_node.color_b = 3
	my_node.color_a = 4

	print(my_node.color_to_list())

	# output:
	# [1,2,3,4]

