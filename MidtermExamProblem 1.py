class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14159

    def Area(self):
        return self.pi * self.radius ** 2

    def Perimeter(self):
        return 2 * self.pi * self.radius

    def Display(self):
        print("Area:", self.Area())
        print("Perimeter:", self.Perimeter())


radius = float(input("Enter the radius of a circle: "))
c = Circle(radius)
c.Display()