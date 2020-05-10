from random import randint, choice

list_of_players = []
list_of_names = []
list_of_things = []


class Thing:
    '''
    Позитивные скилы в сумме до 300 - это абслютные величины
    Негативные скиллы до 30 - это размер, на которыйпри атаке уменьшается скилл противника
    '''
    def __init__(self, name, protect, attack, life, n_protect, n_attack):  
        self.name = name  
        self.protect = protect
        self.attack = attack 
        self.life = life          
        self.n_protect = n_protect
        self.n_attack = n_attack        
    def show(self):
        print(f'{self.name} {self.protect} {self.attack} {self.life} {self.n_protect} {self.n_attack}')
        
        
class Person:
    def __init__(self, name):
        self.name = name
        self.protect = 100
        self.attack = 100
        self.life = 200
        self.n_protect = 0
        self.n_attack = 0 
        self.values = []
        self.update_p = []
        list_of_players.append(name)
        
    
    def show(self):
        print(f'{self.name} {self.protect} {self.attack} {self.life} {self.n_protect} {self.n_attack}')
        
    def show_values(self):
        for elem in self.values:
            print(f'{elem}', end=' ')
        
    def setThings(self, things):
        self.update_p = [self.protect, self.attack, self.life, 0, 0]
        for elem in things:            
            self.protect = min(self.protect + elem.protect, 300)
            self.attack = min(self.attack + elem.attack, 300)
            self.life = min(self.life + elem.life, 300)
            self.n_protect = min(self.n_protect + elem.n_protect, 30)
            self.n_attack = min(self.n_attack + elem.n_attack, 30)
            self.values.append(elem.name)
            self.update_p = [self.protect, self.attack, self.life, self.n_protect, self.n_attack]
    
    def battle(self, rival):                    
        self.protect -= rival.n_protect
        if self.protect < 0:
            self.protect = 0
        self.attack -= rival.n_attack
        if self.attack < 0:
            self.attack = 0               
        self.life -= int(rival.attack*(1 - 0.002*self.protect))
        #чем больше атака нападающего, тем больше урон жизни защищающегося
        #чем больше защита защищаюшегося, тем меньше урон жизни защищающегося       
        
        if self.life < 0:
            self.life = 0



class Paladin(Person):
    def __init__(self, name):
        super().__init__(name)
        self.protect = 200
        self.attack = 100
        self.life = 250
        self.n_protect = 0
        self.n_attack = 0
        self.values = []
        
        
class Warrior(Person):
    def __init__(self, name):
        super().__init__(name)
        self.protect = 100
        self.attack = 200
        self.life = 150
        self.n_protect = 0
        self.n_attack = 0
        self.values = []
    



def fight_top(p1, p2):
    print('участники боя:')
    print('имя', '\t\t', p1.name, '\t\t', p2.name)
    print('класс', '\t\t', p1.__class__.__name__, '\t\t', p2.__class__.__name__)
    print('защита', '\t\t', p1.protect, '\t\t\t', p2.protect)
    print('атака', '\t\t', p1.attack, '\t\t\t', p2.attack)
    print('жизнь', '\t\t', p1.life, '\t\t\t', p2.life)
    #print('артефакты не толькр увеличивают уровень защиты, атаки и жизни, но и уменьшают скиллы противника')
    if p1.values == []:
        print(p1.name, 'не использует артефакты')
    else:
        print(p1.name, 'в бою использует:', *p1.values)
    if p2.values == []:
        print(p2.name, 'не использует артефакты')
    else:
        print(p2.name, 'в бою использует:', *p2.values)
    print('при атаке участники наносят ущерб скиллам противника:')
    print('ушерб атаке', '\t', p1.n_attack, '\t\t\t', p2.n_attack)
    print('ушерб защите', '\t', p1.n_protect, '\t\t\t', p2.n_protect)
    print('-----------------------------------------------------------------------')
    print('Сражение началось!')
    print('-----------------------------------------------------------------------')
    print('\t\t', p1.name, '\t\t', p2.name)
    

    
def fight(p1, p2, i):
    
    
    
    p1.battle(p2)
    
    print('Раунд', i, 'результат атаки', p2.name)    
    print('защита', '\t\t', p1.protect, '\t\t\t', p2.protect)
    print('атака', '\t\t', p1.attack, '\t\t\t', p2.attack)
    print('жизнь', '\t\t', p1.life, '\t\t\t', p2.life)    
    print('-----------------------------------------------------------------------')
    if p1.life <= 0:        
        print(f'Победил {p2.name}. Из соревнований выбыл {p1.name}')
        print('-----------------------------------------------------------------------')
        list_of_players.remove(p1)
        player_update(p2)
        return False
    elif p2.life <= 0:        
        print(f'Победил {p1.name}. Из соревнований выбыл {p2.name}')
        print('-----------------------------------------------------------------------')
        list_of_players.remove(p2)
        player_update(p1)
        return False
    
    p2.battle(p1)
    print('Раунд', i, 'результат атаки', p1.name)    
    print('защита', '\t\t', int(p1.protect), '\t\t\t', p2.protect)
    print('атака', '\t\t', p1.attack, '\t\t\t', p2.attack)
    print('жизнь', '\t\t', p1.life, '\t\t\t', p2.life)    
    print('-----------------------------------------------------------------------')
    
    if p1.life <= 0:        
        print(f'Победил {p2.name}. Из соревнований выбыл {p1.name}')
        print('-----------------------------------------------------------------------')
        list_of_players.remove(p1)
        player_update(p2)        
        return False
    elif p2.life <= 0:        
        print(f'Победил {p1.name}. Из соревнований выбыл {p2.name}')
        print('-----------------------------------------------------------------------')
        list_of_players.remove(p2)
        player_update(p1)
        return False
    
    return True
    
def player_update(player):
    player.protect = player.update_p[0]
    player.attack = player.update_p[1]
    player.life = player.update_p[2]
    player.n_protect = player.update_p[3]
    player.n_attack = player.update_p[4]
    print(player.name, 'отдохнул, залечил свои раны. Герой снова как новый и готов к сражениям.')
    

def player_formation(list_of_names):
    res = []
    
    for name in list_of_names:
        cub = randint(0, 1) #специализация
        if cub > 0:
            pers = Paladin(name)
                       
        else:
            pers = Warrior(name)
            
        
        res.append(pers)
    
    return res
            
def rand_list_t(list_of_things):
    len_l = len(list_of_things)-1
    set_t = set()
    cub1 = randint(0, 4)    
    while len(set_t) < cub1:
        cub2 = randint(0, len_l)        
        set_t.add(list_of_things[cub2])
    return set_t    


    

#--------------------------------------------------------------------------------
#-- список артефактов: название, + к защите, + к атаке, + к жизни, урон защите противника, урон атаке противника

t0 = Thing('кольчуга', 50, -10, 25, 0, 0)
t1 = Thing('меч-кладенец', 0, 50 , 0, 0, 0)
t2 = Thing('кислота', 0, 0, 0, 15, 15)
t3 = Thing('зелье', -10, -10 , 75, 0, 0)
t4 = Thing('собака', 50, 25 , 0, 5, 5)
t5 = Thing('каска', 15, 0, 0, 0, 0)
t6 = Thing('VR-очки', -10, 50 , 0, 0, 0)
t7 = Thing('перечный-балончик ', 0, -5, -5, 15, 15)
t8 = Thing('плащ-невидимка', 50, 25, 0, 0, 0)
t9 = Thing('заклинания', 0, 0, 0, 10, 10)
t10 = Thing('рогатка', 0, 30, 0, 5, 0)
t11 = Thing('граната', 0, 100, 0, 10, 10)
t12 = Thing('спирт', -25, 30, -10, 0, 0)
t13 = Thing('кольцо', 100 , 100, 100, 25, 25)
t14 = Thing('бутерброд', 20, 0, 20, 0, 0)

list_of_things = [t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14]
#--------------------------------------------------------------------------------
#--список имен игроков
list_of_names = ['Деннис Ритчиб',
                 'Рич Столлман',
                 'Лин Торвальдс',
                 'Стив Джобс',
                 'Стив Возняк',
                 'Билл Гейтс',
                 'Марк Цукерберг',
                 'Павел Дуров',
                 'Алан Тьюринг',
                 'Конрад Цузе',
                 'Дуг Энгельбарт',
                 'Ральф Баер']


list_of_players = player_formation(list_of_names) #формирование игроков

for elem in list_of_players:                      #раздача артефактов
    elem.setThings(rand_list_t(list_of_things))




print('========================================================================================')
print('\t\t\tСПИСОК УЧАСТНИКОВ')   
print('========================================================================================')
print('     имя\t\tспециальность\t\tартефакты')   
for elem in list_of_players:    
    print(elem.name, '\t\t-', elem.__class__.__name__, '\t', *elem.values)  

    
while len(list_of_players) > 1:
    
    player1 = choice(list_of_players)
    list_of_players.remove(player1)
    player2 = choice(list_of_players)
    list_of_players.append(player1)

    print('========================================================================================')
    print('\t\t\tСРАЖЕНИЕ')   
    print('========================================================================================')

    fight_top(player1, player2)
    i = 1
    f = True
    while f:
        f = fight(player1, player2, i)
        i += 1
    
    if len(list_of_players) > 1:
        print('-----------------------------------------------------------------------')
        print('их осталось', len(list_of_players), 'и это следующие герои:')
        for elem in list_of_players:
            print(elem.name, end=', ')
        print()
    else:
        print('========================================================================================')
        print('\t\t\tТУРНИР ЗАВЕРШЕН')  
        print('========================================================================================')
        print('победу одержал', list_of_players[0].name)
        print()
        

