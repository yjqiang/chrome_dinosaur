import utils
import scene
import random


class Cactuses():
    def __init__(self, width):
        sprites = utils.load_sprite_sheet('cacti-small.png', 6, 1, 17, 35, [(0, 1), (0, 2), (3, 1), (2, 2), (2, 3)])
        self.cactuses = [Cactus(width, texture, scale) for texture, scale in sprites]
        self.coords = [cactus.coord for cactus in self.cactuses]
        self.textures = [cactus.texture for cactus in self.cactuses]
        
    def check_collision(self, position, size):
        for cactus in self.cactuses:
            if (scene.Rect(*position, *size)).intersects(scene.Rect(*cactus.left_buttom_coord, *cactus.scale)):
                # print(scene.Rect(*position, *size))
                # print(scene.Rect(*cactus.left_buttom_coord, *cactus.scale))
                return True
        return False
    
    def update(self):
        # if all((cactus.check_new() for cactus in self.cactuses)):
        for cactus in self.cactuses:
            if not cactus.check_new():
                break
        else:
            # random.shuffle(self.cactuses)
            for cactus in random.sample(self.cactuses, 5):
                if cactus.check_new_self():
                    cactus.init()
                    break
        self.coords = [cactus.update() for cactus in self.cactuses]
        return self.coords
        
        
    

class Cactus():
    def __init__(self, width, texture, scale):
        self.texture = texture
        self.scale = scale
        self.speed = 5
        self.init_x = width
        self.left_buttom_coord = scene.Size(-100, 0)
        self.counter = 0
        self.update_img()
        
    def update_img(self):
        self.coord = self.scale / 2 + self.left_buttom_coord
    
    # 左出-->可以允许出现新的且可以安排我   右边完全离开边界后(正常显示在屏幕上或左出)->可以允许出现新的
    def check_new_self(self):
        if self.left_buttom_coord.x + self.scale.x < 0:
            if self.counter % 100 == 0:
                return random.choices([True, False], [0.9, 0.1])
        return False
        
    def check_new(self):
        if self.left_buttom_coord.x + self.scale.x + 50 < self.init_x:
            if self.counter % 100 == 0:
                return random.choices([True, False], [0.9, 0.1])
        return False
        
    def init(self):
        self.left_buttom_coord = scene.Size(self.init_x + random.randrange(20, 400), 10)
        self.update_img()

    def update(self):
        self.counter += 1
        self.left_buttom_coord += (-5, 0)
        self.update_img()
        
        return self.coord
