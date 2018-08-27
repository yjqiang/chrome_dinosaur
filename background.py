import utils
import scene
from ground import Ground
from cloud import Cloud
from cactus import Cactus
import random


class Grounds(scene.Node):
    def __init__(self, speed=-5):
        texture, size = utils.load_sprite_sheet('ground.png', 1, 1)[0]
        self.ground0 = Ground(texture, size, scene.Point(0, 0))
        self.ground1 = Ground(texture, size, scene.Point(size.x, 0))
        self.add_child(self.ground0)
        self.add_child(self.ground1)
        self.position = scene.Point(0, 0)
        self.velocity = speed

    def update(self):
        self.position += (self.velocity, 0)
        self.ground0.update(self.position.x)
        self.ground1.update(self.position.x)
        

class Clouds(scene.Node):
    def __init__(self, speed, scene_size_x):
        self.position = scene.Point(0, 0)
        self.velocity = -2
        
        texture, size = utils.load_sprite_sheet('cloud.png', 1, 1, int(90*30/42), 30)[0]
        position = scene.Point(-200, random.randrange(90, 150))
        cloud0 = Cloud(texture, size, position, scene_size_x)
        cloud1 = Cloud(texture, size, position, scene_size_x)
        cloud2 = Cloud(texture, size, position, scene_size_x)
        cloud3 = Cloud(texture, size, position, scene_size_x)
        self.add_child(cloud0)
        self.add_child(cloud1)
        self.add_child(cloud2)
        self.add_child(cloud3)

    def update(self):
        self.position += (self.velocity, 0)
                
        for cloud in self.children:
            if not cloud.check_new(self.position.x):
                break
        else:
            for cloud in self.children:
                if cloud.check_new_self(self.position.x):
                    cloud.reset(self.position.x)
                    break

                                        
class Cactuses(scene.Node):
    def __init__(self, scene_size_x):
        self.position = scene.Point(0, 0)
        self.velocity = -5
        sprites = utils.load_sprite_sheet('cacti-small.png', 6, 1, 17, 35, [(0, 1), (0, 2), (3, 1), (2, 2), (2, 3)])
        position = scene.Point(-100, 0)
        cactuses = [Cactus(texture, size, position, scene_size_x) for texture, size in sprites]
        for cactus in cactuses:
            self.add_child(cactus)
        
    def check_collision(self, position, size):
        dino_rect = scene.Rect(*(position - self.position), *size)
        for cactus in self.children:
            cactus_rect = scene.Rect(*(cactus.left_buttom_coord), *cactus.size)
            if dino_rect.intersects(cactus_rect):
                return True
        return False
    
    def update(self):
        self.position += (self.velocity, 0)
        # if all((cactus.check_new() for cactus in self.children)):
        for cactus in self.children:
            if not cactus.check_new(self.position.x):
                break
        else:
            for cactus in random.sample(self.children, 5):
                if cactus.check_new_self(self.position.x):
                    cactus.reset(self.position.x)
                    break
        
        
        


    

