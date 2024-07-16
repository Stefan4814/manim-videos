from manim import *

class Queue(Scene):
    def construct(self):
        font_size = 30
        expected_arrivals1 = MathTex(r"E\left[\text{\# arrivals}\right] = \lambda", font_size = font_size)
        expected_arrivals2 = MathTex(r"P(\text{arriving in one subinterval}) = {\lambda \over n}", font_size = font_size)
        expected_arrivals = VGroup(expected_arrivals1, expected_arrivals2).arrange(DOWN)

        right_arrow = MathTex(r"\Rightarrow")

        expected_departures1 = MathTex(r"E\left[\text{\# departures}\right] = \mu", font_size = font_size)
        expected_departures2 = MathTex(r"P(\text{departing in one subinterval}) = {\mu \over n}", font_size = font_size)
        expected_departures = VGroup(expected_departures1, expected_departures2).arrange(DOWN)

        arrivals_and_departures = VGroup(expected_arrivals, right_arrow, expected_departures).arrange(RIGHT, buff = 1.5)
        arrivals_and_departures.to_edge(UP)

        self.play(FadeIn(expected_arrivals))
        self.wait()
        self.play(FadeIn(right_arrow))
        self.wait()
        self.play(FadeIn(expected_departures))
        self.wait()

        notation_explanation = MathTex(r"\text{(}p_k(t) = \text{the probability of the queue be in state } k \text{ at time } t \text{)}", font_size = font_size)
        notation_explanation.to_corner(DL)
        self.play(FadeIn(notation_explanation))
        self.wait()

        font_size2 = 40
        states = VGroup(
            Circle(radius = 0.75, color = ORANGE).shift(LEFT * 2),
            Circle(radius = 0.75, color = ORANGE),
            Circle(radius = 0.75, color = ORANGE).shift(RIGHT * 2),
        ).arrange(RIGHT, buff = 1.5)
        
        state_labels = VGroup(
            MathTex(r"k - 1", font_size = font_size2).move_to(states[0].get_center()),
            MathTex(r"k", font_size = font_size2).move_to(states[1].get_center()),
            MathTex(r"k + 1", font_size = font_size2).move_to(states[2].get_center()),
        )
        
        arrows = VGroup(
            Arrow(start = states[0].get_top(), end = states[1].get_top(), buff = 0.2, stroke_width = 3).shift(UP * 0.5),
            Arrow(start = states[1].get_top(), end = states[2].get_top(), buff = 0.2, stroke_width = 3).shift(UP * 0.5),
            Arrow(start = states[1].get_bottom(), end = states[0].get_bottom(), buff = 0.2, stroke_width = 3).shift(DOWN * 0.5),
            Arrow(start = states[2].get_bottom(), end = states[1].get_bottom(), buff = 0.2, stroke_width = 3).shift(DOWN * 0.5),
        )
        
        arrow_labels = VGroup(
            MathTex(r"\lambda", font_size = font_size2).next_to(arrows[0], UP, buff = 0.1),
            MathTex(r"\lambda", font_size = font_size2).next_to(arrows[1], UP, buff = 0.1),
            MathTex(r"\mu", font_size = font_size2).next_to(arrows[2], DOWN, buff = 0.1),
            MathTex(r"\mu", font_size = font_size2).next_to(arrows[3], DOWN, buff = 0.1),
        )
        
        self.play(Create(states), Write(state_labels))
        self.wait()
        self.play(Create(arrows), Write(arrow_labels))
        self.wait()

        formula_state = MathTex(
            r"p_k\left(t + {1 \over n}\right) = ",
            r"p_k(t)\left(1 - \frac{\lambda}{n}\right)\left(1 - \frac{\mu}{n}\right)",
            r"+ p_{k-1}(t)\frac{\lambda}{n}",
            r"+ p_{k+1}(t)\frac{\mu}{n}",
            r"\quad \forall k \geq 1",
            font_size = font_size
        ).next_to(notation_explanation, UP, aligned_edge = LEFT)
                
        formula_state[2].set_color(GREEN)
        formula_state[3].set_color(RED)



        self.play(FadeIn(formula_state[0]))
        self.wait()
        self.play(
            FadeIn(formula_state[1]),
            arrow_labels[0].animate.set_opacity(0.5), arrows[0].animate.set_opacity(0.33), 
            arrow_labels[3].animate.set_opacity(0.5), arrows[3].animate.set_opacity(0.33)
        )
        self.wait()
        self.play(
            FadeIn(formula_state[2]),
            arrow_labels[1].animate.set_color(GREEN), arrows[1].animate.set_color(GREEN),
        )
        self.wait()
        self.play(
            FadeIn(formula_state[3]),
            arrow_labels[2].animate.set_color(RED), arrows[2].animate.set_color(RED),
        )
        self.wait()
        self.play(FadeIn(formula_state[4]))
        self.wait()
        
        elements_to_fadeout = [mob for mob in self.mobjects if mob not in [formula_state[i] for i in range(5)]]
        self.play(*[FadeOut(mob) for mob in elements_to_fadeout], formula_state.animate.set_color(WHITE))
        self.wait()

        formula_0 = MathTex(r"p_0\left(t + {1 \over n}\right) = p_0(t)\left(1 - \frac{\lambda}{n}\right)\left(1 - \frac{\mu}{n}\right) + p_1(t)\frac{\mu}{n}",
                            r"\Rightarrow",
                            r"p_0'(t) = -\lambda p_0(t)+\mu p_1(t)",
                            font_size = font_size
                    )  
        formula_0.to_corner(UL)
        self.play(FadeIn(formula_0[0]))
        self.wait()
        self.play(formula_state.animate.move_to(ORIGIN))
        self.wait()
        formula_before_diff_eq = MathTex(r"\frac{p_{k + 1}\left(t + \frac{1}{n}\right) - p_k(t)}{\frac{1}{n}} = \left(-\lambda - \mu + \frac{\lambda \mu}{n}\right)p_k(t) + \mu p_{k + 1}(t) + \lambda p_{k - 1}(t)}", font_size = font_size)
        formula_before_diff_eq.next_to(formula_state, DOWN)
        self.play(FadeIn(formula_before_diff_eq))

        long_arrow = MathTex(r"\Longrightarrow").rotate(3 * PI / 2).next_to(formula_before_diff_eq, DOWN)
        n_to_infty = MathTex(r"n \rightarrow \infty", font_size = font_size)
        n_to_infty.next_to(long_arrow, RIGHT)
        formula_diff_eq = MathTex(r"p_k'(t) = -(\lambda + \mu)p_k(t) + \mu p_{k + 1} + \lambda p_{k - 1}t", font_size = font_size)
        formula_diff_eq.next_to(long_arrow, DOWN)

        self.play(FadeIn(long_arrow))
        self.play(Write(n_to_infty))
        self.wait()
        self.play(FadeIn(formula_diff_eq))
        self.wait()
        self.play(FadeIn(formula_0[1]), FadeIn(formula_0[2]))
        self.wait()

        # self.play(*[FadeOut(mob for mob in self.mobjects if mob not in [formula_0[1], formula_diff_eq])])
        elements_to_fadeout = [mob for mob in self.mobjects if mob not in [formula_0[2], formula_diff_eq]]
        self.play(*[FadeOut(mob) for mob in elements_to_fadeout])
        self.wait()

        desired_pos = VGroup(formula_0[2].copy(), formula_diff_eq.copy()).arrange(DOWN).to_corner(UL)
        self.play(formula_0[2].animate.move_to(desired_pos[0]), formula_diff_eq.animate.move_to(desired_pos[1]))
        self.wait()

        
