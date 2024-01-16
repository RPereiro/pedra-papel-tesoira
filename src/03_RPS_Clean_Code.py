import random
from enum import IntEnum

afterrock_probs = {
    'after_win':{'rock':0,'paper':0,'scissors':0},
    'after_draw':{'rock':0,'paper':0,'scissors':0},
    'after_lose':{'rock':0,'paper':0,'scissors':0}
    }
afterpaper_probs = {
    'after_win':{'rock':0,'paper':0,'scissors':0},
    'after_draw':{'rock':0,'paper':0,'scissors':0},
    'after_lose':{'rock':0,'paper':0,'scissors':0} 
    }
afterscissors_probs = {
    'after_win':{'rock':0,'paper':0,'scissors':0},
    'after_draw':{'rock':0,'paper':0,'scissors':0},
    'after_lose':{'rock':0,'paper':0,'scissors':0}
    }

last_user_actions = list()
LastGamesResults = list()

class GameAction(IntEnum):

    Rock = 0
    Paper = 1
    Scissors = 2

class game_result(str):

    Draw = 'Draw'
    Win = 'Win'
    Lose = 'Lose'


def assess_game(user_action, computer_action):

    if user_action == computer_action:
        print(f"User and computer picked {user_action.name}. Draw game!")
        GameResult = game_result.Draw

    # You picked Rock
    elif user_action == GameAction.Rock:
        if computer_action == GameAction.Scissors:
            print("Rock smashes scissors. You won!")
            GameResult = game_result.Win
        else:
            print("Paper covers rock. You lost!")
            GameResult = game_result.Lose

    # You picked Paper
    elif user_action == GameAction.Paper:
        if computer_action == GameAction.Rock:
            print("Paper covers rock. You won!")
            GameResult = game_result.Win
        else:
            print("Scissors cuts paper. You lost!")
            GameResult = game_result.Lose

    # You picked Scissors
    elif user_action == GameAction.Scissors:
        if computer_action == GameAction.Rock:
            print("Rock smashes scissors. You lost!")
            GameResult = game_result.Lose
        else:
            print("Scissors cuts paper. You won!")
            GameResult = game_result.Win

    return GameResult 

def get_computer_action():
    computer_selection = random.randint(0, len(GameAction) - 1)
    computer_action = GameAction(computer_selection)
    print(f"Computer picked {computer_action.name}.")
    return computer_action

def get_user_action():
    # Scalable to more options (beyond rock, paper and scissors...)
    game_choices = [f"{game_action.name}[{game_action.value}]" for game_action in GameAction]
    game_choices_str = ", ".join(game_choices)
    user_selection = int(input(f"\nPick a choice ({game_choices_str}): "))
    user_action = GameAction(user_selection)

    return user_action

def probabilities ():

    if LastGamesResults[0] == 'Draw':
        number_draws = number_draws + 1

        if last_user_actions[0] == 'rock':
            if last_user_actions[1] == 'rock':
                afterrock_probs['after_draw']['rock'] = afterrock_probs['after_draw']['rock'] + 1
            elif last_user_actions[1] == 'paper':
                afterrock_probs['after_draw']['paper'] = afterrock_probs['after_draw']['paper'] + 1
            elif last_user_actions[1] == 'scissors':
                afterrock_probs['after_draw']['scissors'] = afterrock_probs['after_draw']['scissors'] + 1

        elif last_user_actions[0] == 'paper':
            if last_user_actions[1] == 'rock':
                afterpaper_probs['after_draw']['rock'] = afterpaper_probs['after_draw']['rock'] + 1
            elif last_user_actions[1] == 'paper':
                afterpaper_probs['after_draw']['paper'] = afterpaper_probs['after_draw']['paper'] + 1
            elif last_user_actions[1] == 'scissors':
                afterpaper_probs['after_draw']['scissors'] = afterpaper_probs['after_draw']['scissors'] + 1

        elif last_user_actions[0] == 'scissors':
            if last_user_actions[1] == 'rock':
                afterscissors_probs['after_draw']['rock'] = afterscissors_probs['after_draw']['rock'] + 1
            elif last_user_actions[1] == 'paper':
                afterscissors_probs['after_draw']['paper'] = afterscissors_probs['after_draw']['paper'] + 1
            elif last_user_actions[1] == 'scissors':
                afterscissors_probs['after_draw']['scissors'] = afterscissors_probs['after_draw']['scissors'] + 1

    if LastGamesResults[0] == 'Win':
        number_wins = number_wins + 1

        if last_user_actions[0] == 'rock':
            if last_user_actions[1] == 'rock':
                afterrock_probs['after_win']['rock'] = afterrock_probs['after_win']['rock'] + 1
            elif last_user_actions[1] == 'paper':
                afterrock_probs['after_win']['paper'] = afterrock_probs['after_win']['paper'] + 1
            elif last_user_actions[1] == 'scissors':
                afterrock_probs['after_win']['scissors'] = afterrock_probs['after_win']['scissors'] + 1

        elif last_user_actions[0] == 'paper':
            if last_user_actions[1] == 'rock':
                afterpaper_probs['after_win']['rock'] = afterpaper_probs['after_win']['rock'] + 1
            elif last_user_actions[1] == 'paper':
                afterpaper_probs['after_win']['paper'] = afterpaper_probs['after_win']['paper'] + 1
            elif last_user_actions[1] == 'scissors':
                afterpaper_probs['after_win']['scissors'] = afterpaper_probs['after_win']['scissors'] + 1

        elif last_user_actions[0] == 'scissors':
            if last_user_actions[1] == 'rock':
                afterscissors_probs['after_win']['rock'] = afterscissors_probs['after_win']['rock'] + 1
            elif last_user_actions[1] == 'paper':
                afterscissors_probs['after_win']['paper'] = afterscissors_probs['after_win']['paper'] + 1
            elif last_user_actions[1] == 'scissors':
                afterscissors_probs['after_win']['scissors'] = afterscissors_probs['after_win']['scissors'] + 1

    if LastGamesResults[0] == 'Lose':
        number_loses = number_loses + 1
        
        if last_user_actions[0] == 'rock':
            if last_user_actions[1] == 'rock':
                afterrock_probs['after_lose']['rock'] = afterrock_probs['after_lose']['rock'] + 1
            elif last_user_actions[1] == 'paper':
                afterrock_probs['after_lose']['paper'] = afterrock_probs['after_lose']['paper'] + 1
            elif last_user_actions[1] == 'scissors':
                afterrock_probs['after_lose']['scissors'] = afterrock_probs['after_lose']['scissors'] + 1

        elif last_user_actions[0] == 'paper':
            if last_user_actions[1] == 'rock':
                afterpaper_probs['after_lose']['rock'] = afterpaper_probs['after_lose']['rock'] + 1
            elif last_user_actions[1] == 'paper':
                afterpaper_probs['after_lose']['paper'] = afterpaper_probs['after_lose']['paper'] + 1
            elif last_user_actions[1] == 'scissors':
                afterpaper_probs['after_lose']['scissors'] = afterpaper_probs['after_lose']['scissors'] + 1

        elif last_user_actions[0] == 'scissors':
            if last_user_actions[1] == 'rock':
                afterscissors_probs['after_lose']['rock'] = afterscissors_probs['after_lose']['rock'] + 1
            elif last_user_actions[1] == 'paper':
                afterscissors_probs['after_lose']['paper'] = afterscissors_probs['after_lose']['paper'] + 1
            elif last_user_actions[1] == 'scissors':
                afterscissors_probs['after_lose']['scissors'] = afterscissors_probs['after_lose']['scissors'] + 1


def play_another_round():
    another_round = input("\nAnother round? (y/n): ")
    return another_round.lower() == 'y'



def main():

    while True:
        try:
            user_action = get_user_action()
        except ValueError:
            range_str = f"[0, {len(GameAction) - 1}]"
            print(f"Invalid selection. Pick a choice in range {range_str}!")
            continue

        computer_action = get_computer_action()
        GameResult = assess_game(user_action, computer_action)
        GameResult

        LastGamesResults.append(GameResult)
        if len(LastGamesResults) == 2 :
            LastGamesResults[0] = LastGamesResults[1]
            LastGamesResults.remove(1)

        last_user_actions.append(user_action)
        if len(last_user_actions) == 2 :
            last_user_actions[0] = last_user_actions[1]
            last_user_actions.remove(1)
        
        probabilities()

        if not play_another_round():
            break


if __name__ == "__main__":
    main()


