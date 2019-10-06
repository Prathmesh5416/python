class Aircraft:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        print(self.x)
        print(self.y)

    def move_down(self):
        self.x = self.x-1

    def move_right(self):
        self.x = self.x+1

    def move_up(self):
        self.y = self.y+1

    def move_left(self):
        self.y = self.y-1

    instances=["instance1", "instance2", "instance3", "instance4", "instance5"]
    def instance_create(self):
        for i in range(len(instances)):
            if i==0: instances[i] = Aircraft(6,3)
            if i==1: instances[i] = Aircraft(7,8)
            if i==2: instances[i] = Aircraft(3,11)
            if i==3: instances[i] = Aircraft(19,13)
            if i==4: instances[i] = Aircraft(14,12)

    def final_x_y_coord(self):
        for i in range(len(instances)):
            print("\nAircraft [",i,"]")
            print("Final X-Coord:", instances[i].x)
            print("Final Y-Coord:", instances[i].y)

    def initial_x_y_coord(self):
        print("Creating New Aircraft Object:",i)
        print("New Aircraft Object Has Been Initalized:",i)
        print("Initial X-Coord:",instances[i].x)
        print("Initial Y-Coord:",instances[i].y)

    def directions(self):
        instances[i].move_down()
        instances[i].move_left()
        instances[i].move_right()
        instances[i].move_left()
        instances[i].move_up()
        instances[i].move_down()
        instances[i].move_left()
        instances[i].move_right()
        instances[i].move_down()
        instances[i].move_right()
        instances[i].move_left()

class Boeing_747(Aircraft):

    def __init__(self,x,y,x_d,y_d):
        self.x = x
        self.y = y
        self.x_d = x_d
        self.y_d = y_d


if __name__=='__main__':

    instances=["instance1", "instance2", "instance3", "instance4", "instance5"]
    for i in range(len(instances)):
        if i==0: instances[i] = Boeing_747(71,61,83,20)
        if i==1: instances[i] = Boeing_747(73,84,63,10)
        if i==2: instances[i] = Boeing_747(64,25,94,40)
        if i==3: instances[i] = Boeing_747(28,45,30,38)
        if i==4: instances[i] = Boeing_747(76,74,54,82)

        instances[i].initial_x_y_coord()
        print("New Boeing 747 Object Has Just Been Iniitalized:", i)
        print("X-Coord:",instances[i].x_d)
        print("Y-Coord:",instances[i].y_d)
        instances[i].directions()
    instances[i].final_x_y_coord()
