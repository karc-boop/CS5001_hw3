'''
Name: Jiawen Cai
Class: CS5001
This is for #3 Programming in HW3: Booleans, Decision Making & Repetition
'''
import random

def get_player(num):
    """
    Get the name of a Pokemon for a player based on a given number.

    Args:
        num (int): A number used to determine the player's Pokemon.

    Returns:
        str: The name of the player's Pokemon.
    """
    player_name = ""
    pokemon_list = [
        "Bulbasaur", "Charmander", "Butterfree", "Rattata", "Weedle",
        "Pikachu", "Sandslash", "Jigglypuff", "Raichu", "Diglett"
    ]
    default_pokemon = "Diglett"
    player_name = " "

    # Check if the number is within the valid range
    if 1 <= num <= len(pokemon_list):
        player_name =  pokemon_list[num - 1]
    else:
        player_name =  default_pokemon

    return player_name
    
color_option = input("What team do you want? red or blue")

def check_battle():
    """
    Simulate a battle between the player and the computer.

    Returns:
        str: The winner of a single game, either "player" or "computer."
    """

    PRS = ["Rock", "Paper", "Scissor"]

    num1 = random.randint(0,99)
    num2 = random.randint(0,99)
    player_name = get_player(num1)
    computer_name = get_player(num2)
    computer_color = " "

    player_choice = int(input\
                        ("Enter 1 for Rock, 2 for Paper, 3 for Scissors."))
    computer_choice = random.randint(1, 3)

    if color_option.lower() == "red":
        computer_color == "blue"
        print(f"RED pokemon {player_name} vs BLUE pokemon {computer_name}")
    else:
        computer_color == "red"
        print(f"BLUE pokemon {player_name} vs RED pokemon {computer_name}")
        

    print(f"{player_name} played {PRS[player_choice-1]},\
            {computer_name} played {PRS[computer_choice-1]}")

    if player_choice == computer_choice:    
        print("It's a draw, no winner.")

    elif (
        (player_choice == 2 and computer_choice == 1) or
        (player_choice == 3 and computer_choice == 2) or
        (player_choice == 1 and computer_choice == 3)

    ):
        print(f"Your {color_option} team wins with {player_name}!")
        return "player"

    else:
        opposite_color = "red" if color_option.lower() == "blue" else "blue"
        print(f"Your {opposite_color} team loses with {player_name}...")
        return "computer"

red_points = 0
blue_points = 0
player_wins = 0
computer_wins = 0

#Use a while loop to simulate a tournament that will not end until the user ends
while True:
    winner = check_battle()
    if winner == "player":
        player_wins+= 1
    else: computer_wins += 1

    if_game_continues = input("Play agian?(y/n)")
    if if_game_continues == "n":
        break

print("Tournament has ended!")
if player_wins > computer_wins:
    print(f"You got {player_wins} scores. \
          Your opoonent got {computer_wins} scores.\
        \n Congratulations! The {color_option} team that you lead won!")
elif player_wins < computer_wins:
    print(f"You got {player_wins} scores. \
          Your opoonent got {computer_wins} scores.\
          The {color_option} team that you lead lost... \
        \n Try it again?")
else:
    print(f"You got {player_wins} scores. \
          Your opoonent got {computer_wins} scores.\
          \n It is a draw game!")