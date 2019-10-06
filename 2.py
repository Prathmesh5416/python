#An Aircraft Object

class Aircraft:
    x=y = 0
    acceleration = 1

    def move_left(self):
        self.x = self.x-1

    def move_right(self):
        self.x = self.x+1

    def move_up(self):
        self.y = self.y+1

    def move_down(self):
        self.y = self.y-1

print("# Exercise 2")
instance = Aircraft()
print("Initial X-Coord:", instance.x)
print("Initial Y-Coord:", instance.y)

instance.move_left()
instance.move_up()
instance.move_right()
instance.move_left()
instance.move_down()
instance.move_up()
instance.move_right()
instance.move_left()
instance.move_down()
instance.move_up()
instance.move_right()
print("Final X-Coord:", instance.x)
print("Final Y-Coord:", instance.y)
