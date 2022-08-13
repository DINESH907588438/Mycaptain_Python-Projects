#String Methods

s = str(input("Enter The String: "))
print(" 1.capitalize \n 2.casefold \n 3.center \n 4.count\n 5.encode\n 6.endswith\n 7.expandtabs")
print(" 8.find\n 9.format\n 10.format_map\n 11.index\n 12.isalnum\n 13.isalpha\n 14.isdecimal")
print(" 15.isdigit\n 16.isidentifier\n 17.islower\n 18.isnumeric\n 19.isprintable\n 20.issapce")
print(" 21.istitle\n 22.isupper\n 23.join\n 24.ljust\n 25.lower\n 26.lstrip\n 27.maketrans")
print(" 28.partion\n 29.replace\n 30.rfind\n 31.rindex\n 32.rpartition\n 33.rsplit\n 34.split")
print(" 35.splitlines\n 36.startswith\n 37.swapcase\n 38.title\n 39.translate\n 40.upper")
print(" 41.rjust\n 42.zfill\n 43.rstrip\n 44.strip")
opt = int(input("Enter Your Choice: "))
print("Your String is:  ",s)

if opt == 1:
    # 1.Capitalize Converts the first character to upper case.
    print("The Capitalized string : ", s.capitalize())
elif opt == 2:
    # 2.The casefold() method returns a string where all the characters are lower case.
    print("The casefolded string: ",s.casefold())
elif opt == 3:
    #The center() method will center align the string, using a specified character (space is default) as the fill character.
    k = int(input("Enter the Value to Center the String: "))
    fill = input("Enter the Fill Character: ")
    print("The Centered string : ",s.center(k,fill))
elif opt == 4:
    # The count() method returns the number of times a specified value appears in the string.
    k = input("Enter any Element to count: ")
    print("Count({}) = {}".format(k,s.count(k)))
elif opt == 5:
    k = s.encode()
    print("The Encoded Version of the String: ",k)
    #The encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.
elif opt == 6:
    ch = input("Enter to Find the End character: ")
    #The endswith() method returns True if the string ends with the specified value, otherwise False.
    ou = s.endswith(ch)
    if ou == True :
        print("The String is Endswith :'{}'".format(ch))
    else:
        print("The string does not Endswith {}".format(ch))
elif opt == 8:
    s1 = input("Enter a string to find: ")
    #The find() method finds the first occurrence of the specified value.
    x = s.find(s1)
    print("Your string '{}' is find at Position: {}".format(s1,x))
elif opt == 9:
    #The format() method formats the specified value(s) and insert them inside the string's placeholder.
    print("Your string is : {}".format(s))
elif opt == 10:
    print(f"Your string = {s}".format_map(s))
    # The format() method formats the specified value(s) and insert them inside the string's placeholder.
elif opt == 11:
    #The index() method finds the first occurrence of the specified value.
    k = input("Enter the number to find Index: ")
    ou = L.index(k)
    print("Index({}) = {}".format(k,ou))
elif opt == 12:
    #The isalnum() method returns True if all characters in the string are alphanumeric.
    if s.isalnum():
        print("All characters in the given string are alphanumeric")
    else:
        print("All characters in the given string are not alphanumeric")
elif opt == 13:
    #The isalpha()method returns True if all characters in the string are in the alphabet.
    if s.isalpha():
        print("All characters in the given string are Numeric")
    else:
        print("All characters in the given string are not Numeric")
elif opt == 14:
    #The isascii() method returns True if all characters in the string are ascii characters
    if s.isdecimal():
        #The isdecimal() methods True if all the characters are decimals (0-9).
        print("All characters in the given string are Decimals(0-9)")
    else:
        print("All characters in the given string are not Decimals(0-9)")
elif opt == 15:
    #The isdigit() method returns True if all the characters are digits, otherwise False.
    if s.isdigit():
        print("All characters in the given string are Numeric")
    else:
        print("All characters in the given string are not Numeric")
elif opt == 16:
    #The isidentifier() method returns True if the string is a valid identifier, otherwise False.
    if s.isidentifier():
        print("Your String is an Identifier")
    else:
        print("Your String is not an Identifier")
elif opt == 17:
    if s.islower():
        #The islower() method returns True if all the characters are in lower case, otherwise False.
        print("All characters in the string are Lower case")
    else:
        print("All characters in the string are not Lower case")
elif opt == 18:
    #The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.
    if s.isnumeric():
        print("All characters in the string are Numeric")
    else:
        print("All characters in the string are not Numeric")
elif opt == 19:
    #The isprintable() method returns True if all the characters are printable, otherwise False.
    if s.isprintable():
        print("All characters in the string are printable")
    else:
        print("All characters in the string are not printable")
elif opt == 20:
    #The isspace() method returns True if all the characters in a string are whitespaces, otherwise False.
    if s.isspace():
        print("All characters in the string are whitespaces")
    else:
        print("All characters in the string are not whitespaces")
elif opt == 21:
    #The istitle()	Returns True if the string follows the rules of a title.
    if s.istitle():
        print("Your String follows the rules of title")
    else:
        print("Your String does not follow the rules of title")
elif opt == 22:
    #The isupper() method returns True if all the characters are in upper case, otherwise False.
    if s.isupper():
        print("All characters in the string are Upper case")
    else:
        print("All characters in the string are Upper case")
elif opt == 23:
    #The join() method takes all items in an iterable and joins them into one string.
    s1 = tuple(s)
    d = input("Enter the fill character: ")
    print("The Modified string =",d.join(s1))
elif opt == 24:
    #The ljust() method will left align the string, using a specified character (space is default) as the fill character.
    k = input("Enter the Fill character: ")
    l = int(input("Enter the Length: "))
    print("The String after ljust method : ",s.ljust(l,k))
elif opt == 25:
    #The lower() method returns a string where all characters are lower case.
    l = s.lower()
    print("The lowered case string = ",l)
elif opt == 26:
    #The lstrip() method removes any leading characters.
    r = input("Enter the charcter to remove: ")
    x = s.lstrip(r)
    print("The string after lstrip opertion: ",x)
elif opt == 27:
    #The maketrans() method returns a mapping table that can be used with the translate() method to replace specified characters.
    l1 = input("Which character do you want to remove: ")
    l2 = input("Which character do you want to fill: ")
    d = s.maketrans(l1,l2)
    print("The String after: ",s.translate(d))
elif opt == 28:
    p = input("Enter the String to Partion: ")
    k = s.partition(p)
    print("The partion string is: ",k)
else:
    print("Please,Enter the Valid Option")










