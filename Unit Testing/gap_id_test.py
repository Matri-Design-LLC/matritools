import pandas as pd
from matritools import nodefile as nf
import os
# *************************
# Set up node and tag files
# *************************
ntf = nf.NodeFile("gbm")
glyph = nf.AntzGlyph("gumball.csv")
glyphDist = 20
glyphIndex = 0
# ********************************
# Setup node file helper functions
# ********************************
def make_gbm():
    global glyphIndex

    #scale
    #location
    glyph.node_file_rows[0].translate_x = glyphDist*glyphIndex
    ntf.add_glyph_to_node_file_rows(glyph)
    glyph.increment_node_file_rows()
    glyphIndex += 1
def populate_node_and_tag_file():
    for index in range(10):
        make_gbm()

populate_node_and_tag_file()
# Write node csv file
ntf.write_to_csv()
#open atz from file placed in working directory after node file creation
#os.system(os.path.join(os.sys.path[0], "antz-xr_2021-06-22_app/ANTz-Xr.exe"))