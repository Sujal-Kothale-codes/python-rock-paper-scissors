
# Game logic :
# you enter (rock , paper , scissor )
# computer will choose random -- import random !!

# if user_choice = computer choice = tie 
# you   computer =  win/loose
# rock - rock    = tie
# rock - paper   = loose/computer
# rock - scissor = win/you

# paper - paper   = tie
# paper - rock    = win/you
# paper - scissor = loose/computer

# scissor -scissor  = tie
# scissor - rock    = loose/computer
# scissor - paper   = win/you

# if user-choice == computer-choice ==== tie
# print tie

import random
item_choice = ["rock", "paper" , "scissor"]

user_choice=(input("enter Rock, Paper, Scissor: "))
computer_choice = random.choice(item_choice)

print("your choice :", user_choice)
print("computer choice: ",computer_choice)

if user_choice == computer_choice :
   print("tie")

#for user Rock ! 
if user_choice == "rock" and  computer_choice == "paper" :
   print("Computer Win")

elif user_choice == "rock" and computer_choice == "scissor" :
   print("You win")

#for user paper ! 

elif user_choice == "paper"  and computer_choice == "rock" :
   print("You Win")

elif user_choice == "paper" and computer_choice == "scissor" :
   print("Computer Win")

#for user scissor

elif user_choice == "scissor" and computer_choice == "rock":
   print("Computer Win")

elif user_choice=="scissor" and computer_choice == "paper":
   print("You Win")

