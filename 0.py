import scene
from dino import Dino
from background import Grounds, Clouds, Cactuses


class MyScene (scene.Scene):
    def setup(self):
        self.background_color = 'white'
        
        # self.dino.position.x = (self.size.w / 1)
        # self.dino.position.y = (self.size.h * 0.98)
        # self.dino.position = (self.size.w / 15, self.size.h * 0.1)
        
        self.dino = Dino()
        # 这个sb中心点是坐标
        self.add_child(self.dino)
           
        self.grounds = Grounds()
        self.add_child(self.grounds)
        
        self.clouds = Clouds(-2, self.size.x)
        self.add_child(self.clouds)
        
        self.cactuses = Cactuses(self.size.x)
        self.add_child(self.cactuses)
        
    def check_collision(self):
        if self.cactuses.check_collision(self.dino.left_buttom_coord, self.dino.size):
            self.dino.is_dead = True
            self.dino.update()
            self.paused = True

    def update(self):
        self.dino.update()
        self.grounds.update()
        self.clouds.update()
        self.cactuses.update()
        
        self.check_collision()
            
    def touch_began(self, touch):
        middle_x = self.size.x / 2
        if touch.location.x < middle_x:
            self.dino.start_jump()
        else:
            self.dino.start_duck()
            
    def touch_ended(self, touch):
        self.dino.end_duck()

scene.run(MyScene(), scene.PORTRAIT)
