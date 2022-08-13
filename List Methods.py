#To Create The List
n = int(input("Enter the number Elements in the List: "))
L = list()
print("Enter the Array Elements")
for i in range(n):
    L.append(input()) #append used to insert the Element to the list at the last position
print(" 1.Append\n 2.Extend\n 3.Copy\n 4.Count\n 5.Reverse \n 6.Sort\n 7.Index\n 8.Insert\n 9.Pop \n 10.Remove \n 11.Clear ")
print("Your List is : ",L)
opt = int(input("Enter your choice: "))
#List Methods

if opt == 1:
    k=input("Enter the Element to Insert the list: ")
    L.append(k)   #The append() method appends an element to the end of the list
    print(L)
elif opt == 2:
    m = list()
    x1 = int(input("How many Elements do you like to insert: "))
    print('Enter the Elements: ')
    for i in range(x1):
        m.append(input())
    for i in m:
        L.extend(i)   #The extend() method adds the specified list elements (or any iterable) to the end of the current list
    print(L)
elif opt == 3:
    X = L.copy()  ##The copy() method returns a copy of the specified list.
    print("Copied List = ",X)
elif opt == 4:
    K = input("Enter the Element to Count: ")
    X = L.count(K)   #The count() method returns the number of elements with the specified value.
    print("Count('{}') = {}".format(K,X))
elif opt == 5:
      L.reverse() #The reverse() method reverses the sorting order of the elements
      print("The Reversed list = ",L)
elif opt == 6:
    #The sort() method sorts the list ascending by default.
    L.sort()
    print("The sorted list :", L)
elif opt == 7:
    key = input("Which Element do you want to find Index: ")
    #The index() method returns the position at the first occurrence of the specified value.
    print("Position({}) = {}".format(key,L.index(key)))
elif opt == 8:
    K = input("Enter the Element to insert: ")
    pos = int(input("Enter the position to Insert: "))
    L.insert(pos,K)  #The insert() method inserts the specified value at the specified position.
    print("The List after Insert method:",L)
elif opt == 9:
    k = int(input("Enter the postion to remove the element: "))
    L.pop(k)  #The pop() method removes the element at the specified position.
    print(L)
elif opt == 10:
    K = input("Enter the Element to remove from the list: ")
    L.remove(K)  #The remove() method removes the first occurrence of the element with the specified value.
    print(L)
elif opt == 11:
    L.clear() #The clear() method removes all the elements from a list.
    print('The list after clear method:',L)
else:
    print("Please,Enter the Valid option.")














