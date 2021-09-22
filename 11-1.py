import math

class Circle:
    PI = 3.1415

    def calc_cirumference(self,radius):
        res = 2 * Circle.PI * radius
        return math.floor(res * 10 **3)/(10 ** 3)

    def calc_area(self, radius):
        res = 2 * Circle.PI * radius ** 2
        return math.floor(res * 10 ** 3)/(10 ** 3)

class Main:

    def execute(self):
        circle = Circle()