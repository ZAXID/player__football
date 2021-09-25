class Football:
    def __init__ (self, name, position):
        self.name = name
        self.position = position

    def talk(self):
        print("How do you want to name football player", self.name, "What is his position", self.position)

def main():
    
    crit1 = Football ("Тибо", "1")
    crit1.talk()

    crit2 = Football ("Давид", "4")
    crit2.talk()

    crit3 = Football ("Начо", "6")
    crit3.talk()

    crit4 = Football ("Даниэль", "2")
    crit4.talk()

    crit5 = Football ("Мигель", "35")
    crit5.talk()

    crit6 = Football ("Эдер", "3")
    crit6.talk()

    crit7 = Football ("Марко", "11")
    crit7.talk()

    crit8 = Football ("Родриго", "21")
    crit8.talk()

    crit9 = Football ("Лука", "10")
    crit9.talk()

    crit10 = Football ("Антонио", "27")
    crit10.talk()

    crit11 = Football ("Карим", "9")
    crit11.talk()

main() 