from scenes import *


class Part2(NextScene):
    def construct(self):
        # self.add(Text('Made by Loulou').scale(0.3).to_corner(RIGHT + DOWN))
        partTip = Text('PART 2').scale(3).set_color(YELLOW)
        self.play(DrawBorderThenFill(partTip))
        self.play(FadeOut(partTip))

        mobjects = self.build()
        pat = mobjects[1]
        prefix = mobjects[2]
        k = mobjects[3]
        j = mobjects[4]
        index = mobjects[5]

        self.play(FadeIn(mobjects[0]), FadeIn(prefix))
        self.play(FadeIn(pat))
        self.play(Write(index), Write(mobjects[6]))
        ShowLines(self, "k: 指向前缀末尾位置\n\nj: 指向后缀末尾位置", size=0.7)
        self.play(FadeIn(k), FadeIn(j))
        origin_k = k.get_center()
        '''k=-1'''
        ShowLines(self, '第一位只有一个字符串，最大相等前后缀长度自然是 0')
        self.play(Write(Text('0').move_to(prefix[0].get_bottom() + UP * 0.6)))
        self.play(ApplyMethod(j.shift, RIGHT * 1.2),
                  ApplyMethod(k.shift, RIGHT * 1.2))
        '''判断0和1'''
        ShowLines(self, '判断位置 0 和位置 1 上的字符，两者不相等')
        self.play(Indicate(pat[0], color=RED), Indicate(pat[1], color=RED))
        ShowLines(self, 'k 回退一位至 -1')
        self.play(ApplyMethod(k.move_to, origin_k))
        '''k=-1'''
        ShowLines(self, '此时 k=-1，代表子串最大公共前后缀长度是 0')
        self.play(Write(Text('0').move_to(prefix[1].get_bottom() + UP * 0.6)))
        ShowLines(self, '注意，j始终指向子串的末尾')
        ShowLines(self, 'j，k均右移，进行下一轮循环')
        self.play(ApplyMethod(j.shift, RIGHT * 1.2),
                  ApplyMethod(k.shift, RIGHT * 1.2))
        '''判断0和2'''
        ShowLines(self, '判断位置 0 和位置 2 上的字符，两者不相等')
        self.play(Indicate(pat[0], color=RED), Indicate(pat[2], color=RED))
        ShowLines(self, 'k 回退一位至 -1，之后的操作与前面相同')
        self.play(ApplyMethod(k.move_to, origin_k))
        self.play(Write(Text('0').move_to(prefix[2].get_bottom() + UP * 0.6)))
        '''k=-1'''
        self.play(ApplyMethod(j.shift, RIGHT * 1.2),
                  ApplyMethod(k.shift, RIGHT * 1.2))
        '''判断0和3'''
        ShowLines(self, '判断位置 0 和位置 3 上的字符，两者相等')
        self.play(ApplyMethod(pat[0].set_color, GREEN),
                  ApplyMethod(pat[3].set_color, GREEN))
        ShowLines(self, '此时，子串最大公共前后缀长度是 1')
        self.play(Write(Text('1').move_to(prefix[3].get_bottom() + UP * 0.6)))
        ShowLines(self, 'j，k均右移，进行下一轮循环')
        self.play(ApplyMethod(j.shift, RIGHT * 1.2),
                  ApplyMethod(k.shift, RIGHT * 1.2))
        '''判断1和4'''
        ShowLines(self, '判断位置 1 和位置 4 上的字符，两者不相等')
        self.play(Indicate(pat[1], color=RED), Indicate(pat[4], color=RED))
        self.play(ApplyMethod(pat[0].set_color, WHITE),
                  ApplyMethod(pat[3].set_color, WHITE))
        ShowLines(self, 'k 回退一位，进行下一轮循环的比较')
        self.play(ApplyMethod(k.shift, LEFT * 1.2))
        '''比较0和4'''
        ShowLines(self, '判断位置 0 和位置 4 上的字符，两者相等')
        self.play(ApplyMethod(pat[0].set_color, GREEN),
                  ApplyMethod(pat[4].set_color, GREEN))
        ShowLines(self, '此时，子串最大公共前后缀长度是 1')
        self.play(Write(Text('1').move_to(prefix[4].get_bottom() + UP * 0.6)))
        ShowLines(self, 'j，k均右移，进行下一轮循环')
        self.play(ApplyMethod(j.shift, RIGHT * 1.2),
                  ApplyMethod(k.shift, RIGHT * 1.2))
        '''比较1和5'''
        ShowLines(self, '接下来，我们分别比较1和5，2和6，3和7上的字符，结果均相等，我们实行与上述相同的操作', time=2)
        self.play(ApplyMethod(pat[1].set_color, GREEN),
                  ApplyMethod(pat[5].set_color, GREEN))
        self.play(Write(Text('2').move_to(prefix[5].get_bottom() + UP * 0.6)))
        self.play(ApplyMethod(j.shift, RIGHT * 1.2),
                  ApplyMethod(k.shift, RIGHT * 1.2))
        '''比较2和6'''
        self.play(ApplyMethod(pat[2].set_color, GREEN),
                  ApplyMethod(pat[6].set_color, GREEN))
        self.play(Write(Text('3').move_to(prefix[6].get_bottom() + UP * 0.6)))
        self.play(ApplyMethod(j.shift, RIGHT * 1.2),
                  ApplyMethod(k.shift, RIGHT * 1.2))
        '''比较3和7'''
        self.play(ApplyMethod(pat[3].set_color, GREEN),
                  ApplyMethod(pat[7].set_color, GREEN))
        self.play(Write(Text('4').move_to(prefix[7].get_bottom() + UP * 0.6)))
        ShowLines(self, '此时，子串的最大相同前后缀的长度为 3，我们即将进入位置 4 和位置 8 的比较', time=2)
        self.play(ApplyMethod(j.shift, RIGHT * 1.2),
                  ApplyMethod(k.shift, RIGHT * 1.2))
        '''比较4和8'''
        ShowLines(self, '比较发现，4和8并不相等')
        self.play(Indicate(pat[4], color=RED), Indicate(pat[8], color=RED))
        self.play(ApplyMethod(pat.set_color, WHITE))
        ShowLines(self, '也就是说，当前子串的最大相同前后缀长度不可能为 4', time=1)
        ShowLines(self, '我们退而求其次，看看是否有长度为 3 的前后缀，因此使 k 回退', time=1)
        self.play(ApplyMethod(k.shift, LEFT * 1.2))
        '''比较3和8'''
        ShowLines(self, '比较发现，3和8也不相等')
        self.play(Indicate(pat[3], color=RED), Indicate(pat[8], color=RED))
        ShowLines(self, '看来也找不到长度为3的前后缀了，再退一个试试？', time=1)
        self.play(ApplyMethod(k.shift, LEFT * 1.2))
        '''比较2和8'''
        ShowLines(self, '2和8又不相等')
        self.play(Indicate(pat[2], color=RED), Indicate(pat[8], color=RED))
        ShowLines(self, '没办法了，再退一格试试吧')
        self.play(ApplyMethod(k.shift, LEFT * 1.2))
        '''比较1和8'''
        ShowLines(self, '1和8终于相等了！')
        self.play(ApplyMethod(pat[1].set_color, GREEN),
                  ApplyMethod(pat[8].set_color, GREEN))
        ShowLines(self, '恭喜！我们经过多次回退，得到了字串的最大相同前后缀长度为2', time=1)
        self.play(
            ApplyMethod(pat[7].set_color, GREEN),
            ApplyMethod(pat[0].set_color, GREEN),
        )
        self.play(Write(Text('2').move_to(prefix[8].get_bottom() + UP * 0.6)))
        ShowLines(self, '继续前进吧！')
        self.play(ApplyMethod(j.shift, RIGHT * 1.2),
                  ApplyMethod(k.shift, RIGHT * 1.2))
        '''比较2和9'''
        ShowLines(self, '比较发现，2和9并不相等')
        self.play(Indicate(pat[2], color=RED), Indicate(pat[9], color=RED))
        ShowLines(self, '老办法，k继续回退')
        self.play(ApplyMethod(pat.set_color, WHITE))
        self.play(ApplyMethod(k.shift, LEFT * 1.2))
        '''比较1和9'''
        ShowLines(self, '比较1和9，仍然不相等')
        self.play(Indicate(pat[1], color=RED), Indicate(pat[9], color=RED))
        ShowLines(self, '退，都可以退')
        self.play(ApplyMethod(k.shift, LEFT * 1.2))
        '''比较0和9'''
        ShowLines(self, '比较0和9，两者不相等')
        self.play(Indicate(pat[0], color=RED), Indicate(pat[9], color=RED))
        ShowLines(self, 'k 回退一位至 -1')
        self.play(ApplyMethod(k.shift, LEFT * 1.2))
        ShowLines(self, '此时 k=-1，代表子串最大公共前后缀长度是 0')
        self.play(Write(Text('0').move_to(prefix[9].get_bottom() + UP * 0.6)))
        self.wait(0.5)
        self.play(FadeOut(j), FadeOut(k), FadeOut(index[-1]),
                  ApplyMethod(pat[0].set_color, WHITE),
                  ApplyMethod(pat[9].set_color, WHITE))
        ShowLines(self, '至此，我们填满了所有的空格，循环结束', time=1.5)
        self.wait()