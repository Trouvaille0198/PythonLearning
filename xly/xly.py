from manim import *


def ShowLines(self, line, direction=DOWN * 2.5, time=0.5, size=0.5):
    text = Text(line).shift(direction).scale(size)
    self.play(FadeIn(text))
    self.wait(time)
    self.play(FadeOut(text))


class xly1(Scene):
    def construct(self):
        x = MathTex('1', '2', '3')
        self.add(x)
        self.play(ApplyMethod(x[1].set_color, YELLOW))


class xly(Scene):
    def construct(self):
        x_origin = MathTex(
            r'X:'
            r'2',
            r'^{-011}',
            r'\times',
            r'-0.',
            r'11000',
        )
        x_float = MathTex(
            r'11',
            r'011',
            r',',
            r'11',
            r'.11000',
        ).next_to(x_origin, DOWN)

        self.add(x_origin, x_float)
        self.play(FadeOut(x_origin[0]))
        self.play(Transform(x_origin[1], x_float[0:2]))
        # x_tip = MathTex('X:')
        # x_origin1 = MathTex(r'2^{-011}')
        # times1 = MathTex(r'\times')
        # x_origin2 = MathTex(r'-0.011000')
        # x_ori = VGroup(x_tip, x_origin1, times1, x_origin2).arrange(
        #     buff=LARGE_BUFF).shift(LEFT * 2 + UP * 1.5).scale(1.5)
        # '''x_flo'''
        # x_float1 = VGroup(MathTex(r'11'),
        #                   MathTex(r'011')).arrange(buff=0.1).shift(LEFT * 2 +
        #                                                            UP * 1.5)
        # dot1 = MathTex(', ').next_to(x_origin1).shift(DOWN * 0.2)
        # x_float2 = VGroup(
        #     MathTex(r'11'),
        #     MathTex(r'.011000')).arrange(buff=0.1).next_to(times1)
        # x_flo = VGroup(x_float1, dot1, x_float2).scale(1.5)
        # '''y_ori'''
        # y_tip = MathTex('Y:')
        # y_origin1 = MathTex(r'2^{-100}')
        # times2 = MathTex(r'\times').next_to(y_origin1)
        # y_origin2 = MathTex(r'0.111011').next_to(times2)
        # y_ori = VGroup(y_tip, y_origin1, times2,
        #                y_origin2).next_to(x_ori, DOWN).scale(1.5)
        # '''y_flo'''
        # y_float1 = VGroup(MathTex(r'11'),
        #                   MathTex(r'100')).arrange(buff=0.1).next_to(
        #                       x_origin1, DOWN)
        # dot2 = MathTex(',').next_to(y_origin1).shift(DOWN * 0.2)
        # y_float2 = VGroup(
        #     MathTex(r'00'),
        #     MathTex(r'.111011')).arrange(buff=0.1).next_to(times2)
        # y_flo = VGroup(y_float1, dot2, y_float2).scale(1.5)
        # # self.add(x_origin1, times1, x_origin2, y_origin1, times2, y_origin2)
        # self.add(x_ori, y_ori)
        # ShowLines(self, '转换为浮点数')

        # self.play(Transform(x_origin1, x_float1), run_time=1)
        # self.play(Transform(times1, dot1), run_time=1)
        # self.play(Transform(x_origin2, x_float2), run_time=1)

        # self.play(Transform(y_origin1, y_float1), run_time=1)
        # self.play(Transform(times2, dot2), run_time=1)
        # self.play(Transform(y_origin2, y_float2), run_time=1)

        # ShowLines(self, '正负用双符号位表示')
        # self.play(ApplyMethod(x_float1[0].set_color, BLUE),
        #           ApplyMethod(x_float2[0].set_color, BLUE),
        #           ApplyMethod(y_float1[0].set_color, BLUE),
        #           ApplyMethod(y_float2[0].set_color, BLUE))
        # self.play(x_float1[0].animate.set_color(GREEN))
        # self.wait()