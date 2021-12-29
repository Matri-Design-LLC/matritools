set_tag
-------
Sets tag text and tag mode.

Parameters:

+------------+---------------------------------------------+------------------+---------+
| Name       | Description                                 | Type             | Default |
+============+=============================================+==================+=========+
| tag_text   | sets NodeFile.tag_text                      | any              | None    |
+------------+---------------------------------------------+------------------+---------+
| tag_mode   | sets NodeFile.tag_mode                      | int              | None    |
+------------+---------------------------------------------+------------------+---------+

Returns:
    self

Raises:
    TypeError

Example::

    from matritools import nodefile as nf

    # create node
	node = nf.Node()

	node.set_tag('tag', 1)

	# same as

	node.tag_text = 'tag
    node.tag_mode = 1

