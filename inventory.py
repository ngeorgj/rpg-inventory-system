class Item:

    def __init__(self, name, description, amount, individual_value):
        self.name = name
        self.description = description
        self.amount = amount
        self.individual_value = individual_value

    @property
    def worth(self):
        return f'${self.amount * self.individual_value:.2f}'

    def sell(self):
        if self.amount >= 1:
            print('How many do you want to sell?')
            amt = int(input('amt > '))
            print(f'Are you sure you want to sell {self.amount} {self.name} for ${self.individual_value * amt:.2f}?')
            confirm = input('[y/n] > ')
            if confirm == 'y':
                self.amount -= amt
                print(f'{amt} {self.name} sold for ${amt * self.individual_value:.2f}!')

            else:
                pass

        pass

    def add_to_inventory(self, inventory):
        if len(inventory.items) < inventory.capacity:
            inventory.items.append(self)
            print(f'x{self.amount} {self.name} added to your Inventory')

        else:
            print('No room for more items...')


class Inventory:

    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def show(self):
        index = 1
        for item in self.items:
            print(str(f'{index} -> [x{item.amount}] {item.name}'))
            index += 1

    def drop_item(self):
        print('\nWhich item do you want to drop? ["0" to Quit]')
        self.show()
        i = int(input('\nNº > '))
        if i == 0:
            print('\nClosing the Inventory...')
            quit()

        item = self.items[i - 1]
        if item.amount == 1:
            amt = 1
            self.items.pop(i - 1)
            print(f'Item {item.name}[x{amt}] Dropped!\nNow your Inventory is this:')

        else:
            print(f'You have {item.amount} of this, how many do you want to drop?')
            amt = int(input('amt > '))
            if item.amount <= 0:
                amt = 0
                self.items.pop(item)
                print(f'Item {item.name}[x{amt}] Dropped!\nNow your Inventory is this:')
            item.amount -= amt
            print(f'Item {item.name}[x{amt}] Dropped!\nNow your Inventory is this:')

        self.show()
        self.drop_item()

    @property
    def total_worth(self):
        return f'\nThe inventory Total Worth is: ${sum([i.individual_value * i.amount for i in self.items]):.2f}'


# Declaring the Inventory
inventory = Inventory(6)

# Declaring some Items to Populate this Inventory
knife = Item('Knife', 'A normal sized and little rusted Knife.', 1, 25)
knife.add_to_inventory(inventory)

potion = Item('Health Potion', 'A small flask of what appears to be blood..', 12, 45)
potion.add_to_inventory(inventory)

sword = Item('Sword', 'A rusted Sword, you see some scripts on it.', 1, 548.90)
sword.add_to_inventory(inventory)

idol = Item('Cthullu Idol', 'You see a bizarre figure sitted in a little altar...', 1, 159804.60)
idol.add_to_inventory(inventory)

# Checking the Total Worth of the Inventory
print(inventory.total_worth)

# Calling the Function for dropping items.
inventory.drop_item()
