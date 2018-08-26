import utils
import scene
import random


class Cloud():
    def __init__(self, width):
        self.texture, self.scale = utils.load_sprite_sheet('cloud.png', 1, 1, int(90*30/42), 30)[0]
        self.speed = 1
        self.init_x = width
        self.left_buttom_coord = scene.Size(-100, random.randrange(90, 150))
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
        if self.left_buttom_coord.x + self.scale.x + random.randrange(100, 400) < self.init_x:
            if self.counter % 100 == 0:
                return random.choices([True, False], [0.9, 0.1])
        return False
        
    def init(self):
        self.left_buttom_coord = scene.Size(self.init_x, random.randrange(90, 150))
        self.update_img()

    def update(self):
        self.counter += 1
        self.left_buttom_coord += (-2, 0)
        self.update_img()
        
        return self.coord
