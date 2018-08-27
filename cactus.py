import scene
import random
import utils
    
    
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
                        

class Cactus(scene.SpriteNode):
    def __init__(self, texture, size, position, scene_size_x):
        self.texture = texture
        self.size = size
        self.speed = 5
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
        if self.left_buttom_coord.x + self.size.x * 10 + position_x < self.scene_size_x:
            return True
        return False
        
    def reset(self, position_x):
        x = self.scene_size_x + random.randrange(0, 500, 80) - position_x
        y = 10
        self.left_buttom_coord = scene.Size(x, y)
        self.update_img()

