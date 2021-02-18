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
            Square(side_length=1.2).move_to(UP * 2 + LEFT * 4).set_color(BLUE))
        for i in range(1, 9):
            array.add(array[0].copy().next_to(array[0],
                                              RIGHT,
                                              buff=1.2 * (i - 1)))
        # self.play(DrawBorderThenFill(array))
        '''填入字符串'''
        pat_list = ['B', 'A', 'B', 'D', 'B', 'A', 'B', 'A', 'C']
        pat = VGroup()
        for i in range(0, 9):
            pat.add(
                Text(pat_list[i]).move_to(array[i].get_bottom() + UP * 0.6))
        # self.play(Write(pat))
        '''frefix值'''
        prefix = array.copy().shift(DOWN * 1.2)
        # self.play(FadeIn(prefix))
        '''建立k指针'''
        k_text = Text('k', color="YELLOW").scale(0.8)
        k_arrow = Arrow(DOWN, UP * 0.1).next_to(k_text, UP)
        k = VGroup(k_text, k_arrow).next_to(prefix[0], DOWN).shift(LEFT * 1.2)
        # self.play(ShowCreation(k))
        '''建立j指针'''
        j_text = Text('j', color="YELLOW").scale(0.8)
        j_arrow = Arrow(DOWN, UP * 0.1).next_to(j_text, UP)
        j = VGroup(j_text, j_arrow).next_to(prefix[0], DOWN)
        # self.play(ShowCreation(j))
        '''添加指示文字'''
        pat_text = Text('pat').next_to(array[0], LEFT).scale(0.7)
        prefix_text = Text('prefix').next_to(prefix[0], LEFT).scale(0.7)
        tip = VGroup(pat_text, prefix_text)
        # self.play(FadeIn(tip))
        '''添加数组下标'''
        index = VGroup()
        for i in range(0, 9):
            index.add(MathTex(str(i), color=YELLOW).next_to(array[i], UP))
        index.add(MathTex('-1', color=YELLOW).next_to(index[0], LEFT * 3.6))
        # self.play(ShowCreation(index))
        '''return mobjects'''
        mobjects = VGroup(array, pat, prefix, k, j, tip, index)
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