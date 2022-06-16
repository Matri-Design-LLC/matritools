types = {
	'world': 0,
	'camera': 1,
	'video': 2,
	'surface': 3,
	'point': 4,
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

main_grid_id = 7
main_camera_id = 2

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