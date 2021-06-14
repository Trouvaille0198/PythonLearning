import random
from const import *
from logger import logger


class Player():
    def __init__(self, coor=(0, 0), side=-1, position='DEFAULT'):
        self.id = random.randint(0, 65536)
        self.coor = coor
        self.side = side
        self.ball_state = False
        self.done = False
        self.position = position

    # 辅助函数
    def init_player(self, game, coor):
        """
        初始化球员状态
        :param game: 上级game实例
        :param coor: 初始坐标
        """
        self.coor = coor
        self.ball_state = False
        self.done = False
        game.field.update_coor_content(coor, self)

    def is_same_side(self, another_player):
        return self.side == another_player.side

    # 球员操作
    def move_to(self, game, coor: tuple):
        if coor != self.coor:
            game.field.update_player_location(self, coor)

    def pass_ball(self, game, next_player):
        """
        传球
        """
        if ball_state:
            self.ball_state = False
            target_coor = next_player.coor
            # TODO拦截判定
            distance = int(game.field.get_distance(self.coor, next_player.coor)/10)  # 12级
            # TODO补充落地范围判定逻辑
            x = random.choice(target_coor[0]-distance, target_coor[0]+distance)
            y = random.choice(target_coor[1]-distance, target_coor[1]+distance)
            final_coor = (x, y)
            # TODO出界判定
            if final_coor == target_coor:
                # 精准传球
                next_player.ball_state = True
            else:
                game.field.update_ball_location((x, y))

    def scramble(self, another_player):
        """
        争抢球权
        """
        win_player = random.choice((self, another_player))  # TODO补充争抢逻辑，决出胜者
        # win_player.move_to(game, ball_coor)
        return win_player

    def overlap_judge(self):
        """
        持球球员遇到重合时的动作
        """
        pass

    def act(self, game):
        for coor in game.field.get_nearest_player_coor():
            if coor == self.coor:
                self.scramble()
