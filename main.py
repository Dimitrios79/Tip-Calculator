#If the bill was $150.00, split between 5 people, with 12% tip. 
print("Welcome to calculator!")
x = float(input("What was the total bill? $"))
y = int(input("How much tip would you like to give? 10, 12, or 15 "))
c = int(input("How many peaple to split the bill? "))
d = float(x * (y/100)+x)
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60)
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
s = float(round(d/c, 2))
#Write your code below this line 👇
print(f"Each person should pay: {s}")