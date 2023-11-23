from pydantic import BaseModel, Field

class player(BaseModel):
    Name: float 
    bat_score: float 
    bow_score: float 
    all_bat: float
    all_bow: float
    wkt : float
    Oppsition : float
    Roll : float
    Team : float

class totalRun(BaseModel):
    Mat: float 
    Inns: float 
    Afghanistan: float 
    Australia: float
    Bangladesh: float
    England: float
    India: float
    Netherlands: float
    NewZealand: float 
    Pakistan: float
    SouthAfrica: float 
    SriLanka: float
    AVG_Run: float
    AVG_SR: float
    AVG_BF: float
    Player_pre: float
    Team_pre: float

class mostfours(BaseModel):
    Mat: float 
    Inns: float 
    Afghanistan: float 
    Australia: float
    Bangladesh: float
    England: float
    India: float
    Netherlands: float
    New_Zealand: float = Field(..., alias='New Zealand')
    Pakistan: float
    South_Africa: float = Field(..., alias='South Africa')
    Sri_Lanka: float = Field(..., alias='Sri Lanka')
    AVG_Run: float
    AVG_SR: float
    AVG_BF: float
    Player_pre: float
    Team_pre: float

#player
# {
#   "Name": -1.41234016,
#   "bat_score": 0.19088097,
#   "bow_score": -0.80355172,
#   "all_bat": 0.17038773,
#   "all_bow": 0.12463426,
#   "wkt": 0.17287699,
#   "Oppsition": -1.03077641,
#   "Roll": -1.10049766,
#   "Team": -1.03077641
# }

# totalrun
# {
#     "Mat": 1.95815139, 
#     "Inns": 2.44437371, 
#     "Afghanistan": 1.74507384, 
#     "Australia": 0.66948347,
#     "Bangladesh": 1.10318461,
#     "England" : 0.61029341,
#     "India" : 0,
#     "Netherlands" : 1.98640736,
#     "NewZealand": 0.71761757,
#     "Pakistan": 0.76641804, 
#     "SouthAfrica" : 0.72984558, 
#     "SriLanka" : 0.58558649,
#     "AVG_Run" : 2.10224609,
#     "AVG_SR" : 0.22749678, 
#     "AVG_BF" : 1.78218302,
#     "Player_pre"	 : 1.66242976, 
#     "Team_pre" : 1.43902213
# }

# mostfours
# {
#     "Mat": 1.95815139, 
#     "Inns": 2.44437371, 
#     "Afghanistan": 1.74507384, 
#     "Australia": 0.66948347,
#     "Bangladesh": 1.10318461,
#     "England" : 0.61029341,
#     "India" : 0,
#     "Netherlands" : 1.98640736,
#     "New Zealand": 0.71761757,
#     "Pakistan": 0.76641804, 
#     "South Africa" : 0.72984558, 
#     "Sri Lanka" : 0.58558649,
#     "AVG_Run" : 2.10224609,
#     "AVG_SR" : 0.22749678, 
#     "AVG_BF" : 1.78218302,
#     "Player_pre"	 : 1.66242976, 
#     "Team_pre" : 1.43902213
# }