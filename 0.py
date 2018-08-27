import scene
from dino import Dino
from cactus import Cactuses
from cloud import Clouds
from ground import Grounds
from score_board import ScoreBoards




class MyScene (scene.Scene):
    def setup(self):
        self.background_color = 'white'
        
        self.dino = Dino()
        # 这个sb pythonista作者设置的texture中心点作为坐标，而且与opencv坐标不同，|_这种坐标
        self.add_child(self.dino)
           
        self.grounds = Grounds()
        self.add_child(self.grounds)
        
        self.clouds = Clouds(-2, self.size.x)
        self.add_child(self.clouds)
        
        self.cactuses = Cactuses(self.size.x)
        self.add_child(self.cactuses)
        
        self.score_boards = ScoreBoards()
        self.add_child(self.score_boards)
        
        self.middle_x = self.size.x / 2
        
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
        self.score_boards.update()
        
        self.check_collision()
            
    def touch_began(self, touch):
        if touch.location.x < self.middle_x:
            self.dino.start_jump()
        else:
            self.dino.start_duck()
            
    def touch_ended(self, touch):
        self.dino.end_duck()

scene.run(MyScene(), scene.PORTRAIT)
