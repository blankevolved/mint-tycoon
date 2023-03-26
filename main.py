from mods.JSave.jsave import save_to_file, load_from_file
from random import uniform
from time import time
from clear import clear
def random_float(x:float, y:float, place_val=1):
    return round(uniform(x, y), place_val)            


class Market():
    def __init__(self):
        self.coins_val = {}
        for c in coin_list:
            self.coins_val[c] = coin_list.get(c).start_val

    def refresh_vals(self):
        for c in coin_list:
            self.coins_val[c] = random_float(coin_list.get(c).min_val, coin_list.get(c).max_val)
    def get_vals(self):
        for c in coin_list:
            coin = coin_list.get(c)
            print(f'{coin.display_name}: {self.coins_val.get(c)}')

coin_list = {}

class Coin():
    def __init__(self, name:str, min_val:float, max_val:float, start_val:float):
        self.name = name.lower() + '_coin'
        self.display_name = name.capitalize() + ' Coin'
        self.min_val = min_val
        self.max_val = max_val
        self.start_val = start_val
        coin_list[self.name] = self
    def __repr__(self):
        return self.name + '_object'


class Tycoon():
    def __init__(self, owner:str):
        self.owner = owner
        self.produces = {}
        self.coins = {}
        self.bux = 0
        for c in coin_list:
            self.produces[c] = 0
            self.coins[c] = 0
        self.upgrades = {}
    def create_upgrade(self, name:str, display_name:str, cost:float, coin_cost:Coin, boost:float, boost_coin:Coin):
        self.upgrades[name] = {
            'display_name':display_name,
            'coin_cost':coin_cost,
            'cost':cost,
            'boost':boost,
            'boost_coin':boost_coin,
        }
    def buy_upgrade(self, name:str):
        name = name.lower().replace(' ', '_')
        try:
            upgrade = self.upgrades[name]
        except:
            print(f"{name} isn't a valid upgrade")
            return
        coin_amt = self.coins[upgrade['coin_cost'].name]
        if coin_amt == upgrade['cost']:
            self.coins[upgrade['coin_cost'].name] = self.coins[upgrade['coin_cost'].name] - upgrade['cost']
            self.produces[upgrade['boost_coin'].name] = self.produces[upgrade['boost_coin'].name] + upgrade['boost']
            self.upgrades.pop(name)

bronze_coin = Coin('Bronze', .1, 1, .5)
silver_coin = Coin('Silver', 3, 10, 3.75)

tycoon = Tycoon('player')


market = Market()


tycoon.create_upgrade('copper_machine_1', 'Copper Machine 1', 0, bronze_coin, 1, bronze_coin)


while __name__ == '__main__':
    time1 = time()
    def tycoon_menu():
        time1 = time()
        print(f"{tycoon.owner}'s Tycoon:")
        print('\nProduces:')
        for p in tycoon.produces:
            print(f"{tycoon.produces[p]} {coin_list[p].display_name}'s p/s")
        print('\nProduced:')
        for c in tycoon.coins:
            print(f"{tycoon.coins[c]} {coin_list[c].display_name}'s")
        print('\n1. view available upgrades')
        inp = input('>>> ')
        if inp == '1':
            clear()
            for u in tycoon.upgrades:
                print(f"({u}) {tycoon.upgrades[u]['display_name']} costs {tycoon.upgrades[u]['cost']} {tycoon.upgrades[u]['coin_cost'].display_name}'s, makes {tycoon.upgrades[u]['boost']} {tycoon.upgrades[u]['boost_coin'].display_name}'s p/s")
            print('\nuse "buy", to buy a upgrade (buy some_upgrade_name)\n')
            inp = input('>>> ')
            for u in list(tycoon.upgrades):
                if 'buy' in inp and u in inp:
                    tycoon.buy_upgrade(u)
            clear()
        else:
            clear()
        time2 = time()
        for c in coin_list:
            tycoon.coins[c] = round(tycoon.coins[c] + tycoon.produces[c] * round(time2 - time1, 1), 1)

    def market_menu():
        time1 = time()
        print('Market Values: ')
        market.get_vals()
        inp = input('>>> ')
        if inp == '1':
            clear()
            print(1)
        else:
            clear()
        time2 = time()
        for c in coin_list:
            tycoon.coins[c] = round(tycoon.coins[c] + tycoon.produces[c] * round(time2 - time1, 1), 1)

    print("""Pick a Menu:
1. Tycoon
2. Market""")
    inp = input('>>> ')
    if inp == '1':
        clear()
        tycoon_menu()
    elif inp == '2':
        clear()
        market_menu()
    else:
        clear()

    time2 = time()

    print(tycoon.coins)
    for c in coin_list:
        tycoon.coins[c] = round(tycoon.coins[c] + tycoon.produces[c] * round(time2 - time1, 1), 1)