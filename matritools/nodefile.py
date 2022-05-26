from __future__ import annotations
from matritools import utils as mu
from matritools import node as n
from matritools import glyph as g
from matritools import nodecontainer as nc

class NodeFile(nc.NodeContainer):
	"""
	Virtual representation of an ANTZ node csv.

	Used to construct a virtual antz node file.
	On construction, provide a file name. The constructor will append "_node.csv" to the end of the provided file name.

	Basic usage:
	  Call create_node and assign it to a variable and modify its properties individually.

	Advanced usage:
	  Create an Glyph, modify it's Nodes accordingly, then use NodeFile.add_glyph.
	  Repeat as necessary.
	"""
	
	node_file_header = "id,type,data,selected,parent_id," \
					   "branch_level,child_id,child_index,palette_id,ch_input_id," \
					   "ch_output_id,ch_last_updated,average,samples,aux_a_x," \
					   "aux_a_y,aux_a_z,aux_b_x,aux_b_y,aux_b_z," \
					   "color_shift,rotate_vec_x,rotate_vec_y,rotate_vec_z,rotate_vec_s," \
					   "scale_x,scale_y,scale_z,translate_x,translate_y," \
					   "translate_z,tag_offset_x,tag_offset_y,tag_offset_z,rotate_rate_x," \
					   "rotate_rate_y,rotate_rate_z,rotate_x,rotate_y,rotate_z," \
					   "scale_rate_x,scale_rate_y,scale_rate_z,translate_rate_x,translate_rate_y," \
					   "translate_rate_z,translate_vec_x,translate_vec_y,translate_vec_z,shader," \
					   "geometry,line_width,point_size,ratio,color_id," \
					   "color_r,color_g,color_b,color_a,color_fade," \
					   "texture_id,hide,freeze,topo,facet," \
					   "auto_zoom_x,auto_zoom_y,auto_zoom_z,trigger_hi_x,trigger_hi_y," \
					   "trigger_hi_z,trigger_lo_x,trigger_lo_y,trigger_lo_z,set_hi_x," \
					   "set_hi_y,set_hi_z,set_lo_x,set_lo_y,set_lo_z," \
					   "proximity_x,proximity_y,proximity_z,proximity_mode_x,proximity_mode_y," \
					   "proximity_mode_z,segments_x,segments_y,segments_z,tag_mode," \
					   "format_id,table_id,record_id,size\n"
	
	def __init__(self, file_name: str):
		"""
		Parameters:
			file_name (str) - name of node and tag file created on write_to_csv.

		Raises:
			TypeError
			RuntimeError
		"""
		# Error checking
		mu.check_type(file_name, str)
		if file_name == "" or file_name is None:
			raise RuntimeError("NodeFile cannot be constructed without a name")
		
		super(NodeFile, self).__init__()
		self.__is_frozen__ = False
		self.__node_file_name__ = file_name
		self.__add_initial_nodes__()
		self.__is_frozen__ = True
	
	def add_glyph(self, glyph: g.glyph, parent_id: int=0, copy_glyph: bool=True) -> NodeFile:
		"""
		Appends all Nodes of a glyph to nodes and manages it's ID's.
		Clears the temporary Nodes of the passed glyph.

		Parameters:
			glyph (Glyph) - Glyph that has its Nodes copied and incremented
			parent_id (int : 0) - id of node this glyph will be attached too
			copy_glyph (bool : True) - Should the glyph nodes be stored as copies?
									   Mark false if you if want to add the glyph only
									   once and maintain node references.

		Returns:
			self

		Raises:
			TypeError
			RuntimeError
		"""
		if parent_id == 0:
			parent_id = self.main_grid.id
		super(NodeFile, self).add_glyph(glyph, parent_id, copy_glyph)
		glyph.__clear_temp_nodes__()
		return self
	
	def create_node(self, parent_node: n.Node=None, tag_text: str="", tag_mode: int=None, template=None) -> n.Node:
		"""
		Creates and returns a Node inside of the NodeFile. If parent_node is None, main_grid id is assigned as created
		nodes parent id.

		Parameters:
			parent_node (Node: None) - Node that newly created Node will be associated with
			tag_text (str : "") - text that will be written in the tag file associated with the created Node
			tag_mode (int : 0) - int representing how the tag should be displayed by default
			template (Node : None) - Created node will be a copy of template if one is passed.

		Returns:
			Node

		Raises:
			TypeError
			RuntimeError
		"""
		if parent_node is None:
			return super(NodeFile, self).create_node(self.main_grid, tag_text, tag_mode, template)
		else:
			return super(NodeFile, self).create_node(parent_node, tag_text, tag_mode, template)
	
	def write_to_csv(self) -> n.NodeFile:
		"""
		Writes all the parameters of each Node into a node csv file as well as creates a corresponding tag file.

		Returns:
			self

		Raises:
			RuntimeError
		"""
		ids = {}
		i = 0
		for node in self.nodes:
			if node.id in ids.keys():
				ids[node.id].append(i)
			else:
				ids[node.id] = [i]
			i += 1
		
		# check for duplicate ID's
		if len(set(ids.keys())) != len(self.nodes):
			node_container = nc.NodeContainer()
			result = ""
			for key in ids.keys():
				if len(ids[key]) > 1:
					result += str(key) + " | " + str(ids[key]) + "\n"
					
					for index in ids[key]:
						node_container.nodes.append(self.nodes[index])
			
			self.to_dataframe().to_csv("debug_node.csv")
			
			raise RuntimeError("Created debug_node.csv. Node File contains duplicate IDs.\n\nID | Indexes:\n\n" +
							   result + str(node_container.to_dataframe().to_string()))
		
		# open files
		node_file = open(self.__node_file_name__ + "_node.csv", "w", encoding="utf-8")
		tag_file = open(self.__node_file_name__ + "_tag.csv", "w", encoding="utf-8")
		
		# write headers
		tag_file.write("id,record_id,table_id,title,description\n")
		node_file.write(self.node_file_header)
		
		# write tag and node rows
		taginc = 1
		for file_row in self.nodes:
			node_file.write(file_row.to_string())
			if file_row.tag_text != "":
				tag_text = str(taginc) + "," + \
						   str(file_row.record_id) + ",0,\"" + \
						   str(file_row.tag_text) + "\",\"\"\n"
				
				taginc += 1
				tag_file.write(tag_text)
		
		node_file.close()
		tag_file.close()
		return self
	
	def __add_initial_nodes__(self):
		# node for world parameters
		self.nodes.append(n.Node("1,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,"
							   "0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0.1,0,50,101,101,255,0,"
							   "0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,16,16,0,0,0,0,0,420"))
		# node for first camera view
		self.nodes.append(n.Node("2,1,2,0,0,0,2,2,3,0,0,0,0,1,0,0,0,0,0,0,0,0,0.008645,0.825266,-0.564678,"
							   "1,1,1,-32.446629,-180.908295,143.514175,0,0,1,0,0,0,55.620094,0.6002,0,0,0,0,0,0,0,"
							   "0,0,0,0,0,1,0,0.1,0,50,101,101,255,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"
							   "214.306686,0,0,0,0,0,16,16,0,0,0,0,0,420"))
		# node for second camera view
		self.nodes.append(n.Node("3,1,3,0,2,1,3,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,-1,1,1,1,-0.5,0,571.75,0,0,1,0,"
							   "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0.1,0,50,101,101,255,0,0,0,0,0,0,0,0,0,0,0,"
							   "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,16,16,0,0,0,0,0,420"))
		# Third camera view
		self.nodes.append(n.Node("4,1,4,0,2,1,4,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,-0,1,1,1,0,-90,"
							   "7,0,0,1,0,0,0,90,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0.1,0,50,101,101,255,0,"
							   "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,16,16,0,0,0,0,0,420"))
		# Fourth camera view
		self.nodes.append(n.Node("5,1,5,0,2,1,5,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,-1,-0,-0,1,1,1,85,0,7,0,0,1,0,"
							   "0,0,90,270,0,0,0,0,0,0,0,-0,0,0,0,0,1,0,0.1,0,50,101,101,255,0,0,0,0,0,0,"
							   "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,16,16,0,0,0,0,0,420"))
		# Default Grid
		self.main_grid = n.Node("6,6,6,1,0,0,0,1,0,0,0,0,0,1,360,220,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1,0,"
							  "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0.1,3,0,0,255,150,0,0,0,0,0,0,0,0,0,0,0,"
							  "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,420")
		self.nodes.append(self.main_grid)
		