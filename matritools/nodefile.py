from __future__ import annotations
from matritools import utils as mu
from matritools import node as n
from matritools import glyph as g
from matritools import nodecontainer as nc
from matritools import nodefileglobals as globals

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
		self.__check_for_duplicate_ids()
		
		# open files
		node_file = open(self.__node_file_name__ + "_node.csv", "w", encoding="utf-8")
		tag_file = open(self.__node_file_name__ + "_tag.csv", "w", encoding="utf-8")
		
		# write headers
		tag_file.write("id,record_id,table_id,title,description\n")
		node_file.write(globals.node_file_header)
		
		# write tag and node rows
		for taginc, file_row in enumerate(self.nodes, 1):
			node_file.write(file_row.to_string())
			if file_row.tag_text != "":
				tag_text = str(taginc) + "," + \
						   str(file_row.record_id) + ",0,\"" + \
						   str(file_row.tag_text) + "\",\"\"\n"
				tag_file.write(tag_text)
		
		node_file.close()
		tag_file.close()
		return self
	
	def __check_for_duplicate_ids(self):
		ids = {}
		for i, node in enumerate(self.nodes):
			if node.id in ids.keys():
				ids[node.id].append(i)
			else:
				ids[node.id] = [i]
		
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
	
	def __add_initial_nodes__(self):
		# node for world parameters
		self.nodes.append(n.Node("1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,"
							   "0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0.1,0,50,101,101,255,0,"
							   "0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,16,16,0,0,0,0,0,420"))
		# node for first camera view
		self.nodes.append(n.Node("2,1,2,0,0,0,0,2,3,0,0,0,0,1,0,0,0,0,0,0,0,0,0.008645,0.825266,-0.564678,"
							   "1,1,1,-32.446629,-180.908295,143.514175,0,0,1,0,0,0,55.620094,0.6002,0,0,0,0,0,0,0,"
							   "0,0,0,0,0,1,0,0.1,0,50,101,101,255,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"
							   "214.306686,0,0,0,0,0,16,16,0,0,0,0,0,420"))
		# node for second camera view
		self.nodes.append(n.Node("3,1,3,0,2,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,-1,1,1,1,-0.5,0,571.75,0,0,1,0,"
							   "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0.1,0,50,101,101,255,0,0,0,0,0,0,0,0,0,0,0,"
							   "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,16,16,0,0,0,0,0,420"))
		# Third camera view
		self.nodes.append(n.Node("4,1,4,0,2,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,-0,1,1,1,0,-90,"
							   "7,0,0,1,0,0,0,90,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0.1,0,50,101,101,255,0,"
							   "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,16,16,0,0,0,0,0,420"))
		# Fourth camera view
		self.nodes.append(n.Node("5,1,5,0,2,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,-1,-0,-0,1,1,1,85,0,7,0,0,1,0,"
							   "0,0,90,270,0,0,0,0,0,0,0,-0,0,0,0,0,1,0,0.1,0,50,101,101,255,0,0,0,0,0,0,"
							   "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,16,16,0,0,0,0,0,420"))
		# Default Grid
		self.main_grid = n.Node(f"{globals.main_grid_id},6,{globals.main_grid_id},1,0,0,0,1,0,0,0,0,0,1,360,220,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1,0,"
							  "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0.1,3,0,0,255,150,0,0,0,0,0,0,0,0,0,0,0,"
							  "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,420")
		self.nodes.append(self.main_grid)
		
		