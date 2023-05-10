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
            sum_coordinate = sum.coordinate_label()
            self.add(NumberPlane())
            static_coordinates, operand_coordinates = static.coordinate_label(), operand.coordinate_label()
            self.add(static, operand, static_coordinates, operand_coordinates)

            # Show the operand slide up the length of the static vector until the tail of the operand is at the head of the static vector
            self.play(ApplyMethod(operand.shift, static.get_end()))
            # Show the sum vector
            self.play(Create(sum))
            self.remove(static, operand)
            self.add(sum_coordinate)
            self.wait(5)
    return VectorAddition
