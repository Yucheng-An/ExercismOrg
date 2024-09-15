def create_inventory(items):
    inventory = {}
    for item in items:
        if item in inventory:
            inventory[item] = inventory[item] + 1
        else:
            inventory[item] = 1
    return inventory
def add_items(inventory, items):
    for item in items:
        if item in inventory:
            inventory[item] = inventory[item] + 1
        else:
            inventory[item] = 1
    return inventory
def decrement_items(inventory, items):
    for item in items:
        if item in inventory:
            if inventory[item] != 0:
                inventory[item] = inventory[item] - 1
    return inventory
def remove_item(inventory, item):
    inventory.pop(item, "Miss item")
    return inventory
def list_inventory(inventory):
    result = []
    for item in inventory:
        if inventory[item] > 0:
            result.append((item,inventory[item]))
    return result
