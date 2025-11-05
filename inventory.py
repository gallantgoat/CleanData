class InventoryItem:
    def __init__(self, name, quanity, unit_cost):
        self.name = name
        self.quanity = quanity
        self.unit_cost = unit_cost

class CafeInventory:
    def __init__(self):
        self.items = []

    def add_item(self, inventory_item):
        if isinstance(inventory_item, InventoryItem):
            self.items.append(inventory_item)
            print(f"{inventory_item} has been added to the Cafe Inventory")
        else:
            print("Error: Only 'InventoryItem' instances can be added to the Inventory")

    def change_quanity():
        pass
    
    def inventory_dif(self, quanity_before, quanity_after):
        pass 

    def get_low_stock():
        pass