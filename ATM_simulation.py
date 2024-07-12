name =input("enter the name:")
print("Hello",name)
Message="""
How May I help you
Please select any of them option,
Type 1 >> CHECK BALANCE
Type 2 >> DEPOSIT
Type 3 >> WITHDRAWL"""
print(Message)
task = int(input("enter the option:"))
available_amount =5000 #constant amount in your account
if task >=1 and task<=3:
    print("Welcome to you in our virtual bank")
    
    # CHECK BALANCE
    if task ==1:
        print("Your available amount is : ", available_amount)
         #FIRST FILL ONE BLOCK if you doesnot have then write pass 

    # DEPOSIT
    elif task ==2:
        deposit_amount = int(input("please enter deposit amount"))
        if deposit_amount >500:
            available_amount += deposit_amount
            print("you have succesfully deposite your amount :" , deposit_amount)
            print("Your available amount is : ", available_amount)
        else:
            print("Dost me luta do")
    # WITHDRAWAL
    else:
        withdrawl_amount = int(input("please enter withdrawl amount"))
        if withdrawl_amount >5000:
             print("Money is not available")
        else:
            
            available_amount -= withdrawl_amount
            print("you have succesfully withdrawl your amount :" , withdrawl_amount)
            print("Your available amount is : ",available_amount)
else:
    print("select in between 1 to 3")

