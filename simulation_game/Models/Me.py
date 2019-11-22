class Me:
    def __init__(self):
        self.level = 1
        self.exp = 0.0
        self.luck_num = 0
        self.bag = {}
        self.lovers = []
        self.location = None
        self.world_num = 0
        self.age = input('Your Age:')
        self.name = input('Your Name:')
        self.gender = int(input('Your sex: 0.Male 1.Female'))

    def my_gender(self, gender):
        if gender == 0:
            self.gender = 'Boy'
        elif gender == 1:
            self.gender = 'Girl'

    def show_lovers(self):
        if len(self.lovers) == 0:
            print('No one, you are single.. Cheer up!')
        else:
            for i in range(len(self.lovers)):
                print(i+1, ':', self.lovers[i].name)
