#Declare a maximum value
MAX_NUMBER=12
MIN_NUMBER=7


#Prompt user
print("Enter a number between 7 and 12")

#Take input, turn it into an integer
number=int(input())

#Check if the number is too big
if number > MAX_NUMBER:
    print("Your number was too big!")
#Now check if it is too small
elif number < MIN_NUMBER:
    print("Your number was too small!")
#Do this if the other two are both false
else:
    print("Thanks for entering your number!")
