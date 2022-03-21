import pandas as pd
import copy
from typing import List
from matritools import utils as mu

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

types = {
    'world': 0,
    'camera': 1,
    'glyph': 5,
    'grid': 6,
    'link': 7,
}

geos = {
        "z cube": 0,
        "cube": 1,
        "z sphere": 2,
        "sphere": 3,
        "z cone": 4,
        "cone": 5,
        "z toroid": 6,
        "toroid": 7,
        "z dodecahedron": 8,
        "dodecahedron": 9,
        "z octahedron": 10,
        "octahedron": 11,
        "z tetrahedron": 12,
        "tetrahedron": 13,
        "z icosahedron": 14,
        "icosahedron": 15,
        "pin": 16,
        "Z pin": 17,
        "z cylinder": 18,
        "cylinder": 19,
        "z plane": 20,
        "plane": 21
   }

topos = {
        "cube": 1,
        "sphere": 2,
        "toroid": 3,
        "cylinder": 4,
        "pin": 5,
        "rod": 6,
        "point": 7,
        "plane": 8,
        "z cube": 9,
        "z sphere": 10,
        "z toroid": 11,
        "z cylinder": 12,
        "z rod": 13
    }

colors = {
    "red": [255, 0, 0],
    "blue": [0, 0, 255],
    "green": [0, 128, 0],
    "yellow": [255, 255, 0],
    "cyan": [0, 255, 255],
    "magenta": [255, 0, 255],
    "hot pink": [255, 105, 180],
    "orange": [255, 128, 0],
    "white": [255, 255, 255],
    "black": [1, 1, 1],
    "grey": [128, 128, 128],
    "lime": [0, 255, 0],
    "maroon": [128, 0, 0],
    "navy": [0, 0, 128],
    "teal": [0, 128, 128],
    "crimson": [220, 20, 60],
    "purple": [128, 0, 128],
    "olive": [128, 128, 0],
    "brown": [139, 69, 19],
    "silver": [192, 192, 192],
    "gold": [255, 215, 0],
    "tan": [210, 180, 140],
    "olive drab": [107, 142, 35],
    "dark green": [0, 100, 0],
    "aqua marine": [127, 255, 212],
    "dodger blue": [30, 144, 255],
    "deep sky blue": [0, 192, 255],
    "indian red": [205, 92, 92],
    "cadet blue": [95, 158, 160],
    "indigo": [75, 0, 130],
    "pink": [255, 192, 203],
    "beige": [245, 245, 220],
    "honeydew": [240, 255, 240],
    "azure": [240, 255, 255],
    "lavender": [230, 230, 250],
    "peach": [255, 218, 185],
    "rosy brown": [188, 143, 143],
    "chocolate": [210, 105, 30],
    "medium spring green": [0, 250, 154],
    "golden rod": [218, 165, 32],
    "coral": [255, 127, 80]
}

class NodeContainer:
    """
    Class to contain and manage a list of Nodes

    Attributes:
        nodes (list[Node]) - nodes that are managed
    """
    def __init__(self):
        self.nodes = []

    def __getitem__(self, item):
        return self.nodes[item]

    def length(self):
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

    def get_next_id(self):
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

    def get_nodes_of_branch_level(self, branch_level: int):
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

    def unselect_all(self):
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

    def untag_all(self):
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

    def match_record_ids_and_data_to_ids(self):
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

    def to_dataframe(self):
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

    def make_link(self, link_node_a: int, link_node_b: int):
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
        mu.check_type(link_node_a, Node, False)
        mu.check_type(link_node_b, Node, False)
        if (link_node_a == link_node_b):
            raise RuntimeError("link_node_a and link_node_b cannot be the same")
        if self.get_node_by_id(link_node_a.id) is None:
            raise RuntimeError("link_node_a must be an existing Node within the container.")
        if self.get_node_by_id(link_node_b.id) is None:
            raise RuntimeError("link_node_b must be an existing Node within the container.")

        # Create link
        link = self.create_node(link_node_a)
        link.type = 7
        link.child_id = link_node_b.id
        link.geometry = geos['cylinder']
        link.topo = 0

        return link

    def add_glyph(self, glyph, parent_id: int = 0, copy_glyph: bool = True):
        """
        Appends all Nodes of a glyph to nodes and manages it's ID's.
        Returns a list of copied Nodes.

        Parameters:
            glyph (Glyph) - Glyph that has its Nodes copied and incremented
            parent_id (int : 0) - id of node this glyph will be attached too
            copy_glyph (bool : True) - Should the glyph nodes be stored as copies?
                                       Mark false if you if want to add the glyph only
                                       once and maintain node references.

        Returns:
            list[Node]

        Raises:
            TypeError
            RuntimeError
        """
        # Error checking
        mu.check_type(glyph, Glyph, False)
        mu.check_type(parent_id, int)
        mu.check_type(copy_glyph, bool, False)

        # Increment glyph ids to to avoid duplicate IDs inside the NodeContainer as well as
        # maintain outside glyph structure when Node references to assign parent_id's
        glyph.nodes[0].parent_id = parent_id
        glyph.__make_ids_consecutive__(self.get_next_id())

        if parent_id != 0:
            # Error checking
            root_parent_node = self.get_node_by_id(parent_id)
            if root_parent_node  == None :
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

    def create_node(self, parent_node=None, tag_text: str = "", tag_mode: int = 0, template=None):
        """
        Creates and returns a Node inside of the NodeContainer.

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
        # Error checking
        mu.check_type(tag_text, str)
        mu.check_type(tag_mode, int)

        if template is not None:
            mu.check_type(template, Node, False)
            node = copy.deepcopy(template)
        else:
            node = Node()

        # maintain parent child structure
        if parent_node != None:
            mu.check_type(parent_node, Node, False)

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
        node.set_tag(tag_text, int(tag_mode))
        node.set_id(self.get_next_id())

        self.nodes.append(node)
        return node

    def create_grid(self, parent_node=None, grid_tag_text: str = "", grid_tag_mode: int = 0, grid_template=None,
                    create_handle: bool = True, handle_tag_text: str = "", handle_tag_mode: int = 0,
                    handle_template = None):
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
            handle.geometry = geos['pin']
            handle.topo = topos['pin']

            grid = self.create_node(handle, grid_tag_text, grid_tag_mode, grid_template)
            grid.type = types['grid']
            grid.topo = topos['plane']
            grid.geometry = geos['plane']

            return handle, grid
        else:
            grid = self.create_node(parent_node, grid_tag_text, grid_tag_mode, grid_template)
            grid.type = types['grid']
            grid.topo = topos['plane']
            grid.geometry = geos['plane']

            return grid

class NodeFile(NodeContainer):
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
        self.__node_file_name__ = file_name
        self.__add_initial_nodes__()

    def add_glyph(self, glyph, parent_id: int = 0, copy_glyph: bool = True):
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

    def create_node(self, parent_node=None, tag_text: str = "", tag_mode: int = 0, template=None):
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

    def write_to_csv(self):
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
            node_container = NodeContainer()
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
        node_file.write(node_file_header)

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
        self.nodes.append(Node("1,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,"
                               "0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0.1,0,50,101,101,255,0,"
                               "0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,16,16,0,0,0,0,0,420"))
        # node for first camera view
        self.nodes.append(Node("2,1,2,0,0,0,2,2,3,0,0,0,0,1,0,0,0,0,0,0,0,0,0.008645,0.825266,-0.564678,"
                               "1,1,1,-32.446629,-180.908295,143.514175,0,0,1,0,0,0,55.620094,0.6002,0,0,0,0,0,0,0,"
                               "0,0,0,0,0,1,0,0.1,0,50,101,101,255,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"
                                "214.306686,0,0,0,0,0,16,16,0,0,0,0,0,420"))
        # node for second camera view
        self.nodes.append(Node("3,1,3,0,2,1,3,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,-1,1,1,1,-0.5,0,571.75,0,0,1,0,"
                               "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0.1,0,50,101,101,255,0,0,0,0,0,0,0,0,0,0,0,"
                               "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,16,16,0,0,0,0,0,420"))
        # Third camera view
        self.nodes.append(Node("4,1,4,0,2,1,4,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,-0,1,1,1,0,-90,"
                               "7,0,0,1,0,0,0,90,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0.1,0,50,101,101,255,0,"
                               "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,16,16,0,0,0,0,0,420"))
        # Fourth camera view
        self.nodes.append(Node("5,1,5,0,2,1,5,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,-1,-0,-0,1,1,1,85,0,7,0,0,1,0,"
                               "0,0,90,270,0,0,0,0,0,0,0,-0,0,0,0,0,1,0,0.1,0,50,101,101,255,0,0,0,0,0,0,"
                               "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,16,16,0,0,0,0,0,420"))
        # Default Grid
        self.main_grid = Node("6,6,6,1,0,0,0,1,0,0,0,0,0,1,360,220,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1,0,"
                               "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0.1,3,0,0,255,150,0,0,0,0,0,0,0,0,0,0,0,"
                               "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,420")
        self.nodes.append(self.main_grid)


class Glyph(NodeContainer):
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
        self.__temp_nodes__ = []

        if csv_file_name != "":
            if not csv_file_name.endswith(".csv"):
                raise RuntimeError("csv_file_name must be name of csv file (must include '.csv'")
            self.__populate_glyph__(csv_file_name)

            if unselect_all:
                self.unselect_all()

            if untag_all:
                self.untag_all()

    def create_temp_node(self, parent_node = None, tag_text: str = "", tag_mode: int = 0, template = None):
        """
        Creates and returns a node inside of the NodeFile.
        Temporary glyphs get removed on NodeFile.add_glyph.

        Parameters:
            parent_node (Node : None) - Desired parent Node
            tag_text (str: "") - text that will be written in the tag file associated with this Node (default "")
            tag_mode (int: 0) - int representing how the tag should be displayed by default (default 0)
            template (Node : None) - Created node will be a copy of template if one is passed.

        Returns:
            Node

        Raises:
            TypeError
        """
        node = self.create_node(parent_node, tag_text, tag_mode, template)
        self.__temp_nodes__.append(node)
        return node

    def add_temp_glyph(self, glyph, parent_id: int):
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

    def freeze_all(self, freeze: bool = True):
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

    def __make_ids_consecutive__(self, starting_id: int = 8):
        """
        Removes gaps in ids. i.e IDs 1,2,4 become 1,2,3.
        Can also be used to change the ID's of the glyph to start from a specified index.

        Parameters:
            starting_id (int: 8) - first id of the glyph

        Returns:
            None

        Raises:
            TypeError
        """
        # Error checking
        mu.check_type(starting_id, int)

        # keys = old IDs, values = new IDs
        ids = {0: 0}
        if self.nodes[0].parent_id != 0:
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
            node = Node(line)

            if node.parent_id == 0 and node.id > 7:
               root_ids.append(f'Index: {length}, ID: {node.id}\n\t')

            if node.id not in range(8):
                self.nodes.append(node)
                length += 1

        if len(root_ids) > 1:
            print(mu.WARNING + \
                  'Glyph has more than one root node! '
                  'If this is not by mistake, be sure to manage them properly.' + mu.ENDC + \
                  'Root Nodes:\n' + str(root_ids))

        self.__make_ids_consecutive__(8)

class Node:
    """
    Container of properties and property setters for Nodes.

    Attributes:
        id               - node ID used for pin tree relationship graph
        type            - node type - 1: Camera; 2: video; 3: Surface;
                         - 4: Points, 5:Pin, 6:Grid
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

        # endregion

        if comma_string == "":
            return

        values = comma_string.split(",")
        self.set_properties_from_string_list(values)

    def set_properties_from_string_list(self, values: List[str]):
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

    def print_properties(self):
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

    def to_string(self):
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

    def set_id(self, node_id: int):
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

    def set_tag(self, tag_text: str, tag_mode: int = 0):
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

    def set_aux_a(self, x: int = 30, y: int = 30, z: int = 30):
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

    def set_aux_b(self, x: int = 30, y: int = 30, z=30):
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

    def set_rotate_vec(self, x: int = 0, y: int = 0, z: int = 0, s: int = 0):
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

    def set_scale(self, x: float = 1, y: float = 1, z: float = 1):
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

    def set_u_scale(self, scale: float = 1):
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

    def set_translate(self, x: float = 0, y: float = 0, z: float = 0):
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

    def set_tag_offset(self, x: float = 0, y: float = 0, z: float = 0):
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

    def set_rotate(self, x: float = 0, y: float = 0, z: float = 0):
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

    def set_rotate_rate(self, x: int = 0, y: int = 0, z: int = 0):
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

    def set_scale_rate(self, x: int = 0, y: int = 0, z: int = 0):
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

    def set_translate_rate(self, x: float = 0, y: float = 0, z: float = 0):
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

    def set_translate_vec(self, x: int = 0, y: int = 0, z: int = 0):
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

    def set_color(self, r: int = 0, g: int = 0, b: int = 0, a: int = 255):
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

    def set_color_by_name(self, color: str, color_a: int = 255):
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

        return self.set_color(colors[color][0], colors[color][1], colors[color][2], int(color_a))

    def set_color_by_hex(self, hex_code: str, color_a: int = 255):
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

    def set_color_by_id(self, color_id: int, palette_id: int = None, color_a: int = 255):
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

    def color_to_list(self):
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

    def set_color_by_list(self, list):
        self.color_r = list[0]
        self.color_g = list[1]
        self.color_b = list[2]
        self.color_a = list[3]

    def set_auto_zoom(self, x: int = 0, y: int = 0, z: int = 0):
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

    def set_trigger_hi(self, x: int = 0, y: int = 0, z: int = 0):
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

    def set_trigger_lo(self, x: int = 0, y: int = 0, z: int = 0):
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

    def set_set_hi(self, x: float = 0, y: float = 0, z: float = 0):
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

    def set_set_lo(self, x: int = 0, y: int = 0, z: int = 0):
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

    def set_proximity(self, x: float = 0, y: float = 0, z: float = 0):
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

    def set_proximity_mode(self, x: int = 0, y: int = 0, z: int = 0):
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

    def set_segments(self, x: int = 20, y: int = 12, z: int = 0):
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