from Square_square import Square


class Rectangle(Square):
    def __init__(self, said=5, said2=10):
        super().__init__(said)
        self.said = said
        self.said2 = said2

    def calculate_area(self):
        super().calculate_area()
        return self.said * self.said2

    def draw(self):
        for i in range(self.side):
            print(' * ' * self.said2)


r1 = Rectangle()
print(r1.calculate_area())
print(r1.draw())