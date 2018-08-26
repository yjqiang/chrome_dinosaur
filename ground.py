import utils
import scene


class Ground():
    def __init__(self,speed=-5):
        # self.image,self.rect = load_image('ground.png',-1,-1,-1)
        # self.image1,self.rect1 = load_image('ground.png',-1,-1,-1)
        list_ground0 = utils.load_sprite_sheet('ground.png', 1, 1)
        list_ground1 = utils.load_sprite_sheet('ground.png', 1, 1)
        self.list_ground = list_ground0 + list_ground1
        self.ground0, self.ground_scale = self.list_ground[0]
        self.ground1, self.ground_scale = self.list_ground[1]
        self.ground0_left_buttom_coord = scene.Size(0, 0)
        self.ground1_left_buttom_coord = scene.Size(self.ground_scale.x, 0)        
        
        self.update_img()
        
        self.speed = speed
        
    # 随index和左下端坐标改变texture、坐标等
    def update_img(self):
        self.ground0_coord = self.ground_scale / 2 + self.ground0_left_buttom_coord + (0, 5)
        self.ground1_coord = self.ground_scale / 2 + self.ground1_left_buttom_coord + (0, 5)

    def update(self):
        self.ground0_left_buttom_coord += (self.speed, 0)
        self.ground1_left_buttom_coord += (self.speed, 0)

        if self.ground0_left_buttom_coord.x + self.ground_scale.x < 0:
            self.ground0_left_buttom_coord.x = self.ground1_left_buttom_coord.x + self.ground_scale.x
            
        if self.ground1_left_buttom_coord.x + self.ground_scale.x < 0:
            self.ground1_left_buttom_coord.x = self.ground0_left_buttom_coord.x + self.ground_scale.x
            
        self.update_img()
        return self.ground0_coord, self.ground1_coord

