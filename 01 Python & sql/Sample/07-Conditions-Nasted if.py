x = int(input("Enter Your Mark : "))
if x > 100 :
    print("Sorry Number not allowed")
elif x >= 50 :
    if x >=90 :
        print("Excellent")
    elif x >= 75 :
        print("Very Good")
    elif x >= 60 :
        print("Good")
    else :
        print("Pass")
elif x <50 and x >=0 :
    print ("Not Pass")
else :
    print("Not allowed Value")
