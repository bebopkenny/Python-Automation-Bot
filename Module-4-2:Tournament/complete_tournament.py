import random
from sklearn import svm  # Support Vector Machine
from sklearn.ensemble import RandomForestClassifier  # Optional: Tree-based model
from sklearn.linear_model import PassiveAggressiveClassifier  # Optional: Lightweight online model
from sklearn import linear_model  # For LinearRegression if you experiment
import matplotlib.pyplot as plt  # Optional: to graph win trends

# Utility function to play the counter move
def move_to_beat(move):
  if move == 1:
    return 2  # Paper beats Rock
  elif move == 2:
    return 3  # Scissors beats Paper
  else:
    return 1  # Rock beats Scissors

# --------------------------
# Player 1 Setup
# --------------------------
# You can experiment with longer or shorter histories
history_p1 = [1, 2, 3, 1, 1, 2, 3, 2, 1, 2, 3, 3, 2, 3, 1, 2, 2, 1, 3, 2, 1, 3]

# Initial training data: 18-move patterns
input_p1 = [
    [1]*18,
    [2]*18,
    [3]*18,
    [1, 2, 3]*6
]
output_p1 = [2, 3, 1, 1]  # Just some dummy outputs to start training

# MODEL OPTIONS:
# model = svm.SVC()  # Original SVM
# model = PassiveAggressiveClassifier()  # Fast, online model
# model = RandomForestClassifier()  # Tree-based model (great for small data)
model = svm.SVC()  # <-- Change model here if experimenting
model.fit(input_p1, output_p1)

# Predict next move using Player 2's last 18 moves
def getPlayer1():
  if len(history_p1) < 18:
    return random.choice([1, 2, 3])  # Not enough history? Play randomly
  data_record = history_p1[-18:]
  prediction = model.predict([data_record])[0]
  return move_to_beat(prediction)

# --------------------------
# Player 2 Setup
# --------------------------
# Shorter memory: only uses last 4 moves to predict
history_p2 = [1, 2, 3, 1]

input_p2 = [
    [1]*4,
    [2]*4,
    [3]*4,
    [1, 2, 3, 1]
]
output_p2 = [2, 3, 1, 1]

# You can swap this model too:
# model2 = RandomForestClassifier()
# model2 = PassiveAggressiveClassifier()
model2 = svm.SVC()  # <-- Change model here if experimenting
model2.fit(input_p2, output_p2)

def getPlayer2():
  if len(history_p2) < 4:
    return random.choice([1, 2, 3])  # Not enough history
  data_record = history_p2[-4:]
  prediction = model2.predict([data_record])[0]
  return move_to_beat(prediction)

# --------------------------
# Tournament Logic
# --------------------------
wins_player1 = 0
wins_player2 = 0
total_ties = 0

# Optional: Track win trends for graphing
player1_wins_over_time = []
player2_wins_over_time = []

# Run tournament
for i in range(1, 750):
  print("Game ", i)

  player1 = getPlayer1()
  player2 = getPlayer2()
  print("Player1: ", player1, " vs Player2: ", player2)

  # Check who won
  if player1 == player2:
    print("It's a tie!")
    total_ties += 1  
  elif (player1 == 1 and player2 == 3) or (player1 == 2 and player2 == 1) or (player1 == 3 and player2 == 2):
    print("Player 1 Won!")
    wins_player1 += 1
  else:
    print("Player 2 Won!")
    wins_player2 += 1

  # Record current win count
  player1_wins_over_time.append(wins_player1)
  player2_wins_over_time.append(wins_player2)

  # --------------------------
  # Update training models
  # --------------------------
  print("Updating the training model ...")

  # Update Player 1's model with Player 2's move
  history_p1.append(player2)
  if len(history_p1) >= 19:
    input_p1.append(history_p1[-19:-1])  # last 18 moves as input
    output_p1.append(history_p1[-1])     # most recent move as output
    model.fit(input_p1, output_p1)
  print("Finished updating the training model 1.")  

  # Update Player 2's model with Player 1's move
  print("Updating the training model 2...")
  history_p2.append(player1)
  if len(history_p2) >= 5:
    input_p2.append(history_p2[-5:-1])  # last 4 moves as input
    output_p2.append(history_p2[-1])    # most recent move as output
    model2.fit(input_p2, output_p2)
  print("Finished updating the training model 2.")

# --------------------------
# Final Score Summary
# --------------------------
print("***************************")
print("***************************")
print("***************************")
print("Player One Wins: ", wins_player1)
print("Player Two Wins: ", wins_player2)
print("Total Ties: ", total_ties)

total_games = wins_player1 + wins_player2 + total_ties
print("Player 1 Win Rate: {:.2f}%".format(wins_player1 / total_games * 100))
print("Player 2 Win Rate: {:.2f}%".format(wins_player2 / total_games * 100))
print("Tie Rate: {:.2f}%".format(total_ties / total_games * 100))

if wins_player1 > wins_player2:
  print("🏆 Player 1 is the Champion!")
elif wins_player2 > wins_player1:
  print("🏆 Player 2 is the Champion!")
else:
  print("🤝 It's a tie!")

# --------------------------
# Optional: Graph Win Trends
# --------------------------
plt.plot(player1_wins_over_time, label="Player 1 Wins")
plt.plot(player2_wins_over_time, label="Player 2 Wins")
plt.xlabel("Games Played")
plt.ylabel("Wins")
plt.title("AI Tournament Progress")
plt.legend()
plt.grid(True)
plt.show()
