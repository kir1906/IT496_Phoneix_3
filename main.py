import uvicorn
from fastapi import FastAPI
import numpy as np
import pickle 
import pandas as pd
from tensorflow import keras
from sklearn.preprocessing import StandardScaler

app = FastAPI()
total_run_model = keras.models.load_model('./models/total_run_prediction.h5')
most_fours_model = keras.models.load_model('./models/most_fours.h5')
finalists_model = keras.models.load_model('./models/Final_Model.keras')

pickle_model = open('./models/11players.pkl', 'rb')
players_model = pickle.load(pickle_model)


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