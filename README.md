# FUT CHAMPIONS WIN LOSS RATIO
Based on your amount of played matches and gained points, display the win loss ratio for FIFA FUT Champions

## How it works
**The program works the following:**  
The program requires Python being installed on the PC. The programm can be run simply by launching the script. The programm remains visible after the calculation until any key is pressed.

**The calculation works the following:**  
First, it is checked whether an even amount of matches has been played.  
Second, the program tries if an even amount of matches have been won and lost by multiplying one half with the amount of points one gasins by winning and multiplying the other half with 1, for the losses (or if an odd amount of matches have been played, a pessemistic approach is made and one more loss is taken).   
Third, the sum of this first try is substracted from the actual amount of points.  
Fourth, a negative outcome means that the first guess was too much and thus overestimated the amount of wins one must have had. A positive outcome means the opposite: the residuary means that there are still points that must be accounted for, one must have won more that lost. In the case the difference is 0, the guessed amount of wins and losses are equal to the points gained, so the guess is correct.  
Fifth, a new guess is made by substracting one win and adding one loss in case of a negative difference and vice versa for a positive difference.  
Sixth the process repeats until the difference is zero and thus the correct amount of wins and losses are found. A message is printed with the result.     

## Designed for
This tool is designed in March 2022 for FIFA 22. It uses the then standard variables:
<ol>
  <li> Number of maximum played matches is 20 </li>
  <li> Points awarded for a win is 4 </li>
  <li> Points awarded for a loss is 1 </li>
</ol>
