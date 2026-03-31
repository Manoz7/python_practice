count = input("Did you get the year?(Y/N): ")

while (count == 'n' or count == 'N'):
    year = int(input("Enter the year:"))
    if (year%4==0 and year %100 !=0) or year%400==0:
        print("Leap Year Detected")

    else:
        print("Leap Year NOT Detected")

    count = input("Did you get the year?(Y/N): ")

else:
    print("Thank you!")
