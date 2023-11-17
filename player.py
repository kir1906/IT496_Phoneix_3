from pydantic import BaseModel

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