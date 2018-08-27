import scene
import utils


class ScoreBoards(scene.Node):
    def __init__(self):
        self.position = scene.Point(100, 100)
        self.score = 0
        self.sprites = utils.load_sprite_sheet('numbers.png', 12, 1)[:10]
        size = self.sprites[0][1]
        self.score_boards = [ScoreBoard(size, scene.Point(i * size.x, 0)) for i in range(5)]
        self.score_nums = [0, 0, 0, 0, 0]
        for i in range(4, -1, -1):
            self.score_boards[i].texture = self.sprites[0][0]
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
                self.score_boards[i].texture = self.sprites[num][0]
                self.score_nums[i] = num
        
                        
class ScoreBoard(scene.SpriteNode):
    def __init__(self, size, position):
        # self.texture = texture
        self.position = position + size / 2
            
    def update(self, texture):
        self.texture = texture
