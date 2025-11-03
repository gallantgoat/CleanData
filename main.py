apples_week1 = 12

apples_week2 = 6

def inventory_difference(item_before, item_after):
    if item_after > item_before:
        print("How did you end up with more of this than last week?")
    elif item_after == item_before:
        print("You didn't sell any of this")
    else:
        print(f"You sold {item_before - item_after} of this item")

inventory_difference(apples_week1, apples_week2)