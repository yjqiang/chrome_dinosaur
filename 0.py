import scene
from dino import Dino
from ground import Ground
from cloud import Cloud
from cactus import Cactuses


class MyScene (scene.Scene):
    def setup(self):
        self.background_color = 'white'
        
        # self.dino.position.x = (self.size.w / 1)
        # self.dino.position.y = (self.size.h * 0.98)
        # self.dino.position = (self.size.w / 15, self.size.h * 0.1)
        
        self.dino = Dino(self.size)
        self.dino_node = scene.SpriteNode(self.dino.texture)
        # 这个sb中心点是坐标
        self.dino_node.position = self.dino.coord
        self.add_child(self.dino_node)
        
        self.ground = Ground()
        self.ground0_node = scene.SpriteNode(self.ground.ground0)
        self.ground1_node = scene.SpriteNode(self.ground.ground1)
        self.ground0_node.position = self.ground.ground0_coord
        self.ground1_node.position = self.ground.ground0_coord
        self.add_child(self.ground0_node)
        self.add_child(self.ground1_node)
        
        self.cloud0 = Cloud(self.size.x)
        self.cloud1 = Cloud(self.size.x)
        self.cloud2 = Cloud(self.size.x)
        self.cloud3 = Cloud(self.size.x)
        self.cloud0_node = scene.SpriteNode(self.cloud0.texture)
        self.cloud1_node = scene.SpriteNode(self.cloud1.texture)
        self.cloud2_node = scene.SpriteNode(self.cloud2.texture)
        self.cloud3_node = scene.SpriteNode(self.cloud3.texture)
        self.cloud0_node.position = self.cloud0.coord
        self.cloud1_node.position = self.cloud1.coord
        self.cloud2_node.position = self.cloud2.coord
        self.cloud3_node.position = self.cloud3.coord
        self.add_child(self.cloud0_node)
        self.add_child(self.cloud1_node)
        self.add_child(self.cloud2_node)
        self.add_child(self.cloud3_node)
        
        self.cactuses = Cactuses(self.size.x)
        self.cactuses_nodes = []
        for texture, coord in zip(self.cactuses.textures, self.cactuses.coords):
            cactus_node = scene.SpriteNode(texture, position=coord)
            self.cactuses_nodes.append(cactus_node)
        for cactus_node in self.cactuses_nodes:
            self.add_child(cactus_node)
        
    def check_collision(self):
        if self.cactuses.check_collision(self.dino.left_buttom_coord, self.dino.scale):
            self.dino.is_dead = True
            self.paused = True

    def update(self):
        self.dino_node.texture, self.dino_node.position = self.dino.update()
        self.ground0_node.position, self.ground1_node.position = self.ground.update()
        
        self.cloud0_node.position = self.cloud0.update()
        self.cloud1_node.position = self.cloud1.update()
        self.cloud2_node.position = self.cloud2.update()
        self.cloud3_node.position = self.cloud3.update()
        
        tag0_new_self = self.cloud0.check_new_self()
        tag1_new_self = self.cloud1.check_new_self()
        tag2_new_self = self.cloud2.check_new_self()
        tag3_new_self = self.cloud3.check_new_self()
        
        tag0_new = self.cloud0.check_new()
        tag1_new = self.cloud1.check_new()
        tag2_new = self.cloud2.check_new()
        tag3_new = self.cloud3.check_new()
        
        if tag0_new and tag1_new and tag2_new and tag3_new:
            if tag0_new_self:
                self.cloud0.init()
            elif tag1_new_self:
                self.cloud1.init()
            elif tag2_new_self:
                self.cloud2.init()
            elif tag3_new_self:
                self.cloud3.init()
                
        for cactus_node, coord in zip(self.cactuses_nodes, self.cactuses.update()):
            cactus_node.position = coord
        
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
# scene.run(MyScene())
