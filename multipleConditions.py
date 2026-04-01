def grades(num):
    if num>90:
        print("Grade A")
    elif num>80 and num <90:
        print("Grade B")
    elif num>70 and num <80:
        print("Grade C")
    elif num>60 and num <70:
        print("Grade D")
    else:
        print("Grade F")


def days(day):
    return {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday",
    }.get(day, "Invalid day")

def greetings(greet):
    if(greet>=0 and greet<=12):
        print("Good Morning")
    elif(greet>12 and greet<=17):
        print("Good Afternoon")
    elif(greet>17 and greet<=20):
        print("Good Evening")
    elif(greet>21 and greet<=23):
        print("Good Night")
    else:
        print("Invalid Number")

def vote(age):
    if (age >=18):
        print("Vote")
    else:
        print("Not Eligible")

def months(month):
    return {
        1: 32,
        2: 28,
        3: 29,
        4: 31,
        5: 30,
        6: 30,
        7: 31,
        8: 32,
        9: 30,
        10: 31,
        11: 30,
        12: 32,
    }.get(month, "Invalid months")

if __name__=="__main__":
    num = int(input("Enter a number:"))
    grades(num)

    num1 = int(input("Enter a number:"))
    print(days(num1))

    num2 = int(input("Enter a number:"))
    print(months(num2))

    num3 = int(input("Enter a number:"))
    vote(num3)

    num4 = int(input("Enter a number:"))
    greetings(num4)