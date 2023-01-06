#Program to greeting a person....

import datetime
currentTime =datetime.datetime.now()
currentTime.hour

name = input("Enter your name please : ")
if currentTime.hour < 12:
    print("Good Morning,",name)
elif 12<= currentTime.hour <18:
    print("Good AFternoon,",name)
else:
    print("Good Evening,",name)
