from __future__ import annotations
from matritools import fronzenclass as fc
from matritools import nodefileglobals as nfg
from matritools import node as n
from matritools import glyph as g
from matritools import utils as mu
import pandas as pd
import copy

class NodeContainer(fc.FrozenClass):
	"""
	Class to contain and manage a list of Nodes

	Attributes:
		nodes (list[Node]) - nodes that are managed
	"""
	
	def __init__(self):
		self.nodes = []
		self.__is_frozen__ = True
	
	def __getitem__(self, item):
		return self.nodes[item]
	
	def length(self) -> int:
		"""
		Returns the number of Nodes in this NodeContainer.

		Parameters:
			None

		Returns:
			int

		Raises:
			None
		"""
		return len(self.nodes)
	
	def get_last_node(self):
		"""
		Returns the last Node of the NodeContainer. Returns None if nodes is empty.

		Parameters:
			None

		Returns:
			None
			Node

		Raises:
			 None
		"""
		if len(self.nodes) == 0:
			return None
		return self.nodes[self.length() - 1]
	
	def get_next_id(self) -> int:
		"""
			Returns the last id + 1, Returns 1 if empty.

			Parameters:
				None

			Returns:
				int

			Raises:
				None
		"""
		if len(self.nodes) == 0:
			return 1
		return self.get_last_node().id + 1
	
	def get_node_by_id(self, node_id: int):
		"""
		Returns the node with the given ID, None if no Node found.

		Parameters:
			node_id (int) - ID of requested Node

		Returns:
			Node
			None

		Raises:
			TypeError
		"""
		mu.check_type(node_id, int)
		for node in self.nodes:
			if node.id == node_id:
				return node
		return None
	
	def get_nodes_by_parent_id(self, parent_id: int):
		"""
		Returns a list of Nodes with a given parent_id.

		Paramenters:
			parent_id (int) - parent_id of returned nodes

		Returns:
			list[Node]

		Raises:
			TypeError
		"""
		mu.check_type(parent_id, int)
		result = []
		for node in self.nodes:
			if node.parent_id == int(parent_id):
				result.append(node)
		return result
	
	def get_nodes_of_branch_level(self, branch_level: int) -> List[n.Node]:
		"""
		Returns a list of Nodes of a given branch level.

		Parameters:
			branch_level (int)

		Returns:
			list[Node]

		Raises:
			TypeError
		"""
		mu.check_type(branch_level, int)
		result = []
		for node in self.nodes:
			if node.branch_level == branch_level:
				result.append(node)
		return result
	
	def unselect_all(self) -> NodeContainer:
		"""
		Changes the selected property of all NodeContainer's Nodes to 0.
		When glyph template files are saved via "save selected",
		each node is marked selected, use this to reverse this effect.

		Parameters:
			None

		Returns:
			self

		Raises:
			None
		"""
		for node in self.nodes:
			node.selected = 0
		return self
	
	def untag_all(self) -> NodeContainer:
		"""
		Sets tag_mode of all Nodes in a NodeContainer to 0.

		Parameters:
			None

		Returns:
			self

		Raises:
			None
		"""
		for node in self.nodes:
			node.tag_mode = 0
		return self
	
	def match_record_ids_and_data_to_ids(self) -> NodeContainer:
		"""
		Iterates over each Node in the NodeContainer and matches its record id and data to its id.\
		Upon construction of a Glyph, this happens by default.
		The uses of this function are primarily for internal purposes.

		Parameters:
			None

		Returns:
			None

		Raises:
			self
		"""
		for node in self.nodes:
			node.set_id(node.id)
		return self
	
	def to_dataframe(self) -> pd.DataFrame:
		"""
		Returns a DataFrame with all Nodes as rows and Node properties as columns.

		Parameters:
			None

		Returns:
			DataFrame

		Raises:
			 None
		"""
		list_of_lists = []
		for node in self.nodes:
			columns = node.to_string().split(",")
			columns.append(node.tag_text)
			list_of_lists.append(columns)
		column_labels = node_file_header.split(',')
		column_labels.append("tag_text")
		return pd.DataFrame(data=list_of_lists, columns=column_labels)
	
	def make_link(self, link_node_a: n.Node, link_node_b: n.Node, ratio: float = 0.1) -> n.Node:
		"""
		Creates a visible link between link_node_a and link_node_b.
		Returns the created Node.

		Parameters:
			link_node_a (Node) - Node to be linked from
			link_node_b (Node) - Node to to be linked to

		Returns:
			Node

		Raises:
			RuntimeError
			TypeError
		"""
		# Error checking
		mu.check_type(link_node_a, n.Node, False)
		mu.check_type(link_node_b, n.Node, False)
		if (link_node_a == link_node_b):
			raise RuntimeError("link_node_a and link_node_b cannot be the same")
		if self.get_node_by_id(link_node_a.id) is None:
			raise RuntimeError("link_node_a must be an existing Node within the container.")
		if self.get_node_by_id(link_node_b.id) is None:
			raise RuntimeError("link_node_b must be an existing Node within the container.")
		
		# Create link
		link = self.create_node(link_node_a)
		link.type = nfg.types['link']
		link.child_id = link_node_b.id
		link.geometry = nfg.geos['cylinder']
		link.topo = 0
		link.ratio = ratio
		
		return link
	
	def add_glyph(self, glyph: g.Glyph, parent_id: int = 0, copy_glyph: bool = True) -> g.Glyph:
		"""
		Appends all Nodes of a glyph to nodes and manages it's ID's.
		Returns passed glyph (Glyph).

		Parameters:
			glyph (Glyph) - Glyph that has its Nodes copied and incremented
			parent_id (int : 0) - id of node this glyph will be attached too
			copy_glyph (bool : True) - Should the glyph nodes be stored as copies?
									   Mark false if you if want to add the glyph only
									   once and maintain node references.

		Returns:
			Glyph

		Raises:
			TypeError
			RuntimeError
		"""
		# Error checking
		mu.check_type(glyph, g.Glyph, False)
		mu.check_type(parent_id, int)
		mu.check_type(copy_glyph, bool, False)
		
		# Increment glyph ids to to avoid duplicate IDs inside the NodeContainer as well as
		# maintain outside glyph structure when Node references to assign parent_id's
		glyph.nodes[0].parent_id = parent_id
		glyph.__make_ids_consecutive__(self.get_next_id())
		
		if parent_id != 0:
			# Error checking
			root_parent_node = self.get_node_by_id(parent_id)
			if root_parent_node == None:
				raise RuntimeError("parent_id '" + str(parent_id) + "' does not belong to an existing node")
			else:
				try:
					if root_parent_node in self.__temp_nodes__:
						raise RuntimeError('parent_node is a temporary node'
										   ' and cannot be a parent of a non-temporary node.\n'
										   'If this you need to override this restriction, '
										   'you will need to manually keep track of your own temporary nodes.')
				except AttributeError:
					pass
				glyph.nodes[0].branch_level = root_parent_node.branch_level + 1
				
				# Ensure branch levels make sure with new glyph parts
				def update_branch_level(parent_node):
					for node in glyph.get_nodes_by_parent_id(parent_node.id):
						update_branch_level(node)
						node.branch_level = parent_node.branch_level + 1
				
				update_branch_level(glyph.nodes[0])
		
		# Not copying glyph allows references to the glyph being added to still be valid but this can only be done
		# once for that glyph because any changes, such as assigning it's IDs, to that glyph would effect two more than
		# Node and thus have duplicate ID's
		if copy_glyph:
			glyph = copy.deepcopy(glyph)
		
		for node in glyph.nodes:
			self.nodes.append(node)
		return glyph
	
	def create_node(self, parent_node: n.Node = None, tag_text: str = "", tag_mode: int = None,
					template: n.Node = None) -> n.Node:
		"""
		Creates and returns a Node inside of the NodeContainer.

		Parameters:
			parent_node (Node: None) - Node that newly created Node will be associated with
			tag_text (str : "") - text that will be written in the tag file associated with the created Node
			tag_mode (int : None) - int representing how the tag should be displayed by default
			template (Node : None) - Created node will be a copy of template if one is passed.

		Returns:
			Node

		Raises:
			TypeError
			RuntimeError
		"""
		# Error checking
		mu.check_type(tag_text, str)
		if tag_mode is not None:
			mu.check_type(tag_mode, int)
		
		if template is not None:
			print(template.tag_mode)
			mu.check_type(template, n.Node, False)
			node = copy.deepcopy(template)
			print(node.tag_mode)
		else:
			node = n.Node()
		
		# maintain parent child structure
		if parent_node != None:
			mu.check_type(parent_node, n.Node, False)
			
			if parent_node not in self.nodes:
				raise RuntimeError('parent_node does not belong this NodeContainer')
			try:
				if parent_node in self.__temp_nodes__:
					raise RuntimeError('parent_node is a temporary node'
									   ' and cannot be a parent of a non-temporary node.\n'
									   'If this you need to override this restriction, '
									   'you will need to manually keep track of your own temporary nodes.')
			except AttributeError:
				pass
			node.parent_id = copy.deepcopy(parent_node.id)
			node.branch_level = parent_node.branch_level + 1
		if tag_mode is not None:
			node.set_tag(tag_text, int(tag_mode))
		else:
			node.tag_text = tag_text
		node.set_id(self.get_next_id())
		
		self.nodes.append(node)
		return node
	
	def create_grid(self, parent_node: n.Node = None, grid_tag_text: str = "", grid_tag_mode: int = 0,
					grid_template: n.Node = None,
					create_handle: boo = True, handle_tag_text: str = "", handle_tag_mode: int = 0,
					handle_template: n.Node = None):
		"""
		Creates and returns a Node formatted as a grid, inside of the NodeContainer.
		If create_handle is True, the created handle and grid are returned. If not, just the grid is returned.

		Parameters:
			parent_node (Node: None) - Node that newly created Node will be associated with
			grid_tag_text (str : "") - text that will be written in the tag file associated with the created grid
			grid_tag_mode (int : 0) - int representing how the grid's tag should be displayed by default
			grid_template (Node : None) - Created grid will be a copy of template if one is passed.
			create_handle (bool : True) - Should the grid be attached to a handle?
			handle_tag_text (str : "") - text that will be written in the tag file associated with the created handle
			handle_tag_mode (int : 0) - int representing how the handle tag should be displayed by default
			handle_template (Node : None) - Created handle will be a copy of template if one is passed.

		Returns:
			Node
			Node, Node

		Raises:
			TypeError
			RuntimeError
		"""
		
		mu.check_type(create_handle, bool, False)
		if create_handle:
			handle = self.create_node(parent_node, handle_tag_text, handle_tag_mode, handle_template)
			handle.geometry = nfg.geos['pin']
			handle.topo = nfg.topos['pin']
			
			grid = self.create_node(handle, grid_tag_text, grid_tag_mode, grid_template)
			grid.type = nfg.types['grid']
			grid.topo = nfg.topos['plane']
			grid.geometry = nfg.geos['plane']
			
			return handle, grid
		else:
			grid = self.create_node(parent_node, grid_tag_text, grid_tag_mode, grid_template)
			grid.type = nfg.types['grid']
			grid.topo = nfg.topos['plane']
			grid.geometry = nfg.geos['plane']
			
			return grid