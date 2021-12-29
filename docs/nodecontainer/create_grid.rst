create_grid
-----------
Creates and returns a Node formatted as a grid, inside of the NodeContainer.
If create_handle is True, the created handle and grid are returned. If not, just the grid is returned.

Parameters:

+--------------------+------------------------------------------------------------------------------+------+---------+
| Name               | Description                                                                  | Type | Default |
+====================+==============================================================================+======+=========+
| parent_node        | Node that newly created Node will be associated with                         | Node | None    |
+--------------------+------------------------------------------------------------------------------+------+---------+
| grid_tag_text      | text that will be written in the tag file associated with the created grid   | str  | ""      |
+--------------------+------------------------------------------------------------------------------+------+---------+
| grid_tag_mode      | int representing how the tag should be displayed by default                  | int  | 0       |
+--------------------+------------------------------------------------------------------------------+------+---------+
| grid_template      | Created node will be a copy of template if one is passed.                    | Node | None    |
+--------------------+------------------------------------------------------------------------------+------+---------+
| create_handle      | Should the grid be attached to a handle?                                     | bool | True    |
+--------------------+------------------------------------------------------------------------------+------+---------+
| handle_tag_text    | text that will be written in the tag file associated with the created Handle | str  | ""      |
+--------------------+------------------------------------------------------------------------------+------+---------+
| handle_tag_mode    | int representing how the tag should be displayed by default                  | int  | 0       |
+--------------------+------------------------------------------------------------------------------+------+---------+
| handle_template    | Created handle will be a copy of template if one is passed.                  | Node | None    |
+--------------------+------------------------------------------------------------------------------+------+---------+


Returns:
    Node

Raises:
    TypeError

    RuntimeError

Example::

    from matritools import nodefile as nf

    # create node file with 6 default node file rows
    my_node_file = nf.NodeFile("My Node File")

    # create grid with handle
    grid_handle, grid = my_node_file.create_grid()

    # modify properties
    grid.set_segments(2,2,0)

    # move position of grid since it is a child of grid_handle
    grid_handle.set_translate(10, 0, 0)

    # change properties of grid handle
    grid.handle.set_color_by_name('red)

    # create new grid that is the same as the first grid but without a handle
    grid_without_handle = my_node_file.create_grid(grid_template=grid, create_handle=False)

    # create new grid with same properties as first grid and handle with same properties as first handle
    new_grid_handle, new_grid = my_nodefile.create_grid(grid_template=grid, handle_template=handle)



