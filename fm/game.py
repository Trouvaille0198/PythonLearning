from player_group import PlayerGroup
from field import Field
from logger import logger


class Game():
    def __init__(self):
        self.score = [0, 0]
        self.field = Field()
        self.players = PlayerGroup()
        self.ball_side = -1
        self.state = 0

    # 辅助函数
    def check_state(self):
        if self.state == 0:
            # 正常比赛
            pass
        elif self.state == 1:
            # 进球
            self.init_player_location()
        elif self.state == 2:
            # 出底线
            pass
        elif self.state == 3:
            # 出边线
            pass
        else:
            pass

    def start(self):
        for i in range(90):
            for player in self.players.left_players:
                player.act(self)
                self.check_state()
            for player in self.players.right_players:
                player.act(self)
                self.check_state()


if __name__ == '__main__':
    game = Game()
    game.start()