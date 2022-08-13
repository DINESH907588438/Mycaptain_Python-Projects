#Dictionary Elements Changing

n = int(input("Enter the number of Dictionary Elements: "))
d = dict()
for i in range(n):
    key1 = input("Enter the Key {}: ".format(i+1))
    value = input("Enter the value {}: ".format(i+1))
    d[key1] = value
print("Your Dictionary is ")
print(d)
rep = input("Which key value do you want to replace ? ")
key2 = input("Enter the key value to replace: ")
d[rep] = key2
print("Your Dictionary After the Element is replaced ")
print(d)
