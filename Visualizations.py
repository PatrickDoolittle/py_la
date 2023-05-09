from Vector import Vector as myVector
from Matrix import *
from manim import *

def vector_to_manim(vector: myVector):
    return Vector(vector.elements)

def display_vectors(vectors: List[Vector], labeled=True):
    class VectorDisplay(Scene):
        def construct(self):
            self.add(NumberPlane())
            for vector in vectors:
                self.add(vector)
            if labeled:
                for vector in vectors:
                    self.add(vector.coordinate_label())
    return VectorDisplay

def add_vectors(static: Vector, operand: Vector):
    class VectorAddition(Scene):
        def construct(self):
            sum = Vector(static.get_end() + operand.get_end())
            self.add(NumberPlane())
            self.add(static)
            self.add(operand)
            # Show the operand slide up the length of the static vector until the tail of the operand is at the head of the static vector
            self.play(ApplyMethod(operand.shift, static.get_end()))
            # Show the sum vector
            self.play(Create(sum))
            self.wait(5)
    return VectorAddition
