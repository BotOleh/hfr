import random
import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="logs.log", filemode="w",
                    format="We have next logging message: "\
                           "%(asctime)s:%(levelname)s-%(message)s"
                    )
class Human:
    def __init__(self, name="Human", job=None, home=None, car=None, animal=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.animal = animal
        self.home = home

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_animal(self):
        self.animal = animal(Breed_of_animals)


    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <=0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("I bought fuel")
            logging.INFO("I bought fuel")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("Bought food")
            logging.INFO("Bought food")
            self.money -= 50
            self.home.food += 50
            self.animal.feed += 30
        elif manage == "delicacies":
            print("Hooray! Delicious!")
            logging.INFO("Hooray! Delicious!")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0
    def to_repair(self):
        self.car.strength += 100
        self.money -= 50
    def to_buy_a_new_pet(self):
        self.money -= 50
    def to_Start_working(self):
        self.money += 25
        self.animal.Feed -= 25

    def days_indexes(self, day):
        day = f" Today the {day} of {self.name}'s life "
        print(f"{day:=^50}", "\n")
        logging.INFO(f"{day:=^50}", "\n")
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:^50}", "\n")
        logging.INFO(f"{human_indexes:^50}", "\n")
        print(f"Money – {self.money}")
        logging.INFO(f"Money – {self.money}")
        print(f"Satiety – {self.satiety}")
        logging.INFO(f"Satiety – {self.satiety}")
        print(f"Gladness – {self.gladness}")
        logging.INFO(f"Gladness – {self.gladness}")
        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}", "\n")
        logging.INFO(f"{home_indexes:^50}", "\n")
        print(f"Food – {self.home.food}")
        logging.INFO(f"Food – {self.home.food}")
        print(f"Mess – {self.home.mess}")
        logging.INFO(f"Mess – {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:^50}", "\n")
        logging.INFO(f"{car_indexes:^50}", "\n")
        print(f"Fuel – {self.car.fuel}")
        logging.INFO(f"Fuel – {self.car.fuel}")
        print(f"Strength – {self.car.strength}")
        logging.INFO(f"Strength – {self.car.strength}")
        animal_indexes = f"{self.animal.Breed} animal indexes"
        print(f"{animal_indexes:^50}", "\n")
        logging.INFO(f"{animal_indexes:^50}", "\n")
        print(f"Feed – {self.animal.feed}")
        logging.INFO(f"Feed – {self.animal.feed}")
        print(f"Dexterity – {self.animal.dexterity}")
        logging.INFO(f"Dexterity – {self.animal.dexterity}")

    def is_alive(self):
        if self.gladness < 0:
            print("Depression…")
            logging.INFO("Depression…")
            return False
        if self.satiety < 0:
            print("Dead…")
            logging.INFO("Dead…")
            return False
        if self.money < -500:
            print("Bankrupt…")
            logging.INFO("Bankrupt…")
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("Settled in the house")
            logging.INFO("Settled in the house")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a car{self.car.brand}")
            logging.INFO(f"I bought a car{self.car.brand}")
        if self.animal is None:
            self.get_animal()
            print(f"I bought a animal{self.animal.Breed}")
            logging.INFO(f"I bought a animal{self.animal.Breed}")
        if self.job is None:
            self.get_job()
            print(f"I don't have a job, I'm going to get a job "
                  f"{self.job.job} with salary {self.job.salary}")
            logging.INFO(f"I don't have a job, I'm going to get a job "
                  f"{self.job.job} with salary {self.job.salary}")
        self.days_indexes(day)
        dice = random.randint(1, 4)
        if self.satiety < 20:
            print("I'll go eat")
            logging.INFO("I'll go eat")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("I want to chill, but there is so much mess…")
                logging.INFO("I want to chill, but there is so much mess…")
                print("So I will clean the house")
                logging.INFO("So I will clean the house")
                self.clean_home()
            else:
                print("Let`s chill!")
                logging.INFO("Let`s chill!")
                self.chill()
        elif self.money < 0:
            print("Start working")
            logging.INFO("Start working")
            self.work()
        elif self.car.strength < 15:
            print("I need to repair my car")
            logging.INFO("I need to repair my car")
            self.to_repair()
        elif dice == 1:
            print("Let`s chill!")
            logging.INFO("Let`s chill!")
            self.chill()
        elif dice == 2:
            print("Start working")
            logging.INFO("Start working")
            self.work()
        elif dice == 3:
            print("Cleaning time!")
            logging.INFO("Cleaning time!")
            self.clean_home()
        elif dice == 4:
            print("Time for treats!")
            logging.INFO("Time for treats!")
            self.shopping(manage="delicacies")

brands_of_car = {
    "BMW":{"fuel":100, "strength":100, "consumption": 6},
    "Lada":{"fuel":50, "strength":40, "consumption": 10},
    "Volvo":{"fuel":70, "strength":150, "consumption": 8},
    "Ferrari":{"fuel":80, "strength":120, "consumption": 14} }


class Auto:
    def __init__(self, brand_list):
        self.brand=random.choice(list (brand_list))
        self.fuel=brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption=brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cannot move")
            logging.INFO("The car cannot move")
            return False

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

job_list = {
 "Java developer":
                {"salary":50, "gladness_less": 10 },
 "Python developer":
                {"salary":40, "gladness_less": 3 },
 "C++ developer":
                {"salary":45, "gladness_less": 25 },
 "Rust developer":
                {"salary":70, "gladness_less": 1 },
 }


class Job:
    def __init__(self, job_list):
        self.job=random.choice(list(job_list))
        self.salary=job_list[self.job]["salary"]
        self.gladness_less=job_list[self.job]["gladness_less"]

Breed_of_animals = {
    "CAT":{"feed":30, "dexterity":100, "consumption": 5},
    "DOG":{"feed":70, "dexterity":40, "consumption": 8}, }

class animal:
    def __init__(self, Breed_list):
        self.Breed=random.choice(list (Breed_list))
        self.feed=Breed_list[self.Breed]["feed"]
        self.dexterity = Breed_list[self.Breed]["dexterity"]
        self.consumption=Breed_list[self.Breed]["consumption"]
    def walking(self):
        if self.strength > 0 and self.feed >= self.consumption:
            self.feed -= self.consumption
            self.dexterity -= 1
            return True
        else:
            print("The pet died")
            logging.INFO("The pet died")
            return False
        if feed > 200:
            print("pets died of overeating")
            logging.INFO("pets died of overeating")
            return False

nick = Human(name="Nick")
for day in range(1,800):
    if nick.live(day) == False:
        break