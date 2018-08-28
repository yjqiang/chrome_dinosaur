import scene
import utils


class ScoreBoards(scene.Node):
    def __init__(self):
        self.position = scene.Point(100, 100)
        self.score = 0
        sprites = utils.load_sprite_sheet('numbers.png', 12, 1)[:10]
        size = sprites[0][1]
        textures = [sprite[0] for sprite in sprites]
        self.score_boards = [ScoreBoard(textures, size, scene.Point(i * size.x, 0)) for i in range(5)]
        self.score_nums = [0, 0, 0, 0, 0]
        for i in range(4, -1, -1):
            self.score_boards[i].update(0)
        for score_board in self.score_boards:
            self.add_child(score_board)
                    
    def update(self):
        self.score += 0.1
        score = int(self.score)
        for i in range(4, -1, -1):
            # i 个十百千万 num对应数字
            num = score % 10
            score = int(score / 10)
            if self.score_nums[i] != num:
                self.score_boards[i].update(num)                
                self.score_nums[i] = num
        
                        
class ScoreBoard(scene.SpriteNode):
    def __init__(self, textures, size, position):
        self.textures = textures
        self.position = position + size / 2
            
    def update(self, num):
        self.texture = self.textures[num]
