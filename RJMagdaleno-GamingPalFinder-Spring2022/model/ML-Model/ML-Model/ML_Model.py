  # Imports
import pandas as pd
pd.set_option('display.max_colwidth', 500)
import numpy as np
import matplotlib.pyplot as plt
import _pickle as pickle
import mysql.connector

try:
      # Connects python file to local database
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="gamingpalfinder_database"
    )
    mycursor = mydb.cursor()
except:
    print("Error: Could not connect to localhost database.")
    quit()

try:
      # Retrieving the numData.pkl as df
    with open("GPF_numData.pkl",'rb') as fp:
        numData = pickle.load(fp)
      # Retrieving ratings.pkl as df
    with open("GPF_ratings.pkl",'rb') as fp:
        ratings = pickle.load(fp)
except:
    print("Error: Could not locate .pkl files inside project.")
    quit()

  # Adds/Updates user id to dataset using values from phpMyAdmin 
def match(id, numData, ratings, newUserAns, numSim):
      # Favorite 3 Categories & Choices for Categories
    fc = ['C1', 'C2', 'C3']
    ansC = ['Battle Royale', 'FPS', 'Horror', 'Platformer', 'RPG', 'Sports']

      # Favorite 3 Games & Choices for Games
    fg = ['G1', 'G2', 'G3']
    ansG = ['Apex Legends', 'Fall Guys', 'Fortnite', 'Battlefield', 'Call of Duty', 'Halo', 
            'Dead Space', 'Resident Evil', 'Silent Hill', 'Crash Bandicoot', 'Shovel Knight', 'Super Mario Bros', 
            'Elder Scrolls', 'Final Fantasy', 'Fire Emblem', 'FIFA', 'Madden NFL', 'NBA 2K']

      # Dataframe of new user
    new = True;  # Bool for if id is already inside dataset
      # Loops for length of numData
    for i in numData.index:
        if(i == id):
              # If user's id is already inside dataset, update
              # values to reflect any changes 
            print("ID inside Dataframe!\n")
            newUser = pd.DataFrame([newUserAns], columns=numData.columns, index=[id])
            for c in fc:
                newUser.at[id, c] = ansC.index(newUser.at[id, c])
            for i in range (len(fg)):
                newUser.at[id, fg[i]] = ansG.index(newUser.at[id, fg[i]]) + 6

              # Updates values in numData row
            numData.loc[id] = newUser.loc[id]
            new = False;
            break;

      # If this is a new user in the dataset, create
      # a new row in dataset & fill in values
    if(new):
        print("Adding ID to Dataframe!\n")
        newUser = pd.DataFrame([newUserAns], columns=numData.columns, index=[id])

        for c in fc:
            newUser.at[id, c] = ansC.index(newUser.at[id, c])
        for i in range (len(fg)):
            newUser.at[id, fg[i]] = ansG.index(newUser.at[id, fg[i]]) + 6
        
          # Add newUser at end of numData
        #numData.append(newUser)
        numData.loc[id] = newUser.loc[id]

         # Create ratings dataset for new user with all
         # other users as "unseen"
        newRatings = pd.DataFrame(columns=ratings.columns, index=[id])
        for r in ratings.columns:
            newRatings.at[id, r] = "unseen"
        newRatings.at[id, id] = "NO"

          # Add newRatings at end of ratings for
          # both row & column
        ratings.loc[id] = newRatings.loc[id]
        ratings[id] = "unseen"
        ratings.at[id, id] = "NO"

      # Converts all newUser values to numerical
    newUser = newUser.apply(pd.to_numeric)

      # Retrievs the top numSim amount of similar users
    simUser = numData.corrwith(newUser.iloc[0],axis=1).sort_values(ascending=False)[:numSim].index
    print("List of similar users:", simUser, '\n')

      # Getting the similar users' ratings
    simRate = ratings.T[simUser]

      # Filling string values with nan for calculation
    simRate.replace("unseen", np.nan, inplace=True)
    simRate.replace("NO", np.nan, inplace=True)

      # Most compatible users according to similar users
    mostComp = simRate.mean(axis=1).sort_values(ascending=False)

      # Updates the .pkl files to reflect any new additions / changes
    with open("GPF_ratings.pkl", "wb") as fp:
        pickle.dump(ratings, fp)
    with open("GPF_numData.pkl", "wb") as fp:
        pickle.dump(numData, fp)

      # Export updated datasets as Execl files for easy viewing
    ratings.to_csv('Updated_ratings.csv',  encoding='utf-8')
    numData.to_csv('Updated_numData.csv',  encoding='utf-8')

    return mostComp

  # Error handling for uid input
def validUid(uid, tSize):
    uid = input("Enter id #: ")

      # Checks if input is integer
    while (uid.isdigit() != True):
        uid = input("Not a number, please try again: ")
    uid = abs(int(uid))  # Converts to absolute integer

      # If uid is bigger than player table, restart process inside itself
    if uid > tSize or uid == 0:
        print("id is bigger than table size", tSize, "or 0. ", end='')
        uid = validUid(1, tSize)

    return uid

try:
      # Retrieves size of player table
    sql = "SELECT COUNT(*) FROM player"
    mycursor.execute(sql)
    tSize = mycursor.fetchall()
    tSize = int(tSize[0][0])
except:
    print("Error: Could not retrieve information from 'player' table.")
    quit()

  # Variable representing a player's id
#####!!!!! ENTER NUMBER id FROM player TABLE YOU WANT TO ACCESS !!!!!#####
uid = validUid(1, tSize)

try:
      # Runs SQL code to retieve category and gamename values
      # from localhost database based on user's id
    sql = "SELECT category,gamename FROM games WHERE id IN (SELECT gameId FROM player_games WHERE userId = %s)"
    tuple = (uid,)
    mycursor.execute(sql,tuple)
    result = mycursor.fetchall()
except:
    print("Error: Could not retrive infomation from 'games' or 'player_games' table")
    quit()

#####!!!!! IF YOU WANT NEW VALUE IN DATASET, INPUT !!!!!#####
#####!!!!! NUMBER >= DATASET ROWS, ELSE ENTER 0    !!!!!#####
size = input("To not overwrite dataset values, entering your dataset's\noriginal size will insert/keep uid as a new value: ")
while size.isdigit() != True:
    size = input("Not a number. Please try again: ")
uid = uid + abs(int(size))  # Converts uid to desired dataset value

  # Inserts SQL query's results into list
newUserAns = [result[0][0], result[1][0], result[2][0], result[0][1], result[1][1], result[2][1]]
print("Values where id =", uid ,':', newUserAns, '\n')

  # Calls match function
recs = match(uid, numData, ratings, newUserAns, numSim=10)
  # Outputs top 20 amount of users
print("Most compatible users:")
print(recs[:20])