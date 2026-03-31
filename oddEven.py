
num = int(input("Enter a number:"))
def odd_even(num):
    if (num%2 == 0):
        print("Even Number")
    else:
        print("Odd Number")

def multiple_of_three(num):
    
    print("Multiple Of Three" if num%3==0 else "Non-Multiple")

def multiple_of_two(num):

    print( num%2==0 ? "Multiple of Two" : "Multiple of Three")

if __name__ == "__main__":
    
    odd_even(num)
    multiple_of_three(num)
    multiple_of_two(num)
