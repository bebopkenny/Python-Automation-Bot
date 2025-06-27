import random
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn import linear_model

def move_to_beat(move):
  if move == 1:
    return 2
  elif move == 2:
    return 3
  else:
    return 1

# Player 1 History
history_p1 = [1, 2, 3, 1, 1, 2, 3, 2, 1, 2, 3, 3, 2, 3, 1, 2, 2, 1, 3, 2, 1, 3]

# Player 1 Machine Learning
input_p1 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
]
output_p1 = [2, 3, 1, 1]
model = svm.SVC()
model.fit(input_p1,output_p1)

# Player 1 Behavior
def getPlayer1():
  # get the last 20 moves
  data_record = [history_p1[-18], history_p1[-17], history_p1[-16], history_p1[-15], history_p1[-14], history_p1[-13], history_p1[-12], history_p1[-11], history_p1[-10], history_p1[-9], history_p1[-8], history_p1[-7], history_p1[-6], history_p1[-5], history_p1[-4], history_p1[-3], history_p1[-2], history_p1[-1]]  
  prediction = model.predict([data_record])[0] # predict the next move
  return move_to_beat(prediction)




#What can we change?
#1. The Model (SVM, Linear Regression, etc.)
#2. What the input predicts
#3. The total games we are going to analyze (3, 4, 5, etc.)

# Player 2 History
history_p2 = [1, 2, 3, 1]

# Player 2 Machine Learning
input_p2 = [
    [1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3],
    [1, 2, 3, 1]
]
output_p2 = [2, 3, 1, 1]
model2 = svm.SVC()
model2.fit(input_p2, output_p2)

# Player 2 Method
def getPlayer2():
  # get the last 4 moves
  data_record = [history_p2[-4],history_p2[-3], history_p2[-2], history_p2[-1]]  
  prediction = model2.predict([data_record])[0] # predict the next move
  return move_to_beat(prediction)

wins_player1 = 0
wins_player2 = 0
total_ties = 0

for i in range(1, 750):
  print("Game ", i)

  player1 = getPlayer1()
  player2 = getPlayer2()
  print("Player1: ", player1, " vs Player2: ", player2)

  # Check who won
  if player1 == 1 and player2 == 2:
    print("Player 2 Won!")
    wins_player2 += 1
  if player1 == 1 and player2 == 3:
    print("Player 1 Won!")
    wins_player1 += 1
  if player1 == 2 and player2 == 1:
    print("Player 1 Won!")
    wins_player1 += 1
  if player1 == 2 and player2 == 3:
    print("Player 2 Won!")
    wins_player2 += 1
  if player1 == 3 and player2 == 1:
    print("Player 2 Won!")
    wins_player2 += 1
  if player1 == 3 and player2 == 2:
    print("Player 1 Won!")
    wins_player1 += 1
  if player1 == player2:
    print("It's a tie!")
    total_ties += 1  

  print("Updating the training model ...")
  history_p1.append(player2)
  input_p1.append([history_p1[-19], history_p1[-18], history_p1[-17], history_p1[-16], history_p1[-15], history_p1[-14], history_p1[-13], history_p1[-12], history_p1[-11], history_p1[-10], history_p1[-9], history_p1[-8], history_p1[-7], history_p1[-6], history_p1[-5], history_p1[-4], history_p1[-3], history_p1[-2]])
  output_p1.append(history_p1[-1])
  model.fit(input_p1, output_p1)
  print("Finished updating the training model 1.")  

  print("Updating the training model 2...")
  history_p2.append(player1)
  input_p2.append([history_p2[-5], history_p2[-4], history_p2[-3], history_p2[-2]])
  output_p2.append(history_p2[-1])
  model2.fit(input_p2, output_p2)
  print("Finished updating the training model 2.")

print("***************************")
print("***************************")
print("***************************")
print("Player One Wins: ", wins_player1)
print("Player Two Wins: ", wins_player2)
print("Total Ties: ", total_ties)
