from manim import Scene, Graph, Create


class Anim(Scene):
    def construct(self):
        vertices = [1, 2]
        edges = [(1, 2)]

        layout = {1: [-1, 0, 1], 2: [1, 0, 2]}

        graph = Graph(
            vertices,
            edges,
            layout=layout,
            layout_scale=3,
        )
        self.play(Create(graph))
        self.wait(1)
