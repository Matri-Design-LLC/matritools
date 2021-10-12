import pandas as pd
import copy
from typing import List


class NodeFile:
    """
    Virtual representation of an ANTZ node csv

    Used to construct a virtual antz node file.
    On construction, provide a file name. The constructor will append "_node.csv" to the end of the provided file name.

    Basic usage:
      After created node_file class, set the properties of the class to what you want a node csv file row to be,
      then call create_node_file_row.4e3
      After adding all desired rows, call write to csv.

    Advanced usage:
      Create an AntzGlyph, modify its rows and use NodeFile.add_glyph_to_rows.
      Then call AntzGlyph.increment_glyph, modify rows again accordingly, then use NodeFile.add_glyph_to_rows.
      Repeat as necessary.

    Attributes:
        node_file_rows (list[NodeFileRow]) - list of NodeFileRows that make up a node file.
        properties (NodeFileRow) - list of NodeFileRows that make up a node file.

    """

    header = "id,type,data,selected,parent_id," \
             "branch_level,child_id,child_index,palette_id,ch_input_id," \
             "ch_output_id,ch_last_updated,average,samples,aux_a_x," \
             "aux_a_y,aux_a_z,aux_b_x,aux_b_y,aux_b_z," \
             "color_shift,rotate_vec_x,rotate_vec_y,rotate_vec_z,rotate_vec_s," \
             "scale_x,scale_y,scale_z,translate_x,translate_y," \
             "translate_z,tag_offset_x,tag_offset_y,tag_offset_z,rotate_rate_x," \
             "rotate_rate_y,rotate_rate_z,rotate_x,rotate_y,rotate_z," \
             "scale_rate_x,scale_rate_y,scale_rate_z,translate_rate_x,translate_rate_y," \
             "translate_rate_z,translate_vec_x,translate_vec_y,translate_vec_z,shader," \
             "geometry,line_width,point_size,ratio,color_index," \
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
            file_name (str: None) - name of node and tag file created on write_to_csv()

        Raises:
            TypeError
            RuntimeError
        """

        file_name = str(file_name)

        if file_name == "" or file_name is None:
            raise RuntimeError("NodeFile constructed without a name")

        self.__taginc__ = 1  # line number for a tag file row
        self.node_file_rows = []
        self.properties = NodeFileRow()
        self.__node_file_name__ = file_name
        self.__add_initial_rows__()

    def length(self):
        """ Returns the number of NodeFileRows in this file. (int) """
        return (len(self.node_file_rows))

    def get_last_row(self):
        """ Returns the last NodeFileRow of the file. (NodeFileRow) """
        return self.node_file_rows[self.length() - 1]

    def get_row_by_id(self, row_id: int):
        """
        Returns the row with the given ID, None if no row found

        Parameters:
            row_id (int: None) - ID of requested NodeFileRow

        Returns: NodeFileRow, None
        """
        for row in self.node_file_rows:
            if row.id == row_id:
                return row

        return None

    def write_to_csv(self):
        """
        Writes all the parameters of each NodeFileRow into a node csv file as well as
        creates a corresponding tag file.

        Returns: None

        Raises:
            RuntimeError
        """

        ids = {}
        i = 0
        for row in self.node_file_rows:
            if row.id in ids.keys():
                ids[row.id].append(i)
            else:
                ids[row.id] = [i]
            i += 1

        if len(set(ids.keys())) != len(self.node_file_rows):
            temp_nf = NodeFile("temp")
            result = ""
            for key in ids.keys():
                if len(ids[key]) > 1:
                    result += str(key) + " | " + str(ids[key]) + "\n"

                    for index in ids[key]:
                        temp_nf.node_file_rows.append(self.node_file_rows[index])
            self.to_dataframe().to_csv("debug_node.csv")
            raise RuntimeError("Created debug_node.csv. Node File contains duplicate IDs.\n\nID | Indexes:\n\n" +
                               result + str(temp_nf.to_dataframe().to_string()))

        node_file = open(self.__node_file_name__ + "_node.csv", "w", encoding="utf-8")
        tag_file = open(self.__node_file_name__ + "_tag.csv", "w", encoding="utf-8")
    
        tag_file.write("id,record_id,table_id,title,description\n")

        node_file.write(self.header)

        for file_row in self.node_file_rows:
            node_file.write(file_row.to_string())
            if file_row.tag_text != "":
                tag_text = str(self.__taginc__) + "," + \
                           str(file_row.record_id) + ",0,\"" + \
                           str(file_row.tag_text) + "\",\"\"\n"

                self.__taginc__ += 1
                tag_file.write(tag_text)

        node_file.close()

    def make_link(self, link_id_a: int, link_id_b: int, link_object_id: int = 0):
        """
        Creates a visible link between two NodeFileRows with IDs of link_id_a, and link_id_b.
        Returns the created NodeFileRow.

        Parameters:
            link_id_a (int: None) - id of NodeFileRow
            link_id_b (int: None) - id of NodeFileRow
            link_object_id: 0) - id of created NodeFileRow, leave as default to generate a unique ID

        Returns: NodeFileRow

        Raises: RuntimeError
        """

        link_id_a = int(link_id_a)
        link_id_b = int(link_id_b)
        link_object_id = int(link_object_id)

        if (link_id_a == link_id_b) or link_id_a == self.properties.id or link_id_b == self.properties.id:
            raise RuntimeError("link_id_a and link_id_b cannot be equal to eachother and neither can be equal to id")

        if (link_object_id == link_id_a) or link_object_id == link_id_b:
            raise RuntimeError("link_object_id must be different from link_id_a, and link_id_b")

        if self.get_row_by_id(link_id_a) is None:
            raise RuntimeError("link_id_a (" + str(link_id_a) + ") must be the id of an existing NodeFileRow.")

        if self.get_row_by_id(link_id_b) is None:
            raise RuntimeError("link_id_b (" + str(link_id_b) + ") must be the id of an existing NodeFileRow.")

        if self.get_row_by_id(link_object_id) is not None:
            raise RuntimeError("link_object_id (" + str(link_object_id) + ") must not be the id of an existing NodeFileRow.")

        link = NodeFileRow()
        if link_object_id == 0:
            link_id = self.get_last_row().id + 1
            while self.get_row_by_id(link_id) is not None:
                link_id += 1
            link.set_id(link_id)
        else:
            link.set_id(link_object_id)

        link._type = 7
        link.parent_id = link_id_a
        link.child_id = link_id_b

        self.node_file_rows.append(link)

        return link

    def create_node_row(self, tag_text: str="", tag_mode: int=0):
        """
        Creates and returns a node file row from node_file current properties and increments id by 1

        Parameters:
            tag_text - text that will be written in the tag file associated with this node file row (default "")
            tag_mode - int representing how the tag should be displayed by default (default 0)

        Returns: NodeFileRow
        """
        node_row = copy.deepcopy(self.properties)
        self.node_file_rows.append(node_row)
        if tag_text != "":
            node_row.set_tag(tag_text, tag_mode)
        self.properties.set_id(self.properties.id + 1)
        return node_row

    def add_glyph(self, glyph):
        """
        Appends all rows of a glyph to node_file_rows and increments glyph template id, parent_id, data, and record_id

        Parameters:
            glyph (AntzGlyph) - AntzGlyph that has its NodeFileRows copied and incremented

        Returns: None
        """

        if not isinstance(glyph, AntzGlyph):
            raise TypeError("glyph must be of type AntzGlyph")
        for row in glyph.node_file_rows:
            self.node_file_rows.append(copy.deepcopy(row))
        glyph.increment_ids()
        self.properties.set_id(self.get_last_row().id + 1)

    def to_dataframe(self):
        """ Returns a data frame with all node file rows (DataFrame) """
        list_of_lists = []
        for row in self.node_file_rows:
            columns = []
            for column in row.to_string().split(","):
                columns.append(column)
            columns.append(row.tag_text)
            list_of_lists.append(columns)
        column_labels = self.header.split(',')
        column_labels.append("tag_text")
        return pd.DataFrame(data=list_of_lists, columns=column_labels)

    def __add_initial_rows__(self):
        # Row for world parameters
        self.node_file_rows.append(NodeFileRow("1,0,1,0,0,"
                                               "0,1,0,0,0,"
                                               "0,0,0,1,0,"
                                               "0,0,0,0,0,"
                                               "0,0,0,0,1,"
                                               "1,1,1,0,0,"
                                               "0,0,0,1,0,"
                                               "0,0,0,0,0,"
                                               "0,0,0,0,0,"
                                               "0,0,0,0,0,"
                                               "0,1,0,0.1,0,"
                                               "50,101,101,255,0,"
                                               "0,0,0,0,0,"
                                               "0,0,0,0,0,"
                                               "0,0,0,1,0,"
                                               "0,0,0,0,0,"
                                               "0,0,0,0,0,"
                                               "0,16,16,0,0,"
                                               "0,0,0,420"))
        # Row for first camera view
        self.node_file_rows.append(NodeFileRow("2,1,2,0,0,"
                                               "0,2,2,3,0,"
                                               "0,0,0,1,0,"
                                               "0,0,0,0,0,"
                                               "0,0,0.008645,0.825266,-0.564678,"
                                               "1,1,1,-32.446629,-180.908295,"
                                               "143.514175,0,0,1,0,"
                                               "0,0,55.620094,0.6002,0,0,"
                                               "0,0,0,0,0,"
                                               "0,0,0,0,0,"
                                               "1,0,0.1,0,"
                                               "50,101,101,255,0,"
                                               "0,0,0,0,0,"
                                               "0,0,0,0,0,"
                                               "0,0,0,0,0,"
                                               "0,0,0,0,0,"
                                               "214.306686,0,0,0,0,"
                                               "0,16,16,0,0,"
                                               "0,0,0,420"))
        # Row for second camera view
        self.node_file_rows.append(NodeFileRow("3,1,3,0,2,"
                                               "1,3,0,0,0,"
                                               "0,0,0,1,0,"
                                               "0,0,0,0,0,"
                                               "0,0,0,0,-1,"
                                               "1,1,1,-0.5,0,"
                                               "571.75,0,0,1,0,"
                                               "0,0,0,0,0,"
                                               "0,0,0,0,0,"
                                               "0,0,0,0,0,"
                                               "0,1,0,0.1,0,"
                                               "50,101,101,255,0,"
                                               "0,0,0,0,0,"
                                               "0,0,0,0,0,"
                                               "0,0,0,0,0,"
                                               "0,0,0,0,0,"
                                               "0,0,0,0,0,"
                                               "0,16,16,0,0,"
                                               "0,0,0,420"))
        # Third camera view
        self.node_file_rows.append(NodeFileRow("4,1,4,0,2,"
                                               "1,4,0,0,0,"
                                               "0,0,0,1,0,"
                                               "0,0,0,0,0,"
                                               "0,0,0,1,-0,"
                                               "1,1,1,0,-90,"
                                               "7,0,0,1,0,"
                                               "0,0,90,0,0,"
                                               "0,0,0,0,0,"
                                               "0,0,0,0,0,"
                                               "0,1,0,0.1,0,"
                                               "50,101,101,255,0,"
                                               "0,0,0,0,0,"
                                               "0,0,0,0,0,"
                                               "0,0,0,0,0,"
                                               "0,0,0,0,0,"
                                               "0,0,0,0,0,"
                                               "0,16,16,0,0,"
                                               "0,0,0,420"))
        # Fourth camera view
        self.node_file_rows.append(NodeFileRow("5,1,5,0,2,"
                                               "1,5,0,0,0,"
                                               "0,0,0,1,0,"
                                               "0,0,0,0,0,"
                                               "0,0,-1,-0,-0,"
                                               "1,1,1,85,0,"
                                               "7,0,0,1,0,"
                                               "0,0,90,270,0,"
                                               "0,0,0,0,0,"
                                               "0,-0,0,0,0,"
                                               "0,1,0,0.1,0,"
                                               "50,101,101,255,0,"
                                               "0,0,0,0,0,"
                                               "0,0,0,0,0,"
                                               "0,0,0,0,0,"
                                               "0,0,0,0,0,"
                                               "0,0,0,0,0,"
                                               "0,16,16,0,0,"
                                               "0,0,0,420"))
        # Default Grid
        self.node_file_rows.append(NodeFileRow("6,6,6,1,0,"
                                               "0,0,1,0,0,"
                                               "0,0,0,1,360,"
                                               "220,0,0,0,0,"
                                               "0,0,0,0,0,"
                                               "1,1,1,0,0,"
                                               "0,0,0,1,0,"
                                               "0,0,0,0,0,"
                                               "0,0,0,0,0,"
                                               "0,0,0,0,0,"
                                               "0,1,0,0.1,3,"
                                               "0,0,255,150,0,"
                                               "0,0,0,0,0,"
                                               "0,0,0,0,0,"
                                               "0,0,0,0,0,"
                                               "0,0,0,0,0,"
                                               "0,0,0,0,0,"
                                               "0,1,1,0,0,"
                                               "0,0,0,420"))


class AntzGlyph:
    """
    Class used to duplicate and edit individual instances glyphs to be rendered in OpenAntz
    Construct using node file generated from antz that contains only one glyph.

    Attributes:
        node_file_rows (List[NodeFileRow]) -  list of NodeFileRows that make up the glyph
    """

    def __init__(self, csv_file_name: str = "", remove_global_params: bool = True, make_ids_consecutive: bool = True):
        """
        Parameters:
            csv_file_name (str: "") - name of the glyph template csv file (default: "")
            remove_global_params (bool: True) - remove rows with an IDs that are 1-7 (default: True)
            make_IDs_consecutive (bool: True) - remove gaps in between row IDs. i.e 1,2,4 becomes 1,2,3 (default: True)

        Raises: RuntimeError
        """

        self.node_file_rows = []

        csv_file_name = str(csv_file_name)
        if not csv_file_name.endswith(".csv"):
            raise RuntimeError("csv_file_name must be name of csv file (must include '.csv'")

        if csv_file_name != "":
            self.__populate_glyph__(csv_file_name, remove_global_params, make_ids_consecutive)
        else:
            raise RuntimeError("antz_glyph was constructed without a csv file name")

    def length(self):
        """ Returns the number of NodeFileRows in this file. (int) """
        return len(self.node_file_rows)

    def get_last_row(self):
        """ Returns the last NodeFileRow of the file. (NodeFileRow) """
        return self.node_file_rows[self.length() - 1]

    def get_row_by_id(self, row_id: int):
        """
        Returns the row with the given ID, None if no row found

        Parameters:
            row_id (int: None) - ID of requested NodeFileRow

        Returns: NodeFileRow, None
        """
        for row in self.node_file_rows:
            if row.id == row_id:
                return row

    def increment_ids(self, match_data_and_record_id_to_id: bool = True):
        """
        Iterates over each NodeFileRow in the glyph and updates its ID, parent ID, and child ID reflect as a new glyph in a node
        file starting with the highest ID + 1. This is called automatically when adding glyph to NodeFile

        Parameters:
            match_data_and_record_id_to_id (bool: True) - Should the rows update their record ID and data to match their ID?

        Returns: None

        """
        self.make_ids_consecutive(self.node_file_rows[len(self.node_file_rows) - 1].id + 1,
                                      match_data_and_record_id_to_id)

    def unselect_all(self):
        """
        Changes the selected property of all glyph node file rows to 0.
        When glyph template files are saved via "save selected",
        each row is marked selected, use this to reverse this effect

        Returns: None
        """

        for row in self.node_file_rows:
            row.selected = 0

    def freeze_all(self, freeze=True):
        if freeze:
            for row in self.node_file_rows:
                row.freeze = 1
        else:
            for row in self.node_file_rows:
                row.freeze = 1

    def match_record_ids_and_data_to_ids(self):
        """
        Iterates over each NodeFileRow in the glyph and matches its record id and data to its id

        Returns: None
        """
        for row in self.node_file_rows:
            row.set_id(row.id)

    def get_rows_of_branch_level(self, branch_level):
        """ Returns a list of NodeFileRow's of a given branch level"""
        rows = []
        for row in self.node_file_rows:
            if row.branch_level == branch_level:
                rows.append(row)
        return rows

    def remove_rows_of_branch_level(self, branch_level):
        """
        Removes all NodeFileRow's of a given branch level

        Parameters:
            branch_level - branch level of all removed items (default: None)

        Returns: None
        """
        rows = self.get_rows_of_branch_level(branch_level)

        for row in rows:
            self.node_file_rows.remove(row)

    def make_ids_consecutive(self, starting_id: int = 8,  match_data_and_record_id_to_id: bool=True ):
        """
        Removes gaps in ids. i.e IDs 1,2,4 become 1,2,3
        Can also be used to change the ID's of the glyph to start from a specified index

        Parameters:
            starting_id (int: 8) - first id of the glyph
            match_data_and_record_id_to_id (bool: True) - set true to set the data and record id of each row to match its id

        Returns: None
        """
        # keys = old IDs, values = new IDs
        ids = {0:0}
        if self.node_file_rows[0].parent_id != 0:
            ids[self.node_file_rows[0].parent_id] = self.node_file_rows[0].parent_id
        current_id = starting_id


        for row in self.node_file_rows:
            # replace old IDs with new IDs
            row.parent_id = ids[row.parent_id]
            row.child_id = ids[row.child_id]

            # map old ID to new ID
            ids[row.id] = current_id

            if match_data_and_record_id_to_id:
                row.set_id(current_id)

            current_id += 1

    def __populate_glyph__(self, csv_file_name: str = "",
                           remove_global_params: bool = False,
                           make_ids_consecutive: bool = True,
                           match_data_and_record_id_to_id: bool = True):

        df = pd.read_csv(csv_file_name)
        df = df.applymap(lambda cell: int(cell) if str(cell).endswith('.0') else cell)

        for index, row in df.iterrows():
            line = ""
            for column in df.columns:
                line += str(row[column]) + ","
            line = line[:len(line) - 1]

            ntr = NodeFileRow(line)
            if (not remove_global_params) or (remove_global_params and ntr.id not in range(8)):
                self.node_file_rows.append(NodeFileRow(line))

        i = 0
        for row in self.node_file_rows:
            if row.id in range(8):
                raise RuntimeError("Glyph template csv contains row id's between 1-7. "
                                   "Perhaps you generated the file in Antz using 'K' as opposed to 'ALT + K'")
            i += 1

        if make_ids_consecutive:
            self.make_ids_consecutive(8, match_data_and_record_id_to_id)




class NodeFileRow:
    """
    Container of properties and property setters for node file rows.

    Attributes:
        geos             - dictionary mapping names of shapes to IDs
        topos            - dictionary mapping names of topos to IDs
        colors           - dictionary mapping names of color names to int list
        id               - node ID used for pin tree relationship graph
        _type            - node type - 1: Camera; 2: video; 3: Surface;
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
        color_index      - color index from color palette
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
        "chcolate": [210, 105, 30],
        "medium spring green": [0, 250, 154],
        "golden rod": [218, 165, 32],
        "coral": [255, 127, 80]
    }

    def __init__(self, comma_string: str = ""):
        """
        Parameters:
             comma_string (str: "") - a string with 94 comma seperated values in the order of an antz node file.

        Raise: RuntimeError
        """

        # region properties

        self.id = 8  # node ID used for pin tree relationship graph
        self._type = 5  # node type - 1: Camera; 2: video; 3: Surface; 4: Points, 5:Pin, 6:Grid
        self.data = 8  # node type - 1: Camera; 2: video; 3: Surface; 4: Points, 5:Pin, 6:Grid

        # selection set status, 1 if part of active set, 0 if not
        # Useful if you want the root nodes selected upon loading.
        self.selected = 0

        self.parent_id = 0  # ID of parent node
        self.branch_level = 0  # root node is 0, each sub-level is 1, 2, 3, … n
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
        self.color_index = 0  # color index from color palette

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

        if not isinstance(comma_string, str):
            raise RuntimeError('comma_string must be of type str')
        if comma_string == "":
            return
        values = comma_string.split(",")

        self.set_properties_from_string_list(values)

    def set_properties_from_string_list(self, values: List[str]):
        """

        Parameters:
            values (List[str]) - list of strings that can be cast as integrals

        Returns: None

        Raises: RuntimeError

        """
        if len(values) != 94:
            raise RuntimeError("Comma separated string has incorrect number of values.\n Values length = " +
                               str(len(values)) + "\nInput: " + str(values))
        self.id = int(float(values[0]))
        self._type = int(float(values[1]))
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
        self.color_shift = int(float(values[20]))
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
        self.rotate_rate_x = int(float(values[34]))
        self.rotate_rate_y = int(float(values[35]))
        self.rotate_rate_z = int(float(values[36]))
        self.rotate_x = float(values[37])
        self.rotate_y = float(values[38])
        self.rotate_z = float(values[39])
        self.scale_rate_x = int(float(values[40]))
        self.scale_rate_y = int(float(values[41]))
        self.scale_rate_z = int(float(values[42]))
        self.translate_rate_x = int(float(values[43]))
        self.translate_rate_y = int(float(values[44]))
        self.translate_rate_z = int(float(values[45]))
        self.translate_vec_x = int(float(values[46]))
        self.translate_vec_y = int(float(values[47]))
        self.translate_vec_z = int(float(values[48]))
        self.shader = int(float(values[49]))
        self.geometry = int(float(values[50]))
        self.line_width = int(float(values[51]))
        self.point_size = int(float(values[52]))
        self.ratio = float(values[53])
        self.color_index = int(float(values[54]))
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
        self.set_hi_x = int(float(values[74]))
        self.set_hi_y = int(float(values[75]))
        self.set_hi_z = int(float(values[76]))
        self.set_lo_x = int(float(values[77]))
        self.set_lo_y = int(float(values[78]))
        self.set_lo_z = int(float(values[79]))
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

    def print_properties(self):
        """
        Prints the label and value of each property.

        Returns: None
        """
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
        print("color_index: " + str(self.color_index))
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
               str(self.color_index) + "," + \
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

    def set_id(self, row_id: int):
        """
        Sets id, record_id, and data to row_id

        Parameters:
            row_id (int: None) - number to set id, record_id and row_id to

        Returns: None

        Raises: TypeError
        """

        row_id = int(row_id)

        self.id = row_id
        self.record_id = row_id
        self.data = row_id

    def set_tag(self, tag_text, tag_mode: int = 0):
        """
        Sets tag_text and tag_mode

        Parameters:

        :param tag_text: (default "")
        :param tag_mode: (default 0)

        Returns: None

        Raises: TypeError
        """
        tag_mode = int(tag_mode)
        self.tag_text = tag_text
        self.tag_mode = tag_mode

    def set_aux_a(self, x: int = 30, y: int = 30, z: int = 30):
        """
        Sets aux_a_x, y, and z

        Parameters:
            x (int: 30)
            y (int: 30)
            z (int: 30)

        Returns: None

        Raises: TypeError
        """

        x = int(x)
        y = int(y)
        z = int(z)

        self.aux_a_x = x
        self.aux_a_y = y
        self.aux_a_z = z

    def set_aux_b(self, x: int = 30, y: int = 30, z=30):
        """
        Sets aux_b_x,y, and z

        Parameters:
            x (int: 30)
            y (int: 30)
            z (int: 30)

        Returns: None

        Raises: TypeError
        """

        x = int(x)
        y = int(y)
        z = int(z)

        self.aux_b_x = x
        self.aux_b_y = y
        self.aux_b_z = z

    def set_rotate_vec(self, x: int = 0, y: int = 0, z: int = 0, s: int = 0):
        """
        Sets rotate_vec_x, y, z, and s

        Parameters:
            x (int: 0)
            y (int: 0)
            z (int: 0)
            s (int: 0)

        Returns: None

        Raises: TypeError
        """

        x = int(x)
        y = int(y)
        z = int(z)
        s = int(s)

        self.rotate_vec_x = x
        self.rotate_vec_y = y
        self.rotate_vec_z = z
        self.rotate_vec_s = s

    def set_scale(self, x: float = 1, y: float = 1, z: float = 1):
        """
        Sets scale_x, y, z

        Parameters:
            x (int: 1)
            y (int: 1)
            z (int: 1)

        Returns: None

        Raises: TypeError
        """

        x = float(x)
        y = float(y)
        z = float(z)

        self.scale_x = x
        self.scale_y = y
        self.scale_z = z

    def set_u_scale(self, scale: float = 1):
        scale = float(scale)
        self.set_scale(scale, scale, scale)

    def set_translate(self, x: float = 0, y: float = 0, z: float = 0):
        """
        Sets translate_x, y, z

        Parameters:
            x (int: 0)
            y (int: 0)
            z (int: 0)

        Returns: None

        Raises: TypeError
        """

        x = float(x)
        y = float(y)
        z = float(z)

        self.translate_x = x
        self.translate_y = y
        self.translate_z = z

    def set_tag_offset(self, x: float = 0, y: float = 0, z: float = 0):
        """
        Sets tag_offset_x, y, z

        Parameters:
            x (int: 0)
            y (int: 0)
            z (int: 0)

        Returns: None

        Raises: TypeError
        """

        x = float(x)
        y = float(y)
        z = float(z)

        self.tag_offset_x = x
        self.tag_offset_y = y
        self.tag_offset_z = z

    def set_rotate(self, x: float = 0, y: float = 0, z: float = 0):
        """
        Sets rotate_x, y, z

        Parameters:
            x (int: 0)
            y (int: 0)
            z (int: 0)

        Returns: None

        Raises: TypeError
        """

        x = float(x)
        y = float(y)
        z = float(z)

        self.rotate_x = x
        self.rotate_y = y
        self.rotate_z = z

    def set_rotate_rate(self, x: int = 0, y: int = 0, z: int = 0):
        """
        Sets rotate_rate_x, y, z

        Parameters:
            x (int: 0)
            y (int: 0)
            z (int: 0)

        Returns: None

        Raises: TypeError
        """

        x = int(x)
        y = int(y)
        z = int(z)

        self.rotate_rate_x = x
        self.rotate_rate_y = y
        self.rotate_rate_z = z

    def set_scale_rate(self, x: int = 0, y: int = 0, z: int = 0):
        """
        Sets scale_rate_x, y, z

        Parameters:
            x (int: 0)
            y (int: 0)
            z (int: 0)

        Returns: None

        Raises: TypeError
        """

        x = int(x)
        y = int(y)
        z = int(z)

        self.scale_rate_x = x
        self.scale_rate_y = y
        self.scale_rate_z = z

    def set_translate_rate(self, x: int = 0, y: int = 0, z: int = 0):
        """
        Sets translate_rate_x, y, z

        Parameters:
            x (int: 0)
            y (int: 0)
            z (int: 0)

        Returns: None

        Raises: TypeError
        """

        x = int(x)
        y = int(y)
        z = int(z)

        self.translate_rate_x = x
        self.translate_rate_y = y
        self.translate_rate_z = z

    def set_translate_vec(self, x: int = 0, y: int = 0, z: int = 0):
        """
        Sets translate_vec_x, y, z

        Parameters:
            x (int: 0)
            y (int: 0)
            z (int: 0)

        Returns: None

        Raises: TypeError
        """

        x = int(x)
        y = int(y)
        z = int(z)

        self.translate_vec_x = x
        self.translate_vec_y = y
        self.translate_vec_z = z

    def set_color(self, r: int = 0, g: int = 0, b: int = 0, a: int = 255):
        """
        Sets color values

        Parameters:

        r (int: 0) - red (int) 0-255 (default 0)
        g (int: 0) - green (int) 0-255 (default 0)
        b (int: 0) - blue (int) 0-255 (default 0)
        a (int: 255) - transparency 0-255 (default 255)

        Returns: None

        Raises: TypeError
        """

        r = int(r)
        g = int(g)
        b = int(b)
        a = int(a)

        self.color_r = r
        self.color_g = g
        self.color_b = b
        self.color_a = a

    def set_color_by_name(self, color: str):
        """

        Parameters:
            color:

        Returns: None

        Raises: TypeError
        """
        if not isinstance(color, str):
            raise TypeError("color must be of type string")

        self.color_r = self.colors[color][0]
        self.color_g = self.colors[color][1]
        self.color_b = self.colors[color][2]
        self.color_a = 255

    def color_to_list(self):
        """
        Returns a list with rgba values of the nodes current color

        Returns: List
        """
        return [self.color_r, self.color_g, self.color_b, self.color_a]

    def set_auto_zoom(self, x: int = 0, y: int = 0, z: int = 0):
        """
        Sets auto_zoom_x, y, z

        Parameters:
            x (int: 0)
            y (int: 0)
            z (int: 0)

        Returns: None

        Raises: TypeError
        """

        x = int(x)
        y = int(y)
        z = int(z)

        self.auto_zoom_x = x
        self.auto_zoom_y = y
        self.auto_zoom_z = z

    def set_trigger_hi(self, x: int = 0, y: int = 0, z: int = 0):
        """
        Sets trigger_hi_x, y, z

        Parameters:
            x (int: 0)
            y (int: 0)
            z (int: 0)

        Returns: None

        Raises: TypeError
        """
        x = int(x)
        y = int(y)
        z = int(z)

        self.trigger_hi_x = x
        self.trigger_hi_y = y
        self.trigger_hi_z = z

    def set_trigger_lo(self, x: int = 0, y: int = 0, z: int = 0):
        """
        Sets trigger_low_x, y, z

        Parameters:
            x (int: 0)
            y (int: 0)
            z (int: 0)

        Returns: None

        Raises: TypeError
        """
        x = int(x)
        y = int(y)
        z = int(z)

        self.trigger_lo_x = x
        self.trigger_lo_y = y
        self.trigger_lo_z = z

    def set_set_hi(self, x: int = 0, y: int = 0, z: int = 0):
        """
        Sets hi_x, y, z

        Parameters:
            x (int: 0)
            y (int: 0)
            z (int: 0)

        Returns: None

        Raises: TypeError
        """

        x = int(x)
        y = int(y)
        z = int(z)

        self.set_hi_x = x
        self.set_hi_y = y
        self.set_hi_z = z

    def set_set_lo(self, x: int = 0, y: int = 0, z: int = 0):
        """
        Sets lo_x, y, z

        Parameters:
            x (int: 0)
            y (int: 0)
            z (int: 0)

        Returns: None

        Raises: TypeError
        """

        x = int(x)
        y = int(y)
        z = int(z)

        self.set_lo_x = x
        self.set_lo_y = y
        self.set_lo_z = z

    def set_proximity(self, x: float = 0, y: float = 0, z: float = 0):
        """
        Sets proximity_x, y, z

        Parameters:
            x (int: 0)
            y (int: 0)
            z (int: 0)

        Returns: None

        Raises: TypeError
        """

        x = float(x)
        y = float(y)
        z = float(z)

        self.proximity_x = x
        self.proximity_y = y
        self.proximity_z = z

    def set_proximity_mode(self, x: int = 0, y: int = 0, z: int = 0):
        """
        Sets proximity_mode_x, y, z

        Parameters:
            x (int: 0)
            y (int: 0)
            z (int: 0)

        Returns: None

        Raises: TypeError
        """

        x = int(x)
        y = int(y)
        z = int(z)

        self.proximity_mode_x = x
        self.proximity_mode_y = y
        self.proximity_mode_z = z

    def set_segments(self, x: int = 20, y: int = 12, z: int = 0):
        """
        Sets segments_x, y, z

        Parameters:
            x (int: 20)
            y (int: 12)
            z (int: 0)

        Returns: None

        Raises: TypeError
        """

        x = int(x)
        y = int(y)
        z = int(z)

        self.segments_x = x
        self.segments_y = y
        self.segments_z = z

    # endregion

