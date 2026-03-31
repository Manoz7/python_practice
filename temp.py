count = input("Do you want more (Y/N):")

while (count == 'y' or count == 'Y'):
    order = input("Select C/F for celcius and Ferhenheit: ")

    if order == 'c' or order =="C":
        temp = int(input("Enter temp in Celcius: "))
        if temp < 10:
            print("Cold")
        elif temp >10 and temp <30:
            print("Warm")
        else:
            print("Hot")

    elif order == 'f' or order == 'F':
        temp = int(input("Enter temp in Ferhenheit: "))
        if temp < 48:
            print("Cold")
        elif temp >48 and temp <80:
            print("Warm")
        else:
            print("Hot")
    else:
        print("Enter valid letter!!")
    
    count = input("Do you want more (Y/N):")

else:
    print("Thank you!")