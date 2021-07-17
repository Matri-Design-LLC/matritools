import pandas as pd
import copy
from .nodefilerow import NodeFileRow, NodeRowProperties


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
    """

    taginc = 1  # line number for a tag file row

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

    node_file_rows = []

    def __init__(self, file_name):
        """
        :param file_name: name of node and tag file created on write_to_csv()
        """
        self.properties = NodeRowProperties()
        self.node_file_name = file_name
        self.__add_initial_rows__()

    def get_row_by_index(self, index):
        return self.node_file_rows[index]

    def get_row_by_id(self, row_id):
        for row in self.node_file_rows:
            if row.properties.id == row_id:
                return row

    def write_to_csv(self):
        """ Write all node_file_rows to csv. This will overwrite the file."""
        node_file = open(self.node_file_name + "_node.csv", "w")
        tag_file = open(self.node_file_name + "_tag.csv", "w")
        tag_file.write("id,record_id,table_id,title,description\n")

        node_file.write(self.header)

        for file_row in self.node_file_rows:
            node_file.write(file_row.properties.to_string())
            if file_row.properties.tag_text != "":
                tag_text = str(self.taginc) + "," + \
                           str(file_row.properties.record_id) + ",0,\"" + \
                           str(file_row.properties.tag_text) + "\",\"\"\n"

                self.taginc += 1
                tag_file.write(tag_text)

        node_file.close()

    def create_node_row(self, tag_text=""):
        """
        Creates a node file row from node_file current properties and increments id by 1
        :param tag_text: text that will be written in the tag file associated with this node file row (default "")
        :return: None
        """
        node_row = NodeFileRow(self.properties.to_string())
        self.node_file_rows.append(node_row)
        if tag_text != "":
            node_row.properties.tag_text = tag_text
        self.properties.set_id(self.properties.id + 1)

    def add_glyph_to_node_file_rows(self, glyph):
        """
        Appends all rows of a glyph to node_file_rows and increments glyph template id, parent_id, data, and record_id
        :param glyph:
        :return: None
        """
        for row in glyph.node_file_rows:
            self.node_file_rows.append(copy.deepcopy(row))
        glyph.increment_node_file_rows()

    def to_dataframe(self):
        """ returns a data frame with all node file rows """
        list_of_lists = []
        for row in self.node_file_rows:
            columns = []
            for column in row.properties.to_string().split(","):
                columns.append(column)
            list_of_lists.append(columns)
        return pd.DataFrame(list_of_lists)

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