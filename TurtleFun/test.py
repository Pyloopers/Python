import turtle as tut
Angle= eval(input("Enter Angle ="))
Limit=int(input("Enter the End limit ="))
Increment=1
for Increment in range(1,Limit,1):
    tut.fd(Increment)
    tut.lt(Angle)
        
