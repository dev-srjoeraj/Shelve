import shelve

# with shelve.open("ShelfTest") as fruit:
#     fruit['organe'] = "a sweet , orange ,citrus fruit"
#     fruit['apple'] = "good for making cider"
#     fruit['lemon'] = "a sour, yellow citrus fruit"
#     fruit['grape'] = "a small, sweet fruit growing in bunches"
#     fruit['lime'] = "a sour, green citrus fruit"
#
#     print(fruit["lemon"])
#     print(fruit["apple"])

with shelve.open("ShelfTest2") as fruit:
    fruit = {
        "orange" : "a sweet, orange, citrus fruit",
        "apple"  : "good for making cider",
        "lemon"  : "a sour, yellow citrus fruit",
        "grape"  : "a small, sweet fruit growing in bunches",
        "lime"   : "a sour, green fruit"

    }

print(fruit['lime'])
print(fruit['orange'])

print(fruit)
