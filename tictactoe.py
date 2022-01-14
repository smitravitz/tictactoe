# Written by Shane Mitravitz for SuperNOVA at Dalhousie University, 2022
# smitravitz@superstaff.ca
# www.supernova.dal.ca

import random, time

def display_board(values, choices, print_choices):
  print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
  print("Game Board")
  print("___________________")
  print("|     |     |     |")
  print("|  {}  |  {}  |  {}  |".format(values[0], values[1], values[2]))
  print("|_____|_____|_____|")
  print("|     |     |     |")
  print("|  {}  |  {}  |  {}  |".format(values[3], values[4], values[5]))
  print("|_____|_____|_____|")
  print("|     |     |     |")
  print("|  {}  |  {}  |  {}  |".format(values[6], values[7], values[8]))
  print("|_____|_____|_____|")

  if print_choices:
    print("\nChoices by Number")
    print("_____________")
    print("|_{}_|_{}_|_{}_|".format(choices[0], choices[1], choices[2]))
    print("|_{}_|_{}_|_{}_|".format(choices[3], choices[4], choices[5]))
    print("|_{}_|_{}_|_{}_|".format(choices[6], choices[7], choices[8]))

  print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")


def get_player_choice():
  global options, choices, values
  while True:
    try:
      selection = int(input("Your move!!! Choose from the \"Choices by Number\" table: "))
      assert(selection in options)
      options.remove(selection)
      choices[selection-1] = " "
      values[selection-1] = "X"
      break
    except ValueError:
      print("Please select a whole number from {}".format(options))
    except AssertionError:
      print("Please ensure that your input is a number from {}".format(options))


def get_computer_choice():
  global options, choices, values
  selection = int(random.choice(options))
  options.remove(selection)
  choices[selection-1] = " "
  values[selection-1] = "O"
  

def check_if_draw():
  global options
  if len(options) == 0:
    print("It's a draw!!")
    print("Thanks for playing!!!\n")
    return True


def check_win_condition():
  global values

  # Board coordinates
  # 1  2  3
  # 4  5  6
  # 7  8  9

  # Board coordinate variables
  # top_left	top_mid		top_right
  # mid_left	mid_mid		mid_right
  # bot_left	bot_mid		bot_right

  # 3 checks for horizontals.   [1-2-3] + [4-5-6] + [7-8-9]
  # 3 checks for verticals.     [1-4-7] + [2-5-8] + [3-6-9]
  # 2 checks for diagonals.     [1-5-9] + [3-5-7]

  # 3+3+2 = 8 total checks to confirm or deny there is a winner

  top_left =  str(values[0])
  top_mid =   str(values[1])
  top_right = str(values[2])

  mid_left =  str(values[3])
  mid_mid =   str(values[4])
  mid_right = str(values[5])

  bot_left =  str(values[6])
  bot_mid =   str(values[7])
  bot_right = str(values[8])

  if top_left != " ":
    # if [1-2-3] or [1-4-7] or [1-5-9]
    if (top_left == top_mid and top_left == top_right) or (top_left == mid_left and top_left == bot_left) or (top_left == mid_mid and top_left == bot_right):
      declare_winner(top_left)
      return True

  if mid_mid != " ":
    # if [2-5-8] or [4-5-6] or [3-5-7]
    if (top_mid == mid_mid and top_mid == bot_mid) or (mid_left == mid_mid and mid_left == mid_right) or (top_right == mid_mid and top_right == bot_left):
      declare_winner(mid_mid)
      return True

  if bot_right != " ":
    # if [7-8-9] or [3-6-9]
    if (bot_right == bot_mid and bot_right == bot_left) or (bot_right == mid_right and bot_right == top_right):
      declare_winner(bot_right)
      return True

  return False


def declare_winner(winner):
  global values, choices

  if winner == "X":
    print("Player, YOU WIN!")
  elif winner == "O":
    print("Nooo! The robot menace wins... This time!")
  print("Thanks for playing!!!\n")
  
  # Note that exit(0) command will work normally, but in colab we need this:
  return True
  

def check_game_over():
  return check_win_condition() or check_if_draw()


def main():
  global values, choices, options

  while True:
    #print("options: {}\nchoices: {}\nvalues: {}".format(options, choices, values))

    # Get Player Choice
    display_board(values, choices, 1)
    get_player_choice()
    display_board(values, choices, 0)
    if check_game_over():
      return

    # Get Computer Choice
    print("The computer says: Nice move, but now it's MY TURN!\n")
    time.sleep(3)
    get_computer_choice()
    display_board(values, choices, 0)
    if check_game_over():
      return


values = [" "] * 9
choices = list(range(1,10))
options = choices.copy()

main()
