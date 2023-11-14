# IT496_Phoneix_3

<h2>Task 2 Predicting the Finalist Teams and Players</h2>
<h3>Problem Description : </h3>
<p>You are required to predict the two finalist teams in the ICC Cricket World Cup 2023 and the players (11 players for each finalist team) who are likely to be part of these teams. This task involves team composition prediction.</p>
<h3>Problem 2 Predicting team composition : </h3>
<b>Dataset : </b><a href='https://www.espncricinfo.com/'>espncricinfo</a>

<b> Dataset description of Odi_bat : </b>

<ol>
<li>Runs: The total number of runs scored by the player in a particular inning.
</li>
<li>Mins (Minutes): The duration, in minutes, for which the player batted during the inning.</li>
<li>
BF (Balls Faced): The number of balls faced by the player in the inning.
</li>
  <li>
4s (Fours): The number of times the player hit the ball to the boundary, scoring four runs each time.
  </li>
  <li>
6s (Sixes): The number of times the player hit the ball over the boundary, scoring six runs each time.
  </li>
  <li>
SR (Strike Rate): The strike rate is a measure of a player's batting performance, calculated as (Runs/Balls Faced) * 100.
  </li>
  <li>
Pos (Position): The batting position of the player in the inning.
  </li>
  <li>
Dismissal: The manner in which the player got out (e.g., Caught, Bowled, LBW - Leg Before Wicket, etc.).
  </li>
  <li>
Dismissal: The manner in which the player got out (e.g., Caught, Bowled, LBW - Leg Before Wicket, etc.).
  </li>
<h2>Task 2 Predicting the Finalist Teams and Players</h2>
<h3>Problem Description : </h3>
<p>You are required to predict the two finalist teams in the ICC Cricket World Cup 2023 and the players (11 players for each finalist team) who are likely to be part of these teams. This task involves team composition prediction.</p>
<h3>Problem 2 Predicting team composition : </h3>
<b>Dataset : </b><a href='https://www.espncricinfo.com/'>espncricinfo</a>

<b> Dataset description of Odi_bat : </b>

<ol>
<li>Runs: The total number of runs scored by the player in a particular inning.
</li>
<li>Mins (Minutes): The duration, in minutes, for which the player batted during the inning.</li>
<li>
BF (Balls Faced): The number of balls faced by the player in the inning.
</li>
  <li>
4s (Fours): The number of times the player hit the ball to the boundary, scoring four runs each time.
  </li>
  <li>
6s (Sixes): The number of times the player hit the ball over the boundary, scoring six runs each time.
  </li>
  <li>
SR (Strike Rate): The strike rate is a measure of a player's batting performance, calculated as (Runs/Balls Faced) * 100.
  </li>
  <li>
Pos (Position): The batting position of the player in the inning.
  </li>
  <li>
Dismissal: The manner in which the player got out (e.g., Caught, Bowled, LBW - Leg Before Wicket, etc.).
  </li>
SR (Strike Rate): The strike rate is a measure of a player's batting performance, calculated as (Runs/Balls Faced) * 100.
  </li>
  <li>
Pos (Position): The batting position of the player in the inning.
  </li>
  <li>
Dismissal: The manner in which the player got out (e.g., Caught, Bowled, LBW - Leg Before Wicket, etc.).
  </li>
  <li>
SR (Strike Rate): The strike rate is a measure of a player's batting performance, calculated as (Runs/Balls Faced) * 100.
  </li>
  <li>
Pos (Position): The batting position of the player in the inning.
  </li>
  <li>
Dismissal: The manner in which the player got out (e.g., Caught, Bowled, LBW - Leg Before Wicket, etc.).
  </li>ner in which the player got out (e.g., Caught, Bowled, LBW - Leg Before Wicket, etc.).
  </li>
  <li>
Inns (Innings): Indicates the inning number of the match (1st inning, 2nd inning, etc.).
  </li>
  <li>
Opposition: The opposing team against which the player played the inning.
  </li>
  <li>
Ground: The cricket ground or stadium where the match took place.
  </li>
  <li>
Start Date: The date when the inning started.
  </li>
</ol>

<b> Dataset description of Odi_bow : </b>

<ol>
  <li>Overs: The number of overs bowled by the player in a particular inning. An over consists of six legal deliveries (bowled by the same bowler).</li>

<li>Mdns (Maidens): The number of maiden overs bowled by the player in the inning. A maiden over is one in which no runs are scored by the batsman.</li>

<li>Runs: The total number of runs conceded by the player in the inning.
</li>

<li>Wkts (Wickets): The number of wickets taken by the player in the inning. A wicket is a dismissal of a batsman by the bowler.</li>

<li>Econ (Economy Rate): The economy rate is a measure of a bowler's efficiency, calculated as (Runs/Overs).</li>

<li>Pos (Position): The batting position or order of the player in the team.</li>

<li>Inns (Innings): Indicates the inning number of the match (1st inning, 2nd inning, etc.).</li>

<li>Opposition: The opposing team against which the player played the inning.</li>


<li>Ground: The cricket ground or stadium where the match took place.</li>

<li>Start Date: The date when the inning started.</li>
</ol>

<b> Dataset description of Odi_f : </b>

<ol>
  <li>Dis (Dismissal): The manner in which the batsman got out, representing various modes of dismissal such as caught, bowled, lbw (leg before wicket), etc.</li>

<li>Ct (Caught): The number of times the batsman was dismissed by being caught by a fielder.</li>

<li>St (Stumped): The number of times the batsman was stumped by the wicketkeeper.</li>

<li>Ct Wk (Caught by Wicketkeeper): The number of times the batsman was caught by the wicketkeeper.</li>

<li>Ct Fi (Caught in the Field): The number of times the batsman was caught by a fielder other than the wicketkeeper.</li>

<li>Inns (Innings): Indicates the inning number of the match (1st inning, 2nd inning, etc.).</li>

<li>Opposition: The opposing team against which the batsman played the inning.</li>

<li>Ground: The cricket ground or stadium where the match took place.</li>

<li>Start Date: The date when the inning started.</li>
</ol>

<h3>Approach : </h3>
<p>We have used this four dataset for predicting 11 player. For that we have calculated 5 scores :
<ol>
  <li>Bat_score</li>
  <li>Bow_score</li>
  <li>bat_all</li>
  <li>bow_all</li>
  <li>wktkep_score</li>
</ol>


For each player using dataset 3 dataset in that we have taken 33 players of team India and South Africa. And this data set contains match wise data set of a perticular player that they played till date. And the for calculating the scores we have calculated through inning wise, Position wise, Ground wise, etc.. We have taken my factors in account for calculating the scores for more reference we have provided the link of a research paper form <a href='https://www.sciencedirect.com/journal/array'>sciencedirect</a>.
</p>

<p>Then we used dataset that contains indian and South Africa's match which contains selection status for world cup 2023 squads for india and south Africa for each match. And according to match date we have calculated the scores. Using that we have predicted the selection status. And we have predicted for worldcup final for indian and south african team. We selected as per the descending probability.</p>

<p><b>Our Results :</b>
  
<b>For indian players : </b>

<ol>
<li>Rahul</li>
<li>Shreyas</li>
<li>Shubman</li>
<li>Virat</li>
<li>Rohit</li>
<li>Suryakumar</li>
<li>Ishan</li>
<li>Jasprit</li>
<li>Kuldeep</li>
<li>Siraj</li>
<li>Shami</li>
</ol>

<br>
<b>For SA players :</b>
<br>


<ol>
<li>Quinton</li>
<li>David</li>
<li>Aiden</li>
<li>Rassie</li>
<li>Henrich</li>
<li>Temba</li>
<li>Keshav</li>
<li>Lungi</li>
<li>Tabraiz</li>
<li>Kagiso</li>
<li>Marco</li>
</ol>
</p>

<h3>Reference : </h3><p>
For Algorithms : https://www.sciencedirect.com/journal/array
</p>

<p>For dataset: https://www.espncricinfo.com/</p>
<h2> Contributors ✨ </h2>
<table>
    <tbody>
     <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/kir1906"><img src="https://avatars.githubusercontent.com/u/137956777?v=4" width="100px;" alt="kir1906"/><br /><sub><b>kir1906</b></sub></a><br /></td>                 
    </tr>
  </tbody>
</table>
