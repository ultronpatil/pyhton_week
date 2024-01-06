# weight=int(input("enter the weight:- "))

# if (weight>0 and weight<=2000):
#     print("the time will be : 25")
# if(weight>2001 and weight<=4000):
#     print("the time will be : 35")
# if(weight>=4001 and weight<=7000):
#     print("the time will be : 45")
i=1
while i==1:
    def low (wei):
        # if (wei>0 and wei<=2000):
            print("the time will be : 25")
            print("the water level is low ")
    def medium(wei):
        # if (wei>=2001 and wei<=4000):
            print("the time will be : 35")
            print("the water level is medium ")
    def high(wei):
        # if (wei>=2001 and wei<=4000):
            print("the time will be : 45")
            print("the water level is high ")
    weight=int(input("\nenter the weight: "))
    if (weight>0 and weight<=2000):
        low(weight)
    if(weight>2001 and weight<=4000):
        medium(weight)
    if(weight>=4001 and weight<=7000):
         high(weight)
    else:
        print("overloaded")