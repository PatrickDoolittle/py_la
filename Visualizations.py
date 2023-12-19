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
            # Show the two vectors used in input
            static_coordinates, operand_coordinates = static.coordinate_label(), operand.coordinate_label()
            static_coordinates.shift(0.2*DOWN + 0.3*RIGHT)
            self.add(static, operand, static_coordinates, operand_coordinates)

            #We will be showing how the sum vector calculated in the next line is found through an animation!
            vector_sum = Vector(static.get_end() + operand.get_end())
            sum_coordinate = vector_sum.coordinate_label()

            # The backdrop is a number plane
            np = NumberPlane()
            self.add(np)
            self.wait(2)


            # Move the two coordinate labels to the left of the screen to show vector addition element wise
            self.play( ApplyMethod(operand_coordinates.shift, 7*LEFT+.4*UP) )
            self.play( ApplyMethod(static_coordinates.next_to, operand_coordinates, RIGHT, {"buff":1}) )

            plus_symbol = Tex("+").next_to(operand_coordinates, RIGHT, buff=.3)
            equal_symbol = Tex("=").next_to(static_coordinates, RIGHT, buff=.3)
            sum_coordinate.next_to(equal_symbol, RIGHT, buff=.3)
            self.play(Write(plus_symbol), Write(equal_symbol), Write(sum_coordinate))
            self.wait(2)

            # Show the operand slide up the length of the static vector until the tail of the operand is at the head of the static vector
            self.play(ApplyMethod(operand.shift, static.get_end()))
            self.wait(1)

            # Show the sum vector
            self.play(Create(vector_sum), FadeOut(plus_symbol), FadeOut(equal_symbol), FadeOut(operand_coordinates), FadeOut(static_coordinates))
            self.play(ApplyMethod(sum_coordinate.next_to, vector_sum, RIGHT))
            self.wait(2)
            self.play(FadeOut(static), FadeOut(operand)) 
            self.remove(static, operand, static_coordinates, operand_coordinates)
            self.wait(2)

    return VectorAddition

def scale_vector(operand, scalar):
    class VectorScaling(MovingCameraScene):
        def construct(self):
            #Adjust camera frame
            self.camera.frame_height = 10
            self.camera.frame_width = 13
            self.camera.frame_center = 3*UP

            # Show the two vectors used in input
            operand_coordinates = operand.coordinate_label()
            operand_coordinates.shift(0.2*DOWN + 0.3*RIGHT)
            self.add(operand, operand_coordinates)

            #We will be showing how the sum vector calculated in the next line is found through an animation!
            vector_scaled = Vector(operand.get_end() * scalar)
            scaled_coordinate = vector_scaled.coordinate_label()

            # The backdrop is a number plane
            np = NumberPlane(
                x_range=[-10, 10, 1],
                y_range=[-2, 20, 1],
                axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
                }
            )


            self.add(np)
            self.wait(2)

            # Move the two coordinate labels to the left of the screen to show vector addition element wise
            self.play( ApplyMethod(operand_coordinates.shift, 7*LEFT+.4*UP) )

            scalar_symbol = Tex("* " + str(scalar)).next_to(operand_coordinates, RIGHT, buff=.3)
            equal_symbol = Tex("=").next_to(scalar_symbol, RIGHT, buff=.3)
            scaled_coordinate.next_to(equal_symbol, RIGHT, buff=.3)
            self.play(Write(scalar_symbol), Write(equal_symbol), Write(scaled_coordinate))
            self.wait(2)

            # Show the operand slide up the length of the static vector until the tail of the operand is at the head of the static vector
            self.play(ApplyMethod(operand.scale, scalar, {"about_point":ORIGIN}))
            self.wait(1)


    return VectorScaling

