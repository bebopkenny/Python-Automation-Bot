# ----------------------------------------------------------------
# Different ML models to try instead of SVM: 
# from sklearn.linear_model import PassiveAggressiveClassifier
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.tree import DecisionTreeClassifier
# ----------------------------------------------------------------

from sklearn import svm

#Player 1: Model
#Player 2: You

#Player 2 history
history = [1,1,3,2,1,1,1,1,1,1,1,1,1,1,1]

# ----------------------------------------------------------------
# input_data changes shape: 
# input_data = [
#   [1, 1, 1],
#   [1, 1, 2],
#   [3, 2, 1],
#   [2, 1, 3],
# ]

# output_data = [3, 2, 1, 1]
# ----------------------------------------------------------------

#Player 1 Model
input_data = [
  [1, 1],
  [1, 2],
  [3, 2],
  [2, 1],
  ]

output_data = [3, 2, 1, 1]

# ----------------------------------------------------------------
# Try out different models by changing the model value: 
# from sklearn.linear_model import PassiveAggressiveClassifier
# model = PassiveAggressiveClassifier()
# --- Or ---
# from sklearn.tree import DecisionTreeClassifier
# model = DecisionTreeClassifier()
# ----------------------------------------------------------------

model = svm.SVC()
model.fit(input_data, output_data)

def getPlayer1():
    # ----------------------------------------------------------------
    # Part 2: Use more history to predict for data_records
    # update data_records to -> data_records = [history[-3], history[-2], history[-1]]
    # ----------------------------------------------------------------
    data_record = [history[-2], history[-1]]
    current = model.predict([data_record])[0]
    if current == 1:
        return 2
    if current == 2:
        return 3
    return 1


def getPlayer2():
  user = int(input("Please enter a number: 1 for Rock, 2 for Paper, and 3 for scissors:"))
  return user

num_player_wins = 0
num_comp_wins = 0
num_ties = 0

#1,2,3,3
#1. Rock, 2. Paper, 3. Scissors
for i in range(1, 40):
  print("Game: ", i)
  comp = getPlayer1()
  user = getPlayer2()
  print("Computer: ", comp, "vs Player: ", user)

  #Rock
  if comp == 1 and user == 1:
    print("its a tie")
    num_ties += 1
  elif comp == 1 and user  == 2:
    print("You win!!")
    num_player_wins += 1
  elif comp == 1 and user == 3:
    print("You lose!!")
    num_comp_wins += 1
    
  #Paper
  elif comp == 2 and user == 2:
    print("its a tie")
    num_ties += 1
  elif comp == 2 and user  ==3:
    print("You win!!")
    num_player_wins += 1
  elif comp == 2 and user == 1:
    print("You lose!!")
    num_comp_wins += 1
    
  #Scissors
  elif comp == 3 and user == 3:
    print("its a tie")
    num_ties += 1
  elif comp == 3 and user  == 1:
    print("You win!!")
    num_player_wins += 1
  elif comp == 3 and user == 2:
    print("You lose!!")
    num_comp_wins += 1

  print("Updating the training model...")
  history.append(user)
  # ----------------------------------------------------------------
  # Update the training logic:
  # Change the input_data.append() to -> input_data.append([history[-4], history[-3], history[-2]])
  # ----------------------------------------------------------------
  input_data.append([history[-3], history[-2]])
  output_data.append(history[-1])
  model.fit(input_data,output_data)
  print("Finished updating the training model")


print("Computer: ", num_comp_wins)
print("Player: ", num_player_wins)
print("Total ties: ", num_ties)
