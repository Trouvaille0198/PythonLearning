from scenes import *


class Part4(Scene):
    def construct(self):
        # self.add(Text('Made by Loulou').scale(0.3).to_corner(RIGHT + DOWN))
        partTip = Text('PART 4').scale(3).set_color(YELLOW)

        self.play(DrawBorderThenFill(partTip))
        self.play(FadeOut(partTip))

        ShowLines(self, '让我们来看看 getNext() 的代码实现')

        code = Code(code=getNext_code,
                    language='cpp',
                    tab_width=4,
                    background="window",
                    font="Monospace",
                    style=Code.styles_list[18])
        self.play(Write(code))