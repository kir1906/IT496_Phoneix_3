import uvicorn
from fastapi import FastAPI
import numpy as np
import pickle 
import pandas as pd
from tensorflow import keras
from player import player, totalRun,mostfours
from sklearn.preprocessing import StandardScaler

app = FastAPI()

# finalists_model = keras.models.load_model('./models/Final_Model.keras')


pickle_model = open("players2.pkl", "rb")
players_model = pickle.load(pickle_model)

total_run_prediction_model = keras.models.load_model('./models/total_run_prediction.h5')
most_fours_model = keras.models.load_model('./most_fours.h5')

@app.post('/player')
def predict(data:player):
    #convert data obj to dictionary
    data=dict(data)
    Name=data['Name']
    bat_score=data['bat_score']
    bow_score=data['bow_score']
    all_bat=data['all_bat']
    all_bow=data['all_bow']
    wkt=data['wkt']
    Oppsition=data['Oppsition']
    Roll=data['Roll']
    Team=data['Team']
    prediction = players_model.predict([[Name,bat_score,bow_score,all_bat,all_bow,wkt,Oppsition,Roll,Team]])
    # prediction = players_model.predict([[-1.41234016,  0.19088097, -0.80355172,  0.17038773,  0.12463426,0.17287699, -1.03077641, -1.10049766, -1.03077641]])
    return {
        'prediction': prediction.tolist()
    }

@app.post('/totalrun')
def predict(data:totalRun):
    #convert data obj to dictionary
    data=dict(data)
    Mat=data['Mat']
    Inns=data['Inns']
    Afghanistan=data['Afghanistan']
    Australia=data['Australia']
    Bangladesh=data['Bangladesh']
    England=data['England']
    India=data['India']
    Netherlands=data['Netherlands']
    NewZealand=data['NewZealand']
    Pakistan=data['Pakistan']
    SouthAfrica=data['SouthAfrica']
    SriLanka=data['SriLanka']
    AVG_Run=data['AVG_Run']
    AVG_SR=data['AVG_SR']
    AVG_BF=data['AVG_BF']
    Player_pre=data['Player_pre']
    Team_pre=data['Team_pre']
    prediction = total_run_prediction_model.predict([[ Mat,
    Inns, 
    Afghanistan,
    Australia,
    Bangladesh,
    England,
    India,
    Netherlands,
    NewZealand,
    Pakistan,
    SouthAfrica,
    SriLanka,
    AVG_Run,
    AVG_SR,
    AVG_BF,
    Player_pre,
    Team_pre]])
   
    return {
        'prediction': prediction.tolist()
    }

@app.post('/most_fours')
def predict(data:mostfours):
    #convert data obj to dictionary
    data=dict(data)
    Mat=data['Mat']
    Inns=data['Inns']
    Afghanistan=data['Afghanistan']
    Australia=data['Australia']
    Bangladesh=data['Bangladesh']
    England=data['England']
    India=data['India']
    Netherlands=data['Netherlands']
    New_Zealand=data['New_Zealand']
    Pakistan=data['Pakistan']
    South_Africa=data['South_Africa']
    Sri_Lanka=data['Sri_Lanka']
    AVG_Run=data['AVG_Run']
    AVG_SR=data['AVG_SR']
    AVG_BF=data['AVG_BF']
    Player_pre=data['Player_pre']
    Team_pre=data['Team_pre']
    prediction = most_fours_model.predict([[ Mat,
    Inns, 
    Afghanistan,
    Australia,
    Bangladesh,
    England,
    India,
    Netherlands,
    New_Zealand,
    Pakistan,
    South_Africa,
    Sri_Lanka,
    AVG_Run,
    AVG_SR,
    AVG_BF,
    Player_pre,
    Team_pre]])
   
    return {
        'prediction': prediction.tolist()
    }

@app.get('/')
def index():
    return {'Hello, this is the project of Group 1: Team Phoenix'}

@app.get('/most-runs')
def most_runs():
    return {'Kane Williomson'}

@app.get('/most-fours')
def  most_fours():
    return {'Kane Williomson'}

@app.get ('/finalists')
async def finalists():
    
    return {'finalist_1': 'India', 'finalist_2': 'South Africa'}

@app.get('/playing-11')
async def playing_11():
    return {'India': ['KL Rahul', 'Shubhman Gil', 'Shreyes Ayer', 'Virat Kohli', 'Rohit Sharma', 'Suryakumar Yadav', 'Ishan Kishan', 'Jasprit Bumrah', 'Kuldeep Yadav', 'Mohammad Siraj', 'Mohammad Shami'],
            'South Africa': ['Quinton', 'David','Aiden', 'Rassie', 'Henrich', 'Temba', 'Keshav', 'Lungi', 'Tarbraiz', 'Kagiso', 'Marco']}


@app.get('/winner')
async def winner():
    return {'India'}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)