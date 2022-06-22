from __future__ import annotations
from matritools import fronzenclass as fc
from matritools import node as nd
from matritools import utils as mu

class GridPattern:
	"""
	A helper class places nodes in a grid pattern.

	Attributes:
		x_distance (float:5) - distance each node will be away from each other on the x axis
		y_distance (float:5) - distance each node will be away from each other on the y axis
		x_offset (float:-180) - starting position of the grid on the x axis
		y_offset (float:-110) - starting position of the grid on the y axis
		max_rows (int:10) - the number of nodes placed on the x axis before moving on the y axis.
		max_columns (int:0) - the number of nodes placed on the y axis before moving on the z axis.
							  Set to 0 for unlmited columns
		z_distance (float:5) - distance each node will be away from each other on the z axis
		z_offset (float:0) - starting position of the grid on the z axis
		
	"""
	def __init__(
			self,
			x_distance: float=5,
			y_distance: float=5,
			x_offset: float=-180,
			y_offset: float=-110,
			max_rows: int=10,
			max_columns: int=0,
			z_distance: float=5,
			z_offset: float = 0):
		"""
		Parameters:
			x_distance (float:5) - distance each node will be away from each other on the x axis
			y_distance (float:5) - distance each node will be away from each other on the y axis
			x_offset (float:-180) - starting position of the grid on the x axis
			y_offset (float:-110) - starting position of the grid on the y axis
			max_rows (int:10) - the number of nodes placed on the x axis before moving on the y axis.
			max_columns (int:0) - the number of nodes placed on the y axis before moving on the z axis.
			                      Set to 0 for unlmited columns.
			z_distance (float:5) - distance each node will be away from each other on the z axis
			z_offset (float:0) - starting position of the grid on the z axis
		"""
		mu.check_type(x_distance, float)
		mu.check_type(y_distance, float)
		mu.check_type(x_offset, float)
		mu.check_type(y_offset, float)
		mu.check_type(max_rows, int)
		mu.check_type(max_columns, int)
		mu.check_type(z_distance, float)
		mu.check_type(z_offset, float)
		
		self.x_distance = x_distance
		self.y_distance = y_distance
		self.x_offset = x_offset
		self.y_offset = y_offset
		self.max_rows = int(max_rows)
		self.max_columns = int(max_columns)
		self.z_distance = z_distance
		self.z_offset = z_offset
		
		self.__row__ = 0
		self.__column__ = 0
		self.__stack__ = 0
		
	def place_node(self, node: nd.Node):
		"""
		Positions a node and increments internal indexes.
		
		Parameters:
			node (Node) - Node to be positions.

		Returns:
			None
			
		Raises:
			TypeError
		"""
		mu.check_type(node, nd.Node, False)
		
		x = (self.__row__ * self.x_distance) + self.x_offset
		y = (self.__column__ * self.y_distance) + self.y_offset
		z = (self.__stack__ * self.z_distance) + self.z_offset
		
		# increment / reset indexes
		self.__row__ += 1
		if self.__row__  == self.max_rows:
			self.__row__ = 0
			self.__column__ += 1
			if self.max_columns != 0:
				if self.__column__ == self.max_columns:
					self.__column__ = 0
					self.__stack__ += 1
		
		node.set_translate(x, y, z)
		
	def reset(self):
		"""
		Reset internal indexes so that next placement will be the begining of the grid pattern.
		
		Returns:
			None
			
		Raises:
			None
		"""
		self.__row__ = 0
		self.__column__ = 0
		self.__stack__ = 0