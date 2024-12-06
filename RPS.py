from collections import Counter


def player(prev_play, opponent_history=[], mine_history=[]):

  opponent_history.append(prev_play)

  if prev_play == "":
    my_choice = "P"
  else:
    if strategyRetriever(opponent_history) == 0:
      my_choice = antiQuincyStrategy()
    elif strategyRetriever(opponent_history) == 1:
      my_choice = antiAbbeyStrategy(sub_history(opponent_history,
                                                mine_history))
    elif strategyRetriever(opponent_history) == 2:
      my_choice = antiKrisStrategy(sub_history(opponent_history, mine_history))
    else:
      my_choice = antiMrugeshStrategy(
          sub_history(opponent_history, mine_history))
  mine_history.append(my_choice)
  return my_choice


def sub_history(opponent_history, mine_history):
  idx = len(opponent_history) - 1 - opponent_history[::-1].index("")
  return mine_history[idx:]


def antiQuincyStrategy(counter=[0]):
  counter[0] += 1
  choices = ["P", "P", "S", "S", "R"]
  return choices[counter[0] % len(choices)]


def antiMrugeshStrategy(opponent_history=[]):
  last_ten = opponent_history[-10:]
  most_frequent = max(set(last_ten), key=last_ten.count)

  apt_choices = {"P": "S", "R": "P", "S": "R"}
  return apt_choices[apt_choices[most_frequent]]


def antiKrisStrategy(opponent_history=[]):
  apt_choices = {"P": "S", "R": "P", "S": "R"}
  return apt_choices[apt_choices[opponent_history[-1]]]


def antiAbbeyStrategy(opponent_history=[]):
  apt_choices = {"P": "S", "R": "P", "S": "R"}
  most_frequent_choices = Counter(opponent_history).most_common(1)
  best_choice = most_frequent_choices[0][0]
  return apt_choices[best_choice]


def strategyRetriever(estimation_list):
  if estimation_list.count("") == 1:
    return 0
  elif estimation_list.count("") == 2:
    return 1
  elif estimation_list.count("") == 3:
    return 2
  else:
    return 3
