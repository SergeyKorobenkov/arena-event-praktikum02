import random as r
from person import Thing
from person import Paladin
from person import Warrior

def throw_coin():
    return r.choice([True, False])

list_names = ['Liu Kang', 'Johnny Cage', 'Kano', 'Raiden', 'Scorpion', 'Sonya Blade', 'Sub-Zero', 'Goro',
     'Shang Tsung', 'Reptile', 'Baraka', 'Jax', 'Kitana', 'Kung Lao', 'Mileena', 'Kintaro', 'Shao Kahn', 'Jade',
      'Noob Saibot', 'Smoke', 'Cyrax', 'Sektor', 'Kabal', 'Nightwolf']

list_things = []

for i in range(50):
    list_things.append(Thing(f"Thing-{i}", round(r.random()/10, 2), r.randint(0, 5), r.randint(0, 10)))


def get_random_players(quantity):
    player_list = []
    for i in range(quantity):
        name = r.choice(list_names)
        list_names.remove(name)
        if throw_coin():
            player = Paladin(name, 50, 10, 0.05)
        else:
            player = Warrior(name, 50, 10, 0.05)
        count_things = r.randint(0,4)
        things = []
        for j in range(count_things):
            thing = r.choice(list_things)
            list_things.remove(thing)
            things.append(thing)
        player.set_things(things)
        player.show()
        player_list.append(player)
    return player_list
            

    


