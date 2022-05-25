from __future__ import annotations
from matritools import fronzenclass as fc
from matritools import utils as mu
from matritools import nodefileglobals as nfg

class Node(fc.FrozenClass):
	"""
	Container of properties and property setters for Nodes.

	Attributes:
		id               - node ID used for pin tree relationship graph
		type            - node type - 1: Camera; 2: video; 3: Surface;
						 - 4: Points, 5:Pin, 6:Grid, 7:Link
		data             - additional node specific type, defined by node type
		selected         - selection set status, 1 if part of active set, 0 if not
						 - Useful if you want the root nodes selected upon loading
		parent_id        - ID of parent node
		branch_level     - root node is 0, each sub-level is 1, 2, 3, … n
		child_id         - When used as to represent a link, parent_id is one
						 - end and child_id is the other.
						 - This object is a link between parent_id and child_id
		child_index      - currently selected child node
		pallete_id       - hard coded palettes.
						 - 0: distinct set of 20 original colors/
						 - 1: same as 0 but inverted/
						 - 2: Rainbow Heatmap a composite of gradients/
						 - 3 Rainbow Heatmap inverted/
						 - 4-25 are gradients with 256 index's each (0-256)
						 - odd palette_id's are inverted of their mirrors -
						 - even numbered pallete_id's
		ch_input_id      - channel number
		ch_output_id     - channel number
		ch_last_updated  - previous data update time-stamp (last read)
		average          - type of averaging applied to channel data
		samples          - number of samples to average
		aux_a_x          - size of grid segments, x axis
		aux_a_y          - size of grid segments, y axis
		aux_a_z          - size of grid segments, z axis
		aux_b_x          - size of grid segments, x axis
		aux_b_y          - size of grid segments, y axis
		aux_b_z          - size of grid segments, z axis
		color_shift      - ?
		rotate_vec_x     - reserved - unit vector calculated from rotate_x/y/z
		rotate_vec_y     - reserved - unit vector calculated from rotate_x/y/z
		rotate_vec_z     - reserved - unit vector calculated from rotate_x/y/z
		rotate_vec_s     - reserved - unit vector calculated from rotate_x/y/z
		scale_x          - 1.0 for no scaling, negative value inverts geometry
		scale_y          - 1.0 for no scaling, negative value inverts geometry
		scale_z          - 1.0 for no scaling, negative value inverts geometry
		translate_x      - longitude, relative to parent coordinate system
		translate_y      - atitude, relative to parent coordinate system
		translate_z      - altitude, relative to parent coordinate system
		tag_offset_x     - ?
		tag_offset_y     - ?
		tag_offset_z     - ?
		rotate_rate_x    - angular velocity rate applied per cycle
		rotate_rate_y    - angular velocity rate applied per cycle
		rotate_rate_z    - angular velocity rate applied per cycle
		rotate_x         - heading, 0 to 360 deg
		rotate_y         - tilt, 0 to 180 deg
		rotate_z         - roll, -180 to 180
		scale_rate_x     - scaling rate applied per cycle
		scale_rate_y     - scaling rate applied per cycle
		scale_rate_z     - scaling rate applied per cycle
		translate_rate_x - velocity rate applied per cycle
		translate_rate_y - velocity rate applied per cycle
		translate_rate_z - velocity rate applied per cycle
		translate_vec_x  - reserved
		translate_vec_y  - reserved
		translate_vec_z  - reserved
		shader           - shader type: 1: Wire / 2: Flat/ 3: Gouraud/ 4:
						 - Phong/ 5: Reflection/ 6: Raytrace
		geometry         - primitive type - the shape visible
		line_width       - line width used for wireframes and line plots
		point_size       - vertex point size used for plots
		ratio            - ratio effects geometry such as inner radius of a torus
		color_id      - color index from color palette
		color_r          - 8bit RGBA color value
		color_g          - 8bit RGBA color value
		color_b          - 8bit RGBA color value
		color_a          - 8bit RGBA color value
		color_fade       - fades older data points over time
		texture_id       - texture map ID, none-0, starts at 1, 2, 3, …n
		hide             - hides the plot if set to 1
		freeze           - freezes the plot if set to 1
		topo             - topology type …uses KML coordinates
		facet            - facet node belongs to, such as which side of a cube
		auto_zoom_x      - auto-zooms plots to keep in bounds of the screen
		auto_zoom_y      - auto-zooms plots to keep in bounds of the screen
		auto_zoom_z      - auto-zooms plots to keep in bounds of the screen
		trigger_hi_x     - if 1 then turn on upper limit
		trigger_hi_y     - if 1 then turn on upper limit
		trigger_hi_z     - if 1 then turn on upper limit
		trigger_lo_x     - if 1 then turn on lower limit
		trigger_lo_y     - if 1 then turn on lower limit
		trigger_lo_z     - if 1 then turn on lower limit
		set_hi_x         - upper limit
		set_hi_y         - upper limit
		set_hi_z         - upper limit
		set_lo_x         - lower limit
		set_lo_y         - lower limit
		set_lo_z         - lower limit
		proximity_x      - reserved for future proximity and collision detection
		proximity_y      - reserved for future proximity and collision detection
		proximity_z      - reserved for future proximity and collision detection
		proximity_mode_x - reserved for future proximity and collision detection
		proximity_mode_y - reserved for future proximity and collision detection
		proximity_mode_z - reserved for future proximity and collision detection
		segments_x       - number of segments, 0 for none
		segments_y       - number of segments, 0 for none
		segments_z       - number of segments, 0 for none
		tag_mode         - type of tag (color, font , size)
		format_id        - draw the label by id
		table_id         - table id maps external DB used by record id and format
		record_id        - record id is external source DB record key
		size             - size in bytes of memory used per node
		tag_text         - tag associated with this node object
	"""
	
	def __init__(self, comma_string: str = ""):
		"""
		Parameters:
			 comma_string (str: "") - a string with 94 comma seperated values in the order of an antz node file.

		Raise:
			TypeError
			RuntimeError
		"""
		# Error checking
		mu.check_type(comma_string, str, False)
		
		# region properties
		
		self.id = 8  # node ID used for pin tree relationship graph
		self.type = 5  # node type - 1: Camera; 2: video; 3: Surface; 4: Points, 5:Pin, 6:Grid
		self.data = 8  # node type - 1: Camera; 2: video; 3: Surface; 4: Points, 5:Pin, 6:Grid
		
		# selection set status, 1 if part of active set, 0 if not
		# Useful if you want the root nodes selected upon loading.
		self.selected = 0
		
		self.parent_id = 0  # ID of parent node
		self.branch_level = 1  # root node is 0, each sub-level is 1, 2, 3, … n
		self.child_id = 0  # same as node ID
		self.child_index = 0  # currently selected child node
		
		# hard coded palettes.
		# 0: distinct set of 20 original colors/
		# 1: same as 0 but inverted/
		# 2: Rainbow Heatmap a composite of gradients/
		# 3 Rainbow Heatmap inverted/
		# 4-25 are gradients with 256 index's each (0-256)
		# odd palette_id's are inverted of their mirrors - even numbered pallete_id's
		self.palette_id = 0
		
		self.ch_input_id = 0  # channel number
		self.ch_output_id = 0  # channel number
		self.ch_last_updated = 0  # previous data update time-stamp (last read)
		self.average = 0  # type of averaging applied to channel data
		self.samples = 0  # number of samples to average
		
		self.aux_a_x = 30  # size of grid segments, x axis (30 is default)
		self.aux_a_y = 30  # size of grid segments, y axis (30 is default)
		self.aux_a_z = 30  # size of grid segments, z axis (30 is default)
		
		self.aux_b_x = 30  # size of grid segments, x axis (30 is default)
		self.aux_b_y = 30  # size of grid segments, y axis (30 is default)
		self.aux_b_z = 30  # size of grid segments, z axis (30 is default)
		
		self.color_shift = 0  # ?
		
		# reserved - unit vector calculated from rotate_x/y/z
		self.rotate_vec_x = 0
		self.rotate_vec_y = 0
		self.rotate_vec_z = 0
		self.rotate_vec_s = 1
		
		# 1.0 for no scaling, negative value inverts geometry
		self.scale_x = 1
		self.scale_y = 1
		self.scale_z = 1
		
		self.translate_x = 0  # longitude, relative to parent coordinate system
		self.translate_y = 0  # latitude, relative to parent coordinate system
		self.translate_z = 0  # altitude, relative to parent coordinate system
		
		# ?
		self.tag_offset_x = 0
		self.tag_offset_y = 0
		self.tag_offset_z = 0
		
		# angular velocity rate applied per cycle
		self.rotate_rate_x = 0
		self.rotate_rate_y = 0
		self.rotate_rate_z = 0
		
		self.rotate_x = 0  # heading, 0 to 360 deg
		self.rotate_y = 0  # tilt, 0 to 180 deg
		self.rotate_z = 0  # roll, -180 to 180
		
		# scaling rate applied per cycle
		self.scale_rate_x = 0
		self.scale_rate_y = 0
		self.scale_rate_z = 0
		
		# velocity rate applied per cycle
		self.translate_rate_x = 0
		self.translate_rate_y = 0
		self.translate_rate_z = 0
		
		# reserved
		self.translate_vec_x = 0
		self.translate_vec_y = 0
		self.translate_vec_z = 0
		
		self.shader = 0  # shader type: 1: Wire / 2: Flat/ 3: Gouraud/ 4: Phong/ 5: Reflection/ 6: Raytrace
		self.geometry = 7  # primitive type - the shape visible
		self.line_width = 1  # line width used for wireframes and line plots
		self.point_size = 0  # vertex point size used for plots
		self.ratio = 0.1  # ratio effects geometry such as inner radius of a torus
		self.color_id = 0  # color index from color palette
		
		# 8bit RGBA color value
		self.color_r = 0
		self.color_g = 0
		self.color_b = 0
		self.color_a = 255
		
		self.color_fade = 0  # fades older data points over time
		self.texture_id = 0  # texture map ID, none-0, starts at 1, 2, 3, …n
		self.hide = 0  # hides the plot if set to 1
		self.freeze = 0  # freezes the plot if set to 1
		self.topo = 3  # topology type …uses KML coordinates
		self.facet = 0  # facet node belongs to, such as which side of a cube
		
		# auto-zooms plots to keep in bounds of the screen
		self.auto_zoom_x = 0
		self.auto_zoom_y = 0
		self.auto_zoom_z = 0
		
		# if 1 then turn on upper limit
		self.trigger_hi_x = 0
		self.trigger_hi_y = 0
		self.trigger_hi_z = 0
		
		# if 1 then turn on lower limit
		self.trigger_lo_x = 0
		self.trigger_lo_y = 0
		self.trigger_lo_z = 0
		
		# upper limit
		self.set_hi_x = 0
		self.set_hi_y = 0
		self.set_hi_z = 0
		
		# lower limit
		self.set_lo_x = 0
		self.set_lo_y = 0
		self.set_lo_z = 0
		
		# reserved for future proximity and collision detection
		self.proximity_x = 0
		self.proximity_y = 0
		self.proximity_z = 0
		
		# reserved for future proximity and collision detection
		self.proximity_mode_x = 0
		self.proximity_mode_y = 0
		self.proximity_mode_z = 0
		
		# number of segments, 0 for none, grid default is 12
		self.segments_x = 20
		self.segments_y = 12
		self.segments_z = 0
		
		self.tag_mode = 0  # type of tag (color, font , size)
		self.format_id = 0  # draw the label by id
		self.table_id = 0  # table id maps external DB used by record id and format
		self.record_id = 8  # record id is external source DB record key
		self.size = 420  # size in bytes of memory used per node
		
		self.tag_text = ""
		
		self.__is_frozen__ = True
		
		# endregion
		
		if comma_string == "":
			return
		
		values = comma_string.split(",")
		self.set_properties_from_string_list(values)
	
	def set_properties_from_string_list(self, values: List[str]) -> Node:
		"""
		Sets the properties of this Node from a list of values in the order they appear in a node file.

		Parameters:
			values (List[str]) - list of strings that can be cast as integrals

		Returns:
			self

		Raises:
			ValueError
			RuntimeError
		"""
		# Error checking
		if len(values) != 94:
			raise RuntimeError("Comma separated string has incorrect number of values.\n Values length = " +
							   str(len(values)) + "\nInput: " + str(values))
		
		self.id = int(float(values[0]))
		self.type = int(float(values[1]))
		self.data = int(float(values[2]))
		self.selected = int(float(values[3]))
		self.parent_id = int(float(values[4]))
		self.branch_level = int(float(values[5]))
		self.child_id = int(float(values[6]))
		self.child_index = int(float(values[7]))
		self.palette_id = int(float(values[8]))
		self.ch_input_id = int(float(values[9]))
		self.ch_output_id = int(float(values[10]))
		self.ch_last_updated = int(float(values[11]))
		self.average = int(float(values[12]))
		self.samples = int(float(values[13]))
		self.aux_a_x = int(float(values[14]))
		self.aux_a_y = int(float(values[15]))
		self.aux_a_z = int(float(values[16]))
		self.aux_b_x = int(float(values[17]))
		self.aux_b_y = int(float(values[18]))
		self.aux_b_z = int(float(values[19]))
		self.color_shift = float(values[20])
		self.rotate_vec_x = float(values[21])
		self.rotate_vec_y = float(values[22])
		self.rotate_vec_z = float(values[23])
		self.rotate_vec_s = float(values[24])
		self.scale_x = float(values[25])
		self.scale_y = float(values[26])
		self.scale_z = float(values[27])
		self.translate_x = float(values[28])
		self.translate_y = float(values[29])
		self.translate_z = float(values[30])
		self.tag_offset_x = float(values[31])
		self.tag_offset_y = float(values[32])
		self.tag_offset_z = float(values[33])
		self.rotate_rate_x = float(values[34])
		self.rotate_rate_y = float(values[35])
		self.rotate_rate_z = float(values[36])
		self.rotate_x = float(values[37])
		self.rotate_y = float(values[38])
		self.rotate_z = float(values[39])
		self.scale_rate_x = float(values[40])
		self.scale_rate_y = float(values[41])
		self.scale_rate_z = float(values[42])
		self.translate_rate_x = float(values[43])
		self.translate_rate_y = float(values[44])
		self.translate_rate_z = float(values[45])
		self.translate_vec_x = float(values[46])
		self.translate_vec_y = float(values[47])
		self.translate_vec_z = float(values[48])
		self.shader = int(float(values[49]))
		self.geometry = int(float(values[50]))
		self.line_width = float(values[51])
		self.point_size = float(values[52])
		self.ratio = float(values[53])
		self.color_id = int(float(values[54]))
		self.color_r = int(float(values[55]))
		self.color_g = int(float(values[56]))
		self.color_b = int(float(values[57]))
		self.color_a = int(float(values[58]))
		self.color_fade = int(float(values[59]))
		self.texture_id = int(float(values[60]))
		self.hide = int(float(values[61]))
		self.freeze = int(float(values[62]))
		self.topo = int(float(values[63]))
		self.facet = int(float(values[64]))
		self.auto_zoom_x = int(float(values[65]))
		self.auto_zoom_y = int(float(values[66]))
		self.auto_zoom_z = int(float(values[67]))
		self.trigger_hi_x = int(float(values[68]))
		self.trigger_hi_y = int(float(values[69]))
		self.trigger_hi_z = int(float(values[70]))
		self.trigger_lo_x = int(float(values[71]))
		self.trigger_lo_y = int(float(values[72]))
		self.trigger_lo_z = int(float(values[73]))
		self.set_hi_x = float(values[74])
		self.set_hi_y = float(values[75])
		self.set_hi_z = float(values[76])
		self.set_lo_x = float(values[77])
		self.set_lo_y = float(values[78])
		self.set_lo_z = float(values[79])
		self.proximity_x = float(values[80])
		self.proximity_y = float(values[81])
		self.proximity_z = float(values[82])
		self.proximity_mode_x = int(float(values[83]))
		self.proximity_mode_y = int(float(values[84]))
		self.proximity_mode_z = int(float(values[85]))
		self.segments_x = int(float(values[86]))
		self.segments_y = int(float(values[87]))
		self.segments_z = int(float(values[88]))
		self.tag_mode = int(float(values[89]))
		self.format_id = int(float(values[90]))
		self.table_id = int(float(values[91]))
		self.record_id = int(float(values[92]))
		self.size = int(float(values[93]))
		
		return self
	
	def print_properties(self) -> Node:
		"""
		Prints the label and value of each property.

		Parameters:
			None

		Returns:
			self

		Raises:
			None
		"""
		print("id: " + str(self.id))
		print("type: " + str(self.type))
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
		print("aux_b_x: " + str(self.aux_b_x))
		print("aux_b_y: " + str(self.aux_b_y))
		print("aux_b_z: " + str(self.aux_b_z))
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
		print("tag_offset_y: " + str(self.tag_offset_y))
		print("tag_offset_z: " + str(self.tag_offset_z))
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
		
		return self
	
	def to_string(self) -> str:
		"""
		Returns a string of all node properties seperated by commas

		Parameters:
			None

		Returns:
			str

		Raises:
			None
		"""
		return str(int(float(self.id))) + "," + \
			   str(int(float(self.type))) + "," + \
			   str(int(float(self.data))) + "," + \
			   str(int(float(self.selected))) + "," + \
			   str(int(float(self.parent_id))) + "," + \
			   str(int(float(self.branch_level))) + "," + \
			   str(int(float(self.child_id))) + "," + \
			   str(int(float(self.child_index))) + "," + \
			   str(int(float(self.palette_id))) + "," + \
			   str(int(float(self.ch_input_id))) + "," + \
			   str(int(float(self.ch_output_id))) + "," + \
			   str(int(float(self.ch_last_updated))) + "," + \
			   str(int(float(self.average))) + "," + \
			   str(int(float(self.samples))) + "," + \
			   str(int(float(self.aux_a_x))) + "," + \
			   str(int(float(self.aux_a_y))) + "," + \
			   str(int(float(self.aux_a_z))) + "," + \
			   str(int(float(self.aux_b_x))) + "," + \
			   str(int(float(self.aux_b_y))) + "," + \
			   str(int(float(self.aux_b_z))) + "," + \
			   str(int(float(self.color_shift))) + "," + \
			   str(float(self.rotate_vec_x)) + "," + \
			   str(float(self.rotate_vec_y)) + "," + \
			   str(float(self.rotate_vec_z)) + "," + \
			   str(float(self.rotate_vec_s)) + "," + \
			   str(float(self.scale_x)) + "," + \
			   str(float(self.scale_y)) + "," + \
			   str(float(self.scale_z)) + "," + \
			   str(float(self.translate_x)) + "," + \
			   str(float(self.translate_y)) + "," + \
			   str(float(self.translate_z)) + "," + \
			   str(float(self.tag_offset_x)) + "," + \
			   str(float(self.tag_offset_y)) + "," + \
			   str(float(self.tag_offset_z)) + "," + \
			   str(int(float(self.rotate_rate_x))) + "," + \
			   str(int(float(self.rotate_rate_y))) + "," + \
			   str(int(float(self.rotate_rate_z))) + "," + \
			   str(float(self.rotate_x)) + "," + \
			   str(float(self.rotate_y)) + "," + \
			   str(float(self.rotate_z)) + "," + \
			   str(int(float(self.scale_rate_x))) + "," + \
			   str(int(float(self.scale_rate_y))) + "," + \
			   str(int(float(self.scale_rate_z))) + "," + \
			   str(float(self.translate_rate_x)) + "," + \
			   str(float(self.translate_rate_y)) + "," + \
			   str(float(self.translate_rate_z)) + "," + \
			   str(int(float(self.translate_vec_x))) + "," + \
			   str(int(float(self.translate_vec_y))) + "," + \
			   str(int(float(self.translate_vec_z))) + "," + \
			   str(int(float(self.shader))) + "," + \
			   str(int(float(self.geometry))) + "," + \
			   str(int(float(self.line_width))) + "," + \
			   str(int(float(self.point_size))) + "," + \
			   str(float(self.ratio)) + "," + \
			   str(int(float(self.color_id))) + "," + \
			   str(int(float(self.color_r))) + "," + \
			   str(int(float(self.color_g))) + "," + \
			   str(int(float(self.color_b))) + "," + \
			   str(int(float(self.color_a))) + "," + \
			   str(int(float(self.color_fade))) + "," + \
			   str(int(float(self.texture_id))) + "," + \
			   str(int(float(self.hide))) + "," + \
			   str(int(float(self.freeze))) + "," + \
			   str(int(float(self.topo))) + "," + \
			   str(int(float(self.facet))) + "," + \
			   str(int(float(self.auto_zoom_x))) + "," + \
			   str(int(float(self.auto_zoom_y))) + "," + \
			   str(int(float(self.auto_zoom_z))) + "," + \
			   str(int(float(self.trigger_hi_x))) + "," + \
			   str(int(float(self.trigger_hi_y))) + "," + \
			   str(int(float(self.trigger_hi_z))) + "," + \
			   str(int(float(self.trigger_lo_x))) + "," + \
			   str(int(float(self.trigger_lo_y))) + "," + \
			   str(int(float(self.trigger_lo_z))) + "," + \
			   str(float(self.set_hi_x)) + "," + \
			   str(float(self.set_hi_y)) + "," + \
			   str(float(self.set_hi_z)) + "," + \
			   str(float(self.set_lo_x)) + "," + \
			   str(float(self.set_lo_y)) + "," + \
			   str(float(self.set_lo_z)) + "," + \
			   str(float(self.proximity_x)) + "," + \
			   str(float(self.proximity_y)) + "," + \
			   str(float(self.proximity_z)) + "," + \
			   str(int(float(self.proximity_mode_x))) + "," + \
			   str(int(float(self.proximity_mode_y))) + "," + \
			   str(int(float(self.proximity_mode_z))) + "," + \
			   str(int(float(self.segments_x))) + "," + \
			   str(int(float(self.segments_y))) + "," + \
			   str(int(float(self.segments_z))) + "," + \
			   str(int(float(self.tag_mode))) + "," + \
			   str(int(float(self.format_id))) + "," + \
			   str(int(float(self.table_id))) + "," + \
			   str(int(float(self.record_id))) + "," + \
			   str(int(float(self.size))) + "\n"
	
	# region setters for x, y , z properties
	
	def set_id(self, node_id: int) -> Node:
		"""
		Sets id, record_id, and data to node_id.

		Parameters:
			node_id (int) - number to set id, record_id and node_id to

		Returns:
			self

		Raises:
			TypeError
		"""
		# Error checking
		mu.check_type(node_id, int)
		
		self.id = int(node_id)
		self.record_id = int(node_id)
		self.data = int(node_id)
		
		return self
	
	def set_tag(self, tag_text: str, tag_mode: int = 0) -> Node:
		"""
		Sets tag_text and tag_mode.

		Parameters:
			tag_text (str) - label or description of this node to appear in Antz
			tag_mode (int : 0) - mode that effects how tag is displayed in Antz

		Returns:
			self

		Raises:
			TypeError
		"""
		# Error checking
		mu.check_type(tag_text, str)
		mu.check_type(tag_mode, int)
		
		self.tag_text = str(tag_text)
		self.tag_mode = int(tag_mode)
		
		return self
	
	def set_aux_a(self, x: int = 30, y: int = 30, z: int = 30) -> Node:
		"""
		Sets aux_a_x, y, and z.

		Parameters:
			x (int: 30)
			y (int: 30)
			z (int: 30)

		Returns:
			self

		Raises:
			TypeError
		"""
		# Error checking
		mu.check_type(x, int)
		mu.check_type(y, int)
		mu.check_type(z, int)
		
		self.aux_a_x = int(x)
		self.aux_a_y = int(y)
		self.aux_a_z = int(z)
		
		return self
	
	def set_aux_b(self, x: int = 30, y: int = 30, z=30) -> Node:
		"""
		Sets aux_b_x,y, and z.

		Parameters:
			x (int: 30)
			y (int: 30)
			z (int: 30)

		Returns:
			self

		Raises:
			TypeError
		"""
		# Error checking
		mu.check_type(x, int)
		mu.check_type(y, int)
		mu.check_type(z, int)
		
		self.aux_b_x = int(x)
		self.aux_b_y = int(y)
		self.aux_b_z = int(z)
		
		return self
	
	def set_rotate_vec(self, x: int = 0, y: int = 0, z: int = 0, s: int = 0) -> Node:
		"""
		Sets rotate_vec_x, y, z, and s.

		Parameters:
			x (int: 0)
			y (int: 0)
			z (int: 0)
			s (int: 0)

		Returns:
			None

		Raises:
			TypeError
		"""
		# Error checking
		mu.check_type(x, int)
		mu.check_type(y, int)
		mu.check_type(z, int)
		mu.check_type(s, int)
		
		self.rotate_vec_x = int(x)
		self.rotate_vec_y = int(y)
		self.rotate_vec_z = int(z)
		self.rotate_vec_s = int(s)
		
		return self
	
	def set_scale(self, x: float = 1, y: float = 1, z: float = 1) -> Node:
		"""
		Sets scale_x, y, z.

		Parameters:
			x (int: 1)
			y (int: 1)
			z (int: 1)

		Returns:
			self

		Raises:
			TypeError
		"""
		# Error checking
		mu.check_type(x, float)
		mu.check_type(y, float)
		mu.check_type(z, float)
		
		self.scale_x = float(x)
		self.scale_y = float(y)
		self.scale_z = float(z)
		
		return self
	
	def set_u_scale(self, scale: float = 1) -> Node:
		"""
		Sets x, y, z scale uniformly.
		Parameters:
			scale (float : 1)

		Returns:
			self

		Raises:
			TypeError
		"""
		# Error checking
		mu.check_type(scale, float)
		self.set_scale(scale, scale, scale)
		
		return self
	
	def set_translate(self, x: float = 0, y: float = 0, z: float = 0) -> Node:
		"""
		Sets translate_x, y, z.

		Parameters:
			x (int: 0)
			y (int: 0)
			z (int: 0)

		Returns:
			self

		Raises:
			TypeError
		"""
		# Error checking
		mu.check_type(x, float)
		mu.check_type(y, float)
		mu.check_type(z, float)
		
		self.translate_x = float(x)
		self.translate_y = float(y)
		self.translate_z = float(z)
		
		return self
	
	def set_tag_offset(self, x: float = 0, y: float = 0, z: float = 0) -> Node:
		"""
		Sets tag_offset_x, y, z.

		Parameters:
			x (int: 0)
			y (int: 0)
			z (int: 0)

		Returns:
			self

		Raises:
			TypeError
		"""
		# Error checking
		mu.check_type(x, float)
		mu.check_type(y, float)
		mu.check_type(z, float)
		
		self.tag_offset_x = float(x)
		self.tag_offset_y = float(y)
		self.tag_offset_z = float(z)
		
		return self
	
	def set_rotate(self, x: float = 0, y: float = 0, z: float = 0) -> Node:
		"""
		Sets rotate_x, y, z.

		Parameters:
			x (int: 0)
			y (int: 0)
			z (int: 0)

		Returns:
			self

		Raises:
			TypeError
		"""
		# Error checking
		mu.check_type(x, float)
		mu.check_type(y, float)
		mu.check_type(z, float)
		
		self.rotate_x = float(x)
		self.rotate_y = float(y)
		self.rotate_z = float(z)
		
		return self
	
	def set_rotate_rate(self, x: int = 0, y: int = 0, z: int = 0) -> Node:
		"""
		Sets rotate_rate_x, y, z.

		Parameters:
			x (int: 0)
			y (int: 0)
			z (int: 0)

		Returns:
			self

		Raises:
			TypeError
		"""
		# Error checking
		mu.check_type(x, int)
		mu.check_type(y, int)
		mu.check_type(z, int)
		
		self.rotate_rate_x = int(x)
		self.rotate_rate_y = int(y)
		self.rotate_rate_z = int(z)
		
		return self
	
	def set_scale_rate(self, x: int = 0, y: int = 0, z: int = 0) -> Node:
		"""
		Sets scale_rate_x, y, z.

		Parameters:
			x (int: 0)
			y (int: 0)
			z (int: 0)

		Returns:
			self

		Raises:
			TypeError
		"""
		# Error checking
		mu.check_type(x, int)
		mu.check_type(y, int)
		mu.check_type(z, int)
		
		self.scale_rate_x = int(x)
		self.scale_rate_y = int(y)
		self.scale_rate_z = int(z)
		
		return self
	
	def set_translate_rate(self, x: float = 0, y: float = 0, z: float = 0) -> Node:
		"""
		Sets translate_rate_x, y, z.

		Parameters:
			x (int: 0)
			y (int: 0)
			z (int: 0)

		Returns:
			self

		Raises:
			TypeError
		"""
		# Error checking
		mu.check_type(x, float)
		mu.check_type(y, float)
		mu.check_type(z, float)
		
		self.translate_rate_x = float(x)
		self.translate_rate_y = float(y)
		self.translate_rate_z = float(z)
		
		return self
	
	def set_translate_vec(self, x: int = 0, y: int = 0, z: int = 0) -> Node:
		"""
		Sets translate_vec_x, y, z.

		Parameters:
			x (int: 0)
			y (int: 0)
			z (int: 0)

		Returns:
			self

		Raises:
			TypeError
		"""
		# Error checking
		mu.check_type(x, int)
		mu.check_type(y, int)
		mu.check_type(z, int)
		
		self.translate_vec_x = int(x)
		self.translate_vec_y = int(y)
		self.translate_vec_z = int(z)
		
		return self
	
	def set_color(self, r: int = 0, g: int = 0, b: int = 0, a: int = 255) -> Node:
		"""
		Sets color values.

		Parameters:

		r (int: 0) - red (int) 0-255 (default 0)
		g (int: 0) - green (int) 0-255 (default 0)
		b (int: 0) - blue (int) 0-255 (default 0)
		a (int: 255) - transparency 0-255 (default 255)

		Returns:
			self

		Raises:
			TypeError
		"""
		# Error checking
		mu.check_type(r, int)
		mu.check_type(g, int)
		mu.check_type(b, int)
		mu.check_type(a, int)
		
		self.color_r = int(r)
		self.color_g = int(g)
		self.color_b = int(b)
		self.color_a = int(a)
		
		return self
	
	def set_color_by_name(self, color: str, color_a: int = 255) -> Node:
		"""
		Set color with the name of a color as a string.

		Parameters:
			color: (str) name of a color i.e 'red'
			color_a (int : 255)

		Returns:
			self

		Raises:
			TypeError
		"""
		# Error checking
		mu.check_type(color, str, False)
		mu.check_type(color_a, int)
		
		return self.set_color(nfg.colors[color][0], nfg.colors[color][1], nfg.colors[color][2], int(color_a))
	
	def set_color_by_hex(self, hex_code: str, color_a: int = 255) -> Node:
		"""
		Sets color by hex code.
		Parameters:
			hex_code: (str) hex_code of a color i.e '#FF0000', Can contain '#' but doesn't have to.
			color_a (int : 255)

		Returns:
			self

		Raises:
			TypeError
			ValueError
		"""
		# Error checking
		mu.check_type(hex_code, str, False)
		mu.check_type(color_a, int)
		hex = hex_code.replace('#', '')
		if len(hex) != 6:
			raise ValueError("hex_code must be in form '#FF0000' or 'FF0000'. hex_code received: " + hex_code)
		
		hex_digits = {
			'0': 0,
			'1': 1,
			'2': 2,
			'3': 3,
			'4': 4,
			'5': 5,
			'6': 6,
			'7': 7,
			'8': 8,
			'9': 9,
			'A': 10,
			'B': 11,
			'C': 12,
			'D': 13,
			'E': 14,
			'F': 15
		}
		
		for c in hex:
			if c.upper() not in hex_digits.keys():
				raise ValueError(c + ' is not a hex code digit. Digit should be between 0-F')
		r_hex = hex[0:2:]
		r = (hex_digits[r_hex[0].upper()] * 16) + hex_digits[r_hex[1].upper()]
		g_hex = hex[2:4:]
		g = (hex_digits[g_hex[0].upper()] * 16) + hex_digits[g_hex[1].upper()]
		b_hex = hex[4:6:]
		b = (hex_digits[b_hex[0].upper()] * 16) + hex_digits[b_hex[1].upper()]
		
		return self.set_color(r, g, b, int(color_a))
	
	def set_color_by_id(self, color_id: int, palette_id: int = None, color_a: int = 255) -> Node:
		"""
		Sets r,g,b to 0 and sets color by color_id, palette_id and color_a.

		Paremeters:
			color_id (int) - color_id of a color in a given palette
			palette_id (int: None) - ID of a palette that effects what color color_id represents
			color_a (int: 255) - int between 0 - 255 that effects the transparency of the color

		Returns:
			self

		Raises:
			TypeError
		"""
		# Error checking
		mu.check_type(color_id, int)
		if palette_id is not None:
			mu.check_type(palette_id, int)
		mu.check_type(color_a, int)
		
		self.color_id = int(color_id)
		if palette_id is not None:
			self.palette_id = int(palette_id)
		
		return self.set_color(a=int(color_a))
	
	def set_color_by_list(self, intList: List[int]) -> Node:
		"""
		Sets colors from a list of ints

		Paremeters:
			list (List[in]) - list of 4 ints

		Returns:
			self

		Raises:
			TypeError
			RuntimeError
		"""
		
		mu.check_type(intList, list)
		if len(intList) < 4:
			raise RuntimeError("intList must have at least 4 elements")
		
		mu.check_type(intList[0], int)
		mu.check_type(intList[1], int)
		mu.check_type(intList[2], int)
		mu.check_type(intList[3], int)
		
		self.color_r = intList[0]
		self.color_g = intList[1]
		self.color_b = intList[2]
		self.color_a = intList[3]
		
		return self
	
	def set_auto_zoom(self, x: int = 0, y: int = 0, z: int = 0) -> Node:
		"""
		Sets auto_zoom_x, y, z.

		Parameters:
			x (int: 0)
			y (int: 0)
			z (int: 0)

		Returns:
			self

		Raises:
			TypeError
		"""
		# Error checking
		mu.check_type(x, int)
		mu.check_type(y, int)
		mu.check_type(z, int)
		
		self.auto_zoom_x = int(x)
		self.auto_zoom_y = int(y)
		self.auto_zoom_z = int(z)
		
		return self
	
	def set_trigger_hi(self, x: int = 0, y: int = 0, z: int = 0) -> Node:
		"""
		Sets trigger_hi_x, y, z.

		Parameters:
			x (int: 0)
			y (int: 0)
			z (int: 0)

		Returns:
			self

		Raises:
			TypeError
		"""
		# Error checking
		mu.check_type(x, int)
		mu.check_type(y, int)
		mu.check_type(z, int)
		
		self.trigger_hi_x = int(x)
		self.trigger_hi_y = int(y)
		self.trigger_hi_z = int(z)
		
		return self
	
	def set_trigger_lo(self, x: int = 0, y: int = 0, z: int = 0) -> Node:
		"""
		Sets trigger_low_x, y, z.

		Parameters:
			x (int: 0)
			y (int: 0)
			z (int: 0)

		Returns:
			self

		Raises:
			TypeError
		"""
		# Error checking
		mu.check_type(x, int)
		mu.check_type(y, int)
		mu.check_type(z, int)
		
		self.trigger_lo_x = int(x)
		self.trigger_lo_y = int(y)
		self.trigger_lo_z = int(z)
		
		return self
	
	def set_set_hi(self, x: float = 0, y: float = 0, z: float = 0) -> Node:
		"""
		Sets hi_x, y, z.

		Parameters:
			x (int: 0)
			y (int: 0)
			z (int: 0)

		Returns:
			self

		Raises:
			TypeError
		"""
		# Error checking
		mu.check_type(x, float)
		mu.check_type(y, float)
		mu.check_type(z, float)
		
		self.set_hi_x = float(x)
		self.set_hi_y = float(y)
		self.set_hi_z = float(z)
		
		return self
	
	def set_set_lo(self, x: int = 0, y: int = 0, z: int = 0) -> Node:
		"""
		Sets lo_x, y, z.

		Parameters:
			x (int: 0)
			y (int: 0)
			z (int: 0)

		Returns:
			self

		Raises:
			TypeError
		"""
		# Error checking
		mu.check_type(x, int)
		mu.check_type(y, int)
		mu.check_type(z, int)
		
		self.set_lo_x = int(x)
		self.set_lo_y = int(y)
		self.set_lo_z = int(z)
		
		return self
	
	def set_proximity(self, x: float = 0, y: float = 0, z: float = 0) -> Node:
		"""
		Sets proximity_x, y, z.

		Parameters:
			x (int: 0)
			y (int: 0)
			z (int: 0)

		Returns:
			self

		Raises:
			TypeError
		"""
		# Error checking
		mu.check_type(x, float)
		mu.check_type(y, float)
		mu.check_type(z, float)
		
		self.proximity_x = float(x)
		self.proximity_y = float(y)
		self.proximity_z = float(z)
		
		return self
	
	def set_proximity_mode(self, x: int = 0, y: int = 0, z: int = 0) -> Node:
		"""
		Sets proximity_mode_x, y, z.

		Parameters:
			x (int: 0)
			y (int: 0)
			z (int: 0)

		Returns:
			self

		Raises:
			TypeError
		"""
		# Error checking
		mu.check_type(x, int)
		mu.check_type(y, int)
		mu.check_type(z, int)
		
		self.proximity_mode_x = int(x)
		self.proximity_mode_y = int(y)
		self.proximity_mode_z = int(z)
		
		return self
	
	def set_segments(self, x: int = 20, y: int = 12, z: int = 0) -> Node:
		"""
		Sets segments_x, y, z.

		Parameters:
			x (int: 20)
			y (int: 12)
			z (int: 0)

		Returns:
			self

		Raises:
			TypeError
		"""
		# Error checking
		mu.check_type(x, int)
		mu.check_type(y, int)
		mu.check_type(z, int)
		
		self.segments_x = int(x)
		self.segments_y = int(y)
		self.segments_z = int(z)
		
		return self
	
	# endregion
	
	def color_to_list(self) -> List[int]:
		"""
		Returns a list with rgba values of the nodes current color.

		Parameters:
			None

		Returns:
			List[int]

		Raises:
			None
		"""
		return [self.color_r, self.color_g, self.color_b, self.color_a]