import scene
import random


class Cloud(scene.SpriteNode):
    def __init__(self, texture, size, position, scene_size_x):
        self.texture = texture
        self.size = size
        self.speed = 1
        self.scene_size_x = scene_size_x
        self.left_buttom_coord = position
        self.update_img()
        
    def update_img(self):
        self.position = self.size / 2 + self.left_buttom_coord
    
    # 左出-->可以允许出现新的且可以安排我   右边完全离开边界后(正常显示在屏幕上或左出)->可以允许出现新的
    def check_new_self(self, position_x):
        if self.left_buttom_coord.x + self.size.x + position_x < 0:
            return True
        return False
        
    def check_new(self, position_x):
        if self.left_buttom_coord.x + self.size.x * 3 + position_x < self.scene_size_x:
            return True
        return False
        
    def reset(self, position_x):
        x = self.scene_size_x - position_x + random.randrange(0, 500, 80)
        y = random.randrange(90, 150)
        self.left_buttom_coord = scene.Point(x, y)
        self.update_img()

        
