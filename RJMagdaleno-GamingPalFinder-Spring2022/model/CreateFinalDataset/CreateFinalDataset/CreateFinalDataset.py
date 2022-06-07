  # Imports
import pandas as pd
import random
import numpy as np
import _pickle as pickle

  # Datasets for users' favorite video game categories & games respectively
category = pd.DataFrame()
games= pd.DataFrame()
  # Datasets 'category' & 'games' but inserted values are integers
catgNum = pd.DataFrame()
gameNum = pd.DataFrame()

#####!!!!! MUST MANUALLY EDIT users VARIABLE FOR SIZE OF DATASETS !!!!!#####
users = 500

  # Favorite 3 Categories
fc = ['C1', 'C2', 'C3']
  # Choices for Categories ; [1, 2, 3, 4, 5, 6]
ansC = ['Battle Royale', 'FPS', 'Horror', 'Platformer', 'RPG', 'Sports']

  # Favorite 3 Games
fg = ['G1', 'G2', 'G3']
  # Choices for Games ; [1.1, 1.2, 1.3, 2.1, 2.2, 2.3, 3.1, 3.2, 3.3, 4.1, 4.2, 4.3, 5.1, 5.2, 5.3, 6.1, 6.2, 6.3]
  # List is ordered so every 3 games are respective to a category in ansC[]
ansG = ['Apex Legends', 'Fall Guys', 'Fortnite', 'Battlefield', 'Call of Duty', 'Halo', 
        'Dead Space', 'Resident Evil', 'Silent Hill', 'Crash Bandicoot', 'Shovel Knight', 'Super Mario Bros', 
        'Elder Scrolls', 'Final Fantasy', 'Fire Emblem', 'FIFA', 'Madden NFL', 'NBA 2K']


  # Initial IDs (Same values for each)
category['id'] = [i for i in range(users)]
games['id'] = category['id']
catgNum['id'] = category['id']
gameNum['id'] = category['id']

# Creating category & catgNum dataset:
  # Chooses random values from ansC[] for all user's categories
for c in fc:
    category[c] = pd.Categorical(random.choices(ansC, k=users), categories=ansC)
  # Loops for each user
for n in range(users):
      # Checks if a user n has any duplicate categories in columns fc[].
      # If duplicate found, then a new random value replaces it
    while category.at[n, fc[0]] == category.at[n, fc[1]]:
        category.at[n, fc[1]] = ansC[np.random.randint(0, len(ansC) - 1)]
    while category.at[n, fc[0]] == category.at[n, fc[2]] or category.at[n, fc[1]] == category.at[n, fc[2]]:
        category.at[n, fc[2]] = ansC[np.random.randint(0, len(ansC) - 1)]

      # Insers integer values for catgNum based on category's values
    for c in fc:
        catgNum.at[n, c] = ansC.index(category.at[n, c])
          
# Creating games & gameNum dataset:
  # Loops for length of fg[]
for i in range (len(fg)):
    for n in range(users):
          # Calculates user game value from ansG[] that relates to that game's category.
          # Ex.: If category.at[8, C1] = ansC[0], then games.at[1, G1] = ~ansC[0,1,2]
        games.at[n, fg[i]] = ansG[np.random.randint(0,3) + ( ansC.index(category.at[n, fc[i]]) * 3 )]

          # Converts game's string values to int & places inside gameNum.
          # Since #0-5 are alread taken, 6 is added to ansG.index()
        gameNum.at[n, fg[i]] = ansG.index(games.at[n, fg[i]]) + 6

  # Setting index as id
category.set_index('id', inplace=True)
games.set_index('id', inplace=True)
catgNum.set_index('id', inplace=True)
gameNum.set_index('id', inplace=True)

  # Joining category and games values together as userData (16,320 unique combinations).
userData = category.join(games)
  # Joining catgNum and gameNum together as numData
numData = catgNum.join(gameNum)


  # Creating match status between users based on userData
ratings = pd.DataFrame(index=userData.index, columns=userData.index)

  # Comparing users to each other to decide who they would like.
  # The more categories & games in common, the higher the chance
for i in ratings.columns:
    seen = 0  # Amount a single user has been seen by others 
    liked = 0
    for n in range(users):
        comp = 0  # Compatability score

          # For every category both users share, compaibility score +1
        for c in fc:
            uFc = userData.at[n, c]
            if uFc == userData.at[ratings.columns[i], fc[0]] or uFc == userData.at[ratings.columns[i], fc[1]] or uFc == userData.at[ratings.columns[i], fc[2]]:
                comp += 1

          # For every game both users share, compaibility score +2
        for g in fg:
            udFg = userData.at[n, g]
            if udFg == userData.at[ratings.columns[i], fg[0]] or udFg == userData.at[ratings.columns[i], fg[1]] or udFg == userData.at[ratings.columns[i], fg[2]]:
                comp += 2
        if comp < 2:
            ratings.at[n, i] = random.choices([0,1,"unseen"], weights=[6,1,2])[0]
        elif comp == 2:
            ratings.at[n, i] = random.choices([0,1,"unseen"], weights=[4,2,1])[0]
        elif comp == 3:
            ratings.at[n, i] = random.choices([0,1,"unseen"], weights=[3,2,1])[0]
        elif comp == 4:
            ratings.at[n, i] = random.choices([0,1,"unseen"], weights=[1,4,1])[0]
        else:
            ratings.at[n, i] = random.choices([0,1,"unseen"], weights=[1,6,1])[0]

          # Prevents user from matching with themself
        ratings.at[n, n] = "NO"

          # If user has been "seen" (0 or 1), increment seen
        if isinstance (ratings.at[n, i], int): 
            seen += 1
              # If user has been "liked", increment liked
            if ratings.at[n, i] == 1:
                liked += 1

      # Amount of times user is seen added to userData dataset
    userData.at[i, 'seen'] = seen

      # Average user was liked, on scale from 0-10, added to userData dataset
    userData.at[i, 'aveLike'] = round( (liked/seen)*10, 2)

      # Prints when current user's data has been completed
      # Only meant to guage time till completion
    print("User #", i, "complete.")

  # Exporting all datasets as .pkl files
with open("GPF_userData.pkl", "wb") as fp:
   pickle.dump(userData, fp)
with open("GPF_ratings.pkl", "wb") as fp:
    pickle.dump(ratings, fp)
with open("GPF_numData.pkl", "wb") as fp:
    pickle.dump(numData, fp)

  # Exporting all datasets as Excel files
userData.to_csv('GPF_userData.csv',  encoding='utf-8')
ratings.to_csv('GPF_ratings.csv',  encoding='utf-8')
numData.to_csv('GPF_numData.csv',  encoding='utf-8')
