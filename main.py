import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

draw = '''
     _                    
    | |                   
  __| |_ __ __ ___      __
 / _` | '__/ _` \ \ /\ / /
| (_| | | | (_| |\ V  V / 
 \__,_|_|  \__,_| \_/\_/  
'''

#Write your code below this line 👇
print("Unraveling the World of Rock Paper Scissors (RPS)")
print("Chose rock or paper or scissors as input.")

choice_list = ["rock", "paper", "scissors"]
computer_choice = random.choice(choice_list)

human_choice = input("Your Choice: ").lower()

if human_choice == "rock":
  if computer_choice == "rock":
    print("You Chose:")
    print(rock)
    print("Computer chose:")
    print(rock)
    print("Draw.")
    print(draw)
  elif computer_choice == "paper":
    print("You Chose:")
    print(rock)
    print("Computer chose:")
    print(paper)
    print("You lose.")
  else:
    print("You Chose:")
    print(rock)
    print("Computer chose:")
    print(scissors)
    print("You Win!")
elif human_choice == "paper":
  if computer_choice == "rock":
    print("You Chose:")
    print(paper)
    print("Computer chose:")
    print(rock)
    print("You win!")
  elif computer_choice == "paper":
    print("You Chose:")
    print(paper)
    print("Computer chose:")
    print(paper)
    print("Draw.")
    print(draw)
  else:
    print("You Chose:")
    print(paper)
    print("Computer chose:")
    print(scissors)
    print("You lose.")
elif human_choice == "scissors":
  if computer_choice == "rock":
    print("You Chose:")
    print(scissors)
    print("Computer chose:")
    print(rock)
    print("You lose.")
  elif computer_choice == "paper":
    print("You Chose:")
    print(scissors)
    print("Computer chose:")
    print(paper)
    print("You win.")
  else:
    print("You Chose:")
    print(scissors)
    print("Computer chose:")
    print(scissors)
    print("Draw.")
    print(draw)
else:
  print("invalid Input.")