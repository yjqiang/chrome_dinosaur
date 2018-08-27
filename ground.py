import scene


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
