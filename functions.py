#define a function read_num to read two input numbers

#Another function sum_num to add the two numbers and return

#write another function sub_num to subtract the two numbers and return

#print all the numbers, the sum and the difference

def read_num():
    number1 = int(input("Give me one number"))
    number2 = int(input("Give me another number"))
    print("The numbers are " + str(number1)+" and " + str(number2))
    return number1,number2

def sum_num(a, b):
    sum=a + b
    print("The sum of the numbers is " +str(sum))
    return sum

def sub_num(number1, number2) :
    difference=number1-number2
    print("The difference of the numbers is " + str(difference))
    return difference

num1, num2=read_num()
print("first number is:"+str(num1))
print("Second# number is:"+str(num2))
tot=sum_num(num1,num2)
print(" Total sum is   "+ str(tot))
diff=sub_num(num1,num2)
prod=tot*diff
print("the product of Sum and Diff is  "+ str(prod))
print(" WellDone,Good Night!")