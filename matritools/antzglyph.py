import pandas as pd
from .nodefilerow import NodeFileRow

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
