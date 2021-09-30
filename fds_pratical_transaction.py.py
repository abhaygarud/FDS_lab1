bal=0
while True :
        str =input("enter the operation you want to perform :")

        total=str.split(" ")
        l1=total[0]
        amount = int(total[1])
        if l1 == 'D' or l1=='d':
         bal+= amount
        
        elif (l1 == 'W' or l1=='w'): 
            if amount>bal:
             print( "account balance is insufficient")
            else:
             bal-=amount
        else:
            pass
       
         
        str1=input("if you want to continue press(y for yes) : ")           
        if not (str1=="Y"  or str=="y"):
          break
        print("TOTAL AMOUNT =", bal)
 

