from manim import *


class test22(Scene):
    def construct(self):
        cir1 = Circle()
        cir2 = Circle(fill_opacity=1)
        text = Text("Text").scale(2)
        mobjects = VGroup(cir1, cir2, text).scale(1.5).arrange(RIGHT, buff=2)

        anims = AnimationGroup(ShowCreation(cir1), Write(cir2), FadeIn(text))
        self.play(anims)
        self.wait()