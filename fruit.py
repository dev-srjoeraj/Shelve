import shelve

fruit = shelve.open('ShelfTest')

# for snack in fruit:
#     print("{0} : {1}".format(snack, fruit[snack]))
#
# #fruit['apple'] = "Good for making cider"
#
# print(" - " * 20)
# for snack in fruit:
#     print("{0} : {1}".format(snack, fruit[snack]))
#
# print(" - " * 20)
#
# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
#
# for snack in ordered_keys:
#     print("{} : {}".format(snack, fruit[snack]))



# for v in fruit.values():
#     print(v)
#
# print(fruit.values())
# for f in fruit.items():
#     print(f)
#
# print(fruit.items())
#
# fruit.close()


while True:
    userInput = input("Enter the fruit :")
    if(userInput == "quit"):
        break
    des = fruit.get(userInput, "We dont have that shit")
    print(des)
    # if userInput in fruit:
    #     des = fruit[userInput]
    #     print(des)
    # else:
    #     print("We dont have that shit")