from manim import (
    LinearTransformationScene,
    Matrix,
    UL,
    ORANGE,
    YELLOW,
    ORIGIN,
    LEFT,
    Rectangle,
)


class Anim(LinearTransformationScene):
    def construct(self):
        matrix = [[1, 2], [3, 4]]
        mmatrix = Matrix(matrix).to_edge(UL)

        # unit = self.get_unit_square()

        # vect = self.get_vector([1,-2], color=GREEN)

        rect = Rectangle(
            height=4, width=2, stroke_color=ORANGE, fill_color=YELLOW, fill_opacity=0.5
        ).next_to(ORIGIN, aligned_edge=LEFT)

        self.add_transformable_mobject(rect)

        self.add_background_mobject(mmatrix)
        # self.apply_matrix(matrix)

        self.wait()
