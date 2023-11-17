# IT496_Phoneix_3

<h2>Task 2 Predicting two specific problems related to ICC Cricket World Cup 2023.</h2>
<h3>Problem Description : </h3>
<p>Predicting the batsman who will score most runs and hit most fours in the tournament.</p>
- **Contributors**: [Dhyey Ladani](https://github.com/dhyeyladani24) & [Het Patel](https://github.com/hetpatel25)
- **Dataset**: Dataset is scrapped from the [ESPN](https://www.espncricinfo.com/) website.

<b> Dataset description of Player_ODIwise : </b>

<ol>
<li>Player: Name of the cricket player.
</li>
<li>Series: The cricket series in which the match was played.</li>
<li>date: start date of the ODI.
</li>
  <li>
Mat: Number of matches played.
  </li>
  <li>
Inns: Number of innings played.
  </li>
  <li>
NO: Number of times the player was not out (no dismissal).
  </li>
  <li>
Runs: Total runs scored by the player in the tournament.
  </li>
  <li>
HS: Highest score in a single inning.
  </li>
    <li>
Avg: Batting average, calculated as Runs/Inns.
  </li>
    <li>
BF: Number of balls faced by the player.
  </li>
    <li>
SR: Batting strike rate, calculated as (Runs/BF) * 100.
  </li>
    <li>
100: Number of centuries scored.
  </li>
   <li>
0: Number of times the player scored zero runs (duck).
  </li>
   <li>
4s: Number of fours hit.
  </li>
   <li>
6s: Number of sixes hit.
  </li>
   <li>
'Afghanistan', 'Australia', 'Bangladesh', 'England', 'India', 'Netherlands', 'New Zealand', 'Pakistan', 'South Africa', 'Sri Lanka': Columns indicating the number of innings played against each respective country in the tournament.  </li>
   <li>
AVG_Run: This column represents the average runs scored by the player until the previous ODIs played. It is calculated by averaging the 'Avg' column values until the previous ODI.  </li>
   <li>
AVG_SR: This column represents the average strike rate of the player until the previous ODIs played. It is calculated by averaging the 'SR' column values until the previous ODIs.
  </li>
   <li>
AVG_BF: This column represents the average ball faced(in percentage) by the player until the previous ODIs played.
  </li>
</ol>
  
