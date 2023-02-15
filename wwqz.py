class television:
    screen_L = 40
    screen_H = 20
class playstation:
    Convenient = 80
class laptop(playstation, television):
    def __init__(self):
        print(self.screen_L)
        print(self.screen_H)
        print(self.Convenient)
PC=laptop()