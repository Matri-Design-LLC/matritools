.. matritools documentation master file, created by
   sphinx-quickstart on Sat Jul 24 13:01:51 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Matritools
======================================

Matritools is a python library that makes 3D data visualization files to be rendered in OpenANTz
as well as commonly used data manipulation functions used by Matri Design LLC.

* Learn more at:
   * `Matri Design <https://www.matridesign.com/>`_
   * `OpenANTz <https://antzglyphs.com/>`_
   * `OpenANTz GitHub <https://github.com/openantz/antz>`_


.. toctree::
   :maxdepth: 2
   :caption: Contents:

.. note::

   This project is under active development.



API
==================

nodefile
-------
* `NodeFile <https://matritools.readthedocs.io/en/main/nodefile.html>`_
   * `Constructor <https://matritools.readthedocs.io/en/main/nodefile-constructor.html>`_
   * `Attributes <https://matritools.readthedocs.io/en/main/nodefile-attributes.html>`_
   * `get_row_by_index <https://matritools.readthedocs.io/en/main/nodefile-get_row_by_index.html>`_
   * `get_row_by_id <https://matritools.readthedocs.io/en/main/nodefile-get_row_by_id.html>`_
   * `write_to_csv <https://matritools.readthedocs.io/en/main/nodefile-write_to_csv.html>`_
   * `check_for_duplicate_id <https://matritools.readthedocs.io/en/main/nodefile-check_for_duplicate_id.html>`_
   * `create_node_row <https://matritools.readthedocs.io/en/main/nodefile-create_node_row.html>`_
   * `add_glyph <https://matritools.readthedocs.io/en/main/nodefile-add_glyph.html>`_
   * `to_dataframe <https://matritools.readthedocs.io/en/main/nodefile-to_dataframe.html>`_
   * `__add_initial_rows__ <https://matritools.readthedocs.io/en/main/nodefile-__add_initial_rows__.html>`_

* `AntzGlyph <https://matritools.readthedocs.io/en/main/antzglyph.html>`_
   * `Constructor <https://matritools.readthedocs.io/en/main/antzglyph-constructor.html>`_
   * `Attributes <https://matritools.readthedocs.io/en/main/antzglyph-attributes.html>`_
   * `increment_ids <https://matritools.readthedocs.io/en/main/antzglyph-increment_ids.html>`_
   * `unselect_all <https://matritools.readthedocs.io/en/main/antzglyph-unselect_all.html>`_
   * `match_record_ids_and_data_to_ids <https://matritools.readthedocs.io/en/main/antzglyph-match_record_ids_and_data_to_ids.html>`_
   * `get_rows_of_branch_level <https://matritools.readthedocs.io/en/main/antzglyph-get_rows_of_branch_level.html>`_
   * `remove_rows_of_branch_level_ <https://matritools.readthedocs.io/en/main/antzglyph-remove_rows_of_branch_level.html>`_
   * `make_ids_consecutive <https://matritools.readthedocs.io/en/main/antzglyph-make_ids_consecutive.html>`_

* `NodeFileRow <https://matritools.readthedocs.io/en/main/nodefilerow.html>`_
   * `Constructor <https://matritools.readthedocs.io/en/main/nodefilerow-constructor.html>`_
   * `Attributes <https://matritools.readthedocs.io/en/main/nodefilerow-attributes.html>`_
   * `set_properties_from_string_list <https://matritools.readthedocs.io/en/main/nodefilerow-set_properties_from_string_list.html>`_
   * `print_properties <https://matritools.readthedocs.io/en/main/nodefilerow-print_properties.html>`_
   * `to_string <https://matritools.readthedocs.io/en/main/nodefilerow-to_string.html>`_
   * `make_link <https://matritools.readthedocs.io/en/main/nodefilerow-make_link.html>`_
   * `set_id <https://matritools.readthedocs.io/en/main/nodefilerow.set_id.html>`_
   * `set_tag <https://matritools.readthedocs.io/en/main/nodefilerow-set_tag.html>`_
   * `set_aux_a <https://matritools.readthedocs.io/en/main/nodefilerow-set_aux_a.html>`_
   * `set_aux_b <https://matritools.readthedocs.io/en/main/nodefilerow-set_aux_b.html>`_
   * `set_rotate_vec <https://matritools.readthedocs.io/en/main/nodefilerow-set_rotate_vec.html>`_
   * `set_scale <https://matritools.readthedocs.io/en/main/nodefilerow-set_scale.html>`_
   * `set_translate <https://matritools.readthedocs.io/en/main/nodefilerow-set_translate.html>`_
   * `set_tag_offset <https://matritools.readthedocs.io/en/main/nodefilerow-set_tag_offset.html>`_
   * `set_rotate <https://matritools.readthedocs.io/en/main/nodefilerow-set_rotate.html>`_
   * `set_rotate_rate <https://matritools.readthedocs.io/en/main/nodefilerow-set_rotate_rate.html>`_
   * `set_translate_rate <https://matritools.readthedocs.io/en/main/nodefilerow-set_translate_rate.html>`_
   * `set_translate_vec <https://matritools.readthedocs.io/en/main/nodefilerow-set_translate.html>`_
   * `set_color <https://matritools.readthedocs.io/en/main/nodefilerow-set_color.html>`_
   * `set_auto_zoom <https://matritools.readthedocs.io/en/main/nodefilerow_set_auto_zoom.html>`_
   * `set_trigger_hi <https://matritools.readthedocs.io/en/main/nodefilerow_set_trigger_hi.html>`_
   * `set_trigger_lo <https://matritools.readthedocs.io/en/main/nodefilerow-set_trigger_lo.html>`_
   * `set_set_hi <https://matritools.readthedocs.io/en/main/nodefilerow-set_set_hi.html>`_
   * `set_set_lo <https://matritools.readthedocs.io/en/main/nodefilerow-set_set_lo.html>`_
   * `set_proximity <https://matritools.readthedocs.io/en/main/nodefilerow-set_proximity.html>`_
   * `set_proximity_mode <https://matritools.readthedocs.io/en/main/nodefilerow-set_proximity_mode.html>`_
   * `set_segments <https://matritools.readthedocs.io/en/main/nodefilerow-set_segments.html>`_

utils
-----
   * `create_df_from_json <https://matritools.readthedocs.io/en/main/utils-create_df_from_json.html>`_
   * `create_df_from_json_string <https://matritools.readthedocs.io/en/main/utils-create_df_from_json_string.html>`_
   * `interpolate_df_column <https://matritools.readthedocs.io/en/main/utils-interpolate_df_column.html>`_
   * `make_interpolator <https://matritools.readthedocs.io/en/main/utils-make_interpolator.html>`_
   * `separate_compound_dataframe <https://matritools.readthedocs.io/en/main/utils-seperate_compound_dataframe.html>`_
   * `find_index_in_set <https://matritools.readthedocs.io/en/main/utils-find_index_inset.html>`_
   * `set_to_list <https://matritools.readthedocs.io/en/main/utils-set_to_list.html>`_
dataexploration
---------------
   * `print_df_column_set <https://matritools.readthedocs.io/en/main/dataexploration-print_df_column_set.html>`_
   * `explore_df <dataexploration-explore_df>`_
