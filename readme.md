# Group 1 - CP 3 (IT496)

- In this project, three tasks were assigned to the group regarding ongoing ICC CWC 2023.

1.  Prediction of the best batsman and the batsman with most fours in the tournament.
2.  Prediction of the finalists and their playing XIs.
3.  Prediction of the winner of the ICC CWC 2023.

- We've used the Deep Neural Networks to predict all of the tasks. We've also used machine learning practices to improve the performance of the model.
- We've scrapped the neccsarry data from the [ESPN](https://www.espncricinfo.com/) website.

---

- The branch [P1](https://github.com/kir1906/IT496_Phoneix_3/tree/P1) contians the code for the 1st task.
- The branch [P2](https://github.com/kir1906/IT496_Phoneix_3/tree/P2) contains the code for predicting the playing XI of the finalists.
- The branch [T2](https://github.com/kir1906/IT496_Phoneix_3/tree/T2) contains the code for the predicting the finalists and the winner of the ICC CWC 2023.

---
You can run deployed model using command  : 

```bash
python -m uvicorn main:app --reload
```

## Task 1

The data was scrapped, cleaned and preprocessed from the [ESPN](https://www.espncricinfo.com/) website.

- The data contains features such as,

  - Player Name
  - Team
  - Series
  - Date
  - Total number of matches
  - Total number of innings played by that player
  - Number of times the player was not out
  - Total number of runs scored by the player
  - Highest score of the player
  - Batting average of the player
  - Number of balls faced by the player
  - Batting strike rate of the player
  - Number of centuries scored by the player
  - Number of half centuries scored by the player
  - Number of times player scored 0 runs
  - Number of 4s scored by the player
  - Number of sixes scored by the player
  - Feature for each team indicating the number of innings played against that team
  - Batting average of the player up untill that match
  - Batting strike rate of the player up untill that match
  - Average number of bowls faced by the player up untill that match

- The training data contained instances about the performance of each player in a perticular series.

### 1. Best Batsman of the torunament

- Contributor: [Dhyey Ladani](https://github.com/dhyeyladani) & [Het Patel](https://github.com/hetpatel25)
- In this task, the best batsman of the tournament was predicted using the Deep Neural Networks.
- By using the training data, the model was trained to predict the best batsman of the tournament.
- **Results**
  1.  Kane Williomson
  2.  Virat Kohli
  3.  Dawid Malan
  4.  Aiden Markram
  5.  Mohammad Rizwan
  6.  Darly Mitchell
  7.  Fakhar Zaman
  8.  Shubman Gill
  9.  Rohit Sharma
  10. Ibrahim Zadran

### 2. Batsman with most fours in the torunament

- Contributor: [Dhyey Ladani](https://github.com/dhyeyladani) & [Het Patel](https://github.com/hetpatel25)
- In this task, the batsman with most fours in the tournament was predicted using the Deep Neural Networks.
- By using the training data, the model was trained to predict the batsman with most fours in the tournament.
- **Results**
  1.  Kane Williomson
  2.  Dawid Malan
  3.  Virat Kohli
  4.  Mohammad Rizwan
  5.  Rohit Sharma
  6.  Shubman Gill
  7.  Fakhar Zaman
  8.  Quinton de Kock
  9.  Aiden Markram
  10. David Warner

## Task 2 - Predict the finalists and their Playing XI

### 1. Predict the finalists

- Contributor: [Krish Rupapara](https://github.com/KrishRupapara) & [Utsav Maru](https://github.com/utsavmaru)
- In this task, the finalists of the tournament were predicted using the Deep Neural Networks.
- In order to predict the finalists, first of all we predicted the outcome of each and every match of the tournament.
- By using the result of those predicted matches, we predicted the semi-finalists based on the matches won by the teams.
- After that, we predicted the finalists based on the semi-finalists.
- The data contains features such as,

  - Name of 1<sup>st</sup> team
  - Name of 2<sup>nd</sup> team
  - Venue of the match (country)
  - Winner of the match
  - total matches between the two teams (from 2015 to 2023)
  - Number of matches won by 1<sup>st</sup> team
  - Number of matches won by 2<sup>nd</sup> team
  - Matches of 1<sup>st</sup> team in that venue (from 2015 to 2023)
  - Number of matches won by 1<sup>st</sup> team in that venue
  - Matches of 2<sup>nd</sup> team in that venue (from 2015 to 2023)
  - Number of matches won by 2<sup>nd</sup> team in that venue
  - Current matches played by 1<sup>st</sup> team (from 2022 to 2023)
  - Current matches won by 1<sup>st</sup> team
  - Winning performance of 1<sup>st</sup> team in current matches
  - Current matches played by 2<sup>nd</sup> team (from 2022 to 2023)
  - Current matches won by 2<sup>nd</sup> team
  - Winning performance of 2<sup>nd</sup> team in current matches
  - Win to lose ratio for 1<sup>st</sup> team
  - Win to lose ratio for 2<sup>nd</sup> team

- **Semi finalists**

  1.  India
  2.  South Africa
  3.  Australia
  4.  New Zealand

- **Finalists**
  1.  India
  2.  South Africa

### 2. Predict the playing XI of the finalists

- Contributor: [Kirtan Soni](https://github.com/kir1906)
- In this task, the playing XI of the finalists were predicted using the Deep Neural Networks.
- The data for batsman contains features such as,
  - The number of runs scored by the player
  - The total duration of player in the field
  - The number of balls faced by the player
  - The number of 4s by the player
  - The number of 6s by the player
  - Batting strike rate of the player
  - The batting position of the player in that inning
  - The manner in which player got out
  - The inning number of that match
  - The opposition team
  - The venue of the match
  - The date of the match
- The data for bowler contains features such as,
  - The number of overs by the bowler
  - Number of maiden overs bowled by the player
  - Number of runs conceded by the bowler in that inning
  - Number of wickets taken by the bowler
  - The economy rate of the bowler
  - The batting position of the bowler
  - The inning number of that match
  - The opposition team
  - The venue of the match
  - The date of the match
- The data for wicketkeeper contains features such as,
  - The manner in which player got out
  - Number of times the batsman was caught by a fielder
  - Number of times the batsman was stumped by the wicketkeeper
  - Number of times the batsman was caught by the wicketkeeper
  - Number of times the bastman was caught by the player other than the wicketkeeper
  - The inning number of that match
  - The opposition team
  - The venue of that match
  - The date of the match
- The data for the matches contains features such as,

  - Batting score of the player using a predeterimined formula
  - Bowling score of the player using a predeterimined formula
  - Batting score of the all rounder
  - Bowling score of the all rounder
  - Wicketkeeping score of the player
  - The opposition team
  - The player's role
  - The date of the match
  - The team of the player

  **Result**

  - **For India**

    1. KL Rahul
    2. Shreyas Iyer
    3. Shubhman Gill
    4. Virat Kohli
    5. Rohit Sharma
    6. Suryakumar Yadav
    7. Ishan Kishan
    8. Jasprit Bumrah
    9. Kuldeep Yadav
    10. Mohammed Siraj
    11. Mohammed Shami

  - **For South Africa**
    1. Quinton de Kock
    2. David Miller
    3. Aiden Markram
    4. Rassie van der Dussen
    5. Heinrich Klaasen
    6. Temba Bavuma
    7. Keshav Maharaj
    8. Lungi Ngidi
    9. Tabraiz Shamsi
    10. Kagiso Rabada
    11. Marco Jansen

## Task 3 - Predict the winner of the ICC CWC 2023

- Contributor: [Krish Rupapara](https://github.com/KrishRupapara) & [Utsav Maru](https://github.com/utsavmaru)
- In this task, we've used the same data as to predict the finalists of the ICC CWC 2023.
- From the previous task, we've found out the finalists of the tournament.
- By using the result of those predicted matches, we predicted the winner of the tournament based on the matches won by the teams.
- **Winner**
  - India

## Task 4 - API for the predictions

- Contributor: [Krish Rupapara](https://github.com/KrishRupapara) & [Utsav Maru](https://github.com/utsavmaru)
- In this task, we've created an API for the predictions of the tasks.
- We've used the Fast API framework to create the API.
