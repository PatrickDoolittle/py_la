from Vector import Vector
from Matrix import *
from manim import Vector as manimVector
from manim import Scene, NumberPlane

def vector_to_manim(vector: Vector):
    return manimVector(vector.elements)

def display_vectors(vectors: List[manimVector]):
    class VectorDisplay(Scene):
        def construct(self):
            self.add(NumberPlane())
            for vector in vectors:
                self.add(vector)
    return VectorDisplay
