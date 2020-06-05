import os

Image_size = 128
Screen_Size = 512
side_tiles = 4
total_tiles = 16
margin = 4

ASSET_DIR = 'assets'

Files_list = []

for x in os.listdir(ASSET_DIR) :
    if x[-3:].lower() == 'png':
        Files_list.append(x)


assert len(Files_list) == 8


