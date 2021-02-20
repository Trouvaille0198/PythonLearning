from scenes import *


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