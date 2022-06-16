from __future__ import annotations
from matritools import nodecontainer as nc
from matritools import node as n
from matritools import utils as mu
from matritools import nodefileglobals as globals
import pandas as pd

class Glyph(nc.NodeContainer):
	"""
	Class used to duplicate and edit individual instances glyphs to be rendered in OpenAntz.
	Can be constructed using node file generated from antz that contains only one glyph.
	"""
	
	def __init__(self, csv_file_name: str = "", unselect_all: bool = True, untag_all: bool = True):
		"""
		Parameters:
			csv_file_name (str: "") - Name of the glyph template csv file
			unselect_all (bool: True) - Should all Nodes selected mode be 0?
			untag_all (bool: True) - Should all Nodes tag mode be 0?

		Raises:
			RuntimeError
			TypeError
		"""
		# Error checking
		mu.check_type(csv_file_name, str, False)
		mu.check_type(unselect_all, bool, False)
		mu.check_type(untag_all, bool, False)
		
		super(Glyph, self).__init__()
		self.__is_frozen__ = False
		self.__temp_nodes__ = []
		
		if csv_file_name != "":
			if not csv_file_name.endswith(".csv"):
				raise RuntimeError("csv_file_name must be name of csv file (must include '.csv'")
			self.__populate_glyph__(csv_file_name)
			
			if unselect_all:
				self.unselect_all()
			
			if untag_all:
				self.untag_all()
		
		self.__is_frozen__ = True
	
	def create_temp_node(self, parent_node: Node = None, tag_text: str = "", tag_mode: int = None,
						 template=None) -> Node:
		"""
		Creates and returns a node inside of the NodeFile.
		Temporary glyphs get removed on NodeFile.add_glyph.

		Parameters:
			parent_node (Node : None) - Desired parent Node
			tag_text (str: "") - text that will be written in the tag file associated with this Node
			tag_mode (int: None) - int representing how the tag should be displayed by default
			template (Node : None) - Created node will be a copy of template if one is passed.

		Returns:
			Node

		Raises:
			TypeError
		"""
		node = self.create_node(parent_node, tag_text, tag_mode, template)
		self.__temp_nodes__.append(node)
		return node
	
	def add_temp_glyph(self, glyph: Glyph, parent_id: int) -> Glyph:
		"""
		Temporarily appends all Nodes of a glyph to nodes and manages it's ID's.
		Temporary glyphs get removed on NodeFile.add_glyph.

		Parameters:
			glyph (Glyph) - Glyph that has its Nodes copied and incremented
			parent_id (int) - id of glyphs's root parent node

		Returns:
			self

		Raises:
			TypeError
		"""
		glyph_copy = self.add_glyph(glyph, parent_id)
		for node in glyph_copy.nodes:
			self.__temp_nodes__.append(node)
		return self
	
	def freeze_all(self, freeze: bool = True) -> Glyph:
		"""
		Sets all Nodes in this NodeContainer to be frozen or unfrozen

		Parameters:
			freeze (bool: True) - Should all nodes in glyph be frozen

		Returns:
			self

		Raises:
			TypeError
		"""
		# Error checking
		mu.check_type(freeze, bool, False)
		
		freeze_mode = 0
		if freeze:
			freeze_mode = 1
		
		for node in self.nodes:
			node.freeze = freeze_mode
		
		return self
	
	def __make_ids_consecutive__(self, starting_id: int = globals.main_grid_id + 1):
		"""
		Removes gaps in ids. i.e IDs 1,2,4 become 1,2,3.
		Can also be used to change the ID's of the glyph to start from a specified index.

		Parameters:
			starting_id (int: 8) - first id of the glyph

		Returns:
			None

		Raises:
			TypeError
			RuntimeError
		"""
		# Error checking
		mu.check_type(starting_id, int, False)
		
		if starting_id <= globals.main_grid_id:
			raise RuntimeError(f"starting_id must be greater than {globals.main_grid_id}")
		
		# keys = old IDs, values = new IDs
		ids = {0: globals.main_grid_id, globals.main_grid_id:globals.main_grid_id}
		if self.nodes[0].parent_id != 0 or self.nodes[0].parent_id != globals.main_grid_id:
			ids[self.nodes[0].parent_id] = self.nodes[0].parent_id
		current_id = starting_id
		
		for node in self.nodes:
			# replace old IDs with new IDs
			node.parent_id = ids[node.parent_id]
			node.child_id = ids[node.child_id]
			
			# map old ID to new ID
			ids[node.id] = current_id
			
			node.set_id(current_id)
			
			current_id += 1
	
	def __clear_temp_nodes__(self):
		"""
		Clears temporary Nodes from nodes

		 Parameters:
			 None

		 Returns:
			 None

		Raises:
			RuntimeError
		"""
		for temp_node in self.__temp_nodes__:
			for child_node in self.get_nodes_by_parent_id(temp_node.id):
				if child_node not in self.__temp_nodes__:
					raise RuntimeError('A temporary node (id: ' + str(temp_node.id) +
									   ', tag: ' + temp_node.tag_text +
									   ') is the parent of a non-temporary node '
									   '(id: ' + str(child_node.id) + ', tag: ' + child_node.tag_text + ')')
		for node in self.__temp_nodes__:
			self.nodes.remove(node)
		self.__temp_nodes__.clear()
	
	def __populate_glyph__(self, csv_file_name: str = ""):
		df = pd.read_csv(csv_file_name)
		df = df.applymap(lambda cell: int(cell) if str(cell).endswith('.0') else cell)
		root_ids = []
		length = 0
		
		for index, row in df.iterrows():
			# build Node from row
			line = ""
			for column in df.columns:
				line += str(row[column]) + ","
			line = line[:len(line) - 1]
			node = n.Node(line)
			
			if (node.parent_id == 0 or node.parent_id == globals.main_grid_id) and node.id > globals.main_grid_id:
				root_ids.append(f'Index: {length}, ID: {node.id}\n\t')
			
			if node.id not in range(globals.main_grid_id + 1):
				self.nodes.append(node)
				length += 1
		
		if len(root_ids) > 1:
			print(mu.WARNING + \
				  'Glyph has more than one root node! '
				  'If this is not by mistake, be sure to manage them properly.' + mu.ENDC + \
				  'Root Nodes:\n' + str(root_ids))
		
		self.__make_ids_consecutive__(globals.main_grid_id + 1)