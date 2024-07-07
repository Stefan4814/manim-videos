from manim import *

class MyScene(Scene):
    def construct(self):
        self.wait()
        # one stickman
        stickman = ImageMobject("./assets/stickman.png")
        stickman.set_color(WHITE)
        stickman.scale_to_fit_height(2.5)

        shop = ImageMobject("./assets/shop.jpg")
        shop.scale_to_fit_height(3.5)
        shop.to_edge(RIGHT, buff = .5)

        stickmen = Group(*[stickman.copy() for _ in range(5)])
        stickmen.arrange(RIGHT, buff = .1)
        stickmen.next_to(shop, LEFT, buff = .1)

        self.wait()
        
        self.add(shop)
        for stickman in reversed(stickmen):
            self.play(FadeIn(stickman))
            self.wait(0.5)
        self.wait()