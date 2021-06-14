import numpy as np
from const import *
import bisect


class Field():
    __length = FIELD_LENGTH
    __width = FIELD_WIDTH

    def __init__(self):
        self.coor = np.zeros((self.__width, self.__length), dtype=int)
        """
        0：空坐标
       -1：左方球员
        1：右方球员
        2：球落点
        """

    def is_out_of_border(self, coor: tuple):
        """
        是否出界
        """
        if 0 <= coor[0] <= FIELD_LENGTH and 0 <= coor[1] <= FIELD_WIDTH:
            return False
        else:
            return True

    def adjust_out_of_border(self, coor: tuple):
        """
        若出界，选取边界坐标
        """
        if self.is_out_of_border(coor):
            coor = list(coor)
            if coor[0] < 0:
                coor[0] = 0
            if coor[0] > FIELD_WIDTH:
                coor[0] = FIELD_WIDTH
            if coor[1] < 0:
                coor[1] = 0
            if coor[1] > FIELD_LENGTH:
                coor[1] = FIELD_LENGTH
            return tuple(coor)
        else:
            return tuple(coor)

    def get_range_player_num(self, coor: tuple, side=1, width=2) -> int:
        """
        获取范围内单方球员数量
        """
        return np.sum(self.coor[
            (coor[0] - width): (coor[0] + width + 1),
            (coor[1] - width): (coor[1] + width + 1),
        ] == side)

    def get_range_player_coor(self, coor: tuple, side=1, width=2) -> tuple:
        """
        获取范围内单方球员坐标
        """
        range_player_coor = []
        for (rindex, row) in enumerate(self.coor):
            if (coor[0]-width) <= rindex <= coor[0]+width:
                for (cindex, col) in enumerate(row):
                    if (coor[1]-width) <= cindex <= coor[1]+width and col == side:
                        range_player_coor.append((rindex, cindex))
        return range_player_coor

    def update_ball_location(self, ball_coor: tuple):
        """
        更新足球位置
        """
        self.adjust_out_of_border(ball_coor)  # TODO暂时不考虑球出界
        if self.is_out_of_border(ball_coor):
            pass
        elif self.coor[ball_coor] == 0:
            self.coor[ball_coor] = 2
        elif self.coor[ball_coor] == 1 or self.coor[ball_coor] == -1:
            # 若更新的位置有球员
            if self.get_ball_location():
                self.coor[self.get_ball_location()] = 0  # 抹除足球原坐标
            # 注意要在外部函数中修改球员持球情况

    def update_player_location(self, player, target_coor: tuple):
        """
        更新球员位置
        """
        self.adjust_out_of_border(target_coor)
        if self.coor[target_coor] == 2:
            # 恰好移动到足球处
            player.ball_state = 1
        elif self.coor[target_coor] == player.side:
            # TODO与对友重叠
            while self.coor[target_coor] == player.side or self.coor[target_coor] == -player.side:
                target_coor = list(target_coor)
                x = random.choice((-1, 1, 0, -2, 2))
                y = random.choice((-1, 1, 0, -2, 2))
                target_coor[0] += y
                target_coor[1] += x
                target_coor = self.adjust_out_of_border(tuple(target_coor))
        elif self.coor[target_coor] == -player.side:
            # 与对手重叠，若无球球员移动到有球球员上，则应该在时间帧开始时进行逼抢判定，这里不修改
            if player.ball_state == 1:
                # 若移动方持球，则避免与对方球员重合
                while self.coor[target_coor] == player.side or self.coor[target_coor] == -player.side:
                    target_coor = list(target_coor)
                    x = random.choice((-1, 1, 0, -2, 2))
                    y = random.choice((-1, 1, 0, -2, 2))
                    target_coor[0] += y
                    target_coor[1] += x
                    target_coor = self.adjust_out_of_border(tuple(target_coor))
            elif

        self.coor[player.coor] = 0  # 修改原位置
        self.coor[target_coor] = player.side  # 修改现位置
        player.coor = target_coor

    def get_distance(self, coor1, coor2):
        return int(((coor1[0]-coor2[0])**2 + (coor1[1]-coor2[1])**2) ** 0.5)

    def get_ball_location(self) -> tuple:
        """
        获取球坐标
        """
        if np.where(self.coor == 2)[0].size != 0:
            # 若存在球落点
            return (np.where(self.coor == 2)[0][0], np.where(self.coor == 2)[1][0])
        else:
            return ()

    def get_nearest_player_coor(self, n=3, coor: tuple = None) -> list:
        """
        获取离指定坐标最近的n个球员的坐标
        :param coor: 指定坐标
        :param n: 返回个数
        """
        if not coor:
            coor = self.get_ball_location()  # 默认取足球坐标
            if not coor:
                # 若不存在足球坐标
                return []
        distance_list = []
        for (rindex, row) in enumerate(self.coor):
            for (cindex, col) in enumerate(row):
                if col == 1 or col == -1:
                    bisect.insort(
                        distance_list, (self.get_distance((rindex, cindex), coor), (rindex, cindex))
                    )
        return [x[1] for x in distance_list[:n]]
