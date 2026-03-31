num = int(input("Enter a number"));

def divisible_by_5(num):
    if (num%5)==0 and (num%3 == 0):
        print("Divisible by 3 and 5!")
    else:
        print("NOT")

divisible_by_5(num)