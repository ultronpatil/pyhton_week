i=0
candy=10
while i==0:
    print("\nthe candies in jar :- ",candy)
    num=int(input("enter the number of candies:- "))
   

    if(num<=10):
        candy=candy-num
        print("you have taken",num,"candies and ",candy,"are remain")
       
        if(candy<=5):
            candy=candy+(10-candy)
            print("jar is refilled candies are:- ",candy)
       
        elif(candy>5):
            print("jar is not refilled candies are:- ",candy)
            
    elif(num<=0):
        print("NO you cant have it")
    elif(num>=10):
        print("NO you cant have it")
        