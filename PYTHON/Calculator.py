#Program of Calculator to perform some basic opertaion...

import math as m
import sourcecal as sc
import os
os.system('cls')
  
while True:
    choice = input("Do u want to use Calculator(y/n) : ")
    while choice in ('y','Y'):
        os.system('cls')
        print("="*20,"Welcome to my Calculator","="*20)
        print("What do you want to do:")
        print("0. Exit")
        print("1. Addtion")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Remainder")
        print("7. Factorial")
        print("8. Square Root")
        print("9. Square")
        print("10. Cube")
        print("11. Inverse")
        print("12. sin")
        print("13. cos")
        print("14. tan")
        print("="*66)
        
        ch = int(input("\nEnter your choice : "))
        if ch in (1,2,3,4,5,6,7,8,9,10,11,12,13,14):

            if ch==0:
                break
            elif ch == 1:
                sc.sum()
            elif ch == 2:
                sc.sub()
            elif ch == 3: 
                sc.multi()
            elif ch == 4:
                sc.div()
            elif ch == 5:
                sc.pow()
            elif ch == 6:
                sc.remainder()
            elif ch == 7:
                sc.fact()
            elif ch == 8:
                sc.sqrt() 
            elif ch ==9:
                sc.sq()
            elif ch==10:
                sc.cube()
            elif ch == 11:
                sc.inverse()
            elif ch == 12:
                sc.sin()
            elif ch== 13:
                sc.cos()
            elif ch == 14:
                sc.tan()
        
        else:
            print("\nInvalid choice")
            ch = int(input("\nEnter your choice : "))

        choice=input("\nWanna continue : ")        
        if choice in ('n','N'):
           print("\nThanks for Using My Calculator")
           
    break
   
    if choice in ('n','N'):
        print("\nThanks for Coming Here")
        break
    
    else:
        print("Please Enter y or n..")
    