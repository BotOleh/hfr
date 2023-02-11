import random
class cat:

    def __init__(self, name):
        self.name = name
        self.rest = 50
        self.eat = 0
        self.alive = True

    def to_eat(self):
        print("Time to eat")
        self.eat += 0.12
        self.rest -= 3


    def to_sleep(self):
        print("I will sleep")
        self.rest += 3

    def to_rest(self):
        print("Rest time")
        self.rest += 5
        self.eat -= 0.1

    def is_alive(self):
        if self.eat < -0.5:
            print("die…")
            self.alive = False
        elif self.rest <= 0:
            print("Depression…")
            self.alive = False
        elif self.eat > 5:
            print("I've eaten…")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.rest}")
        print(f"Progress = {round(self.eat, 2)}")

    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_eat()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_rest()
        self.end_of_day()
        self.is_alive()


George = cat(name="George")
for day in range(365):
    if George.alive == False:
        break
    George.live(day)
print(George)
#
#
#
#


# class Student:
#     print("Hi")
#     def __init__(self):
#         self.height = 160
#         print(self)
#
# first_student = Student()
# print(first_student.height)