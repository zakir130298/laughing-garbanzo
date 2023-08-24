

class Worker:
    def __init__(self, speed, stamina, power, accuracy):
        self.speed = speed
        self.stamina = stamina
        self.power = power
        self.accuracy = accuracy
class Attacker(Worker):
    def __init__(self, speed, stamina, power, accuracy, shoot):
        super().__init__(speed, stamina, power, accuracy)
        self.shoot=shoot

    def show_goals(self, goals):
        return  goals.shoot

class Midfielder(Worker):
    def __init__(self, speed, stamina, power, accuracy, passes):
        super().__init__(speed, stamina, power, accuracy)
        self.passes = passes

    def show_goals(self, passes):
        return passes.passes


class Defender(Worker):
    def __init__(self, speed, stamina, power, accuracy, red_cards):
        super().__init__(speed, stamina, power, accuracy)
        self.red_cards = red_cards

    def show_goals(self, red_cards):
        return red_cards.red_cards

class Goalkeeper(Worker):
    def __init__(self, speed, stamina, power, accuracy, clean_sheets):
        super().__init__(speed, stamina, power, accuracy)
        self.clean_sheets = clean_sheets

    def show_goals(self, clean_sheets):
        return clean_sheets.clean_sheets

goalkeeper = Worker(30,40,100,120,40)



