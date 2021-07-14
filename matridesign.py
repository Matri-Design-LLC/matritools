# Last updated 7/9/21 : 4:22PM PST

import pandas as pd
import numbers
from ast import literal_eval
import json
import copy

# ***********************
# Commonly used functions
# ***********************

#region commonly used functions

#region data exploration

def print_df_column_set(df, column, print_sets=False):
    """
    Prints every out the number unique values in a dataframe column
    :param df: target data frame
    :param column: target column
    :param print_sets: Set True to print out each of the unique values
    :return: None
    """
    col_list = df[column].tolist()
    col_set = set(col_list)

    if print_sets:
        print("\n\t" + column + ", \tLength: " + str(len(col_set)) + "\n")
        for value in col_set:
            print("\t\t" + str(value))
    else:
        print("\t" + column + ", \tLength: " + str(len(col_set)))

def print_df_column_min_max(df, min_max_columns):
    """
    Prints out the min and make of each column in a data frame
    :param df: target data frame
    :param min_max_columns: list of target columns
    :return: None
    """
    for column in min_max_columns:
        if issubclass(df[column].dtype.type, numbers.Integral):
            print("\t" + column + ", \tMin: " + str(df[column].min()) + ", \tMax: " + str(df[column].max()))

def explore_df(df, set_columns=None, min_max_columns=None, print_sets=False):
    """
    Prints out the number of unique values from a list of columns for a data frame as well as the min and max values of each column
    :param df: target dataframe
    :param set_columns: list of columns to display number of unique values (default None)
    :param min_max_columns: list of columns to display min and max values (default None)
    :param print_sets: Set True to print out each of the unique values of the given columns (default False)
    :return:
    """

    print("Shape: " + str(df.shape))
    __explore_sets__(df, set_columns, print_sets)

    if min_max_columns is not None:
        print("\nIntergral Min/Max:")
        print_df_column_min_max(df, min_max_columns)

def __explore_sets__(df, set_columns, print_sets):
    """
    Helper function that calls print_df_column_set as well as a label depending on value of print_sets
    :param df: target dataframe
    :param set_columns: list of columns to display number of unique values
    :param print_sets: Set True to print out each of the unique values of the given columns
    :return:
    """
    if set_columns is None:
        return
    if print_sets:
        print("Sets:")
    else:
        print("Set Lengths:")
    for column in set_columns:
        print_df_column_set(df, column, print_sets)

#endregion

def create_df_from_json(json_file_name):
    with open(json_file_name) as json_data:
        return pd.DataFrame(json.load(json_data))


def create_df_from_json_string(json_string):
    return pd.DataFrame(json.load(json_string))

#region data manipulation

def interpolate_df_column(df, column, obj_scale_min, obj_scale_max, column_tail):
    """
    Scales the values of a data frame column between obj_scale_min and obj_scale_max.
    Adds the interpolated data into a new column labeled (original column name) + (column_tail) and preserves original
    un-interpolated data.

    :param df:
    :param column:
    :param obj_scale_min:
    :param obj_scale_max:
    :param column_tail:
    :return:
    """
    col_min = df[column].min()
    col_max = df[column].max()
    col_list = df[column].tolist()
    scalar = make_interpolater(col_min + .0002, col_max, obj_scale_min, obj_scale_max)
    col_interp = [scalar(x) for x in col_list]
    df[(column + column_tail)] = col_interp


def make_interpolater(old_min, old_max, new_min, new_max):
    """
    Creates a reusable interpolation function to scale a value in between a new min and new max

    :param old_min:
    :param old_max:
    :param new_min:
    :param new_max:
    :return: interpolation function
    """

    # Figure out how 'wide' each range is
    old_span = old_max - old_min
    new_span = new_max - new_min

    # Compute the scale factor between old and new values
    scale_factor = float(new_span) / float(old_span)

    # create interpolation function using pre-calculated scaleFactor
    def interp_fn(value):
        """
        Scale a value in between a set min and  max
        :param value: value to be interpolated
        :return: float
        """
        return new_min + (value - old_min) * scale_factor

    return interp_fn



def separate_compound_dataframe(df, evaluate_df=True, name_template=""):
    """
    Use to create a list of data frames from a dataframe with embedded lists.

    :param df: a data frame that has lists of data contained in individual cells
    :param evaluate_df: set True to apply literal_eval (default True)
    :param name_template: individual data frame columns = lambda x: (name_template + "{}").format(x + 1) (default "")
    :return: list of data frames


    I.E when a data frame is in the form of :

    [ [ 11, 12, 13], [ 14, 15, 16 ], [ 17, 18, 19 ] ]
    [ [ 21, 22, 23], [ 24, 25, 26 ], [ 27, 28, 29 ] ]
    [ [ 31, 32, 33], [ 34, 35, 36 ], [ 37, 38, 39 ] ]

    returns

    df1 [ 11, 12, 13]  df2 [ 14, 15, 16 ]  df3 [ 17, 18, 19 ]
        [ 21, 22, 23]      [ 24, 25, 26 ]      [ 27, 28, 29 ]
        [ 31, 32, 33]      [ 34, 35, 36 ]      [ 37, 38, 39 ]
    """
    # Expand evaluate tupled data into lists
    if evaluate_df:
        for column in df.columns:
            df[column] = df[column].apply(literal_eval)

    df_list = []

    l = lambda x: (name_template + "{}").format(x + 1)
    for column in df.columns:
        df_list.append(pd.DataFrame(df[column].values.tolist(), df.index, dtype=object).fillna(17).rename(columns=l))

    return df_list

#endregion

#region utility

def find_index_in_set(value_set, value):
    """
    returns the index of a value in a set as if it were a list
    :param value_set: target set
    :param value: target value
    :return: (int) index of value in value_set, returns -1 if value is not in value_set
    """
    index = 0
    for i in value_set:
        if value == i:
            return index
        index += 1
    return -1

def set_to_list(value_set):
    """
    Converts a set to a list
    :param value_set: target set
    :return: list
    """
    result = []
    for value in value_set:
        result.append(value)
    return result

#endregion
#endregion




# *****************
# Node File Classes
# *****************

class NodeFile:
    """
    Virtual representation of an ANTZ node csv

    Used to construct a virtual antz node file.
    On construction, provide a file name. The constructor will append "_node.csv" to the end of the provided file name.

    Basic usage:
      After created node_file class, set the properties of the class to what you want a node csv file row to be,
      then call create_node_file_row.

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
            raise RuntimeError("Comma seperated string has incorrect number of values")

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


class AntzGlyph:
    """
    Used to represent a antz_glyph. Construct using node file generated from antz that contains only one glyph.
    node_file_rows[0] is the root object.
    """
    node_file_rows = []

    def __init__(self, csv_file_name):
        """
        :param csv_file_name: name of the glyph template csv file
        """
        if csv_file_name != "":
            df = pd.read_csv(csv_file_name)
            df = df.applymap(lambda cell: int(cell) if str(cell).endswith('.0') else cell)
            for index, row in df.iterrows():
                line = ""
                for column in df.columns:
                    line += str(row[column]) + ","
                line = line[:len(line) - 1]
                self.node_file_rows.append(NodeFileRow(line))
        else:
            raise RuntimeError("antz_glyph was constructed without a csv file name")

    def increment_node_file_rows(self):
        """
        Use this to update the ids, parent ids, data, and record_id of each row of the glyph to represent a new glyph.
        By default this gets called when adding glyph to node file.
        :return: None
        """
        old_parent_ids = []
        new_parent_ids = []

        old_parent_ids.append(self.node_file_rows[0].properties.id)
        row_id = self.node_file_rows[len(self.node_file_rows) - 1].properties.id
        row_id += 1
        new_parent_ids.append(row_id)
        self.node_file_rows[0].properties.set_id(row_id)
        self.node_file_rows[0].properties.tag_text = ""

        for row in self.node_file_rows[1:]:
            row_id += 1
            row.properties.set_id(row_id)
            row.properties.tag_text = ""

            # find parent objects and give them updated parent ids
            if row.properties.parent_id not in old_parent_ids:
                old_parent_ids.append(row.properties.parent_id)
                new_parent_ids.append(row_id - 1)
                row.properties.parent_id = row_id - 1
            else:
                parent_id_index = self.__find_old_parent_id_index__(row, old_parent_ids)

                row.properties.parent_id = new_parent_ids[parent_id_index]

    def unselect_all(self):
        """ Changes the selected property of all node file rows to 0. """
        for row in self.node_file_rows:
            row.properties.selected = 0

    def match_record_ids_and_data_to_ids(self):
        for row in self.node_file_rows:
            row.properties.set_id(row.properties.id)

    def get_rows_of_branch_level(self, branch_level):
        """ Returns a list of NodeFileRow's of a given branch level"""
        rows = []
        for row in self.node_file_rows:
            if row.properties.branch_level == branch_level:
                rows.append(row)
        return rows

    def remove_rows_of_branch_level(self, branch_level):
        """ removes all NodeFileRow's of a given branch level"""
        rows = self.get_rows_of_branch_level(branch_level)

        for row in rows:
            self.node_file_rows.remove(row)


    @staticmethod
    def __find_old_parent_id_index__(row, old_parent_ids):
        parent_id_index = 0
        for row_id in old_parent_ids:
            if row.properties.parent_id != old_parent_ids[parent_id_index]:
                parent_id_index += 1
            else:
                return parent_id_index

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

    # endregion
