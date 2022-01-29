import random

def player(prev_play, opponent_history=[], my_history=[], opponent_probability = [], counter = [0], my_plays = [{
              "RR": 0,
              "RP": 0,
              "RS": 0,
              "PR": 0,
              "PP": 0,
              "PS": 0,
              "SR": 0,
              "SP": 0,
              "SS": 0,
          }]):

    
    if not prev_play:
      opponent_history.clear()
      my_history.clear()


      guess = 'S'
      my_history.append(guess)
      return guess

    counter[0] += 1
    opponent_history.append(prev_play)

    guessed_opponent = guess_opponent(opponent_history, my_history, my_plays)
    opponent_probability.append(guessed_opponent)
    likely_opponent = max(set(opponent_probability), key = opponent_probability.count) if guessed_opponent != 'quincy' else guessed_opponent

    #print(f"I think im playing: {likely_opponent}")

    guess = choose_tactic(likely_opponent, opponent_history, my_history, counter, my_plays)

    my_history.append(guess)
    return guess

def guess_opponent(opponent_history, my_history, my_plays):

  ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

  opponent_history_last_ten = opponent_history[-10:] if len(opponent_history)>10 else opponent_history
  opponent_history_str = "".join(opponent_history_last_ten)
  quincy_choices = "RPPSR"

  my_last_ten = my_history[-10:]
  my_most_common = max(set(my_last_ten), key = my_last_ten.count)

  my_second_last_play = my_history[-2] if len(my_history) > 2 else None
  opp_last_play = opponent_history[-1]

  opponent_first_play = opponent_history[0]

  if quincy_choices in opponent_history_str:
    return "quincy"
  elif my_second_last_play is not None and opp_last_play == ideal_response[my_second_last_play]:
    return 'kris'
  elif opponent_history[-1] == ideal_response[my_most_common]:
    return "mrugesh"
  else:
    return "abbey"
  
def choose_tactic(opponent, opponent_history, my_history, counter, my_plays):
  ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

  if opponent == "quincy":
    response = ['P','P', 'S','S','R']
    return response[(counter[0] % len(response))-1]

  elif opponent == "mrugesh":
    my_last_ten = my_history[-10:]
    my_most_common = max(set(my_last_ten), key = my_last_ten.count)

    if not my_most_common:
      return 'P'
      
    response = ideal_response[ideal_response[my_most_common]]

    return response

  elif opponent == 'kris':
    my_last_play = my_history[-1]
    his_current_play = ideal_response[my_last_play]
    response = ideal_response[his_current_play]
    return response

  elif opponent == 'abbey':
    my_history[0] == 'R'
    my_last_play = my_history[-1]
    my_last_two = "".join(my_history[-2:])
    if len(my_last_two) == 2:
      my_plays[0][my_last_two] += 1
    
    my_potential_plays = [
      my_last_play +'R',
      my_last_play +'P',
      my_last_play +'S'
    ]

    sub_order = {
        k: my_plays[0][k]
        for k in my_potential_plays if k in my_plays[0]
    }

    abbeys_prediction = max(sub_order, key=sub_order.get)[-1:]


    response = ideal_response[ideal_response[abbeys_prediction]]
    return response