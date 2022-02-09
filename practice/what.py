class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square(Rectangle):
    def __init__(self, length):
        super(Square, self).__init__(length, length)   # equivalent to super().__init__(length, length)

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length
        
class Cube(Square):
    def surface_area(self):
        face_area = super(Square, self).area()
        return face_area * 6
        
    def volume(self):
        face_area = super(Square, self).area()
        return face_area * self.length
        
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        super().__init__()
        
    def tri_area(self):
        return 0.5 * self.base * self.height

class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height
        super().__init__(self.base)
        
    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area
        
    def area_2(self):
        base_area = super().area()
        triangle_area = super().tri_area()
        return triangle_area * 4 + base_area
        

pyramid = RightPyramid(2, 4)
print(pyramid.area())
