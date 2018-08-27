import scene
import utils


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


class Ground(scene.SpriteNode):
    def __init__(self, texture, size, position):
        self.texture = texture
        self.size = size
        self.left_buttom_coord = position
        self.update_img()
        
    # 随index和左下端坐标改变texture、坐标等
    def update_img(self):
        self.position = self.size / 2 + self.left_buttom_coord + (0, 5)

    def update(self, position_x):
        if self.left_buttom_coord.x + self.size.x + position_x < 0:
            self.left_buttom_coord.x += self.size.x * 2
            self.update_img()
