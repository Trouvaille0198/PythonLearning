from player import Player
import random
from const import *


class PlayerGroup():
    def __init__(self):
        self.init_player_info()

    # 构造函数
    def init_player_info(self):
        self.left_players = [Player(side=-1)]
        self.right_players = [Player(side=1)]

    def init_player_location(self):
        for player in self.left_players:
            if player.position == 'DEFAULT':
                player.move_to((24, 30))
        for player in self.right_players:
            if player.position == 'DEFAULT':
                player.move_to((24, 38))

    # 辅助函数
    def get_player_by_coor(self, coor: tuple):
        """
        根据坐标返回球员实例
        """
        for player in self.left_players:
            if player.coor == coor:
                return player
        for player in self.right_players:
            if player.coor == coor:
                return player
        return None

    def scramble(self, p1, p2):
        """
        争抢，返回胜负者
        """
        win_player = p1.scramble(p2)
        if win_player == p1:
            return p1, p2
        else:
            return p2, p1

    # 判定函数
    def scramble_judge(self, game):
        """
        争抢判定
        """
        ball_location = game.field.get_ball_location()
        if ball_location:
            # 判定是否无人持球
            players = list(map(self.get_player_by_coor, game.field.get_nearest_player_coor()))
            lplayers = []
            rplayers = []
            for player in players:
                if player in self.left_players:
                    lplayers.append(player)
                else:
                    rplayers.append(player)
            if not lplayers:
                # 没有左队球员
                rplayers[0].move_to(game, ball_location)  # 右队最近的球员移动到球位置
            elif not rplayers:
                lplayers[0].move_to(game, ball_location)
            else:
                while True:
                    lplayer = random.choice(lplayers)
                    rplayer = random.choice(rplayers)
                    win_player, lose_player = self.scramble(lplayer, rplayer)
                    if lose_player in lplayers:
                        lplayers.remove(lose_player)
                    else:
                        rplayers.remove(lose_player)
                    if not lplayers or not rplayers:
                        win_player.move_to(game, ball_location)

    def overlap_judge(self):
        """
        异队球员重合判定
        """
        pass

    def frame_act(self):
        self.scramble_judge()
        self.overlap_judge()
