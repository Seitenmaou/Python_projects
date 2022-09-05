def hello():
    print("Hello!")

def pack(item1, item2, item3):
    list = [item1, item2, item3]
    return list

def eat_lunch(list):
    if len(list) == 0:
        print("My lunchbox is empty!")
    else:
        
        for item in range(len(list)):
            if item == 0:
                print("First, I eat an " + list[0])
            else:
                print("Next, I eat an " + list[item])


lunch = ["Apple", "Sandwich", "Chips"]

hello()

print(pack(lunch[0],lunch[1],lunch[2]))

eat_lunch(lunch[0]) #interesting...?

eat_lunch([lunch[0]])

eat_lunch([])

eat_lunch(lunch)