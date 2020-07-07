import shelve

with shelve.open("bike") as bike:
    bike['make'] = "Honda"
    bike['model'] = "250 dream"
    bike['color'] = "red"
    bike['engine_size'] = 250

    print(bike['make'])
    print(bike['engine_size'])

    # print(bike['engin_size'])

    for key in bike:
        print(key)

    # print("- " * 20)
    #
    # del(bike['engin_size'])
    #
    # for key in bike:
    #     print(key)
