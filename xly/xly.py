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
        partTip = Text('浮点数的减法').scale(2).set_color(YELLOW).shift(UP)
        self.play(DrawBorderThenFill(partTip))
        self.play(FadeOut(partTip))
        x_origin = MathTex(
            r'X: ',
            r'2',
            r'^{-011}',
            r'\times',
            r'-0.',
            r'011000',
        ).shift(LEFT * 3 + UP)
        x_float = MathTex(
            r'X: ',
            r'11',
            r'011',
            r',',
            r'11',
            r'.011000',
        ).next_to(x_origin, DOWN * 1.5)

        y_origin = MathTex(
            r'Y: ',
            r'2',
            r'^{-100}',
            r'\times',
            r'-0.',
            r'111011',
        ).next_to(x_origin, RIGHT, buff=2)
        y_float = MathTex(
            r'Y: ',
            r'11',
            r'100',
            r',',
            r'00',
            r'.111011',
        ).next_to(y_origin, DOWN * 1.5)

        x_origin[0].set_color(YELLOW)
        y_origin[0].set_color(YELLOW)
        x_float[0].set_color(YELLOW)
        y_float[0].set_color(YELLOW)
        x_exp = x_float[1:3]  # exponent
        y_exp = y_float[1:3]
        x_man = x_float[4:]  # mantissa
        y_man = y_float[4:]

        self.play(Write(x_origin), Write(y_origin))
        ShowLines(self, '目标: 计算 X-Y 的值')
        self.play(FadeOut(x_origin[1]))
        self.play(TransformFromCopy(x_origin[2], x_float[1:3]), run_time=1)
        self.play(TransformFromCopy(x_origin[3], x_float[3]))
        self.play(TransformFromCopy(x_origin[4:], x_float[4:]), run_time=1)

        self.play(FadeOut(y_origin[1]))
        self.play(TransformFromCopy(y_origin[2], y_float[1:3]), run_time=1)
        self.play(TransformFromCopy(y_origin[3], y_float[3]))
        self.play(TransformFromCopy(y_origin[4:], y_float[4:]), run_time=1)
        self.remove(x_origin[1], y_origin[1])
        self.play(FadeOut(x_origin[0]), FadeOut(y_origin[0]),
                  FadeOut(x_origin[2:]), FadeOut(y_origin[2:]),
                  FadeIn(x_float[0]), FadeIn(y_float[0]))
        ShowLines(self, '我们将X和Y化成了完全的补码形式，便于进一步计算')

        self.play(
            ApplyMethod(x_float[1].set_color, BLUE),
            ApplyMethod(x_float[4].set_color, BLUE),
            ApplyMethod(y_float[1].set_color, BLUE),
            ApplyMethod(y_float[4].set_color, BLUE),
        )
        ShowLines(self, '蓝色数字为符号位')
        self.play(ApplyMethod(VGroup(x_float, y_float).shift, UP * 3))
        up_left = x_float.get_center()
        ShowLines(self, '步骤一: 对阶', size=1)
        self.play(ApplyMethod(VGroup(x_exp, y_exp).shift, DOWN * 2.5))
        ShowLines(self, '阶码相减')
        minus = MathTex(r'-').next_to(x_exp, RIGHT).set_color(YELLOW)

        self.play(ApplyMethod(y_exp.next_to, minus, RIGHT))
        self.play(FadeIn(minus))
        formula1 = MathTex(r'11', r'011', r'+', r'00',
                           r'100').next_to(x_exp, DOWN, aligned_edge=LEFT)
        formula2 = Tex(r'[', r'11', r'111', r']').next_to(formula1,
                                                          DOWN,
                                                          aligned_edge=LEFT)
        formula1[0:4:3].set_color(BLUE)
        formula1[2].set_color(YELLOW)
        formula2[1].set_color(BLUE)
        formula2[0:4:3].set_color(YELLOW)
        formula3 = MathTex(r'-1').next_to(formula2, DOWN, aligned_edge=LEFT)

        equal1 = MathTex(r'=').next_to(formula1, LEFT).set_color(YELLOW)
        equal2 = equal1.copy().next_to(formula2, LEFT)
        equal3 = equal1.copy().next_to(formula3, LEFT)

        self.play(FadeIn(equal1))
        self.play(Write(formula1))
        self.play(FadeIn(equal2))
        self.play(Write(formula2[1:3]))
        ShowLines(self, '注意，此时始终在进行补码运算')
        self.play(FadeIn(formula2[0:4:3]))
        self.play(FadeIn(equal3))
        self.play(Write(formula3))
        ShowLines(self, 'X与Y的阶码之差为-1, 按照小阶对大阶的规则, 令X尾数右移一位')
        self.play(
            FadeOutAndShift(
                VGroup(minus, formula1, formula2, formula3, equal1, equal2,
                       equal3), DOWN))
        self.play(ApplyMethod(x_exp.shift, UP * 2.5),
                  ApplyMethod(y_exp.next_to, y_float[0]))
        self.play(ApplyMethod(x_float.shift, DOWN * 2 + RIGHT * 2.3))

        x_exp_dot_pos = x_float[1:4].get_center()
        x_man_pos = x_float[4:].get_center()

        arrow = Arrow(UP, DOWN * 0.1).set_color(YELLOW).next_to(x_float, DOWN)
        tip1 = Text('+1').set_color(YELLOW).next_to(arrow, LEFT).scale(0.8)
        tip2 = Text('右移一位').set_color(YELLOW).next_to(arrow, RIGHT,
                                                      buff=0.1).scale(0.5)
        self.play(GrowArrow(arrow))
        x_float_new = MathTex(
            r'X: ',
            r'11',
            r'100',
            r',',
            r'1',
            r'1',
            r'.101100',
        ).next_to(arrow, DOWN)
        x_float_new[0].set_color(YELLOW)
        x_float_new[1].set_color(BLUE)
        x_float_new[4].set_color(BLUE)
        x_float_new[5].set_color(BLUE)
        self.play(Write(tip2), run_time=1)
        self.play(TransformFromCopy(x_float[4:6], x_float_new[5:7]))
        ShowLines(self, '符号位左边补1')
        self.play(Write(x_float_new[4]))
        self.play(Write(tip1), run_time=1)
        self.play(TransformFromCopy(x_float[1:3], x_float_new[1:3]))
        self.play(FadeIn(x_float_new[0]), FadeIn(x_float_new[3]))

        self.play(FadeOutAndShift(VGroup(x_float, arrow, tip1, tip2), DOWN))
        self.play(ApplyMethod(x_float_new.move_to, up_left))
        x_exp = x_float_new[1:3]
        x_man = x_float_new[4:]

        ShowLines(self, '步骤二: 尾数相减', size=1)
        self.play(ApplyMethod(x_man.shift, DOWN * 3 + RIGHT))
        self.play(ApplyMethod(y_man.next_to, x_man, DOWN))
        self.play(FadeIn(minus.next_to(y_man, LEFT)))
        ShowLines(self, '先将减法运算转换成加法运算')
        plus = MathTex(r'+').move_to(minus.get_center()).set_color(YELLOW)
        new_y_man = MathTex(r'11', r'.000101').move_to(y_man.get_center())
        new_y_man[0].set_color(BLUE)
        self.play(FadeOutAndShift(VGroup(y_man, minus), RIGHT))
        self.play(FadeInFrom(VGroup(new_y_man, plus), RIGHT))
        ShowLines(self, '开始二进制加法运算')

        line = Line(start=plus, end=new_y_man.get_right()).next_to(
            new_y_man, DOWN).set_color_by_gradient(BLUE, RED)
        result_man = MathTex(r'10', r'.110001').next_to(line, DOWN)
        result_man[0].set_color(BLUE)
        self.play(Write(line), run_time=1.2)
        self.play(DrawBorderThenFill(result_man))
        ShowLines(self, '我们发现，符号位出现了10的情况\n\n此时要进行规格化处理', time=1)
        self.play(FadeOutAndShift(VGroup(plus, new_y_man, x_man, line), DOWN))

        self.play(ApplyMethod(result_man.move_to, x_man_pos))
        self.play(ApplyMethod(x_float_new[1:4].move_to, x_exp_dot_pos),
                  ApplyMethod(y_float[1:4].move_to, x_exp_dot_pos),
                  FadeOut(x_float_new[0]), FadeOut(y_float[0]))
        x_float = VGroup(x_float_new[1:3], x_float_new[3], result_man)
        ShowLines(self, '步骤三: 规则化处理')
        '''右移步骤'''
        arrow = Arrow(UP, DOWN * 0.1).set_color(YELLOW).next_to(
            result_man.get_left(), DOWN, buff=0.5)
        tip1 = Text('+1').set_color(YELLOW).next_to(arrow, LEFT).scale(0.8)
        tip2 = Text('右移一位').set_color(YELLOW).next_to(arrow, RIGHT,
                                                      buff=0.1).scale(0.5)
        self.play(GrowArrow(arrow))
        x_float_new = MathTex(
            r'X: ',
            r'11',
            r'101',
            r',',
            r'1',
            r'1',
            r'.011000',
        ).next_to(arrow, DOWN)
        x_float_new[1].set_color(BLUE)
        x_float_new[4].set_color(BLUE)
        x_float_new[5].set_color(BLUE)
        self.play(Write(tip2))
        self.play(TransformFromCopy(result_man, x_float_new[5:7]), run_time=1)
        ShowLines(self, '符号位左边补零')
        self.play(Write(x_float_new[4]))
        self.play(Write(tip1))
        self.play(TransformFromCopy(x_exp, x_float_new[1:3]), run_time=1)
        self.play(FadeIn(x_float_new[3]))
        self.play(
            FadeOutAndShift(VGroup(y_float[1:4], x_float, arrow, tip1, tip2),
                            DOWN))
        self.play(ShowCreationThenDestructionAround(x_float_new[1:]),
                  run_time=1)
        ShowLines(self, '得出答案')
        self.wait(3)