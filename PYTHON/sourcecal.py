def sum():
    ch='y'
    add=float(input("\nEnter number : "))
    while ch=='y':
        num=float(input("Enter number : "))
        add+=num
        ch=input("Do you want to add more number(y/n) : ")
        if ch in ('n','N'):
            break 
    else:
        print("Wrong input")
    print("Sum of numbers is :",add)

def sub():
    ch='y'
    sub=float(input("\nEnter number : "))
    while ch=='y':
        num=float(input("Enter number : "))
        sub-=num
        ch=input("Do you want to subtract more number(y/n) : ")
        if ch in ('n','N'):
            break 
    else:
        print("Wrong input")
    print("Subtrcation of numbers is :",sub)

def multi():
    ch='y'
    multi=float(input("\nEnter number : "))
    while ch=='y':
        num=float(input("Enter number : "))
        multi*=num
        ch=input("Do you want to multiply more number(y/n) : ")
        if ch in ('n','N'):
            break 
    else:
        print("Wrong input")
    print("Multiplication of numbers is :",multi)

def div():
    ch='y'
    div=float(input("\nEnter number : "))
    while ch=='y':
        num=float(input("Enter number : "))
        div/=num
        ch=input("Do you want to divide more number(y/n) : ")
        if ch in ('n','N'):
            break 
    else:
        print("Wrong input")
    print("Division of numbers is :",div)

def pow():
    ch='y'
    num1=float(input("\nEnter Base  : "))
    num2=float(input("Enter Power : "))
    res=m.pow(num1, num2)
    print(num1,"raise to power",num2,"is",res)

def fact():
    num=int(input("\nEnter number : "))
    print("Factorial of ",num,"is",m.factorial(num))
    
def sqrt():
    num=int(input("\nEnter number : "))
    print("Square root of ",num,"is",m.sqrt(num))
    
def remainder():
    num1=float(input("\nEnter Dividend"))
    num2=float(input("Enter Divisor"))
    print("Remainderis",num1%num2)
    
def sq():
    num=float(input("\nEnter a Number"))
    print("Square of ",num,"is",num*2)

def cube():
    num=float(input("\nEnter a Number"))
    print("Cube of ",num,"is",num*num*num)

def inverse():
    num=float(input("\nEnter a Number"))
    print("Inverse of ",num,"is",1/num)

def sin():
    num=float(input("\nEnter angle in degrees"))
    print("Sin of ",num,"is",m.sin(num))
    
def cos():
    num=float(input("\nEnter angle in degrees"))
    print("Cos of ",num,"is",m.cos(num))

def tan():
    num=float(input("\nEnter angle in degrees"))
    print("Tan of ",num,"is",m.tan(num))
