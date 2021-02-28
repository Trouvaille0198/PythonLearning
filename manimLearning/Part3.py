from scenes import *


class Part3(NextScene):
    def construct(self):
        # self.add(Text('Made by Loulou').scale(0.3).to_corner(RIGHT + DOWN))
        partTip = Text('PART 3').scale(3).set_color(YELLOW)

        self.play(DrawBorderThenFill(partTip))
        self.play(FadeOut(partTip))
        ShowLines(self, '让我们回到刚才的场景...')
        mobjects = self.build()
        pat = mobjects[1]
        prefix = mobjects[2]
        k = mobjects[3]
        j = mobjects[4]
        index = mobjects[5]

        for i in range(0, 8):
            pat[i].set_color(GREEN)
        k.shift(RIGHT * 1.2 * 5)
        j.shift(RIGHT * 1.2 * 8)
        next_list = [0, 0, 0, 1, 1, 2, 3, 4]

        text_group = VGroup()
        for i in range(0, 8):
            text_group.add(
                Text(str(next_list[i])).move_to(prefix[i].get_bottom() +
                                                UP * 0.6))
        self.play(FadeIn(mobjects), FadeIn(text_group))
        ShowLines(self, '此时4和8正在进行比较，在它们前面已有四位相等', time=1)
        ShowLines(self, '然而4和8并不相等，k需要进行回退\n\n可是，一位一位的回退，不是太浪费时间了吗？', time=1)
        ShowLines(self, '数学家给我们提供了一种效率更高的办法\n\n不使 k--，而使 k=next[k-1]', time=1)
        self.play(ApplyMethod(pat.set_color, WHITE), FadeOut(k[1]),
                  ApplyMethod(k[0].shift, LEFT * 1.2 + DOWN))
        formula = Text('=next[k-1]=1').scale(0.7).next_to(
            k[0], buff=0).set_color(YELLOW)
        self.play(FadeIn(formula))
        self.wait(1)
        self.play(FadeOut(formula), ApplyMethod(k[0].shift,
                                                LEFT * 2 * 1.2 + UP),
                  FadeIn(k[1].shift(LEFT * 3 * 1.2)))
        # self.play(ApplyMethod(pat[0].set_color, GREEN),
        #           ApplyMethod(pat[1].set_color, GREEN),
        #           ApplyMethod(pat[7].set_color, GREEN),
        #           ApplyMethod(pat[8].set_color, GREEN))
        textPrefix2 = Text('2').move_to(prefix[8].get_bottom() + UP * 0.6)
        self.play(Write(textPrefix2))
        ShowLines(self, '这其中的原理是什么？凭什么k可以回退如此多的距离而没有遗漏？', time=2)
        ShowLines(self, '让我们换一种方式来观察它们')
        pat4Copy = pat[4].copy()
        self.add(pat4Copy)
        k_string = VGroup(pat[0], pat[1], pat[2], pat[3], pat4Copy)
        j_string = VGroup(pat[4], pat[5], pat[6], pat[7], pat[8])
        self.play(FadeOut(j), FadeOut(k), FadeOut(mobjects[0]),
                  FadeOut(prefix), FadeOut(mobjects[-1]), FadeOut(text_group),
                  FadeOut(index), FadeOut(textPrefix2), FadeOut(pat[-1]),
                  ApplyMethod(j_string.shift, LEFT * 1.2 * 4),
                  ApplyMethod(k_string.shift, DOWN))
        text1 = Text('这是后缀').next_to(j_string[-1], RIGHT, buff=2).scale(0.5)
        text2 = Text('这是前缀').next_to(k_string[-1], RIGHT, buff=2).scale(0.5)

        self.play(FadeIn(text1))
        self.play(FadeIn(text2))
        ShowLines(self, '此时 j,k 均在末尾')
        '''建立提示框'''
        square = Rectangle(height=2, width=1).move_to(
            VGroup(j_string[-1], k_string[-1]).get_center()).set_color(YELLOW)
        j_text = VGroup(Text('j').scale(0.7),
                        Arrow(UP,
                              DOWN * 0.1)).arrange(DOWN).next_to(square, UP)
        k_text = VGroup(Text('k').scale(0.7),
                        Arrow(DOWN,
                              UP * 0.1)).arrange(UP).next_to(square, DOWN)
        j_text.set_color(YELLOW)
        k_text.set_color(YELLOW)
        squ = VGroup(square, j_text, k_text)

        self.play(FadeIn(squ))
        self.play(FadeOut(text1[0:2]), FadeOut(text2[0:2]),
                  ApplyMethod(text1[2:].shift, LEFT * (1.2 * 5 + 3.8)),
                  ApplyMethod(text2[2:].shift, LEFT * (1.2 * 5 + 3.8)))
        ShowLines(self, '让我们回退几个步骤，观察j,k的运动轨迹')
        self.play(FadeOut(j_string[1]), FadeOut(k_string[1]),
                  FadeOut(j_string[2]), FadeOut(k_string[2]),
                  FadeOut(j_string[3]), FadeOut(k_string[3]),
                  FadeOut(j_string[4]), FadeOut(k_string[4]),
                  ApplyMethod(squ.move_to, VGroup(j_string[0], k_string[0])))

        self.play(ApplyMethod(j_string[0].set_color, GREEN),
                  ApplyMethod(k_string[0].set_color, GREEN))
        self.play(FadeIn(j_string[1]), FadeIn(k_string[1]),
                  ApplyMethod(squ.move_to, VGroup(j_string[1], k_string[1])))

        self.play(ApplyMethod(j_string[1].set_color, GREEN),
                  ApplyMethod(k_string[1].set_color, GREEN))
        self.play(FadeIn(j_string[2]), FadeIn(k_string[2]),
                  ApplyMethod(squ.move_to, VGroup(j_string[2], k_string[2])))

        self.play(ApplyMethod(j_string[2].set_color, GREEN),
                  ApplyMethod(k_string[2].set_color, GREEN))
        self.play(FadeIn(j_string[3]), FadeIn(k_string[3]),
                  ApplyMethod(squ.move_to, VGroup(j_string[3], k_string[3])))

        self.play(ApplyMethod(j_string[3].set_color, GREEN),
                  ApplyMethod(k_string[3].set_color, GREEN))
        self.play(FadeIn(j_string[4]), FadeIn(k_string[4]),
                  ApplyMethod(squ.move_to, VGroup(j_string[4], k_string[4])))
        ShowLines(self, '前几次移动很顺利，最大前后缀长度来到了4\n\n此时要进行最后的比较', time=1)
        ShowLines(self, '我们向着长度5的伟业进发，却发现第5位——发生了失配', time=1)
        self.play(Indicate(j_string[-1], color=RED),
                  Indicate(k_string[-1], color=RED))
        self.play(ApplyMethod(j_string.set_color, WHITE),
                  ApplyMethod(k_string.set_color, WHITE))
        ShowLines(self, '照理说，我们应该退而求其次，让前缀串向右移动一格\n\n等价于k后退一格')
        self.play(ApplyMethod(k_string.shift, RIGHT * 1.2))
        ShowLines(self, '慢着', time=0.25)
        self.play(ApplyMethod(k_string.shift, LEFT * 1.2))
        ShowLines(self, '这个场景，有没有一种 KMP 算法的既视感？', time=1)
        self.play(Indicate(j_string[3], color=GREEN),
                  Indicate(k_string[0], color=GREEN))
        ShowLines(self, '前缀作为模式串与后缀进行匹配\n\n一旦失配，便尽可能地向前移动', time=2)
        self.play(ApplyMethod(k_string.shift, RIGHT * 1.2 * 3))
        ShowLines(self, '我们只需让前后缀一一对应，然后再让j和k进行比较\n\n这与 kmp 算法的思想一致', time=2)
        self.play(
            Transform(
                squ[0],
                Rectangle(height=2, width=2).move_to(
                    VGroup(j_string[3], j_string[4], k_string[0],
                           k_string[1]).get_center()).set_color(YELLOW)))
        ShowLines(
            self,
            '实际上，k=next[k-1] 的思想也就是一种递归的思想\n\n求 next 数组与 kmp 算法也用到了相同的思路\n\n这波啊，这波是互相套娃'
        )
