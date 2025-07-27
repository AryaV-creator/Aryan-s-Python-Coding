"""
Author: Aryan Vemulapalli
Course: ICS3UC
Date: 04/10/2024"
"""
#WELCOME
"""WELCOME TO THE ONE AND ONLY SAVING SIMULATOR!"""

try:
    investment=float(input("What is your current investment($): ")) #Asking the user what their investment is
    initialInvestment=investment #Stores that value in a permenant variable
    interestRate=float(input("What is your interest rate(%): ")) #Asking the user the interest rate in percent
    years=int(input("What are the number of years invested?: ")) #Asking for the number of years invested
    print("Let's invest your money!")
    for i in range(years): #Has to be in the reange of the amount of years so that it will print the amount balance for each year
        interest=float(investment)*float(interestRate)/100 #Does the calculation for the interest by converting it to decimal and multiplying it by the investment
        interest=str(interest)[:str(interest).find('.')+3] #Contricts it to 2 decimal places, no rounding, it finds the decimal point and ensures that it has less than 3 decimal places
        investment=float(interest)+float(investment) #Calculating the interest with the investment toal
        investment=str(investment)[:str(investment).find('.')+3] #Making sure the investment is only to two decimal places
        print("Year", i+1, " $", investment) #Prints the balance per year
        interestGained=float(investment)-float(initialInvestment) #The amount of interest gained by subtracting the initial investment from the current investment balance
        interestGained=str(interestGained)[:str(investment).find('.')+3]#Keeps it at 2 decimal places
    withdrawAmount=(input("Amount to withdraw($): ")) #Asks the user how much money they want to withdraw
    print("Let's invest your money!")
    while float(withdrawAmount)<float(investment): #convert it to float since it can be a decimal number. Also, while the withdraw amount is less than the investment, it should execute the commands following
        interestRate=float(input("What is your interest rate(%): ")) #Ask for the interest rate
        years=int(input("What are the number of years invested?: ")) #Ask for the numbers of years
        print("Let's invest your money!")
        while float(withdrawAmount)<float(investment):            
            investment=float(investment)-float(withdrawAmount)           
            for i in range(years): #While it is within the number of years inputted
                interest=float(investment)*float(interestRate)/100 #Converts interest to decimal and then multiplies it by investment to get the interest
                interest=str(interest)[:str(interest).find('.')+3] #Keeps it at 2 decimal places without rounding, just slices the number                
                interestGained=float(interest)+float(interestGained)                
                interestGained=round(interestGained,2)                
                investment=float(interest)+float(investment) #Adds the interest to the investment
                investment=round(investment,2)#Rounds to two decimal places
                print("Year", i+1, ":", investment)              
            print("Your investment amount available: "+str(investment))
            withdrawAmount=float((input("Amount to withdraw($): ")))
            print("Let's invest your money!")
            loopBreak=0
            while float(withdrawAmount)<=float(investment) and loopBreak==0: #This will happen only once when the withdraw is lower than or equal to the investment since loopBreak has to equal 0 but we are adding 1
                interestRate=float(input("What is your interest rate(%): "))
                years=int(input("What are the number of years invested?: "))
                loopBreak=1
            
    finalAmount=float(initialInvestment)+float(interestGained) #Calculates the final amount by adding the interests to the investment
    print('Your withdraw amount is greater than Available Amount') #Lets the user know they are withdrawing more than what is possible
    print("Your final amount: $"+str(round(finalAmount,2))) #Tells the user their final amount
except ValueError:  #If an error arrises in case they include a word instead of a number, it will ask them to re-run
    print("The input was not a valid integer. Re-run again")    
      