from random import randint

options = ['Rock', 'Paper', 'Scissors']
winnerMap = {"00" : -1, "01" : 1, "02": 0, "10": 1, "11": -1, "12": 2, "20": 0, "21": 2, "22": -1}

player = ""

while len(player) < 1:
  computer = options[randint(0,2)]
  player = input("Rock, Paper or Scissors?: ")
  if player == "q": break
  if player not in options:
    print("check your input...")
    player = ""
    continue
  
  p = options.index(player)
  c = options.index(computer)
  key = str(p)+str(c)
  val = winnerMap[key]
  if val == -1:
    print("Tie!")
  elif val == p:
    print("You win!")
  else:
    print("You lose! :(")
  
  player = ""

