import random
computer = random.randint(0,2)
user = int(input("What do you choose?? type 0 for rock, 1 for paper or 2 for scissors"))
if user == 0 :
  print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif user == 1:
  print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
elif user == 2:
  print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
else:
  print("choose a valid number")
print("Computer chose:")
if computer == 0 :
  print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif computer == 1:
  print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
elif computer == 2:
  print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
else:
  print("choose a valid number")

if user == 0 and computer == 0:
  print("Its a draw!,Try again")
elif user == 1 and computer == 1:
  print("Its a draw!,Try again")
elif user == 2 and computer == 2:
  print("Its a draw!,Try again")
elif user == 0 and computer == 1:
  print("You lose, that paper smoked you!")
elif user == 0 and computer == 2:
  print("You win, You broke that scissor")
elif user == 1 and computer == 0:
  print("You won, you smoked that rock")
elif user == 1 and computer == 2:
  print("You lose, That scissor ripped you")
elif user == 2 and computer == 0:
  print("You lose, Your scissors need some repairing")
elif user == 2 and computer == 1:
  print("You win, You ripped that piece of paper")
           
    
output -
What do you choose?? type 0 for rock, 1 for paper or 2 for scissors0

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

Computer chose:

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

Its a draw!,Try again
