# RPG : Inventory System

When I was learning Python, I tried to do it by some different ways, the best way I found was trough making a <b>Text-RPG</b>, it was very funny and I've learned a lot!

The most difficult part was the inventory, Jesus it was Hard! Now I'm a little more experienced than I was and I'm leaving this for the newcomers, hope it helps!

Now let's go to the explanation!

# The Classes

I've created two classes for this one, `Inventory` and `Item` (because you need to have something to put in your inventory, lol).

You can create the inventory as a `dict()` but I (personally) find it not effective! It's better to have functions inside it,
I like to imagine the inventory as a <b>Backpack</b>, you can imagine the player interacting with it, and you can name (and function) the actions
that the player makes with a backpack. `drop_item()` is a good example, you can imagine the player openning his backpack and thinking "What is dead weight here?".

Classes let you do almost exactly that! haha!

```python
class Inventory:
    
    # The Class Constructor
    # This one is very basic, it just declares how many items you can fit 
    # in your inventory and creates an Empty list to keep them!
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []
        
class Item:

    # The Class Constructor
    # Creates a basic item, more attrs can be added for more complexity!
    def __init__(self, name, description, amount, individual_value):
        self.name = name
        self.description = description
        self.amount = amount
        self.individual_value = individual_value
    
    # Property that shows the worth of the item (x amount).
    @property
    def worth(self):
        return f'${self.amount * self.individual_value:.2f}'
```

We need to see those items somehow, so I've created the class `show()` inside the Inventory().

```python
    # It iterates trough the list of items showing the index no., the amount and the item name.
    def show(self):
        index = 1
        for item in self.items:
            print(str(f'{index} -> [x{item.amount}] {item.name}'))
            index += 1
```

# Handling Items
I've created a function `drop_item()` that shows you your items and asks you which one do you want to drop.

```python
def drop_item(self):
        print('\nWhich item do you want to drop? ["0" to Quit]')
        self.show()
        
        # Accepts user input to reference the index. If the Number is 0, quits the program (can be changed of course).
        i = int(input('\nNº > '))
        if i == 0:
            print('\nClosing the Inventory...')
            quit()
        
        # References the item with -1 (Python indexes start with 0).
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
        
        # Recursion (Can be Removed)
        self.drop_item()
```

It haves an example of how to sell items, that is shown inside the `Item` Class.

```python
    def sell(self):
        if self.amount >= 1:
            print('How many do you want to sell?')
            amt = int(input('amt > '))
            print(f'Are you sure you want to sell {self.amount} {self.name} for ${self.individual_value * amt:.2f}?')
            confirm = input('[y/n] > ')
            if confirm == 'y':
                self.amount -= amt
                print(f'{amt} {self.name} sold for ${amt * self.individual_value:.2f}!')

```

And for check the total worth of your richness in Items, I've created a property inside the `Inventory` named `total_worth`.

```python
    # It uses a list comprehension inside a sum() function inside a formatted string (That's why I love Python).
    @property
    def total_worth(self):
        return f'\nThe inventory Total Worth is: ${sum([i.individual_value * i.amount for i in self.items]):.2f}'
```

I Really hope it Helps newcomers, I can say that learning by making little games made that initial bad from learning something "complex" and new, a good thing!

If you want more content about Text RPG's plase email: ngj.netrunner@gmail.com!

Happy Coding!

by @ngeorgj at 16/08/2020
made during the pandemic.
    


