class NodeFileRow:

    def __init__(self, comma_string):
        """
        :param comma_string: a string with 94 comma seperated values in the order of an antz node file
        """
        self.properties = NodeRowProperties()
        values = comma_string.split(",")
        if len(values) != 94:
            print("Values length = " + str(len(values)))
            print(comma_string)
            raise RuntimeError("Comma separated string has incorrect number of values")

        self.set_properties_from_string_list(values)

    def set_properties_from_string_list(self, values):
        self.properties.id = int(float(values[0]))
        self.properties._type = int(float(values[1]))
        self.properties.data = int(float(values[2]))
        self.properties.selected = int(float(values[3]))
        self.properties.parent_id = int(float(values[4]))
        self.properties.branch_level = int(float(values[5]))
        self.properties.child_id = int(float(values[6]))
        self.properties.child_index = int(float(values[7]))
        self.properties.palette_id = int(float(values[8]))
        self.properties.ch_input_id = int(float(values[9]))
        self.properties.ch_output_id = int(float(values[10]))
        self.properties.ch_last_updated = int(float(values[11]))
        self.properties.average = int(float(values[12]))
        self.properties.samples = int(float(values[13]))
        self.properties.aux_a_x = int(float(values[14]))
        self.properties.aux_a_y = int(float(values[15]))
        self.properties.aux_a_z = int(float(values[16]))
        self.properties.aux_b_x = int(float(values[17]))
        self.properties.aux_b_y = int(float(values[18]))
        self.properties.aux_b_z = int(float(values[19]))
        self.properties.color_shift = int(float(values[20]))
        self.properties.rotate_vec_x = float(values[21])
        self.properties.rotate_vec_y = float(values[22])
        self.properties.rotate_vec_z = float(values[23])
        self.properties.rotate_vec_s = float(values[24])
        self.properties.scale_x = float(values[25])
        self.properties.scale_y = float(values[26])
        self.properties.scale_z = float(values[27])
        self.properties.translate_x = float(values[28])
        self.properties.translate_y = float(values[29])
        self.properties.translate_z = float(values[30])
        self.properties.tag_offset_x = float(values[31])
        self.properties.tag_offset_y = float(values[32])
        self.properties.tag_offset_z = float(values[33])
        self.properties.rotate_rate_x = int(float(values[34]))
        self.properties.rotate_rate_y = int(float(values[35]))
        self.properties.rotate_rate_z = int(float(values[36]))
        self.properties.rotate_x = float(values[37])
        self.properties.rotate_y = float(values[38])
        self.properties.rotate_z = float(values[39])
        self.properties.scale_rate_x = int(float(values[40]))
        self.properties.scale_rate_y = int(float(values[41]))
        self.properties.scale_rate_z = int(float(values[42]))
        self.properties.translate_rate_x = int(float(values[43]))
        self.properties.translate_rate_y = int(float(values[44]))
        self.properties.translate_rate_z = int(float(values[45]))
        self.properties.translate_vec_x = int(float(values[46]))
        self.properties.translate_vec_y = int(float(values[47]))
        self.properties.translate_vec_z = int(float(values[48]))
        self.properties.shader = int(float(values[49]))
        self.properties.geometry = int(float(values[50]))
        self.properties.line_width = int(float(values[51]))
        self.properties.point_size = int(float(values[52]))
        self.properties.ratio = float(values[53])
        self.properties.color_index = int(float(values[54]))
        self.properties.color_r = int(float(values[55]))
        self.properties.color_g = int(float(values[56]))
        self.properties.color_b = int(float(values[57]))
        self.properties.color_a = int(float(values[58]))
        self.properties.color_fade = int(float(values[59]))
        self.properties.texture_id = int(float(values[60]))
        self.properties.hide = int(float(values[61]))
        self.properties.freeze = int(float(values[62]))
        self.properties.topo = int(float(values[63]))
        self.properties.facet = int(float(values[64]))
        self.properties.auto_zoom_x = int(float(values[65]))
        self.properties.auto_zoom_y = int(float(values[66]))
        self.properties.auto_zoom_z = int(float(values[67]))
        self.properties.trigger_hi_x = int(float(values[68]))
        self.properties.trigger_hi_y = int(float(values[69]))
        self.properties.trigger_hi_z = int(float(values[70]))
        self.properties.trigger_lo_x = int(float(values[71]))
        self.properties.trigger_lo_y = int(float(values[72]))
        self.properties.trigger_lo_z = int(float(values[73]))
        self.properties.set_hi_x = int(float(values[74]))
        self.properties.set_hi_y = int(float(values[75]))
        self.properties.set_hi_z = int(float(values[76]))
        self.properties.set_lo_x = int(float(values[77]))
        self.properties.set_lo_y = int(float(values[78]))
        self.properties.set_lo_z = int(float(values[79]))
        self.properties.proximity_x = float(values[80])
        self.properties.proximity_y = float(values[81])
        self.properties.proximity_z = float(values[82])
        self.properties.proximity_mode_x = int(float(values[83]))
        self.properties.proximity_mode_y = int(float(values[84]))
        self.properties.proximity_mode_z = int(float(values[85]))
        self.properties.segments_x = int(float(values[86]))
        self.properties.segments_y = int(float(values[87]))
        self.properties.segments_z = int(float(values[88]))
        self.properties.tag_mode = int(float(values[89]))
        self.properties.format_id = int(float(values[90]))
        self.properties.table_id = int(float(values[91]))
        self.properties.record_id = int(float(values[92]))
        self.properties.size = int(float(values[93]))


class NodeRowProperties:
    """ Container of properties and property setters for node file rows."""

    # region properties

    id = 7  # node ID used for pin tree relationship graph
    _type = 5  # node type - 1: Camera; 2: video; 3: Surface; 4: Points, 5:Pin, 6:Grid
    data = 0  # additional node specific type, defined by node type

    # selection set status, 1 if part of active set, 0 if not
    # // Useful if you want the root nodes selected upon loading.
    selected = 0

    parent_id = 0  # ID of parent node
    branch_level = 0  # root node is 0, each sub-level is 1, 2, 3, … n
    child_id = 0  # same as node ID
    child_index = 0  # currently selected child node

    # hard coded palettes.
    # 0: distinct set of 20 original colors/
    # 1: same as 0 but inverted/
    # 2: Rainbow Heatmap a composite of gradients/
    # 3 Rainbow Heatmap inverted/
    # 4-25 are gradients with 256 color_id's each (0-256)
    # odd palette_id's are inverted of their mirrors - even numbered pallete_id's
    palette_id = 0

    ch_input_id = 0  # channel number
    ch_output_id = 0  # channel number
    ch_last_updated = 0  # previous data update time-stamp (last read)
    average = 0  # type of averaging applied to channel data
    samples = 0  # number of samples to average

    aux_a_x = 30  # size of grid segments, x axis (30 is default)
    aux_a_y = 30  # size of grid segments, y axis (30 is default)
    aux_a_z = 30  # size of grid segments, z axis (30 is default)

    aux_b_x = 30  # size of grid segments, x axis (30 is default)
    aux_b_y = 30  # size of grid segments, y axis (30 is default)
    aux_b_z = 30  # size of grid segments, z axis (30 is default)

    color_shift = 0  # ?

    # reserved - unit vector calculated from rotate_x/y/z
    rotate_vec_x = 0
    rotate_vec_y = 0
    rotate_vec_z = 0
    rotate_vec_s = 1

    # 1.0 for no scaling, negative value inverts geometry
    scale_x = 1
    scale_y = 1
    scale_z = 1

    translate_x = 0  # longitude, relative to parent coordinate system
    translate_y = 0  # latitude, relative to parent coordinate system
    translate_z = 0  # altitude, relative to parent coordinate system

    # ?
    tag_offset_x = 0
    tag_offset_y = 0
    tag_offset_z = 0

    # angular velocity rate applied per cycle
    rotate_rate_x = 0
    rotate_rate_y = 0
    rotate_rate_z = 0

    rotate_x = 0  # heading, 0 to 360 deg
    rotate_y = 0  # tilt, 0 to 180 deg
    rotate_z = 0  # roll, -180 to 180

    # scaling rate applied per cycle
    scale_rate_x = 0
    scale_rate_y = 0
    scale_rate_z = 0

    # velocity rate applied per cycle
    translate_rate_x = 0
    translate_rate_y = 0
    translate_rate_z = 0

    # reserved
    translate_vec_x = 0
    translate_vec_y = 0
    translate_vec_z = 0

    shader = 0  # shader type: 1: Wire / 2: Flat/ 3: Gouraud/ 4: Phong/ 5: Reflection/ 6: Raytrace
    geometry = 7  # primitive type - the shape visible
    line_width = 1  # line width used for wireframes and line plots
    point_size = 0  # vertex point size used for plots
    ratio = 0.1  # ratio effects geometry such as inner radius of a torus
    color_id = 0  # color index from color palette

    # 8bit RGBA color value
    color_r = 0
    color_g = 0
    color_b = 0
    color_a = 255

    color_fade = 0  # fades older data points over time
    texture_id = 0  # texture map ID, none-0, starts at 1, 2, 3, …n
    hide = 0  # hides the plot if set to 1
    freeze = 0  # freezes the plot if set to 1
    topo = 3  # topology type …uses KML coordinates
    facet = 0  # facet node belongs to, such as which side of a cube

    # auto-zooms plots to keep in bounds of the screen
    auto_zoom_x = 0
    auto_zoom_y = 0
    auto_zoom_z = 0

    # if 1 then turn on upper limit
    trigger_hi_x = 0
    trigger_hi_y = 0
    trigger_hi_z = 0

    # if 1 then turn on lower limit
    trigger_lo_x = 0
    trigger_lo_y = 0
    trigger_lo_z = 0

    # upper limit
    set_hi_x = 0
    set_hi_y = 0
    set_hi_z = 0

    # lower limit
    set_lo_x = 0
    set_lo_y = 0
    set_lo_z = 0

    # reserved for future proximity and collision detection
    proximity_x = 0
    proximity_y = 0
    proximity_z = 0

    # reserved for future proximity and collision detection
    proximity_mode_x = 0
    proximity_mode_y = 0
    proximity_mode_z = 0

    # number of segments, 0 for none, grid default is 12
    segments_x = 20
    segments_y = 12
    segments_z = 0

    tag_mode = 0  # ?
    format_id = 0  # draw the label by id
    table_id = 0  # table id maps external DB used by record id and format
    record_id = 0  # record id is external source DB record key
    size = 420  # size in bytes of memory used per node

    tag_text = ""

    # endregion

    def print_properties(self):
        print("id: " + str(self.id))
        print("type: " + str(self._type))
        print("data: " + str(self.data))
        print("selected: " + str(self.selected))
        print("parent_id: " + str(self.parent_id))
        print("branch_level: " + str(self.branch_level))
        print("child_id: " + str(self.child_id))
        print("child_index: " + str(self.child_index))
        print("pallette_id: " + str(self.palette_id))
        print("ch_input_id: " + str(self.ch_input_id))
        print("ch_output_id: " + str(self.ch_output_id))
        print("ch_last_updated: " + str(self.ch_last_updated))
        print("average: " + str(self.average))
        print("samples: " + str(self.samples))
        print("aux_a_x: " + str(self.aux_a_x))
        print("aux_a_y: " + str(self.aux_a_y))
        print("aux_a_z: " + str(self.aux_a_z))
        print("aux_b_x: " + str(self.aux_b_y))
        print("aux_b_y: " + str(self.aux_b_z))
        print("aux_b_z: " + str(self.aux_b_x))
        print("color_shift: " + str(self.color_shift))
        print("rotate_vec_x: " + str(self.rotate_vec_x))
        print("rotate_vec_y: " + str(self.rotate_vec_y))
        print("rotate_vec_z: " + str(self.rotate_vec_z))
        print("rotate_vec_s: " + str(self.rotate_vec_s))
        print("rotate_scale_x: " + str(self.scale_x))
        print("rotate_scale_y: " + str(self.scale_y))
        print("rotate_scale_z: " + str(self.scale_z))
        print("translate_x: " + str(self.translate_x))
        print("translate_y: " + str(self.translate_y))
        print("translate_z: " + str(self.translate_z))
        print("tag_offset_x: " + str(self.tag_offset_x))
        print("tag_offsett_y: " + str(self.tag_offset_y))
        print("tag_offsett_z: " + str(self.tag_offset_z))
        print("rotate_rate_x: " + str(self.rotate_rate_x))
        print("rotate_rate_y: " + str(self.rotate_rate_y))
        print("rotate_rate_z: " + str(self.rotate_rate_z))
        print("rotate_x: " + str(self.rotate_x))
        print("rotate_y: " + str(self.rotate_y))
        print("rotate_z: " + str(self.rotate_z))
        print("scale_rate_x: " + str(self.scale_rate_x))
        print("scale_rate_y: " + str(self.scale_rate_y))
        print("scale_rate_z: " + str(self.scale_rate_z))
        print("translate_rate_x: " + str(self.translate_rate_x))
        print("translate_rate_y: " + str(self.translate_rate_y))
        print("translate_rate_z: " + str(self.translate_rate_z))
        print("translate_vec_x: " + str(self.translate_vec_x))
        print("translate_vec_y: " + str(self.translate_vec_y))
        print("translate_vec_z: " + str(self.translate_vec_z))
        print("shader: " + str(self.shader))
        print("geomotry: " + str(self.geometry))
        print("line_width: " + str(self.line_width))
        print("point_size: " + str(self.point_size))
        print("ratio: " + str(self.ratio))
        print("color_id: " + str(self.color_id))
        print("color_r: " + str(self.color_r))
        print("color_g: " + str(self.color_g))
        print("color_b: " + str(self.color_b))
        print("color_a: " + str(self.color_a))
        print("color_fade: " + str(self.color_fade))
        print("texture_id: " + str(self.texture_id))
        print("hide: " + str(self.hide))
        print("freeze: " + str(self.freeze))
        print("topo: " + str(self.topo))
        print("facet: " + str(self.facet))
        print("auto_zoom_x: " + str(self.auto_zoom_x))
        print("auto_zoom_y: " + str(self.auto_zoom_y))
        print("auto_zoom_z: " + str(self.auto_zoom_z))
        print("trigger_hi_x: " + str(self.trigger_hi_x))
        print("trigger_hi_y: " + str(self.trigger_hi_y))
        print("trigger_hi_z: " + str(self.trigger_hi_z))
        print("trigger_lo_x: " + str(self.trigger_lo_x))
        print("trigger_lo_y: " + str(self.trigger_lo_y))
        print("trigger_lo_z: " + str(self.trigger_lo_z))
        print("set_hi_x: " + str(self.set_hi_x))
        print("set_hi_y: " + str(self.set_hi_y))
        print("set_hi_z: " + str(self.set_hi_z))
        print("set_low_x: " + str(self.set_lo_x))
        print("set_low_y: " + str(self.set_lo_y))
        print("set_low_z: " + str(self.set_lo_z))
        print("proximity_x: " + str(self.proximity_x))
        print("proximity_y: " + str(self.proximity_y))
        print("proximity_z: " + str(self.proximity_z))
        print("proximity_mode_x: " + str(self.proximity_mode_x))
        print("proximity_mode_y: " + str(self.proximity_mode_y))
        print("proximity_mode_z: " + str(self.proximity_mode_z))
        print("segments_x: " + str(self.segments_x))
        print("segments_y: " + str(self.segments_y))
        print("segments_z: " + str(self.segments_z))
        print("tag_mode: " + str(self.tag_mode))
        print("format_id: " + str(self.format_id))
        print("table_id: " + str(self.table_id))
        print("record_id: " + str(self.record_id))
        print("size: " + str(self.size))

    def to_string(self):
        """ Returns a string of all node properties seperated by commas """
        return str(self.id) + "," + \
               str(self._type) + "," + \
               str(self.data) + "," + \
               str(self.selected) + "," + \
               str(self.parent_id) + "," + \
               str(self.branch_level) + "," + \
               str(self.child_id) + "," + \
               str(self.child_index) + "," + \
               str(self.palette_id) + "," + \
               str(self.ch_input_id) + "," + \
               str(self.ch_output_id) + "," + \
               str(self.ch_last_updated) + "," + \
               str(self.average) + "," + \
               str(self.samples) + "," + \
               str(self.aux_a_x) + "," + \
               str(self.aux_a_y) + "," + \
               str(self.aux_a_z) + "," + \
               str(self.aux_b_x) + "," + \
               str(self.aux_b_y) + "," + \
               str(self.aux_b_z) + "," + \
               str(self.color_shift) + "," + \
               str(self.rotate_vec_x) + "," + \
               str(self.rotate_vec_y) + "," + \
               str(self.rotate_vec_z) + "," + \
               str(self.rotate_vec_s) + "," + \
               str(self.scale_x) + "," + \
               str(self.scale_y) + "," + \
               str(self.scale_z) + "," + \
               str(self.translate_x) + "," + \
               str(self.translate_y) + "," + \
               str(self.translate_z) + "," + \
               str(self.tag_offset_x) + "," + \
               str(self.tag_offset_y) + "," + \
               str(self.tag_offset_z) + "," + \
               str(self.rotate_rate_x) + "," + \
               str(self.rotate_rate_y) + "," + \
               str(self.rotate_rate_z) + "," + \
               str(self.rotate_x) + "," + \
               str(self.rotate_y) + "," + \
               str(self.rotate_z) + "," + \
               str(self.scale_rate_x) + "," + \
               str(self.scale_rate_y) + "," + \
               str(self.scale_rate_z) + "," + \
               str(self.translate_rate_x) + "," + \
               str(self.translate_rate_y) + "," + \
               str(self.translate_rate_z) + "," + \
               str(self.translate_vec_x) + "," + \
               str(self.translate_vec_y) + "," + \
               str(self.translate_vec_z) + "," + \
               str(self.shader) + "," + \
               str(self.geometry) + "," + \
               str(self.line_width) + "," + \
               str(self.point_size) + "," + \
               str(self.ratio) + "," + \
               str(self.color_id) + "," + \
               str(self.color_r) + "," + \
               str(self.color_g) + "," + \
               str(self.color_b) + "," + \
               str(self.color_a) + "," + \
               str(self.color_fade) + "," + \
               str(self.texture_id) + "," + \
               str(self.hide) + "," + \
               str(self.freeze) + "," + \
               str(self.topo) + "," + \
               str(self.facet) + "," + \
               str(self.auto_zoom_x) + "," + \
               str(self.auto_zoom_y) + "," + \
               str(self.auto_zoom_z) + "," + \
               str(self.trigger_hi_x) + "," + \
               str(self.trigger_hi_y) + "," + \
               str(self.trigger_hi_z) + "," + \
               str(self.trigger_lo_x) + "," + \
               str(self.trigger_lo_y) + "," + \
               str(self.trigger_lo_z) + "," + \
               str(self.set_hi_x) + "," + \
               str(self.set_hi_y) + "," + \
               str(self.set_hi_z) + "," + \
               str(self.set_lo_x) + "," + \
               str(self.set_lo_y) + "," + \
               str(self.set_lo_z) + "," + \
               str(self.proximity_x) + "," + \
               str(self.proximity_y) + "," + \
               str(self.proximity_z) + "," + \
               str(self.proximity_mode_x) + "," + \
               str(self.proximity_mode_y) + "," + \
               str(self.proximity_mode_z) + "," + \
               str(self.segments_x) + "," + \
               str(self.segments_y) + "," + \
               str(self.segments_z) + "," + \
               str(self.tag_mode) + "," + \
               str(self.format_id) + "," + \
               str(self.table_id) + "," + \
               str(self.record_id) + "," + \
               str(self.size) + "\n"

    # region setters for x, y , z properties

    def set_id(self, row_id):
        """ Sets id, record_id, and data to row_id """
        self.id = row_id
        self.record_id = row_id
        self.data = row_id

    def set_tag(self, tag_text="", tag_mode=0):
        """
        Sets tag_text and tag_mode
        :param tag_text: (default "")
        :param tag_mode: (default 0)
        :return: None
        """
        self.tag_text = tag_text
        self.tag_mode = tag_mode

    def set_aux_a(self, x=30, y=30, z=30):
        """
        Sets aux_a_x, y, and z

        :param x: (default 30)
        :param y: (default 30)
        :param z: (default 30)
        :return: None
        """
        self.aux_a_x = x
        self.aux_a_y = y
        self.aux_a_z = z

    def set_aux_b(self, x=30, y=30, z=30):
        """
        Sets aux_b_x,y, and z

        :param x: (default 30)
        :param y: (default 30)
        :param z: (default 30)
        :return: None
        """
        self.aux_b_x = x
        self.aux_b_y = y
        self.aux_b_z = z

    def rotate_vec(self, x=0, y=0, z=0, s=0):
        """
        Sets rotate_vec_x, y, z, and s
        :param x: (default 0)
        :param y: (default 0)
        :param z: (default 0)
        :param s: (default 0)
        :return: None
        """
        self.rotate_vec_x = x
        self.rotate_vec_y = y
        self.rotate_vec_z = z
        self.rotate_vec_s = s

    def set_scale(self, x=1, y=1, z=1):
        """
        Sets scale_x, y, z
        :param x: (default 1)
        :param y: (default 1)
        :param z: (default 1)
        :return: None
        """
        self.scale_x = x
        self.scale_y = y
        self.scale_z = z

    def set_translate(self, x=0, y=0, z=0):
        """
        Sets translate_x, y, z
        :param x: (default 0)
        :param y: (default 0)
        :param z: (default 0)
        :return: None
        """
        self.translate_x = x
        self.translate_y = y
        self.translate_z = z

    def set_tag_offset(self, x=0, y=0, z=0):
        """
        Sets tag_offset_x, y, z
        :param x: (default 0)
        :param y: (default 0)
        :param z: (default 0)
        :return: None
        """
        self.tag_offset_x = x
        self.tag_offset_y = y
        self.tag_offset_z = z

    def set_rotate(self, x=0, y=0, z=0):
        """
        Sets rotate_x, y, z
        :param x: (default 0)
        :param y: (default 0)
        :param z: (default 0)
        :return: None
        """
        self.rotate_x = x
        self.rotate_y = y
        self.rotate_z = z

    def set_rotate_rate(self, x=0, y=0, z=0):
        """
        Sets rotate_rate_x, y, z
        :param x: (default 0)
        :param y: (default 0)
        :param z: (default 0)
        :return: None
        """
        self.rotate_rate_x = x
        self.rotate_rate_y = y
        self.rotate_rate_z = z

    def set_scale_rate(self, x=0, y=0, z=0):
        """
        Sets scale_rate_x, y, z
        :param x: (default 0)
        :param y: (default 0)
        :param z: (default 0)
        :return: None
        """
        self.scale_rate_x = x
        self.scale_rate_y = y
        self.scale_rate_z = z

    def set_translate_rate(self, x=0, y=0, z=0):
        """
        Sets translate_rate_x, y, z
        :param x: (default 0)
        :param y: (default 0)
        :param z: (default 0)
        :return: None
        """
        self.translate_rate_x = x
        self.translate_rate_y = y
        self.translate_rate_z = z

    def set_translate_vec(self, x=0, y=0, z=0):
        """
        Sets translate_vec_x, y, z
        :param x: (default 0)
        :param y: (default 0)
        :param z: (default 0)
        :return: None
        """
        self.translate_vec_x = x
        self.translate_vec_y = y
        self.translate_vec_z = z

    def set_color(self, r=0, g=0, b=0, a=255):
        """
        Sets color values
        :param r: red (int) 0-255 (default 0)
        :param g: green (int) 0-255 (default 0)
        :param b: blue (int) 0-255 (default 0)
        :param a: transparency 0-255 (default 255)
        :return: None
        """
        self.color_r = r
        self.color_g = g
        self.color_b = b
        self.color_a = a

    def set_auto_zoom(self, x=0, y=0, z=0):
        """
        Sets auto_zoom_x, y, z
        :param x: (default 0)
        :param y: (default 0)
        :param z: (default 0)
        :return: None
        """
        self.auto_zoom_x = x
        self.auto_zoom_y = y
        self.auto_zoom_z = z

    def set_trigger_hi(self, x=0, y=0, z=0):
        """
        Sets trigger_hi_x, y, z
        :param x: (default 0)
        :param y: (default 0)
        :param z: (default 0)
        :return: None
        """
        self.trigger_hi_x = x
        self.trigger_hi_y = y
        self.trigger_hi_z = z

    def set_trigger_lo(self, x=0, y=0, z=0):
        """
        Sets trigger_low_x, y, z
        :param x: (default 0)
        :param y: (default 0)
        :param z: (default 0)
        :return: None
        """
        self.trigger_lo_x = x
        self.trigger_lo_y = y
        self.trigger_lo_z = z

    def set_hi(self, x=0, y=0, z=0):
        """
        Sets hi_x, y, z
        :param x: (default 0)
        :param y: (default 0)
        :param z: (default 0)
        :return: None
        """
        self.set_hi_x = x
        self.set_hi_y = y
        self.set_hi_z = z

    def set_lo(self, x=0, y=0, z=0):
        """
        Sets lo_x, y, z
        :param x: (default 0)
        :param y: (default 0)
        :param z: (default 0)
        :return: None
        """
        self.set_lo_x = x
        self.set_lo_y = y
        self.set_lo_z = z

    def set_proximity(self, x=0, y=0, z=0):
        """
        Sets proximity_x, y, z
        :param x: (default 0)
        :param y: (default 0)
        :param z: (default 0)
        :return: None
        """
        self.proximity_x = x
        self.proximity_y = y
        self.proximity_z = z

    def proximity_mode(self, x=0, y=0, z=0):
        """
        Sets proximity_mode_x, y, z
        :param x: (default 0)
        :param y: (default 0)
        :param z: (default 0)
        :return: None
        """
        self.proximity_mode_x = x
        self.proximity_mode_y = y
        self.proximity_mode_z = z

    def set_segments(self, x=20, y=12, z=0):
        """
        Sets segments_x, y, z
        :param x: (default 0)
        :param y: (default 0)
        :param z: (default 0)
        :return: None
        """
        self.segments_x = x
        self.segments_y = y
        self.segments_z = z