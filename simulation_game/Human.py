class Human:
    def __init__(self, *age, **name):
        assert isinstance(age, int)
        self.age = age
        assert isinstance(name, String)
        self.name = name
        self.love_num = 0
        self.money = 0
        self.health = 100.0
        self.mood = None

    def eat(self, food):
        pass

    def use(self, stuff):
        pass

    def pay(self, money):
        pass

    def mood(self, mood):
        self.mood = mood
        if mood == 'happpy':
            self.happy()
        elif mood == 'sad':
            self.sad()
        elif mood == 'angry':
            self.angry()
        elif mood == 'lukewarm':
            self.lukewarm()
        elif mood == 'heart_beating':
            self.heart_beating()

    def happy(self):
        pass

    def sad(self, self1):
        pass

    def angry(self):
        pass

    def lukewarm(self):
        pass

    def heart_beating(self):
        pass
