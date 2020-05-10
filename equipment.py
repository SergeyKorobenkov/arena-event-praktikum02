class Equipment():
    '''
    A class used to represent different Equipment types.

    Attributes:
        name (str): equipment name.
        protection (int): equipment protection.
        attack (int): equipment attack.
        hp (int): equipment hp.
    '''

    def __init__(self, name, protection, attack, hp):
        '''
        The constructor for Equipment class.

        Parameters:
            name (str): equipment name.
            protection (int): equipment protection.
            attack (int): equipment attack.
            hp (int): equipment hp.
        '''
        self.name = name
        self.protection = protection
        self.attack = attack
        self.hp = hp
