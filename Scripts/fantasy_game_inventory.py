#Script to display inventory from dictionary 
stuff = {
    'rope':1,
    'torch':6,
    'gold coin':42,
    'dagger':1,
    'arrow':12
}

def display_inventory(inventory):
    print('Inventory: ')
    item_total = 0
    for key, value in inventory.items():
        print(str(value) + ' ' + str(key))
        item_total += value
    print('Total number of items: ' + str(item_total))
print('Original inventory: \n')
display_inventory(stuff)

#Script to add loot from list to inventory dictionary
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory.keys():
            inventory[item] += 1
        else:
            inventory.setdefault(item, 1)

add_to_inventory(stuff,dragon_loot)
print('Inventory after loot: \n')
display_inventory(stuff)
