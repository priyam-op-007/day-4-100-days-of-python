import random
import my_module
random_integer = random.randint(1,10)
print(random_integer)
print(my_module.pi)

##########################################
random_float = random.random()
print(random_float)
##########################################
random_value_float = random_integer*random.random()
print(random_value_float)

##########################################
love_score = random.randint(1,100)
print(f"your love score is {love_score}")

#############################################
states_of_india = ["Gujarat","Delhi","odisha","Haryana"]
print(states_of_india[-1])
print(states_of_india[2])
print(states_of_india[-3])
print(states_of_india[0])

states_of_india[0] = "GUJ"
print(states_of_india[0])
states_of_india.append("Priyamland")
print(states_of_india)

###########################################

import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
name_length = len(names)
random_num = random.randint(0,name_length-1)
print(names[random_num] + " is going to buy the meal today!")
#Write your code below this line 👇
##########################################################################
fruits = ["apple","banana","cherry","papaya"]
veges = ["potato","beans", "tomato", "carrot"]
all = [fruits,veges]
print(all)
#################################################################
# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
horizontal = int(int(position)/10)
vertical = int(position)%10
map[vertical-1][horizontal-1] = "X"



#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

###########################################################


output - 
9
3.1111232
0.16621868880244584
3.0419783276962082
your love score is 75
Haryana
odisha
Delhi
Gujarat
GUJ
['GUJ', 'Delhi', 'odisha', 'Haryana', 'Priyamland']
Create a seed number: 34343
Give me everybody's names, separated by a comma. tack, jack, will, john
john is going to buy the meal today!
[['apple', 'banana', 'cherry', 'papaya'], ['potato', 'beans', 'tomato', 'carrot']]
['⬜️', '️⬜️', '️⬜️']
['⬜️', '⬜️', '️⬜️']
['⬜️️', '⬜️️', '⬜️️']
Where do you want to put the treasure? 20
['⬜️', '️⬜️', '️⬜️']
['⬜️', '⬜️', '️⬜️']
['⬜️️', 'X', '⬜️️']
