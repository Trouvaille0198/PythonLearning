'''
播放 KMP 演示动画：命令行输入 manim getNext.py PlayKmp -p
播放 Next 演示动画：命令行输入 manim getNext.py PlayNext -p
'''
from manim import *

getNext_code = '''
void getNext(const string &pat, int *next)
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
            next[j] = k+1; //记录到此索引前字符串真子串的长度
        }
        else
            k = next[k-1]; //寻求新的匹配字符
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


def ShowLines(self, line, direction=DOWN * 2.5, time=0.5, size=0.5):
    text = Text(line).shift(direction).scale(size)
    self.play(FadeIn(text))
    self.wait(time)
    self.play(FadeOut(text))
