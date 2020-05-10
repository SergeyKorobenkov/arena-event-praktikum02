class Person():
    '''
    A class used to represent different Person types.

    Attributes:
        name (str): persons name.
        base_hp (int): persons health.
        base_attack (int): persons attack.
        base_protection (int): persons protection from 0.001 to 0.25.
        equipments (list, optional): list of persons equipment.
        hp (int): persons health with equipments.
        attack (int): persons attack with equipments.
        protection (int): persons protection with equipments.
    '''

    def __init__(self, name, base_hp, base_attack, base_protection):
        '''
        The constructor for Person class.

        Parameters:
            name (str): persons name.
            base_hp (int): persons health.
            base_attack (int): persons attack.
            base_protection (int): persons protection from 0.001 to 0.25.
        '''

        self.name = name
        self.base_hp = base_hp
        self.base_attack = base_attack
        self.base_protection = base_protection
        self.hp = base_hp
        self.attack = base_attack
        self.protection = base_protection

    def set_equipments(self, equipments):
        '''
        The function add list of Equipment class objects to Person and
        update Persons hp, attack and protection.

        Parametrs:
            equipments (list): list of Equipment class objects.
        '''

        self.equipments = equipments

        for equipment in self.equipments:
            self.hp = self.base_hp + equipment.hp
            self.attack = self.base_attack + equipment.attack
            self.protection = self.base_protection + equipment.protection

    def make_attack(self, victim):
        '''
        The function passes Persons attack value to victims
        method reduction_hp().

        Parametrs:
            victim (Person): object of Person class or of it's childs classes.

        Returns:
            damage (int): finally inflicted damage.
        '''

        damage = victim.reduction_hp(self.attack)

        return damage

    def reduction_hp(self, incoming_attack):
        '''
        The function reduce Persons hp by a value equal to incoming_attack.

        Parametrs:
            incoming_attack (int): amount of incoming attack.

        Returns:
            damage (int): finally received damage.
        '''

        damage = incoming_attack * (1 - self.protection)
        self.hp -= damage

        return damage

    def is_dead(self):
        '''
        The function wich defines Persons death.

        Returns:
            (bool) True if dead, False if not.
        '''

        return self.hp <= 0

    def get_name(self):
        '''
        The function wich return Persons name.

        Returns:
            (srt) Persons name.
        '''

        return self.name


class Paladin(Person):
    '''
    A class used to represent Paladin types.

    Attributes:
        Same as Person class, only base_hp, hp and
        base_protection, protection double.
    '''

    def __init__(self, name, base_hp, base_attack, base_protection):
        '''
        The constructor for Paladin class.

        Parameters:
            Same as Person class, only base_hp, hp and
            base_protection, protection double.
        '''

        super().__init__(name, base_hp, base_attack, base_protection)
        self.base_hp *= 2
        self.hp *= 2
        self.set_protection()

    def set_protection(self):
        '''
        The function doubles base_protection and protectiom attributes and
        sets them to 0.5 if their amount bigger then 0.5.
        '''

        self.base_protection *= 2
        self.protection *= 2

        if self.base_protection > 0.5:
            self.base_protection = 0.5
            self.protection = 0.5


class Warrior(Person):
    '''
    A class used to represent Warrior types.

    Attributes:
        Same as Person class, only base_attack and attack double.
    '''

    def __init__(self, name, base_hp, base_attack, base_protection):
        '''
        The constructor for Warrior class.

        Parameters:
            Same as Person class, only base_attack and attack double.
        '''

        super().__init__(name, base_hp, base_attack, base_protection)
        self.base_attack *= 2
        self.attack *= 2
