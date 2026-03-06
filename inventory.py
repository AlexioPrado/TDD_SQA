def add_item(inventory, item):
    #Check for inventory errors
    if inventory["locked"]:
        raise ValueError("This item is locked")
    elif len(inventory["items"]) >= 10:
        raise ValueError("The inventory is full")
    #Check if item is valid
    if isinstance(item, str) and item:
       inventory["items"].append(item)
       return inventory
    else:
        raise ValueError("Item must be of type str")

def remove_item(inventory, item):
    #Check for inventory erros
    if inventory["locked"]:
        raise ValueError("This item is locked")
    elif not item in inventory["items"]:
        raise ValueError("Item is not found in the inventory")
    inventory["items"].remove(item)
    return inventory

def get_item_count(inventory):
    return len(inventory["items"])