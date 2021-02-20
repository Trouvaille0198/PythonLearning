from scenes import *


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
