import datetime

now=datetime.datetime.now()
Name=input("Enter Your Name :")

if now.hour<12 and now.hour >5 :
    print("Good Morning...Have a Good Day",Name)
elif now.hour>12 and now.hour<16 :
    print("Good AfterNoon...I Wish your day was good",Name)
elif now.hour >=16 and now.hour<21:
    print("Good Evening...How's your Day goin",Name)
elif now.hour >= 21 :
    print("Good Night...Have a Nice sleep",Name)
