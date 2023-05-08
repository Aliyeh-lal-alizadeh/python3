import random
pc_number = random.randint(1,20)
i = 0
while True:
    user_number = int (input (" Enter number : "))
    i= i+1

    if user_number  == pc_number :
         print(" barande shodi")
         print("tedad talash : " , i) 
         break

    if user_number<pc_number :
                    print("bro balatar")
                    
    if user_number> pc_number :
                    print("bro paeentar")