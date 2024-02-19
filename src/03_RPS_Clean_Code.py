import random
from enum import IntEnum

Stats = {
    'after_rock':{'Rock':[0,33.33],
                  'Paper':[0,33.33],
                  'Scissors':[0,33.33]},
                  
    'after_paper':{'Rock':[0,33.33],
                   'Paper':[0,33.33],
                   'Scissors':[0,33.33]},

    'after_scissors':{'Rock':[0,33.33],
                      'Paper':[0,33.33],
                      'Scissors':[0,33.33]},
    
    'user_record' : [],
    'total_games' : 0

    }


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


def probabilities (user_action,Stats):

    Stats['user_record'].append(user_action.name)

    if Stats['total_games'] > 0 :
        last_user_action = Stats['user_record'][Stats['total_games']-1]

        if last_user_action == 'Rock':
            Stats['after_rock'][user_action.name][0] += 1

        if last_user_action == 'Paper':
            Stats['after_paper'][user_action.name][0] += 1

        if last_user_action == 'Scissors':
            Stats['after_scissors'][user_action.name][0] += 1

    for z,i in zip(['after_rock','after_paper','after_scissors'],['Rock','Paper','Scissors']) :
        total = (sum(Stats[z][i][0] for i in Stats[z]))
        print(i,total)
        for m in ['Rock','Paper','Scissors'] :
            if total > 0:
                Stats[z][m][1] =( Stats[z][m][0]/total)*100
            print(Stats[z][m][1])

    Stats['total_games'] += 1
    print(Stats)
    



            

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
        probabilities(user_action,Stats)
        if not play_another_round():
            break


if __name__ == "__main__":
    main()


