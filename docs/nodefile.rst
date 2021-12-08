NodeFile
========
Base Class:
    `NodeContainer <nodecontainer.html>`_
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
   write_to_csv <nodefile-write_to_csv>
   add_glyph <nodefile-add_glyph>