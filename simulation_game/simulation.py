print('Simulation')

import random
import threading
from time import sleep


# Tips
class tip:
    a = 'If you reach 10 level, something special will be happen..'
    b = 'you will die if you arent in home at exactily 00:00 A.M'
    c = 'Go airport and have trip on another world!'
    d = 'Your maximum health increases when you level up'
    e = ' if you are lucky guy, then you may know what the love is...'
    f = 'raise your love score, then you\'ll get a special title!'
    g = 'coffees in this world are pretty expensive, why...?'
    h = 'You will be much more happy when you watch movie with your girlfriend..'
    i = 'In some islands, there are markets sell rare stuffs'
    j = 'The giftshop keeper is so tough, watch out!'
    k = 'You may get bad title if you be a bad guy to girls!'
    tiplist = [a, b, c, d, e, f, g, h, i, j, k]

    def tips(self):
        print(self.tiplist[random.randint(0, len(self.tiplist) - 1)])


tip = tip()


# Time
class time:
    hour = 0
    minute = 0
    second = 0
    ap = 'A.M'
    apnum = 0

    def second_append(self):
        while True:
            self.second += 1
            sleep(1)
            if self.second >= 60:
                self.minute_append(1)
                self.second = 0

    def minute_append(self, n):
        self.minute += n
        if self.minute >= 60:
            self.hour_append(int(self.minute / 60))
            self.minute %= 60

    def hour_append(self, n):
        if n == 0:
            return None
        self.hour += 1
        if self.hour == 12:
            self.hour = 0
            ap_list = ['A.M', 'P.M']
            ap_list.remove(self.ap)
            self.ap = ap_list[0]
            if self.ap == 'A.M':
                print('\n' * 5)
                print('Day 1 passed')
        self.hour_append(n - 1)

    def midnight(self):
        self.show_time()
        if self.hour == 0 and self.ap == 'A.M':
            print('IT\'S MIDNIGHT,TOO COLD..')
            self.hour_append(1)

    def show_time(self):
        print('%02d : %02d : %02d' % (self.hour, self.minute, self.second), self.ap)


# Me
class me():
    level = 1
    exp = 0.0
    money = 0.0
    health = 100.0
    positive = 0
    height = 175
    luck = 0
    girllist = []
    girlfriend = 0
    love = 0
    quitnumber = True
    bag = []
    bag_index = {}
    location = None
    world = 0
    another = False
    doctor = 0
    workspace = []
    s = []
    init = 0

    def __init__(self, age, name):
        self.age = age
        self.name = name

    for i in range(10):
        s.append(0)
    for i in range(200):
        s.append(1)
    for i in range(200):
        s.append(2)
    for i in range(300):
        s.append(3)
    for i in range(500):
        s.append(4)
    for i in range(1000):
        s.append(4)
    for i in range(2000):
        s.append(5)

    titlelist = ['lonely guy', 'love seeker', 'intermediate lover', 'upper-class lover', 'pick-up artist',
                 'love master♡', '•Casanova•']

    title = 'lonely guy'
    label = ''

    def my_girl(self):
        if self.girllist == []:
            print('No one... you solo...cheer up!')
        else:
            for i in range(len(self.girllist)):
                print(i + 1, ':', self.girllist[i].name)

    def my_love(self, n):
        self.love += n
        if self.love >= len(self.s):
            self.title = self.titlelist[6]
            print('You got the title "Casanova", what a fatal guy!')
        else:
            self.title = self.titlelist[self.s[self.love]]

    def init(self):
        input()
        self.level = 1
        self.exp = 0.0
        self.money = 100000000000.0
        self.health = 1.0
        self.positive = 0
        self.height = 175
        self.luck = 1000
        self.girllist = []
        self.girlfriend = 0
        self.love = 0
        self.bag = [magnifiner, warper]
        self.bag_index = {magnifiner.name: 1, warper.name: 1}
        self.location = home
        self.world = 0
        self.doctor = 0
        self.workspace = []
        self.title = 'lonely guy'
        self.label = '●TIME WARPER●'

    def wait(self, place):
        for i in range(10):
            n = random.randint(0, 1000)
            time.minute_append(10)
            r = int((me.luck) / 10)
            print('*' * (10 - i))
            sleep(0.3)
            if n + int(place.mood / 10) > 1000 - r:
                print('Someone girl talks to you. would you reply?')
                print('Yes : 1       No : 0')
                answer = int(input())
                if answer == 1:
                    girl_list[random.randint(0, len(girl_list)) - 1].initiate()
                return None
        print('No one you have met.. lonely')

    def pay(self, n):
        m = self.money - n
        if m < 0:
            print('you don\'t have enough money')
            return False
        else:
            self.money = round(m, 2)
            return True

    def show_bag(self):
        print('-------your bag----------')
        for i in range(len(self.bag)):
            print(i + 1, self.bag[i].name, '(', self.bag_index[self.bag[i].name], ')')
        print('-------------------------')

    def show_money(self):
        print('your money:', round(self.money, 2), '$')

    def die(self):
        if revivestone in me.bag:
            print('You revived by revive stone')
            revivestone.use()
        else:
            print('you died.........')
            print('<<<<<', self.name, 'record >>>>>>')
            self.my_status()
            self.quitnumber = False

    def my_status(self):
        print('------------------------------')
        print('name:', self.name, '    age:', self.age)
        print('level:', self.level, '     exp:', self.exp, '/', 100 + pow(self.level, 2) * 3)
        print('health:', self.health, '   luck:', self.luck)
        print('《', self.title, '》', ' [love]:', self.love)
        print('girlfriend :', self.girlfriend, '   loc:', self.location.location)
        print(self.label)
        print('------------------------------')
        time.show_time()
        self.show_bag()
        self.show_money()

    def go(self, n):
        print('where do you wanna go?')
        print('Cancle : 0')
        place = []
        for i in world[n]:
            place.append(i)
        if self.level >= 5:
            place.append(airport)
        place.remove(me.location)
        for i in range(len(place)):
            print(i + 1, ':', place[i].name)
        answer = int(input())
        if answer == 0:
            return None
        goal = place[answer - 1]
        if goal.restrict > me.level:
            print('Level restrict :', goal.restrict)
            input()
            return None
        if goal.l_restrict > me.love:
            print('Love restrict :', goal.l_restrict)
            input()
            return None
        if goal.g_restrict > me.girlfriend:
            print('You have to have', goal.g_restrict, ' girlfriend')
            input()
            return None
        distance = round(self.location.distance(goal), 2)
        print('The distance is', distance, 'm')
        print('how will you go by?')
        print('1: by foot(cost 10health per 100m)')
        print('2: taxi(cost 3$ per 100m)')
        print('3: bus(cost 1health & 1$ per 100m)')
        print('Cancle : 0')
        answer = int(input())
        if answer == 1:
            self.by_foot(goal)
        elif answer == 2:
            self.take_taxi(goal)
        elif answer == 3:
            self.take_bus(goal)
        elif answer == 0:
            return None

    def warp(self, n):
        pass

    def by_foot(self, goal):
        tired = round(self.location.distance(goal) / 10, 2)
        print('you will lose', tired, 'health')
        print('your health :', self.health)
        print('Cancel : 0')
        i = input()
        if i == '0':
            return None
        self.my_health(-tired)
        self.location = goal
        time.minute_append(int(self.location.distance(goal) / 50))

    def work(self, place):
        if self.level < place.level:
            print('sorry ' + self.name + ', you can\'t work for us until your level is', place.level)
        else:
            print('how many times do you wanna work?')
            pay = place.pay * (self.girlfriend + 1)
            exp = place.exp * (self.girlfriend + 1)
            difficulty = place.difficulty
            print('pay:', pay, '$ per hour')
            print('exp:', exp, 'per hour')
            print('you will lose', difficulty, 'health per hour')
            print('your health :', self.health)
            t = int(input())
            tired = difficulty * t
            if self.health < tired:
                print('you died from overwork....')
                self.die()
            else:
                self.my_health(-tired)
                time.hour_append(t)
                self.money += pay * t
                self.my_exp(place.exp * t)
                self.workspace.append(place)

    def take_taxi(self, goal):
        distance = self.location.distance(goal)
        taxi_cost = round((distance / 100) * 3, 2)
        print('you will lose :', taxi_cost, '$')
        print('your money :', self.money, '$')
        print('Cancel : 0')
        if input() == '0':
            return None
        if self.pay(taxi_cost):
            self.location = goal
            time.minute_append(int(distance / 500))

    def take_bus(self, goal):
        distance = self.location.distance(goal)
        bus_cost = round(distance / 100, 2)
        print('you will lose :', bus_cost, 'health and $')
        print('your health :', self.health, 'your money :', self.money, '$')
        print('Cancel : 0')
        if input() == '0':
            return None
        self.my_health(-bus_cost)
        if self.pay(bus_cost):
            self.location = goal
            time.minute_append(int(distance / 200))

    def quit(self):
        self.quitnumber = False

    def watch_tv(self):
        self.luck += 1
        time.hour_append(1)

    def steal(self):
        n = random.randint(1, 100)
        if n + self.luck > 70:
            print('you stole some stuff! ')
            time.minute_append(20)
            stuff = stuff_list[random.randint(0, len(stuff_list) - 1)]
            if stuff in me.bag:
                me.bag_index[stuff.name] += 1
            else:
                me.bag.append(stuff)
                me.bag_index[stuff.name] = 1
        else:
            print('you caught by clerk!')
            me.my_health(-50)
            time.minute_append(20)
        pass

    def sleep(self):
        self.my_health(70)
        time.hour_append(8)

    def my_exp(self, n):
        e = self.exp + n
        new_e = e - 100 - pow(self.level, 2) * 3
        if e >= 100 + pow(self.level, 2) * 3:
            self.level += 1
            if self.level >= 100:
                if self.girlfriend == 0:
                    print('You reached the highest level without no girlfriend. You are the Best Solo!')
                    self.label = 'The Best Solo Man'
                    self.my_status()
                    self.quit()
                    return None
                else:
                    print('Congratulation! You reached the highest level of this game!')
                    self.my_status()
                    self.label = '《GAME MASTER》'
                    self.quit()
                    return None
            self.exp = new_e
            self.luck += 1
            self.my_exp(0)
            print('congratulation! you level up')
        else:
            self.exp = e

    def my_health(self, n):
        h = round(self.health + n, 2)
        if h < 0:
            print('you died too tired')
            self.die()
        elif h > 100 + 10 * self.level:
            self.health = 100 + 10 * self.level
        else:
            self.health = h


# script
class script():
    p_response = ['I want to date with you..:)', 'I like you! so much!', 'what a cute guy♡', 'How charming^_^!',
                  'Awww...so sweet♡']
    n_response = ['No way..', 'you serious?', 'it dosent make sense', 'You bad guy!', 'I dont wanna see you']
    question = ['the weather is great! isnt it?', 'what are you looking at?', 'how looks am I?']
    answer = [['1: because of you', '2: yeah, the weather is great', '3: dont talk to me'],
              ['1: so beautiful sky', '2: two blue lake on your face', '3:  girl over there'],
              ['1: umm..quite cute.', '2: like hulk.', '3: can you see the sun exactly?']]
    responce = ['yeah, bye bye!.', 'see you later', 'thank you for chat with me']
    ccc = [1, 2, 3]
    nnn = [3, 3, 2]
    rrr = [2, 1, 1]


# Girl
class girl(me, script):
    def __init__(self, a):
        self.name = a

    def hello(self):
        print('Hello, my name is', self.name)

    def bye(self):
        print('bye,' + me.name + '!')

    def init(self):
        print('Could you chat with me?')

    def sad(self):
        print('O...K..... T_T')

    def makespace(self):
        for i in range(10):
            print()

    def initiate(self):

        print('press any key')
        input()
        self.makespace()
        self.hello()
        self.init()
        print('Yes : 1  No : 0')
        answer = int(input())
        if answer == 1:
            self.makespace()
            self.dialog()
        elif answer == 0:
            self.sad()

    def dialog(self):
        q = self.question
        a = self.answer
        p = self.p_response
        n = self.n_response
        r = self.responce
        anslist = []
        for i in range(len(q)):
            self.makespace()
            print(q[i])
            for j in range(len(a[i])):
                print(a[i][j])
            answer = int(input())
            anslist.append(answer)
        if anslist == script.ccc:
            self.makespace()
            me.my_love(150)
            print(p[random.randint(0, len(p) - 1)])
            print('you\'ve got 150 loves')
            if self not in me.girllist:
                me.girlfriend += 1
                me.girllist.append(self)
                print(self.name, 'be your girlfriend')
        elif anslist == script.nnn:
            print(n[random.randint(0, len(p) - 1)])
            me.my_love(-50)
            print('you lose 50 loves')
            me.title = 'negetive guy-_-'
            print('you gain rare title!')
        else:
            print(r[random.randint(0, len(r) - 1)])


# Stuffs

class stuff:
    cost = 0
    nut = 0
    exp = 0
    time = 0
    luck = 0
    num = 10000000
    name = ''
    love = 0
    etc = ''
    comment = ''

    def buy(self, n):
        cost = self.cost * n
        stuff = self
        if me.money < cost:
            print('you don\'t have enough money')
        else:
            me.money -= cost
            self.num -= 1 * n
            if stuff not in me.bag:
                me.bag.append(stuff)
                me.bag_index[stuff.name] = 1 * n
            else:
                me.bag_index[stuff.name] += 1 * n

    def use(self, n):
        if n == 0:
            return None
        if me.bag_index[self.name] < n:
            print('you can use it up to', me.bag_index[self.name])
            return None
        nut = self.nut * n
        stuff = self
        me.my_health(nut)
        me.my_exp(self.exp * n)
        me.my_love(self.love * n)
        time.minute_append(self.time * n)
        me.luck += self.luck * n
        me.bag_index[stuff.name] -= 1 * n
        print(self.comment)
        if me.bag_index[stuff.name] == 0:
            me.bag.remove(stuff)


# Revive Stone
class revivestone(stuff):
    name = 'revivestone'
    cost = 1200
    num = 3


# perfume
class p1(stuff):
    name = 'perfume(white musk)'
    love = 15
    luck = 10
    cost = 150
    num = 5


class p2(stuff):
    name = 'perfume(berbery weekend)'
    love = 30
    luck = 10
    cost = 280
    num = 5


class p3(stuff):
    name = 'perfume(The key)'
    love = 50
    luck = 15
    cost = 450
    num = 5


class book(stuff):
    name = 'Strange Book'
    cost = 1000

    def use(self, n):
        if me.level < 15:
            print('????????????????????')
            print('you can\'t use it now')
            print('¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿')
        else:
            if n > 1:
                print('you must use it one bye one')
                return None
            g = girl_list
            print('=========================')
            for i in range(len(g)):
                g[i].height = random.randint(150, 165)
                g[i].positive = random.randint(0, 100)
                print('name :', g[i].name, 'height :', g[i].height)
                if g[i].positive >= 50:
                    print('positive girl')
                else:
                    print('skeptive girl')
            print('=========================')
            super().use(n)


# Lovely red rose
class rose(stuff):
    name = 'lovley red rose'
    cost = 600
    love = 100
    comment = 'Aww...Smell....'


# Apple
class apple(stuff):
    name = 'apple'
    cost = 2
    nut = 5
    comment = 'delicious apple.'


# Peae
class pear(stuff):
    name = 'pear'
    cost = 3
    nut = 12
    comment = 'sparkling pear!'


# Chocolate
class chocolate(stuff):
    num = 100
    name = 'chocolate'
    cost = 3
    nut = -1
    exp = 5
    comment = 'you feel better for eating chocolate'


# Medicine
class medicine(stuff):
    name = 'medicine'
    cost = 30
    nut = 100
    comment = 'you got treatment!'


# magnifiner
class magnifiner(stuff):
    num = 1
    name = 'Magnifiner{?}'
    cost = 100
    etc = 'To see stuff information'

    def use(self, n):
        b = me.bag
        for i in range(len(b)):
            print('===========information==========')
            print(b[i].name, 'exp :', b[i].exp, 'health :', b[i].nut, 'luck :', b[i].luck, 'love :', b[i].love, 'etc :',
                  b[i].etc)


# master's note
class note(stuff):
    num = 5
    time = 30
    name = '[Mater\'s Note]'
    cost = 1000
    exp = 5000
    etc = 'The Note contains high knowledge'
    comment = 'The Love master\'s knowledge permeates all of your body'


# warper
class warper(stuff):
    num = 1
    name = '(Hidden)Warper\'s trace'
    etc = 'The Life of Time Warper'
    comment = 'The Time Warper, you got qualification to reach the MAXIMUM LEVEL'

    def use(self, n):
        me.level = 99
        print(self.comment)


# timewarper
class timewarper(stuff):
    num = 1
    name = '※TIME WARPER※'

    def use(self, n):
        print('*YOU CAN\'T USE IT NOW*')
        return None


# Places
class place:
    pay = 0
    difficulty = 0
    restrict = 0
    l_restrict = 0
    g_restrict = 0
    level = 0
    exp = 0
    q = 0
    name = ''

    def question(self):
        print('You are now in {', me.location.name, '}')
        print('Type the key you want')
        print('------------------------------')
        print('[1] Go get in     [s] watch my status')
        print('[2] leave hear    [g] watch my girlfriends')
        print('[3] work in here  [t] see random tips')
        print('[4] open my bag   [d] suicide')
        print()
        self.q = 0
        answer = input()
        if answer == '1':
            print('What will you do?')
            self.q = 1
        elif answer == '2':
            if me.another:
                me.warp(me.world)
                return None
            me.go(me.world)
        elif answer == '3':
            me.work(me.location)
        elif answer == '4':
            me.show_bag()
            print('Select the item')
            print('cancel: 0')
            answer = int(input())
            if answer == 0:
                pass
            else:
                if me.bag_index[me.bag[answer - 1].name] == 1:
                    me.bag[answer - 1].use(1)
                    return None
                print('How many?')
                num = int(input())
                me.bag[answer - 1].use(num)
        elif answer == 's':
            me.my_status()
        elif answer == 't':
            tip.tips()
        elif answer == 'd':
            me.die()
        elif answer == 'g':
            me.my_girl()
        else:
            self.question()

    def loc(self, x, y):
        self.location = (x, y)

    def distance(self, goal):
        return round(
            pow(pow(self.location[0] - goal.location[0], 2) + pow(self.location[1] - goal.location[1], 2), 0.5),
            2) * 100

    def shopping(self, s):
        print('type the number you want to buy')
        for i in range(len(s)):
            print(i + 1, ':', s[i].name, s[i].cost, '$  (', s[i].num, ')')
        print('cancel : 0')
        answer = int(input())
        if answer == 0:
            return None
        stuff = s[answer - 1]
        print('how many do you want')
        print('your money :', me.money)
        num = int(input())
        if stuff.num < num:
            print('you can\'t buy more than', stuff.num)
            self.shopping(s)
            return None
        print('Total cost is', num * stuff.cost, '$')
        print('1: Buy  2: Sorry')
        a = int(input())
        if a == 1:
            if me.money < num * stuff.cost:
                print('you don\'t have enough money')
                self.shopping(s)
                return None
            else:
                stuff.buy(num)
                me.show_bag()
                me.show_money()
                print('Continue shopping : 1   No : 2')
                if int(input()) == 1:
                    self.shopping(s)


# Home
class home(place):
    def __init__(self):
        pass

    name = 'my home♡'
    mood = 0
    pay = 1
    difficulty = 5
    exp = 5

    def question(self):
        if me.girlfriend >= 1:
            print('YOU SNEAKY...♡')
            input()
        super().question()
        if self.q == 1:
            print('[1] sleep')
            print('[2] watch Tv')
            print('Cancle : 0')
            answer = int(input())
            if answer == 1:
                me.sleep()
            elif answer == 2:
                me.watch_tv()
            elif answer == 0:
                return None


# Market
class market(place):
    name = 'Lily\'s Market'
    pay = 5
    difficulty = 10
    level = 0
    mood = 10
    exp = 10

    def question(self):
        super().question()
        if self.q == 1:
            print('[1] shopping')
            print('[2] steal some stuff')
            print('[3] just standing..')
            print('Cancel : 0')
            answer = int(input())
            if answer == 1:
                self.shopping(stuff_list)
            elif answer == 2:
                me.steal()
            elif answer == 3:
                me.wait(self)
            elif answer == 0:
                return None


# Cafe
class cafe(place):
    def __init__(self):
        pass

    name = 'Cafe ` Modern'
    pay = 10
    restrict = 3
    difficulty = 5
    level = 5
    mood = 60
    exp = 15

    def question(self):
        super().question()
        if self.q == 1:
            print('[1] order')
            print('[2] just sit and wait anybody')
            print('Cancel : 0')
            answer = int(input())
            if answer == 1:
                self.order()
            elif answer == 2:
                me.wait(self)
            elif answer == 0:
                return None

    def order(self):
        c = coffee_list
        for i in range(len(c)):
            print(i + 1, ':', c[i].name, c[i].cost, '$')
        answer = int(input())
        c[answer - 1].drink()


# Theater
class theater(place):
    def __init__(self):
        pass

    name = 'CGV Cinema'
    pay = 20
    difficulty = 10
    restrict = 5
    level = 10
    mood = 50
    exp = 20

    def question(self):
        super().question()
        if self.q == 1:
            print('[1] watch movie')
            print('[2] wait anyone')
            print('Cancel : 0')
            answer = int(input())
            if answer == 1:
                self.movie()
            elif answer == 2:
                me.wait(self)
            elif answer == 0:
                return None

    def movie(self):
        m = movie_list
        for i in range(len(m)):
            m[i].lovescore()
            print(i + 1, ':', m[i].name, '    ', m[i].cost, '$    ', m[i].time, 'minute')
            print('-------------------------')
        print('type the number you want')
        print('more information : s')
        print('Cancle : 0')
        answer = input()
        if answer == 's':
            print('what movie you wanna know?')
            ans = int(input())
            n = m[ans - 1]
            print('exp number:', n.exp)
            print('love number :', n.love)
            print('health number :', n.nut)
            print('lucky number :', n.luck)
            self.movie()
        elif answer == '0':
            return None
        else:
            m[int(answer) - 1].watch()


# company
class company(place):
    level = 10
    name = 'EMMA electronic Co.'

    def question(self):
        print('1 : Go back   2 : Knock')
        a = int(input())
        if a == 1:
            me.go(me.world)
        elif a == 2:
            self.work()
            self.question()
        else:
            self.question()

    def work(self):
        print('You will get money if you work hard')
        input()
        print('If you want to resign, press 0 key')
        input()
        while True:
            print('Working...')
            for i in range(5):
                print(5 - i);
                sleep(1)
            r = random.randint(100, 500)
            e = random.randint(10, 100)
            print('You earn :', r, '$')
            print('exp +', e)
            me.money += r
            me.my_exp(e)
            i=input('work more?(No: 0)');
            if i == '0':
                break


# Airport
class airport(place):
    name = 'AIRPORT'
    restrict = 10
    difficulty = 10
    level = 15
    exp = 50
    mood = 80
    land = ['Homeland', 'Twilight island', 'Science CITY', 'Cosmos World']

    def question(self):
        self.loc(airport_loc[me.world][0], airport_loc[me.world][1])
        print('-------------------------')
        print('     ☆☆☆AIRPORT☆☆☆     ')
        print('>>', self.land[me.world])
        print('-------------------------')
        super().question()
        if self.q == 1:
            for i in range(len(world)):
                if i >= len(self.land):
                    continue
                print('[', i + 1, '].', self.land[i])
            print('Cancle : 0')
            answer = int(input())
            if self.land[answer - 1] == 'Cosmos World':
                print('You must board SPACE SHIP in Science CITY');
                input()
                return None
            if answer == 0:
                return None
            cost = abs(answer - 1 - me.world) * 1000
            t = abs(answer - 1 - me.world) * 10
            print('This Line costs', cost, '$')
            print('Are you sure? (Yes:1  No:0)')
            sign = input()
            if sign == '1':
                if me.pay(cost):
                    time.hour_append(t)
                    me.world = answer - 1


# Gift Shop
class giftshop(place):
    def __init__(self):
        pass

    name = 'Charles` Gift Shop'
    level = 15
    mood = 300
    pay = 5
    difficulty = 10

    def question(self):
        super().question()
        if self.q == 1:
            print('[1]. shopping')
            print('[2]. stand without shopping')
            print('Cancle : 0')
            answer = int(input())
            if answer == 1:
                self.shopping(royal_list)
            elif answer == 2:
                if self in me.workspace:
                    print('you, waiting for, her somebody.')
                    i = random.randint(0, 10)
                    me.luck += i
                    print('you gain', i, 'lucks')
                    me.wait(self)
                else:
                    print('shopkeeper throw you out!')
            elif answer == 0:
                return None


# beach
class beach(place):
    def __init__(self):
        pass

    name = 'Twilight Beach'
    restrict = 20
    difficulty = 50
    exp = 300

    def question(self):
        super().question()
        if self.q != 1:
            return None
        n = random.randint(0, 15)
        print('sunlight....sea wave....horizon....')
        input()
        print('Maybe someone else come here..')
        input()
        print('you\'ve got', n, 'love')
        me.my_love(n)
        input()
        print('1: go back    2: look vacantly the horizon')
        answer = int(input())
        if answer == 1:
            me.go(me.world)
        elif answer == 2:
            k = random.randint(0, 10)
            if k >= 7:
                girl_list[random.randint(0, len(girl_list) - 1)].initiate()
            elif k >= 5:
                print('street cleaner : hey! go back! the wave will be larger!')
            else:
                print('weather is getting cold. better to go back')


# Lily's house
class lh(place):
    name = 'Lily\'s house'
    l_restrict = 500
    g_restrict = 1
    girl_index = 0

    def question(self):
        super().question()
        if self.q != 1:
            return None
        print('1 : go back   2 : knock')
        i = int(input())
        if i == 1:
            me.go(me.world)
        elif i == 2:
            self.owner()
            if self.owner not in me.girllist:
                self.owner.initiate()
            else:
                print('you have great time with', self.owner.name, '...♡')
                print(self.owner.name, 'walked you to the airport.')
                print('you earned 300 loves')
                me.my_love(300)
                me.location = airport
                place_list2.remove(self)

    def owner(self):
        self.owner = girl_list[self.girl_index]


class place1(lh):
    l_restrict = 1000
    name = 'Scallet\'s house'
    girl_index = 1


class place2(place):
    name = 'Observatory'
    level = 20

    def question(self):
        super().question()
        if self.q == 1:
            print('1: See the sky  2: Open the door')
            print('Cancel : 0')
            a = int(input())
            if a == 1:
                self.sky()
            elif a == 2:
                self.door()

    def sky(self):
        print('.....I want to see beautiful Stars.....')
        input()
        r = random.randint(0, 5)
        if r == 3:
            self.doctor()
        return None

    def door(self):
        print('I opened heavy glass door')
        print('And I started to climb stairs')
        input()
        print('During climbing, I found a strange door')
        print('1: Keep climbing the stairs ')
        print('2: Carefully knock the door')
        a = int(input())
        if a == 1:
            self.star()
            return None
        elif a == 2:
            self.doctor()
            return None

    def star(self):
        print('I succeed to see the stars')
        input()
        print('☆  ☆   ☆       ☆          ☆')
        print()
        print('  ☆   ☆        ☆       ☆       ☆')
        print()
        print('   ☆     ☆  ☆            ☆')
        print()
        print('☆     ☆        ☆')

    def doctor(self):
        print('A crazy man came to you')
        input()
        if me.level < 25:
            print('Oh..... I almost complete....')
            return None
        if me.doctor == 0:
            print('Hey buddy, I made something tremendous! See it')
            input()
            print('Its name is "Time Warper"')
            print('You wanna buy it? 50000$')
            print('1: Buy   2: No, thanks')
            a = int(input())
            if a == 1:
                timewarper.buy(1)
                me.doctor += 1
                print('You leaved observatory with awkward stuff in hand')
                input()
                return None
            else:
                print('You ran away from the mad guy')
                return None
        print('Hey! Look at the sky. I will reach the star someday')
        input()
        return None


class place3(place):
    level = 30
    name = 'Space E. laboratory'

    def question(self):
        super().question()
        if self.q != 1:
            return None
        print('you can only see the sights,')
        print('If you are not space researcher.')
        print()
        print('Press any key to continue')
        input()
        if timewarper in me.bag or me.label == '| SPACE RESERCHER |':
            self.warp()
            return None
        print('Here is where Space engineers work')
        print('Have a good time!')
        input()
        if me.doctor != 0:
            return None
        print('........we need teleport machine..')
        input()

    def warp(self):
        if timewarper in me.bag:
            self.chat()
        print('You can go to another space')
        print('Go?  1: Yes  2: Cancel')
        if input() == '1':
            me.world += 1
            me.location = c1

    def chat(self):
        print('Engineer: Hey! what is this on your hand!?');
        input()
        print('You: Aww.... TIMEWARPER?');
        input()
        print('Engineer: What!......you doctor?');
        input()
        print('You got the unique title : Space Researcher')
        me.label = '| SPACE RESERCHER |'
        input();
        print('You used TIMEWARPER')
        me.bag_index[timewarper.name] = 0
        me.bag.remove(timewarper)
        me.my_status()
        input()
        print('Engineer: We finally made WARP SHIP!')
        print('We can go another dimension cosmos by this ship!');
        input()


class cosmos1(place):
    name = 'Space Migration Zone'

    def question(self):
        if me.positive == 0:
            print('Where is it...?');
            input()
            print(' 1 : continue swimming')
            input()
            me.positive = 1
            me.location = c3
            return None
        print('Scientists developed warp portal')
        input()
        a = input('1 : go to portal  2 : Nah, just swimming')
        if a == '1':
            self.portal()
        elif a == '2':
            self.swim()
        else:
            return None

    def portal(self):
        me.world += 1
        me.location = port

    def swim(self):
        input('There is so many stars ...')
        self.star()
        me.location = c2;
        input()

    def star(self):
        for i in range(100):
            r = random.randint(0, 5)
            print('  ☆', ' ' * r, end='')


class cosmos2(place):
    name = 'Unknown'
    pass


class cosmos3(place):
    name = 'BLACK HOLE'

    def question(self):
        print('Dark... Too dark....')
        input()
        print('I\'m pulled by UNKOWN POWER...!')
        for i in range(6):
            sleep(0.5);
            print()
        print('1: escape   2: go to the hole')
        a = int(input())
        if a == 1:
            self.move()
        elif a == 2:
            self.hole()
        else:
            self.question()

    def move(self):
        print('You tried to escape, but');
        input()
        print('The BLACK HOLE is too huge..');
        input()
        print('You warped time, Finally went back to the past..')
        me.init()
        return None

    def hole(self):
        print('You entered the hole.');
        input()
        for i in range(10):
            print('*' * (10 - i))
            sleep(0.5)
        print('You finally exit the hole');
        input()
        print('What is this light? too bright!');
        input()
        print('○WHITE HOLE○')
        print('You can go EVERYWHERE')
        n = 1
        d = {}
        w = {}
        for i in range(len(world)):
            if i == len(world) - 1:
                continue
            for j in range(len(world[i])):
                d[n] = world[i][j]
                w[n] = i
                print(n, ':', world[i][j].name)
                n += 1
        a = int(input())
        me.location = d[a]
        me.world = w[a]


class port(place):
    name = 'Warp Portal'

    def question():
        if self.q == 1:
            answer = input('1: Warp  0: Cancel')
            if answer == 1:
                self.warp()
            else:
                return None

    pass


class e1(place):
    pass


class e2(place):
    pass


class e3(place):
    pass


# movies

class movie:
    name = ''
    exp = 0
    cost = 0
    love = 0
    time = 0
    luck = 0
    nut = 0
    lovenum = 0

    def lovescore(self):
        self.love = me.girlfriend * self.lovenum

    def watch(self):
        if me.pay(self.cost):
            me.my_exp(self.exp)
            time.minute_append(self.time)
            me.luck += self.luck
            me.my_love(self.love)
            me.my_health(self.nut)


# Romantic Movie
class romantic(movie):
    name = 'romantic'
    exp = 10
    cost = 30
    time = 120
    lovenum = 20

    def watch(self):
        self.luck = random.randint(0, 2)
        super().watch()


# Horror Movie
class horror(movie):
    name = 'horror'
    exp = 30
    cost = 25
    lovenum = 15
    time = 100
    nut = -10


# Comedy Movie
class comedy(movie):
    name = 'comedy'
    exp = 50
    cost = 30
    lovenum = 10
    time = 120
    nut = 10

    def watch(self):
        self.luck = random.randint(0, 5)
        super().watch()


# Action Movie
class action(movie):
    name = 'action'
    exp = 30
    cost = 15
    time = 150
    nut = 15
    luck = 1


# coffees
class coffee:
    name = ''
    cost = 0
    love = 0
    exp = 0
    luck = 0
    time = 0

    def drink(self):
        me.pay(self.cost)
        me.my_exp(self.exp)
        print('you gain', self.exp, 'exp')
        me.my_love(self.love)
        print('you gain', self.love, 'love')
        me.luck += self.luck
        print('you gain', self.luck, 'luck')
        time.minute_append(self.time)


# Americano
class americano(coffee):
    name = 'Americano'
    cost = 50
    love = me.girlfriend * 30
    exp = 10
    time = 30
    luck = 1


# Cafe Mocha
class cafemocha(coffee):
    name = 'Cafe mocha'
    cost = 60
    love = me.girlfriend * 40
    exp = 12
    time = 40
    luck = 3


# Cappuccino
class cappuccino(coffee):
    name = 'Cappuccino'
    cost = 70
    love = me.girlfriend * 40
    luck = 5
    time = 40


# Strawberry Latte
class strawberrylatte(coffee):
    name = '♡Strawberry Latte♡'
    cost = 300
    love = me.girlfriend * 200
    luck = 10


# stuff lists
apple = apple()
chocolate = chocolate()
medicine = medicine()
pear = pear()
magnifiner = magnifiner()
stuff_list = [apple, pear, chocolate, medicine, magnifiner]

revivestone = revivestone()
rose = rose()
timewarper = timewarper()
warper = warper()
p1 = p1()
p2 = p2()
p3 = p3()
note = note()
book = book()
royal_list = [revivestone, rose, p1, p2, p3, book, note]

# movie lists
movie = movie()
romantic = romantic()
horror = horror()
comedy = comedy()
action = action()

movie_list = [romantic, horror, comedy, action]

# coffee lists
coffee = coffee()
amer = americano()
caf = cafemocha()
cap = cappuccino()
straw = strawberrylatte()

coffee_list = [amer, caf, cap, straw]

# time set
time = time()
time.hour = 7
time.ap = 'A.M'

t = threading.Thread(target=time.second_append)

# places set
place = place()

market = market()
theater = theater()
cafe = cafe()
home = home()
company = company()
airport = airport()

place_list1 = [home, market, cafe, theater, company]

giftshop = giftshop()
beach = beach()
lh = lh()
place_list2 = [giftshop, lh, beach]

place1 = place1()
place2 = place2()
place3 = place3()
place_list3 = [place1, place2, place3]

c1 = cosmos1()
c2 = cosmos2()
c3 = cosmos3()
cosmos = [c1, c2, c3]

port = port()
e1 = e1()
e2 = e2()
e3 = e3()

another_earth = [port, e1, e2, e3]
world = [place_list1, place_list2, place_list3, cosmos, another_earth]

# places location
home.loc(0, 0)
market.loc(1, 1)
theater.loc(3, 4)
cafe.loc(2, 1)
company.loc(5, 5)
airport_loc = [[9, 12], [100, 100], [300, 300]]
airport.loc(airport_loc[me.world][0], airport_loc[me.world][1])
giftshop.loc(115, 110)
lh.loc(120, 130)
beach.loc(200, 220)
place1.loc(312, 315)
place2.loc(350, 340)
place3.loc(700, 500)
port.loc(211235, 212030)
e1.loc(211002, 183220)
e2.loc(211121, 183120)
e3.loc(210183, 192330)

# girl set
lily = girl('Lily')
scallet = girl('Scallet')
emily = girl('Emily')
ellen = girl('Ellen')
jessica = girl('Jessica')
girl_list = [lily, scallet, emily, ellen, jessica]

# me set
age = input('Your age :')
name = input('Your name :')
me = me(age, name)
me.money = 10000000
me.level = 39
me.location = home
me.health = 100
me.my_status()

t.start()

# game loop
while me.quitnumber:
    if me.init == 1:
        pass
    try:
        print()
        my_loc = me.location
        my_loc.question()
        time.midnight()
        print()
        print()
        print()
    except:
        print()
        print()
        print('error. try again')
        print()
        print()
        continue
