#Dictionary Methods

print(" 1.clear\n 2.copy\n 3.fromkeys\n 4.get\n 5.keys\n 6.pop\n 7.popitem\n 8.setdefault\n 9.update\n 10.values")
n = int(input("Enter the number keys in your Dictionary: "))
d = dict()
for i in range(n):
    k1 = input("Enter the key-{}: ".format(i+1))
    v1 = input("Enter the value-{}: ".format(i+1))
    d[k1] = v1
print("Your Dictionary is: ",d)
opt = int(input("Enter you option: "))
if opt == 1:
    #The clear() method removes all the elements from a dictionary.
    print("clear({}) = {}".format(d,d.clear()))
elif opt == 2:
    #The copy() method returns a copy of the specified dictionary.
    d2 =d.copy()
    print("The copied dictionary is: ",d2)
elif opt == 3:
    #The fromkeys() method returns a dictionary with the specified keys and the specified value.
    m = input("Which key value do you want to see? ")
    g = d.fromkeys(m)
    print(g)
elif opt == 4:
    #The fromkeys() method returns a dictionary with the specified keys and the specified value.
    k = input("Enter the key to see the Value: ")
    d2 = d.get(k)
    print("get({}) = {}".format(k,d2))
elif opt == 5:
    #The keys() method returns a view object.
    print("keys(d) = {}".format(d.keys()))
elif opt == 6:
    #The pop() method removes the specified item from the dictionary.
    k = input("Enter the key to remove: ")
    d.pop(k)
    print("The Dictionary After pop function: ",d)
elif opt == 7:
    #The popitem() method removes the item that was last inserted into the dictionary.
    d.popitem()
    print("The Dictinary After popitem function: ",d)
elif opt == 8:
    #The setdefault() method returns the value of the item with the specified key.
    k = input("Enter the key to add: ")
    v = input("Enter the value to add: ")
    d.setdefault(k,v)
    print("The dictionary after setdefult operation",d)
elif opt == 9:
    #The update() method inserts the specified items to the dictionary.
    k = input("Enter the key to add: ")
    v = input("Enter the value to add: ")
    d.update({k:v})
    print("The dictinary After updating the Elements: ",d)
elif  opt == 10:
    #The values() method returns a view object.
    print("Values(d) = {}".format(d.values()))
else:
    print("Please,Enter the Valid Option")








