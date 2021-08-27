NodeFile
========
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

.. toctree::
   :maxdepth: 1

   Constructor <nodefile-constructor>
   Attributes <nodefile-attributes>
   length <nodefile-length>
   get_last_row <nodefile-get_last_row>
   get_row_by_id <nodefile-get_row_by_id>
   make_link <nodefile-make_link>
   write_to_csv <nodefile-write_to_csv>
   create_node_row <nodefile-create_node_row>
   add_glyph <nodefile-add_glyph>
   to_dataframe <nodefile-to_dataframe>