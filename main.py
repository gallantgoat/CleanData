from inventory import Inventory

def main():
    # Input
    apples_week1 = 12

    apples_week2 = 6

    invdif_dict = {
        "apples": 0
    }

    def inventory_difference(item_before, item_after):
        if item_after > item_before:
            print("How did you end up with more of this than last week?")
        elif item_after == item_before:
            print("You didn't sell any of this")
        else:
            print(f"You sold {item_before - item_after} of this item")
            invdif_dict["apples"] = item_before - item_after
        print(invdif_dict)

    inventory_difference(apples_week1, apples_week2)

if __name__=="__main__":
    main()