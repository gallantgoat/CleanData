from inventory import *

def main():
    # Input
    #apples_week1 = 12

    #apples_week2 = 6

    #invdif_dict = {
        #"apples": 0
    #}

    #def inventory_difference(item_before, item_after):
        #if item_after > item_before:
            #print("How did you end up with more of this than last week?")
        #elif item_after == item_before:
            #print("You didn't sell any of this")
        #else:
            #print(f"You sold {item_before - item_after} of this item")
            #invdif_dict["apples"] = item_before - item_after
        #print(invdif_dict)

    #inventory_difference(apples_week1, apples_week2)
    # Input
    apple = InventoryItem("apple", 12, 1.50)

    cafe_inventory = CafeInventory()

    # Process

    cafe_inventory.add_item(apple)

    # Verify
    print(cafe_inventory.items)
if __name__=="__main__":
    main()