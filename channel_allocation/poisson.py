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

        for _ in range(5):  
            self.play(FadeOut(stickmen[len(stickmen) - 1]))  
            stickmen.remove(stickmen[len(stickmen) - 1])  
            self.play(stickmen.animate.arrange(RIGHT, buff= .1).next_to(shop, LEFT, buff= .1))  
            
            self.wait()

        self.play(FadeOut(shop))
        self.wait()

        x_axis = NumberLine(
            x_range = [0, 10, 1], 
            length = 10,           
            color = WHITE,        
            include_numbers = False, 
            include_tip = True
        )

        font_size = 35

        time_label = MathTex(r"\text{Time}", font_size = font_size)
        time_label.next_to(x_axis.get_end(), DOWN)

        no_subintervals = MathTex(r"n \text{ subintervals}", font_size = font_size)
        no_subintervals.next_to(x_axis, DOWN)

        probability_subinterval = MathTex(r"P(\text{joining in one subinterval}) = p", font_size = font_size)
        expected_customers = MathTex(r"E\left[\text{\# customers}\right] = np", font_size = font_size) 

        formulas = VGroup(probability_subinterval, expected_customers)
        formulas.arrange(DOWN, aligned_edge = LEFT)
        formulas.to_corner(UL)

        self.play(Create(x_axis))
        self.play(Write(time_label), Write(no_subintervals))


        interval_highlight = Line(
            start = x_axis.n2p(2), 
            end = x_axis.n2p(3), 
            color = ORANGE, 
            stroke_width = 10
        )

        self.play(Write(probability_subinterval), Create(interval_highlight))

        self.wait()

        interval_highlight2 = Line(
            start = x_axis.n2p(4), 
            end = x_axis.n2p(5), 
            color = ORANGE, 
            stroke_width = 10
        )

        self.play(Create(interval_highlight2), Uncreate(interval_highlight))

        self.wait()

        self.play(Write(expected_customers))

        stickman1 = ImageMobject("./assets/stickman.png")
        stickman1.set_color(WHITE)
        stickman1.scale_to_fit_height(1)

        stickman2 = stickman1.copy()

        # Position the stickmen above the highlighted intervals
        stickman1.next_to(interval_highlight2.get_start(), UP)
        stickman1.shift(RIGHT * 0.2)
        stickman2.next_to(interval_highlight2.get_end(), UP)
        stickman2.shift(LEFT * 0.2)

        self.play(FadeIn(stickman1), FadeIn(stickman2))

        x_axis_final = NumberLine(
            x_range = [0, 10, 0.2], 
            length = 10,           
            color = WHITE,        
            include_numbers = False, 
            include_tip = True
        )

        self.wait()

        self.play(Uncreate(interval_highlight2))

        self.wait(.5)

        n_to_infty = MathTex(r"n \rightarrow \infty", font_size = font_size)
        n_to_infty.next_to(no_subintervals, DOWN)
        self.play(Transform(x_axis, x_axis_final), Write(n_to_infty))

        self.wait()

        interval_highlight1_final = Line(
            start = x_axis_final.n2p(4), 
            end = x_axis_final.n2p(4.2), 
            color = ORANGE, 
            stroke_width = 10
        )

        interval_highlight2_final = Line(
            start = x_axis_final.n2p(4.6), 
            end = x_axis_final.n2p(4.8), 
            color = ORANGE, 
            stroke_width = 10
        )

        self.wait(.5)

        self.play(Create(interval_highlight1_final), Create(interval_highlight2_final))

        self.wait()

        # adjusted_probability = MathTex(r"P(\text{joining in one subinterval}) = p = {\lambda \over n}", font_size = font_size)
        adjusted_probability = MathTex(r"P(\text{joining in one subinterval}) = p = {\lambda \over n}",
            font_size=font_size
        )
        expected_customers_infinite = MathTex(r"E\left[\text{\# customers}\right] = np \rightarrow \infty", font_size=font_size)
        expected_customers_lambda = MathTex(r"E\left[\text{\# customers}\right] = np = n{\lambda \over n} = \lambda", font_size=font_size)

        adjusted_probability.move_to(probability_subinterval)
        adjusted_probability.align_to(probability_subinterval, LEFT)

        expected_customers_infinite.move_to(expected_customers)
        expected_customers_infinite.align_to(expected_customers, LEFT)

        expected_customers_lambda.move_to(expected_customers)
        expected_customers_lambda.align_to(expected_customers, LEFT)

        self.play(Transform(probability_subinterval, adjusted_probability))

        self.wait(.5)

        self.play(Transform(expected_customers, expected_customers_infinite))   
        self.wait(.5)

        self.play(Transform(expected_customers, expected_customers_lambda))

        self.wait(.5)     

        self.play(FadeOut(stickman1, stickman2))
        self.play(Uncreate(interval_highlight1_final), Uncreate(interval_highlight2_final))

        def create_highlight_intervals(start_points, interval_length, chosen_color):
            intervals = []
            for start in start_points:
                interval = Line(
                    start = x_axis_final.n2p(start), 
                    end = x_axis_final.n2p(start + interval_length), 
                    color = chosen_color, 
                    stroke_width = 10
                )
                intervals.append(interval)
            return intervals

        # First set of intervals
        start_points1 = [1.0, 4.4, 5.0, 5.4]
        interval_length = 0.2
        intervals1 = create_highlight_intervals(start_points1, interval_length, ORANGE)

        start_points2 = [1.4, 2.0, 2.6, 4.6]
        intervals2 = create_highlight_intervals(start_points2, interval_length, GREEN)


        self.play(*[Create(interval) for interval in intervals1])
        self.wait()

        self.play(*[Create(interval) for interval in intervals2])
        self.wait()

        binomial_distribution = MathTex(r"X \sim \text{Bin}(n, p)", font_size = font_size)
        # probability_formula_binomial = MathTex(r"P(X = k) = \binom{n}{k}p^k(1-p)^{n-k}", font_size = font_size)

        part1 = MathTex(r"P(X = k) = ", font_size = font_size)
        part2 = MathTex(r"\binom{n}{k}", font_size = font_size)
        part3 = MathTex(r"p^k", font_size = font_size)
        part4 = MathTex(r"(1-p)^{n-k}", font_size = font_size)
        probability_formula_binomial = VGroup(part1, part2, part3, part4).arrange(RIGHT)

        VGroup(binomial_distribution, probability_formula_binomial).arrange(DOWN, aligned_edge = LEFT).to_corner(DL)

        self.play(Write(binomial_distribution))

        self.wait()

        self.play(Write(part1))  # Write P(X = k) =
        self.wait(.5)
        self.play(Write(part3))
        self.wait()
        self.play(Write(part4))
        self.wait()
        self.play(Write(part2))
        self.wait()

        self.play(FadeOut(*[mob for mob in self.mobjects]))

        probability_formula_binomial = MathTex(
            r"P(X = k) = ",
            r"\binom{n}{k}",
            r"p^k",
            r"(1-p)^{n-k}"
        )
        probability_formula_binomial.move_to(ORIGIN)
        self.wait()
        self.play(FadeIn(probability_formula_binomial))
        
        assumption = MathTex(r"\text{Assumption: } n \rightarrow \infty", font_size = font_size)
        assumption.to_corner(UR)
        self.play(FadeIn(assumption))

        font_size2 = 38
        probability_formula_expanded = MathTex(
            r"P(X = k) = ",
            r"{n(n-1)\dots 1 \over k!}",
            r"\left({\lambda \over n}\right)^k",
            r"\left(1 - {\lambda \over n}\right)^n \left(1 - {\lambda \over n}\right)^{-k}",
            font_size = font_size2
        )

        probability_formula_expanded2 = MathTex(
            r"P(X = k) = ",
            r"{\lambda^k \over k!}",
            r"{n(n - 1)\dots1 \over n^k}",
            r"\left(1 - {\lambda \over n}\right)^n",
            r"\left(1 - {\lambda \over n}\right)^{-k}",
            font_size = font_size2
        )
        probability_formula_expanded3 = MathTex(
            r"P(X = k) = ",
            r"{\lambda^k \over k!}",
            r"\left(1 - {0 \over n}\right) \left(1 - {1 \over n}\right) \left(1 - {2 \over n}\right) \dots \left(1 - {(k - 1) \over n}\right)",
            r"\left(1 - {\lambda \over n}\right)^n",
            r"\left(1 - {\lambda \over n}\right)^{-k}",
            font_size = font_size
        )
        # self.play(probability_formula_expanded[0].animate.move_to(probability_formula_binomial[0]))
        # self.play(Transform(probability_formula_binomial[1], probability_formula_expanded[1]))
        # self.play(Transform(probability_formula_binomial[3], probability_formula_expanded[3]))
        # self.wait()
        self.play(TransformMatchingShapes(probability_formula_binomial, probability_formula_expanded))
        self.wait()
        self.play(TransformMatchingShapes(probability_formula_expanded, probability_formula_expanded2))
        self.wait()
        self.play(TransformMatchingShapes(probability_formula_expanded2, probability_formula_expanded3))
        
        rect = SurroundingRectangle(probability_formula_expanded3[2])
        rect.set_color(ORANGE)
        self.play(Create(rect))
        self.wait()

        rect2 = SurroundingRectangle(probability_formula_expanded3[4])
        rect2.set_color(ORANGE)
        self.play(Create(rect2))

        self.wait()
        self.play(Uncreate(rect), Uncreate(rect2))
        self.wait()

        probability_formula_expanded4 = MathTex(
            r"P(X = k) = ",
            r"{\lambda^k \over k!}",
            r"\left(1 - {\lambda \over n}\right)^n",
            font_size = font_size2
        )

        self.play(TransformMatchingShapes(probability_formula_expanded3, probability_formula_expanded4))
        self.wait()

        probability_formula_expanded5 = MathTex(
            r"P(X = k) = ",
            r"{\lambda^k \over k!}",
            r"e^{-\lambda}",
            font_size = font_size2
        )

        self.play(TransformMatchingShapes(probability_formula_expanded4, probability_formula_expanded5))
        self.wait()

        poisson = MathTex(r"\text{Poisson Process}", font_size = 50)
        poisson.set_color(ORANGE)
        poisson.to_edge(DOWN)
        self.play(Write(poisson))
        self.wait()