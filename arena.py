import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#отдельно выделены основные настройки игры
from ref import *

#Класс доспехов
class Thing:
    def __init__(self, title, health, attack, protection):
        self.title = title
        self.protection = min(protection, .1)
        self.attack = attack
        self.health = health

    def show_thing(self):
        print('   >' + self.title, '(HP:' + str(self.health), 'At:' + str(self.attack), 'Pt:' + str(self.protection) + ')')

    #Для вывода в html
    def thing_html(self):
        return ('<li>' + self.title + ' (HP:' + str(self.health) + ', At:' + str(self.attack) + ', Pt:' + str(self.protection) + ')</li>')

#Класс Герой
class Person:
    def __init__(self, name, hit_points, base_attack, base_protection):
        self.name = name
        self.hit_points = hit_points
        self.base_attack = base_attack
        self.base_protection = base_protection
        self.things = []

    #Надевание доспехов (Доп атака и защита от доспехов учитываются в методе takeDamage)
    def setThings(self, things):
        self.things += things
        self.hit_points += sum(c.health for c in self.things)

    #Понести урон, вычетает hp, возвращает урон
    def takeDamage(self, attack_damage):
        thingsProtection = min(sum(c.protection for c in self.things), 0.4)
        finalProtection = self.base_protection + thingsProtection
        caused_damage = int(attack_damage - attack_damage*finalProtection)
        self.hit_points -= caused_damage
        return caused_damage

    def show_params(self):
        print(self.name, '(HP:' + str(self.hit_points), 'At:' + str(self.base_attack), 'Pt:' + str(self.base_protection) + ')')
        for i in self.things:
            i.show_thing()
        print()

    #Для вывода в html
    def person_html(self):
        txt = '<p>'
        txt += (self.name + ' (HP:' + str(self.hit_points) + ', At:' + str(self.base_attack) + ', Pt:' + str(self.base_protection) + ')')
        txt += '<ul>'
        for i in self.things:
            txt += i.thing_html()
        txt += '</ul></p>'
        return txt

#Класс Palladin
class Palladin(Person):
    def __init__(self, name, hit_points, base_attack, base_protection):
        super().__init__(name, hit_points, base_attack, base_protection)
        self.hit_points = hit_points * 2
        self.base_protection = base_protection * 2

#Класс Warrior
class Warrior(Person):
    def __init__(self, name, hit_points, base_attack, base_protection):
        super().__init__(name, hit_points, base_attack, base_protection)
        self.base_attack = base_attack * 2


#Генерируем N доспехов
def generate_n_things(n):
    n = min(n, 30)
    things = []
    for i in range(n):
        things.append(create_thing())
    return sorted(things, key = lambda x: x.protection)


#Генерируем доспех с рандомными параметрами
def create_thing():
    ttl_ix = random.randint(0, len(things_list) - 1)
    ttl = things_list[ttl_ix]
    h = random.randint(0, T_HP_MAX)
    a = random.randint(0, T_ATTACK_MAX)
    p = random.randint(0, T_PROTECTION_MAX * 1000)/1000
    del things_list[ttl_ix]
    return Thing(ttl, h, a, p)

#Генерируем N героев (палладинов и воинов)
def create_heroes(n=NUM_OF_HEROES):
    pd_num = random.randint(0, n)
    wr_num = n - pd_num

    units = []
    for i in range(n):
        n = random.randint(0, len(heroes) - 1)
        h = random.randint(HP_MIN, HP_MAX)
        a = random.randint(ATTACK_MIN, ATTACK_MAX)
        p = random.randint(0, PROTECTION_MAX * 1000) / 1000

        if i < pd_num:
            units.append(Palladin('pd ' + heroes[n], h, a, p))
        else:
            units.append(Warrior('wr ' + heroes[n], h, a, p))

        del heroes[n]
    return units


#Распределяем доспехи героям
def things_allocation(units, things):
    for unit in units:
        num_of_things = random.randint(NUM_OF_THINGS_PER_HERO_MIN, NUM_OF_THINGS_PER_HERO_MAX)
        unit_things = []
        for i in range(num_of_things):
            j = random.randint(0, len(things) - 1)
            unit_things.append(things[j])
            del things[j]
        unit.setThings(unit_things)
    return units


things_set = generate_n_things(50)
heroes_set = create_heroes()
units_with_things = things_allocation(heroes_set, things_set)

#Список героев с доспехами для вывода
all_heroes_list_html = ''
for unit in heroes_set:
    all_heroes_list_html += unit.person_html()


k = 0
A = pd.DataFrame()
heroes_html = ''

#Битва
while len(units_with_things) > 1:
    a_ix = random.randint(0, len(units_with_things) - 1)
    d_ix = random.randint(0, len(units_with_things) - 1)
    if d_ix == a_ix:
        d_ix = (d_ix + 1) % len(units_with_things)
    attacking = units_with_things[a_ix]
    defending = units_with_things[d_ix]

    things_attack_damage = sum(c.attack for c in attacking.things)
    base_attack_damage = attacking.base_attack

    attack_damage = things_attack_damage + base_attack_damage
    caused_damage = defending.takeDamage(attack_damage)
    resp_caused_damage = 0
    if defending.hit_points <= 0:
        print('>', units_with_things[d_ix].name, 'is out')
        #Если включен режим "забрать трофейные доспехи"
        if take_trophy:
            attacking.things += defending.things
        del units_with_things[d_ix]
    else:
        #Если включен режим контратаки
        if contrattack:
            resp_attack_damage = (sum(c.attack for c in defending.things) + defending.base_attack) * CONTR_KOEF
            resp_caused_damage = attacking.takeDamage(resp_attack_damage)
            if attacking.hit_points <= 0:
                print('>', units_with_things[a_ix].name, 'is out')
                if take_trophy:
                    attacking.things += defending.things
                del units_with_things[a_ix]
            A = A.append(pd.Series({'att': defending.name, 'def': attacking.name, 'damage': resp_caused_damage}), ignore_index=True)

    #Выводы в консоль и html файл
    print(attacking.name, '->', defending.name, attack_damage, 'rest:', defending.hit_points)
    heroes_html += ('<tr><td>'+str(k)+'</td><td>' + attacking.name + '</td><td>' + defending.name + '</td><td>' + str(caused_damage) + '</td><td>'+str(resp_caused_damage)+'</td><td>'+str(defending.hit_points)+'</td></tr>')
    if defending.hit_points <= 0:
        heroes_html += '<tr><td colspan = "6">'+defending.name+' is dead, ' + str(len(defending.things)) + ' things go to ' + attacking.name + '</td><tr>'
    if attacking.hit_points <= 0:
        heroes_html += '<tr><td colspan = "6">'+attacking.name+' is dead by contratack, ' + str(len(attacking.things)) + ' things go to ' + defending.name + '</td><tr>'

    A = A.append(pd.Series({'att': attacking.name, 'def': defending.name, 'damage': caused_damage}),ignore_index=True)
    k += 1



#Делаем матрицу урона
A['att'] = A['att'].str[3:8]
A['def'] = A['def'].str[3:8]
B = A.groupby(['att', 'def'])['damage'].sum().reset_index()
B['damage'] = B['damage'].astype(int)
B = B.pivot('att', 'def', 'damage')
B = B.fillna(0)

#Отрисовываем матрицу и сохраняем в png файл
f, ax = plt.subplots(figsize=(8, 8))
sns_plot = sns.heatmap(B, annot=True, cbar=False, linewidths=.5, fmt='g', ax=ax)
figure = sns_plot.get_figure()
figure.savefig('out.png', dpi=600)

#Вывод хода боя в html файл
out_html = "<html><body><h1>Winner: " + units_with_things[0].name + " HP: " + str(units_with_things[0].hit_points) + "</h1><p>Герои с аммуницией:<br>"+all_heroes_list_html+"</p><p>Битва:<br><table><tr><th>Round</th><th>Attacking</th><th>Defending</th><th>Damage</th><th>Contra Damage</th><th>Def HP</th></tr>"+heroes_html+"</table></p>Кто кому нанес сколько урона:<br><img src='out.png' width='600' height='600'><body></html>"
f = open("result.html", "w")
f.write(out_html)
f.close()