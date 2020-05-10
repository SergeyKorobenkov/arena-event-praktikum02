from functools import reduce
import random
import datetime as dt


class Entity:
    def __init__(self, name, hitpoints=5, protection=0.05, damage=5, label=''):
        self.name = name
        self.label = label
        self.hitpoints = hitpoints
        self.protection = protection
        self.damage = damage

    # округление вывода

    def _getNumberString(self, number, forced_plus=False):
        sign = '+' if forced_plus and number > 0 else ''
        return f'{sign}{number:.2f}'.rstrip('0').rstrip('.')

    def getInfoString(self, isOwner=False):
        if isOwner:
            hitpoints = f'жизнь - {self._getNumberString(self.hitpoints)}'
            protection = f'защита - {self._getNumberString(self.protection*100)}%'
            damage = f'урон - {self._getNumberString(self.damage)}'
        else:
            hitpoints = f'{self._getNumberString(self.hitpoints, not isOwner)} к жизни'
            protection = f'{self._getNumberString(self.protection*100, not isOwner)}% к защите'
            damage = f'{self._getNumberString(self.damage, not isOwner)} к урону'

        return f'{self.getFullName()}: {hitpoints}, {protection}, {damage}'

    def getFullName(self):
        return f'{self.label} {self.name}' if self.label else self.name


class Person (Entity):
    def __init__(self, name, things_array=[], hitpoints=30, protection=0.2, damage=20, label='Персонаж'):
        super().__init__(name, hitpoints, protection, damage, label)
        self.total = Entity('Итого', hitpoints, protection, damage)
        self.current_hitpoints = self.total.hitpoints
        self._normalizeTotalProtection()
        self.setThings(things_array)

    def _normalizeTotalProtection(self):
        self.total.protection = min(self.total.protection, 1)

    # сила удара зависит от здоровья
    def attack(self):
        return max(self.total.damage*self.current_hitpoints/self.total.hitpoints, 0)

    def setThings(self, things_array):
        # в общем случае вещи могут не единичными
        # сохраним их в словаре
        self.things = {}

        if not things_array:
            return

        def updateThing(obj, elem):
            obj[elem] = obj[elem] + 1 if elem in obj else 1
            return obj

        self.things = reduce(updateThing, things_array, {})

        total_hitpoints = self.hitpoints + \
            sum([i.hitpoints for i in things_array])
        total_damage = self.damage + sum([i.damage for i in things_array])
        total_protection = self.protection + \
            sum([i.protection for i in things_array])
        self.total = Entity('Итого', total_hitpoints,
                            total_protection, total_damage)
        self.current_hitpoints = self.total.hitpoints
        self._normalizeTotalProtection()

    def defend(self, agressor: 'Person'):
        attack = agressor.attack()
        loss = attack*(1 - self.total.protection)
        current_hitpoints = self._getNumberString(self.current_hitpoints)
        self.current_hitpoints -= loss

        attack = self._getNumberString(attack)
        base_attack = self._getNumberString(agressor.total.damage)
        loss = self._getNumberString(loss)

        total_hitpoints = self._getNumberString(self.total.hitpoints)

        return f'{agressor.getFullName()} наносит удар силой {attack} (из {base_attack})' + \
            f' по {self.getFullName()} (жизнь: {current_hitpoints} из ' + \
            f'{total_hitpoints}) и наносит урон {loss}\n'

    def isAlive(self):
        return self.current_hitpoints > 0

    def getInfoString(self):
        result = super().getInfoString(True)
        if not self.things:
            return result
        result += '\nВ его арсенале'
        result += ': ' if len(self.things) > 1 else ' '

        def getThingString(elem):
            result = str(elem.name)
            if self.things[elem] > 1:
                result += f' ({self.things[elem]} шт.)'
            return result

        result += ', '.join(list(map(getThingString, self.things))) + '\n'
        result += self.total.getInfoString(True)
        return result


class Paladin(Person):
    def __init__(self, name, things_array=[], hitpoints=30, protection=0.2, damage=20):
        super().__init__(name, things_array, hitpoints, protection, damage, 'Паладин', )

    def setThings(self, things):
        super().setThings(things)
        self.total.hitpoints *= 2
        self.current_hitpoints = self.total.hitpoints
        self.total.protection *= 2
        self._normalizeTotalProtection


class Warrior(Person):
    def __init__(self, name, things_array=[], hitpoints=30, protection=0.2, damage=20):
        super().__init__(name, things_array, hitpoints, protection, damage, 'Воин', )

    def setThings(self, things):
        super().setThings(things)
        self.total.damage *= 2


class Duel():
    def __init__(self, entrants):
        self.entrants = entrants
        self.log = ''

    def run(self):
        if len(self.entrants) != 2:
            return 'Участников должно быть двое\n'

        entrant_one, entrant_two = self.entrants
        name_one = entrant_one.getFullName()
        name_two = entrant_two.getFullName()
        self.log = f'БОЙ {name_one.upper()} VS {name_two.upper()}\n'
        while entrant_one.isAlive() and entrant_two.isAlive():
            if random.getrandbits(1):
                self.log += entrant_one.defend(entrant_two)
            else:
                self.log += entrant_two.defend(entrant_one)

        self.log += 'БОЙ ОКОНЧЕН! ПОБЕДИТЕЛЬ: '
        if entrant_one.isAlive():
            self.log += f'{name_one.upper()}\n\n'
            return 1
        else:
            self.log += f'{name_two.upper()}\n\n'
            return 0


class Tourney():
    def __init__(self, participants=[]):
        self.participants = participants

    def setParticipants(self, participants):
        self.__init__(participants)

    def getThingsUsed(self):
        all_things = []
        for participant in self.participants:
            if participant.things:
                all_things.extend(participant.things)
        things_set = list(set(all_things))

        def sortByProtection(elem):
            return elem.protection

        things_set.sort(key=sortByProtection)

        return '\n'.join(list(map(lambda x: x.getInfoString(), things_set)))

    def run(self):
        if not self.participants:
            return 'Нет участников'

        result = f'Турнир от {dt.datetime.now().strftime("%d.%m.%Y %H:%M:%S")}\n\n'
        things_used = self.getThingsUsed()
        if (things_used):
            result += 'ИСПОЛЬЗУЕМЫЕ ВЕЩИ:\n' + things_used + '\n\nСПИСОК УЧАСТНИКОВ:\n'
        result += '\n'.join(list(map(lambda x: x.getInfoString(),
                                     self.participants))) + '\n\n'

        while len(self.participants) > 1:
            length = len(self.participants)
            indexes = random.sample(range(0, length), 2)
            while (indexes[0] == indexes[1]):
                indexes[1] = random.randint(0, length-1)
            duel = Duel([self.participants[indexes[0]],
                         self.participants[indexes[1]]])
            del self.participants[indexes[duel.run()]]
            result += duel.log

        winner = self.participants[0]
        result += f'ТУРНИР ОКОНЧЕН! ПОБЕДИТЕЛЬ: {winner.label.upper()} {winner.name.upper()}'
        return result


class Randomizer():
    def __init__(self, values=[]):
        self.values = values

    def setValues(self, values):
        self.values = values

    def get(self):
        return random.choice(self.values) if self.values else None


class EntitiesGenerator():
    def __init__(self, names, hitpoints_contstraints=(-5, 15), protection_contstraints=(-0.05, 0.15), damage_constraints=(-5, 15)):
        self.names = names
        self.contstraints = (hitpoints_contstraints,
                             protection_contstraints, damage_constraints)

    def generate(self, count=1):
        result = []
        used_names = set()
        for i in range(0, count):
            [hitpoints, protection, damage] = [random.uniform(
                self.contstraints[j][0], self.contstraints[j][1]) for j in range(0, 3)]

            name = self.names[random.randint(0, len(self.names)-1)]

            cast_name = name
            name_count = 1
            while cast_name in used_names:
                name_count += 1
                cast_name = f'{name}-{name_count}'
            used_names.add(cast_name)
            result.append(Entity(cast_name, hitpoints,
                                 protection, damage))
        return result


class ParticipantsGenerator(EntitiesGenerator):
    def __init__(self, names, things, max_things_count=4, hitpoints_contstraints=(30, 100), protection_contstraints=(0.1, 0.4), damage_constraints=(10, 30)):
        super().__init__(names, hitpoints_contstraints,
                         protection_contstraints, damage_constraints)
        self.things = things
        self.max_things_count = max_things_count

    def generate(self, count=1):
        result = []
        for i in range(0, count):
            new_things = []
            person = super().generate()[0]
            things_count = random.randint(0, self.max_things_count) + 1
            for j in range(0, things_count):
                rindex = random.randint(0, len(self.things)-1)
                new_things.append(self.things[rindex])

            if random.getrandbits(1):
                result.append(Warrior(person.name, new_things, person.hitpoints,
                                      person.protection, person.damage))
            else:
                result.append(Paladin(person.name, new_things, person.hitpoints,
                                      person.protection, person.damage))
        return result


if __name__ == '__main__':
    names = [[['Пафнутий', 'Владлен', 'Поликарп', 'Иннокентий', 'Зигмунд'],
              ['Забалуев', 'Крепкосмехов', 'Красноштанов', 'Ящиков', 'Попытайло']],
             [['Фрося', 'Глаша', 'Дуня', 'Василина', 'Травертина'],
              ['Новохудоносорова', 'Кафинькина', 'Киндзмараулова', 'Коробейникова', 'Сталелитейникова']]]

    things = ['меч', 'ружье', 'броня', 'копье',
              'транспортир', 'дротики', 'пиджак Баскова']

    def generateNames():
        generated_names = []
        for block in names:
            for first_name in block[0]:
                for surname in block[1]:
                    generated_names.append(f'{first_name} {surname}')
        return generated_names

    things_generator = EntitiesGenerator(things)
    generated_things = things_generator.generate(10)

    participants_generator = ParticipantsGenerator(
        generateNames(), generated_things)
    tour = Tourney(participants_generator.generate(10))
    print(tour.run())
