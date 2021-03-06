Attributes
----------

.. note::

   Parameter descriptions maybe be missing due to the mysterious nature of OpenANTZ

+------------------+---------------------------------------------------------+----------------------+-----------+
| Name             | Description                                             | Type                 | Default   |
+==================+=========================================================+======================+===========+
| id               | node ID used for pin tree relationship graph            | int                  | 8         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| type             | node type - 1: Camera; 2: video; 3: Surface;            | int                  | 5         |
|                  | 4: Points, 5:Pin, 6:Grid                                |                      |           |
+------------------+---------------------------------------------------------+----------------------+-----------+
| data             | additional node specific type, defined by node type     | int                  | 8         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| selected         | selection set status, 1 if part of active set, 0 if not | int                  | 0         |
|                  | Useful if you want the root nodes selected upon loading |                      |           |
+------------------+---------------------------------------------------------+----------------------+-----------+
| parent_id        | ID of parent node                                       | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| branch_level     | root node is 0, each sub-level is 1, 2, 3, … n          | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| child_id         | When used as to represent a link, parent_id is one      | int                  | 0         |
|                  | end and child_id is the other.                          |                      |           |
+------------------+---------------------------------------------------------+----------------------+-----------+
|                  | This object is a link between parent_id and child_id    |                      |           |
| child_index      | currently selected child node                           | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| pallete_id       | hard coded palettes.                                    | int                  | 0         |
|                  | 0: distinct set of 20 original colors/                  |                      |           |
|                  | 1: same as 0 but inverted/                              |                      |           |
|                  | 2: Rainbow Heatmap a composite of gradients/            |                      |           |
|                  | 3 Rainbow Heatmap inverted/                             |                      |           |
|                  | 4-25 are gradients with 256 index's each (0-256)        |                      |           |
|                  | odd palette_id's are inverted of their mirrors -        |                      |           |
|                  | even numbered pallete_id's                              |                      |           |
+------------------+---------------------------------------------------------+----------------------+-----------+
| ch_input_id      | channel number                                          | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| ch_output_id     | channel number                                          | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| ch_last_updated  | previous data update time-stamp (last read)             | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| average          | type of averaging applied to channel data               | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| samples          | number of samples to average                            | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| aux_a_x          | size of grid segments, x axis                           | int                  | 30        |
+------------------+---------------------------------------------------------+----------------------+-----------+
| aux_a_y          | size of grid segments, y axis                           | int                  | 30        |
+------------------+---------------------------------------------------------+----------------------+-----------+
| aux_a_z          | size of grid segments, z axis                           | int                  | 30        |
+------------------+---------------------------------------------------------+----------------------+-----------+
| aux_b_x          | size of grid segments, x axis                           | int                  | 30        |
+------------------+---------------------------------------------------------+----------------------+-----------+
| aux_b_y          | size of grid segments, y axis                           | int                  | 30        |
+------------------+---------------------------------------------------------+----------------------+-----------+
| aux_b_z          | size of grid segments, z axis                           | int                  | 30        |
+------------------+---------------------------------------------------------+----------------------+-----------+
| color_shift      | ?                                                       | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| rotate_vec_x     | reserved - unit vector calculated from rotate_x/y/z     | float                | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| rotate_vec_y     | reserved - unit vector calculated from rotate_x/y/z     | float                | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| rotate_vec_z     | reserved - unit vector calculated from rotate_x/y/z     | float                | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| rotate_vec_s     | reserved - unit vector calculated from rotate_x/y/z     | float                | 1         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| scale_x          | 1.0 for no scaling, negative value inverts geometry     | float                | 1         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| scale_y          | 1.0 for no scaling, negative value inverts geometry     | float                | 1         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| scale_z          | 1.0 for no scaling, negative value inverts geometry     | float                | 1         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| translate_x      | longitude, relative to parent coordinate system         | float                | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| translate_y      | atitude, relative to parent coordinate system           | float                | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| translate_z      | altitude, relative to parent coordinate system          | float                | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| tag_offset_x     | ?                                                       | float                | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| tag_offset_y     | ?                                                       | float                | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| tag_offset_z     | ?                                                       | float                | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| rotate_rate_x    | angular velocity rate applied per cycle                 | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| rotate_rate_y    | angular velocity rate applied per cycle                 | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| rotate_rate_z    | angular velocity rate applied per cycle                 | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| rotate_x         | heading, 0 to 360 deg                                   | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| rotate_y         | tilt, 0 to 180 deg                                      | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| rotate_z         | roll, -180 to 180                                       | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| scale_rate_x     | scaling rate applied per cycle                          | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| scale_rate_y     | scaling rate applied per cycle                          | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| scale_rate_z     | scaling rate applied per cycle                          | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| translate_rate_x | velocity rate applied per cycle                         | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| translate_rate_y | velocity rate applied per cycle                         | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| translate_rate_z | velocity rate applied per cycle                         | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| translate_vec_x  | reserved                                                | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| translate_vec_y  | reserved                                                | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| translate_vec_z  | reserved                                                | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| shader           | shader type: 1: Wire / 2: Flat/ 3: Gouraud/ 4:          | int                  | 0         |
|                  | Phong/ 5: Reflection/ 6: Raytrace                       |                      |           |
+------------------+---------------------------------------------------------+----------------------+-----------+
| geometry         | primitive type - the shape visible                      | int                  | 7         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| line_width       | line width used for wireframes and line plots           | int                  | 1         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| point_size       | vertex point size used for plots                        | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| ratio            | ratio effects geometry such as inner radius of a torus  | int                  | 0.1       |
+------------------+---------------------------------------------------------+----------------------+-----------+
| color_id         | color index from color palette                          | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| color_r          | 8bit RGBA color value                                   | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| color_g          | 8bit RGBA color value                                   | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| color_b          | 8bit RGBA color value                                   | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| color_a          | 8bit RGBA color value                                   | int                  | 255       |
+------------------+---------------------------------------------------------+----------------------+-----------+
| color_fade       | fades older data points over time                       | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| texture_id       | texture map ID, none-0, starts at 1, 2, 3, …n           | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| hide             | hides the plot if set to 1                              | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| freeze           | freezes the plot if set to 1                            | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| topo             | topology type …uses KML coordinates                     | int                  | 3         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| facet            | facet node belongs to, such as which side of a cube     | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| auto_zoom_x      | auto-zooms plots to keep in bounds of the screen        | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| auto_zoom_y      | auto-zooms plots to keep in bounds of the screen        | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| auto_zoom_z      | auto-zooms plots to keep in bounds of the screen        | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| trigger_hi_x     | if 1 then turn on upper limit                           | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| trigger_hi_y     | if 1 then turn on upper limit                           | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| trigger_hi_z     | if 1 then turn on upper limit                           | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| trigger_lo_x     | if 1 then turn on lower limit                           | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| trigger_lo_y     | if 1 then turn on lower limit                           | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| trigger_lo_z     | if 1 then turn on lower limit                           | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| set_hi_x         | upper limit                                             | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| set_hi_y         | upper limit                                             | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| set_hi_z         | upper limit                                             | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| set_lo_x         | lower limit                                             | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| set_lo_y         | lower limit                                             | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| set_lo_z         | lower limit                                             | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| proximity_x      | reserved for future proximity and collision detection   | float                | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| proximity_y      | reserved for future proximity and collision detection   | float                | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| proximity_z      | reserved for future proximity and collision detection   | float                | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| proximity_mode_x | reserved for future proximity and collision detection   | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| proximity_mode_y | reserved for future proximity and collision detection   | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| proximity_mode_z | reserved for future proximity and collision detection   | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| segments_x       | number of segments, 0 for none                          | int                  | 20        |
+------------------+---------------------------------------------------------+----------------------+-----------+
| segments_y       | number of segments, 0 for none                          | int                  | 12        |
+------------------+---------------------------------------------------------+----------------------+-----------+
| segments_z       | number of segments, 0 for none                          | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| tag_mode         | type of tag (color, font , size)                        | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| format_id        | draw the label by id                                    | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| table_id         | table id maps external DB used by record id and format  | int                  | 0         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| record_id        | record id is external source DB record key              | int                  | 8         |
+------------------+---------------------------------------------------------+----------------------+-----------+
| size             | size in bytes of memory used per node                   | int                  | 420       |
+------------------+---------------------------------------------------------+----------------------+-----------+
| tag_text         | tag associated with this node object                    | str                  | ""        |
+------------------+---------------------------------------------------------+----------------------+-----------+

