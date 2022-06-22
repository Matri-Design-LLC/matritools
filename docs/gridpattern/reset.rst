place_node
----------

Positions a node and increments internal indexes.

Parameters:
	None

Raises:
    None

Example Default Parameters::

	import matritools as mt

	ntf = mt.NodeFile(file_name)
	node = ntf.create_node()

	grid_pattern = mt.GridPattern()

	print('initial placement: ', node.translate_x, node.translate_y, node.translate_z)

	grid_pattern.place_node(node)
	print('grid placement 1: ', node.translate_x, node.translate_y, node.translate_z)

	grid_pattern.place_node(node)
	print('grid placement 2: ', node.translate_x, node.translate_y, node.translate_z)

	grid_pattern.reset()
	grid_pattern.place_node(node)
	print('grid placement after reset: ', node.translate_x, node.translate_y, node.translate_z)

Output::

	initial placement:  0 0 0
	grid placement 1:  -180.0 -110.0 0.0
	grid placement 2:  -175.0 -110.0 0.0
	grid placement after reset:  -180.0 -110.0 0.0