from manim import *


class jobs(Scene):
    def construct(self):
        headline = Text('第九组 求解失效函数').shift(UP * 3)
        text1 = Text('孙天野: 动画制作,失效函数思路讲解', t2c={
            '[0:3]': YELLOW
        }).next_to(headline, DOWN).scale(0.5)
        text2 = Text('桂文珑: 文稿撰写,失效函数思路讲解', t2c={
            '[0:3]': YELLOW
        }).next_to(text1, DOWN).scale(0.5)
        text3 = Text('冯毅凯: kmp 算法实现与思路讲解', t2c={
            '[0:3]': YELLOW
        }).next_to(text2, DOWN).scale(0.5)
        text4 = Text('孟旭: 代码实现与思路讲解', t2c={
            '[0:2]': YELLOW
        }).next_to(text3, DOWN).scale(0.5)

        a = VGroup(text1, text2, text3, text4).arrange(DOWN, aligned_edge=LEFT)
        self.play(ShowCreation(headline))
        self.play(FadeIn(a))
        self.wait(3)
