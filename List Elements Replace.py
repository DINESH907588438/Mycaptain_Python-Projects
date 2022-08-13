#List Elements changing

n = int(input("Enter the number of Elements in the list: "))
l = list()
print("Enter the array Elements")
for i in range(n):
    l.append(input())
print("Your List is:",l)
key  = input("Which Element do you want to Replace: ")
Ele = input("Enter the Element to Insert: ")
l[l.index(key)] = Ele
print("Your List After The Element Inserted",l)