'''
播放 KMP 演示动画：命令行输入 manim getNext.py PlayKmp -p
播放 Next 演示动画：命令行输入 manim getNext.py PlayNext -p
'''
from manim import *

getNext = '''
void GetNext(const string &pat, int *next)
//p[k]表示前缀，p[j]表示后缀
{
    int j = 0, k = -1;
    next[0] = -1; //设next[0]的初始值为-1
    while (pat[j] != '\\0')
    {
        if (k == -1 || pat[j] == pat[k])
        {
            j++;
            k++;         //j,k向后走
            next[j] = k; //记录到此索引前字符串真子串的长度
        }
        else
            k = next[k]; //寻求新的匹配字符
    }
}
'''


class CodeScene(Scene):
    def build(self):
        code = Code(code=getNext,
                    language='cpp',
                    tab_width=4,
                    background="window",
                    font="Monospace",
                    style=Code.styles_list[18])
        self.play(Write(code))


class NextScene(Scene):
    def build(self):
        '''建立数组格'''
        array = VGroup()
        array.add(
            Square(side_length=1.2).move_to(UP * 2 + LEFT * 5).set_color(BLUE))
        for i in range(1, 10):
            array.add(array[0].copy().next_to(array[0],
                                              RIGHT,
                                              buff=1.2 * (i - 1)))
        # self.play(DrawBorderThenFill(array))
        '''填入字符串'''
        pat_list = ['B', 'A', 'C', 'B', 'B', 'A', 'C', 'B', 'A', 'C']
        pat = VGroup()
        for i in range(0, 10):
            pat.add(
                Text(pat_list[i]).move_to(array[i].get_bottom() + UP * 0.6))
        # self.play(Write(pat))
        '''frefix值'''
        prefix = array.copy().shift(DOWN * 1.2)
        # self.play(FadeIn(prefix))
        '''建立k指针'''
        k_text = Text('k', color="YELLOW").scale(0.8)
        k_arrow = Arrow(DOWN, UP * 0.1).next_to(k_text, UP).set_color(YELLOW)
        k = VGroup(k_text, k_arrow).next_to(prefix[0], DOWN).shift(LEFT * 1.2)
        # self.play(ShowCreation(k))
        '''建立j指针'''
        j_text = Text('j', color="YELLOW").scale(0.8)
        j_arrow = Arrow(DOWN, UP * 0.1).next_to(j_text, UP).set_color(YELLOW)
        j = VGroup(j_text, j_arrow).next_to(prefix[0], DOWN)
        # self.play(ShowCreation(j))
        '''添加指示文字'''
        pat_text = Text('pat').next_to(array[0], LEFT).scale(0.5)
        prefix_text = Text('next').next_to(prefix[0], LEFT, buff=0).scale(0.5)
        tip = VGroup(pat_text, prefix_text)
        # self.play(FadeIn(tip))
        '''添加数组下标'''
        index = VGroup()
        for i in range(0, 10):
            index.add(MathTex(str(i), color=YELLOW).next_to(array[i], UP))
        index.add(MathTex('-1', color=YELLOW).next_to(index[0], LEFT * 3.6))
        # self.play(ShowCreation(index))
        '''return mobjects'''
        mobjects = VGroup(array, pat, prefix, k, j, index, tip)
        return mobjects


class KmpScene(Scene):
    def build(self):
        '''建立ob'''
        ob_block = VGroup()
        ob_block.add(
            Square(side_length=1, color=BLUE).move_to(UP * 1.5 + LEFT * 5))
        for i in range(1, 10):
            ob_block.add(ob_block[0].copy().next_to(ob_block[0],
                                                    RIGHT,
                                                    buff=1 * (i - 1)))

        ob_list = ['B', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'A', 'D']
        ob_text = VGroup()
        for i in range(0, 10):
            ob_text.add(
                Text(ob_list[i]).move_to(ob_block[i].get_bottom() + UP * 0.5))
        '''建立pat'''
        pat_block = VGroup()
        pat_block.add(
            Square(side_length=1).next_to(ob_block[0], DOWN).set_color(BLUE))
        for i in range(1, 5):
            pat_block.add(pat_block[0].copy().next_to(pat_block[0],
                                                      RIGHT,
                                                      buff=1 * (i - 1)))

        pat_list = ['A', 'B', 'C', 'A', 'A']
        pat_text = VGroup()
        for i in range(0, 5):
            pat_text.add(
                Text(pat_list[i], ).move_to(pat_block[i].get_bottom() +
                                            UP * 0.5))
        mobjects = VGroup(ob_block, ob_text, pat_block, pat_text)
        return mobjects


class PlayKmp(KmpScene):
    def construct(self):
        self.add(Text('Made by Trouvaille').scale(0.3).to_corner(RIGHT + DOWN))
        mobjects = self.build()
        self.add(mobjects)
        ob_block = mobjects[0]
        ob_text = mobjects[1]
        pat_block = mobjects[2]
        pat_text = mobjects[3]
        '''建立提示框'''
        squ = Rectangle(height=2.6, width=0.7).move_to(
            VGroup(ob_block[0], pat_block[0])).set_color(YELLOW)
        i = VGroup(Text('i'),
                   Arrow(UP, DOWN * 0.1)).arrange(DOWN).next_to(squ, UP)
        j = VGroup(Text('j'), Arrow(DOWN,
                                    UP * 0.1)).arrange(UP).next_to(squ, DOWN)
        j.set_color(YELLOW)
        i.set_color(YELLOW)
        squ = VGroup(squ, i, j)
        '''Step 1'''
        self.play(ShowCreation(squ))
        self.play(Indicate(ob_text[0], color=RED),
                  Indicate(pat_text[0], color=RED))
        self.play(ApplyMethod(VGroup(pat_block, pat_text).shift, RIGHT), )
        self.play(ApplyMethod(squ.shift, RIGHT))
        '''Step 2'''
        self.play(ApplyMethod(ob_text[1].set_color, GREEN),
                  ApplyMethod(pat_text[0].set_color, GREEN))
        self.play(ApplyMethod(squ.shift, RIGHT))
        '''Step 3'''
        self.play(ApplyMethod(ob_text[2].set_color, GREEN),
                  ApplyMethod(pat_text[1].set_color, GREEN))
        self.play(ApplyMethod(squ.shift, RIGHT))
        '''Step 4'''
        self.play(ApplyMethod(ob_text[3].set_color, GREEN),
                  ApplyMethod(pat_text[2].set_color, GREEN))
        self.play(ApplyMethod(squ.shift, RIGHT))
        '''Step 5'''
        self.play(ApplyMethod(ob_text[4].set_color, GREEN),
                  ApplyMethod(pat_text[3].set_color, GREEN))
        self.play(ApplyMethod(squ.shift, RIGHT))
        '''Step 6'''
        self.play(Indicate(ob_text[5], color=RED),
                  Indicate(pat_text[4], color=RED))
        self.play(ApplyMethod(ob_text[1].set_color, WHITE),
                  ApplyMethod(ob_text[2].set_color, WHITE),
                  ApplyMethod(ob_text[3].set_color, WHITE),
                  ApplyMethod(pat_text[1].set_color, WHITE),
                  ApplyMethod(pat_text[2].set_color, WHITE),
                  ApplyMethod(pat_text[3].set_color, WHITE))
        self.play(ApplyMethod(VGroup(pat_block, pat_text).shift, RIGHT * 3))
        '''Step 7'''
        self.play(ApplyMethod(ob_text[5].set_color, GREEN),
                  ApplyMethod(pat_text[1].set_color, GREEN))
        self.play(ApplyMethod(squ.shift, RIGHT))
        '''Step 8'''
        self.play(ApplyMethod(ob_text[6].set_color, GREEN),
                  ApplyMethod(pat_text[2].set_color, GREEN))
        self.play(ApplyMethod(squ.shift, RIGHT))
        '''Step 9'''
        self.play(ApplyMethod(ob_text[7].set_color, GREEN),
                  ApplyMethod(pat_text[3].set_color, GREEN))
        self.play(ApplyMethod(squ.shift, RIGHT))
        '''Step 10'''
        self.play(ApplyMethod(ob_text[8].set_color, GREEN),
                  ApplyMethod(pat_text[4].set_color, GREEN))
        self.play(FadeOut(squ))
        squ = Rectangle(height=2.6, width=4.7).move_to(
            VGroup(ob_block[6], pat_block[2])).set_color(YELLOW)

        self.play(ShowCreation(squ))
        self.wait()


def ShowLines(self, line, direction=DOWN * 2.5, time=0.5, size=0.5):
    text = Text(line).shift(direction).scale(size)
    self.play(FadeIn(text))
    self.wait(time)
    self.play(FadeOut(text))


class PlayNext(NextScene):
    def construct(self):
        mobjects = self.build()
        pat = mobjects[1]
        prefix = mobjects[2]
        k = mobjects[3]
        j = mobjects[4]
        index = mobjects[5]
        self.add(mobjects)
        origin_k = k.get_center()
        '''Step 1 k=-1'''
        ShowLines(self, '第一位只有一个字符串，自然写 0')
        self.play(Write(Text('0').move_to(prefix[0].get_bottom() + UP * 0.6)))
        self.play(ApplyMethod(j.shift, RIGHT * 1.2),
                  ApplyMethod(k.shift, RIGHT * 1.2))
        '''Step 2'''
        self.play(Indicate(pat[0], color=RED), Indicate(pat[1], color=RED))
        self.play(ApplyMethod(k.move_to, origin_k))
        self.play(Write(Text('0').move_to(prefix[1].get_bottom() + UP * 0.6)))
        '''Step 3 k=-1'''
        self.play(ApplyMethod(j.shift, RIGHT * 1.2),
                  ApplyMethod(k.shift, RIGHT * 1.2))
        '''Step 4'''
        self.play(Indicate(pat[0], color=RED), Indicate(pat[2], color=RED))
        self.play(ApplyMethod(k.move_to, origin_k))
        self.play(Write(Text('0').move_to(prefix[2].get_bottom() + UP * 0.6)))
        '''Step 5 k=-1'''
        self.play(ApplyMethod(j.shift, RIGHT * 1.2),
                  ApplyMethod(k.shift, RIGHT * 1.2))
        '''Step 6'''
        self.play(ApplyMethod(pat[0].set_color, GREEN),
                  ApplyMethod(pat[3].set_color, GREEN))
        self.play(Write(Text('1').move_to(prefix[3].get_bottom() + UP * 0.6)))
        self.play(ApplyMethod(j.shift, RIGHT * 1.2),
                  ApplyMethod(k.shift, RIGHT * 1.2))
        '''Step 7'''
        self.play(Indicate(pat[1], color=RED), Indicate(pat[4], color=RED))
        self.play(ApplyMethod(pat[0].set_color, WHITE),
                  ApplyMethod(pat[3].set_color, WHITE))
        self.play(ApplyMethod(k.shift, LEFT * 1.2))
        self.play(ApplyMethod(pat[0].set_color, GREEN),
                  ApplyMethod(pat[4].set_color, GREEN))
        self.play(Write(Text('1').move_to(prefix[4].get_bottom() + UP * 0.6)))
        self.play(ApplyMethod(j.shift, RIGHT * 1.2),
                  ApplyMethod(k.shift, RIGHT * 1.2))
        '''Step 8'''
        self.play(ApplyMethod(pat[1].set_color, GREEN),
                  ApplyMethod(pat[5].set_color, GREEN))
        self.play(Write(Text('2').move_to(prefix[5].get_bottom() + UP * 0.6)))
        self.play(ApplyMethod(j.shift, RIGHT * 1.2),
                  ApplyMethod(k.shift, RIGHT * 1.2))
        '''Step 9'''
        self.play(ApplyMethod(pat[2].set_color, GREEN),
                  ApplyMethod(pat[6].set_color, GREEN))
        self.play(Write(Text('3').move_to(prefix[6].get_bottom() + UP * 0.6)))
        self.play(ApplyMethod(j.shift, RIGHT * 1.2),
                  ApplyMethod(k.shift, RIGHT * 1.2))
        '''Step 10'''
        self.play(ApplyMethod(pat[3].set_color, GREEN),
                  ApplyMethod(pat[7].set_color, GREEN))
        self.play(Write(Text('4').move_to(prefix[7].get_bottom() + UP * 0.6)))
        self.play(ApplyMethod(j.shift, RIGHT * 1.2),
                  ApplyMethod(k.shift, RIGHT * 1.2))
        '''Step 11'''
        self.play(Indicate(pat[4], color=RED), Indicate(pat[8], color=RED))
        self.play(ApplyMethod(pat.set_color, WHITE))
        self.play(ApplyMethod(k.shift, LEFT * 1.2 * 3))
        '''Step 12'''
        self.play(ApplyMethod(pat[8].set_color, GREEN),
                  ApplyMethod(pat[7].set_color, GREEN),
                  ApplyMethod(pat[0].set_color, GREEN),
                  ApplyMethod(pat[1].set_color, GREEN))
        self.play(Write(Text('2').move_to(prefix[8].get_bottom() + UP * 0.6)))
        self.play(ApplyMethod(j.shift, RIGHT * 1.2),
                  ApplyMethod(k.shift, RIGHT * 1.2))
        '''Step 13'''
        self.play(Indicate(pat[2], color=RED), Indicate(pat[9], color=RED))
        self.play(ApplyMethod(pat.set_color, WHITE))
        self.play(ApplyMethod(k.shift, LEFT * 1.2 * 2))
        '''Step 14'''
        self.play(ApplyMethod(pat[0].set_color, GREEN),
                  ApplyMethod(pat[9].set_color, GREEN))
        self.play(Write(Text('1').move_to(prefix[9].get_bottom() + UP * 0.6)))
        self.wait(0.5)
        self.play(FadeOut(j), FadeOut(k), FadeOut(index[-1]),
                  ApplyMethod(pat[0].set_color, WHITE),
                  ApplyMethod(pat[9].set_color, WHITE))
        self.wait()


class Part2(NextScene):
    def construct(self):
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


class Part3(NextScene):
    def construct(self):
        ShowLines(self, '让我们回到刚才的场景...', time=2)
        mobjects = self.build()
        pat = mobjects[1]
        prefix = mobjects[2]
        k = mobjects[3]
        j = mobjects[4]
        index = mobjects[5]
        green_list = [0, 1, 2, 3, 5, 6, 7]
        for i in green_list:
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
        ShowLines(self, '4和8并不相等，k需要回退\n\n可是，一位一位的回退，不是太浪费时间了吗？', time=2)
        ShowLines(self, '数学家给我们提供了一种效率更高的办法\n\n不使 k--，而使 k=next[k-1]', time=2)
        self.play(FadeOut(k[1]), ApplyMethod(k[0].shift, LEFT * 1.2 + DOWN))
        formula = Text('=next[k-1]=1').scale(0.7).next_to(
            k[0], buff=0).set_color(YELLOW)
        self.play(FadeIn(formula))
        self.wait(1)
        self.play(FadeOut(formula), ApplyMethod(k[0].shift,
                                                LEFT * 2 * 1.2 + UP),
                  FadeIn(k[1].shift(LEFT * 3 * 1.2)))
