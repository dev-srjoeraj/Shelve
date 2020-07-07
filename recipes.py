import shelve
blt = ["bacon", "lettuce", "tomato", "bread"]
beans_on_toast = ["beans", "toast"]
scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
pasta = ["pasta", "cheese"]

# with shelve.open('recepies') as recipes:
    # recipes["blt"] =  blt
    # recipes["beans on toast"] = beans_on_toast
    # recipes["scrambled eggs"] = scrambled_eggs
    # recipes["pasta"] = pasta
    # recipes["soup"] = soup
    #
    # for dish in recipes:
    #     print("{0} : {1} " . format(dish, recipes[dish]))
    #
    # #updating blt and pasta
    #
    # temp_list = recipes["blt"]
    # temp_list.append("butter")
    # recipes["blt"] = temp_list
    #
    # temp_list = recipes["pasta"]
    # temp_list.append("tomato")
    # recipes["pasta"] = temp_list

    # for dish in recipes:
    #     print("{0} : {1} ".format(dish, recipes[dish]))

with shelve.open('recepiesWithWriteback', writeback=True) as recipes:
    recipes["blt"] = blt
    recipes["beans on toast"] = beans_on_toast
    recipes["scrambled eggs"] = scrambled_eggs
    recipes["pasta"] = pasta
    recipes["soup"] = soup

    for dish in recipes:
        print("{0} : {1} ".format(dish, recipes[dish]))

    print(" = " * 50)
    recipes["soup"].append("cream")

    for dish in recipes:
        print("{0} : {1} ".format(dish, recipes[dish]))
