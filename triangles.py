

def checkValidity(a, b, c):
    if ((a+b) >c) and (a+c)>b and (b+c)>a:
        print("Valid triangle")
        return True
    else:
        return False

def typeTriangle(a, b, c):
    if (a==b==c):
        return "It is Equilatoral Triangle"
    elif (a==b) or (b==c) or (a==c):
        return "It is Isolesces Triangle"
    else:
        return "It is scalene Triangle"

if __name__ == "__main__":
    sideA = int(input("Enter side A: "))
    sideB = int(input("Enter side B: "))
    sideC = int(input("Enter side C: "))

    check = checkValidity(sideA, sideB, sideC)

    if check ==True:
        print(typeTriangle(sideA, sideB, sideC))
    else:
        print("Not a valid Triangle")
