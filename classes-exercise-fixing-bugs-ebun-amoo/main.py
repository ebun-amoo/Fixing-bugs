
class Point:
    def __init__(self, initial_x, initial_y):
        self.x = initial_x
        self.y = initial_y
    def move_right(self):
        self.x += 1


instance = Point(0,0)
instance.move_right()

