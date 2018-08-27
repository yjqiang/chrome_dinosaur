import utils
import scene


gravity = 0.6


class Dino(scene.SpriteNode):
    def __init__(self):
        self.z_position = 2
        self.is_jumping = False
        self.is_ducking = False
        self.is_blinking = False
        self.is_dead = False
        self.counter = 0
        list_running_dinos = utils.load_sprite_sheet('dino.png', 5, 1, 44, 47)
        list_ducking_dinos = utils.load_sprite_sheet('dino_ducking.png', 2, 1, 59, 47)
        self.list_dinos = list_running_dinos + list_ducking_dinos
                
        self.index = 0
        self.left_buttom_coord = scene.Point(10, 10)
        self.update_img()
                
        self.velocity = [0, 0]
                
    def check_bound(self):
        if self.left_buttom_coord.y < 10:
            self.left_buttom_coord.y = 10
            self.is_jumping = False
            
    def start_jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.is_blinking = False
            self.velocity[1] = 10
            
    def start_duck(self):
        if not self.is_jumping:
            self.is_ducking = True
            self.index = 5
            
    def end_duck(self):
        self.is_ducking = False
        self.index = 2
    
    # 随index和左下端坐标改变texture、坐标等
    def update_img(self):
        self.texture, self.size = self.list_dinos[self.index]
        self.position = self.size / 2 + self.left_buttom_coord
    
    def update(self):
        self.counter += 1
        if self.is_jumping:
            self.velocity[1] -= gravity
            
        if self.is_jumping:
            self.index = 0
        elif self.is_blinking:
            if self.index == 0:
                if self.counter % 40 == 39:
                    self.index = 1
            elif self.counter % 20 == 19:
                self.index = 0
        elif self.is_ducking:
            if self.counter % 10 == 0:
                self.index = (self.index) % 2 + 5
        else:
            if self.counter % 10 == 0:
                self.index = (self.index + 1) % 2 + 2
                
        if self.is_dead:
            self.index = 4
        
        self.left_buttom_coord += (self.velocity[0] * 1.5, self.velocity[1] * 1.5)
        self.check_bound()
        self.update_img()
    

            
    
        
