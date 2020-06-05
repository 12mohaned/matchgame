import os, random
import game_config as gc
from pygame import image, transform 

animals_count = dict((a,0) for a in gc.Files_list)

def available_animals():
        animals = []
        for a,c in animals_count.items():
            if c < 2 :
                animals.append(a)
        return animals

class Animal:
    def __init__ (self,index):
        self.index = index
        self.row = index // gc.side_tiles
        self.col = index % gc.side_tiles
        self.name = random.choice(available_animals())
        animals_count[self.name] +=1
        self.image_path = os.path.join(gc.ASSET_DIR,self.name)
        self.image = image.load(self.image_path)
        self.image = transform.scale(self.image,(gc.Image_size - 2 * gc.margin,gc.Image_size - 2*gc.margin))
        self.box = self.image.copy()
        self.box.fill((200,200,200))
        self.skip = False



