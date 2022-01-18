#1.write a python function to find the max of 3 numbers.
from os import lseek


n1=int(input ("Enter first number:"))
4
n2=int(input("Enter second number:"))
12
n3=int(input("Enter third number:"))
8
def f():
    if(n1>=n2) and (n1>=n3):
      l=n1
    elif(n2>=n1) and (n2>=n3):
      l=n2
    else:
      l=n3
    print("Largest number among the three is",l)
f()
#2. Write a python function to sum all the numbers in a list.
def sum(num):
    sum = 0
    for i in num:
     sum+= i
    return sum
list = [1,2,3,4]
print(sum((list)))
#3. Write a python function to multiply all numbers in a list
list1 = [3,2,4]
def multiplylist(mylist):
    result = 1
    for x in mylist:
        result = result * X
    return result
print(multiplylist)(list1)        
#4. Write a python function to reverse a given string.
s = "mylaptopisgood"
def reverse(s):
    str = ""
    for i in s:
     str = i + str
    return str
print("The original string is:", end="")
print(s)
print(reverse(s))
#5. Write a python function that takes a string and displays the number of upper case letters and the number of lower case letters.
def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
     if c.isupper():
      d["UPPER_CASE"]+=1
     elif c.islower():
       d["LOWER_CASE"]+=1
     else: 
      pass
    print("The original string : ", s)
    print("No of Upper case characters : ", d["UPPER_CASE"])
    print("No of Lower case charaters : ", d["LOWER_CASE"])
string_test("Okere is Good Always")
#Question of the day Jan 11
#Create a function func() which takes a variable number of arguments and prints out those variables.
#So for example if func(23, 25, 25)
#it should print 23, 25, and 25,
#if func(20, 21)
#it should print 20, 21
numbers = (23,25,25)
def vaiables_numbers():
    print(numbers)
 #Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction.
#Also, it must return both addition and subtraction in a single return call.
def func(num1, num2): 
     sum_ = num1+num2
     sub_ = num1-num2
     return sum_, sub_
func(22,10)
#Write a program to create a function show_employee() using the following conditions.
#It should accept the employee’s name and salary and display both.
#If the salary is missing in the function call then assign default value 9000 to salary
def fargate(employee, salary = 9000):
    print('employee: ', employee)
    print('salary: ', salary)
fargate('okere', 6000)
#Write a shut_down functioon that takes one argument. if the argument is yes, the function should return shutting down, if no it should return shut down aborted. if the argument is neither yes or no, the function should return sorry
def shut_down(s):
    if s == "yes":
        return "shutting down"
    elif s == "no":
        return "shutting aborted"
    else:
        return "sorry" 
#Define a function called hotel_cost with one argument nights as input. The hotel costs $140 per night. So, the function hotel_cost should return 140 * nights.        
def hotel_cost(nights):
  return 140 * nights
#Define a function called plane_ride_cost that takes a string, city, as input. The function should return a different price depending on the location. 
def plane_ride_cost(city):
    if "Montreal" == city:
     return 150
    elif "Quebec" == city:
     return 200
    elif "Toronto" == city:
     return 250
    elif "Alberta" == city:
         return 400
#Define a function called rental_car_cost with an argument called days. Calculate the cost of renting the car: Every day you rent the car costs $40.(cost=40*days) if you rent the car for 7 or more days, you get $50 off your total(cost-=50). Alternatively (elif), if you rent the car for 3 or more days, you get $20 off your total. You cannot get both of the above discounts. Return that cost.
def rental_car_cost(days):
    car = 40 * days
    if days >= 7:
        car -= 50
    elif days >= 3:
        car -= 20
    return car 
#Now define a function called trip cost that takes the output from the three functions above and prints the total cost of the trip
def trip_cost(city, days):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city)
    #First, def a function called distance_from_zero, with one argument (choose any argument name you like). If the type of the argument is either int or float, the function should return the absolute value of the function input. Otherwise, the function should return "Nope". Check if it works calling the function with -5.6 and "what?".
  

     

