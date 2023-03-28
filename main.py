from mods.JSave.jsave import save_to_file, load_from_file
from random import uniform
from time import time
from clear import clear


def random_float(x: float, y: float, place_val=1):
    return round(uniform(x, y), place_val)


coin_list = {}


class Coin:
    def __init__(self, name: str):
        self.name = name.lower() + '_coin'
        self.display_name = name.capitalize() + ' Coin'
        coin_list[self.name] = self

    def __repr__(self):
        return self.name + '_object'


class Tycoon:
    def __init__(self, owner: str):
        self.owner = owner
        self.produces = {}
        self.coins = {}
        self.bux = 0
        for c in coin_list:
            self.produces[c] = 0
            self.coins[c] = 0
        self.upgrades = {}

    def buy_upgrade(self, name: str):
        name = name.lower().replace(' ', '_')
        try:
            upgrade = self.upgrades[name]
        except KeyError:
            print(f"{name} isn't a valid upgrade")
            return
        if upgrade['has']:
            print(f"{name} isn't a valid upgrade")
            return

        coin_amt = self.coins[upgrade['coin_cost'].name]

        if coin_amt >= upgrade['cost']:
            self.coins[upgrade['coin_cost'].name] = self.coins[upgrade['coin_cost'].name] - upgrade['cost']
            self.produces[upgrade['boost_coin'].name] = self.produces[upgrade['boost_coin'].name] + upgrade['boost']
            upgrade['has'] = True

    def list_upgrades(self):
        for u in self.upgrades:
            if tycoon.upgrades[u]['needs'] == () and self.upgrades[u]['has'] is not True:
                print(
                    f"({u}) {self.upgrades[u]['display_name']} costs {self.upgrades[u]['cost']} {self.upgrades[u]['coin_cost'].display_name}'s, makes {self.upgrades[u]['boost']} {self.upgrades[u]['boost_coin'].display_name}'s p/s")

            for nu in self.upgrades[u]['needs']:

                if self.upgrades[nu].get('has'):
                    print(
                        f"({u}) {self.upgrades[u]['display_name']} costs {self.upgrades[u]['cost']} {self.upgrades[u]['coin_cost'].display_name}'s, makes {self.upgrades[u]['boost']} {self.upgrades[u]['boost_coin'].display_name}'s p/s")

    def list_produced(self):
        print('Produced:')
        for index, c in enumerate(self.coins, 1):
            if index % 5 == 0:
                print(f"[{self.coins[c]} {coin_list[c].display_name}'s]", end='\n')
            else:
                print(f"[{self.coins[c]} {coin_list[c].display_name}'s]", end=' ')

        print(f"[{self.bux} Bux's]", end=' ')

        print('\n')

    def list_produces(self):
        print('Produces:')
        for p in self.produces:
            print(f"[{self.produces[p]} {coin_list[p].display_name}'s p/s]", end=' ')
        print('\n')


class Upgrade:
    def __init__(self, upgrades_tycoon: Tycoon, name: str, display_name: str, cost: float, coin_cost: Coin,
                 boost: float,
                 boost_coin: Coin, *needed_before_available):
        self.tycoon = upgrades_tycoon
        self.tycoon.upgrades[name] = {
            'display_name': display_name,
            'coin_cost': coin_cost,
            'cost': cost,
            'boost': boost,
            'boost_coin': boost_coin,
            'has': False,
            'needs': needed_before_available
        }


bronze_coin = Coin('Bronze')
silver_coin = Coin('Silver')
gold_coin = Coin('Gold')
diamond_coin = Coin('Diamond')

tycoon = Tycoon('player')

copper_1 = Upgrade(tycoon, 'copper_machine_1', 'Copper Machine 1', 0, bronze_coin, 1, bronze_coin)
copper_2 = Upgrade(tycoon, 'copper_machine_2', 'Copper Machine 2', 50, bronze_coin, 1, bronze_coin, 'copper_machine_1')

while __name__ == '__main__':

    def give_coins(time_1, time_2):
        for c in coin_list:
            tycoon.coins[c] = round(tycoon.coins[c] + tycoon.produces[c] * round(time_2 - time_1, 1), 1)

        def upgrades_menu():
            clear()

            tycoon.list_upgrades()

            print('\nType the name of an upgrade to buy it (some_upgrade_name)\n')

            upgrade_inp = input('>>> ')

            if upgrade_inp in list(tycoon.upgrades):
                tycoon.buy_upgrade(upgrade_inp)
                upgrades_menu()

            clear()

        tycoon_time1 = time()

        print(f"{tycoon.owner.capitalize()}'s Tycoon:")

        tycoon.list_produces()

        tycoon.list_produced()

        print('1. view available upgrades')

        tycoon_inp = input('>>> ')

        tycoon_time2 = time()
        give_coins(tycoon_time1, tycoon_time2)

        if tycoon_inp == '1':
            upgrades_menu()
        else:
            clear()
