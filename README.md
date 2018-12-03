# grindfest-prediction-contest-calculator
This script calculates the scores of the Grindfest prediction contest. The script assumes output from a Qualtrics survey, where there is exactly one respondent called "answer_key" that has the true results. When scoring N runners, guessing the winner earns you N points, guessing the runner-up gets you N-1 points and so on. Being close earns you points as well. When scoring N runners, if you predict that runner A takes second, but runner A wins, then you receive N-1 points. If runner A takes third, you get N-2 points. You do not receive negative points for a wildly bad prediction though. The maximum score is N*(N+1)/2 and the minimum score is zero.

## Example
Here is a sample data set with numbers replaced by letters for clarity's sake. The first value is the respondent name. The next three values are the predicted placement of the women finishers. The final values are those of the men.
```
                ┍  women  ┑    ┍ ----------- men ----------- ┑
    ['thomas', 'B', 'C', 'A', 'G', 'E', 'F', 'C', 'A', 'D', 'B']
     ['jerry', 'C', 'A', 'B', 'G', 'D', 'A', 'C', 'E', 'F', 'B']
['answer_key', 'A', 'C', 'B', 'F', 'E', 'B', 'C', 'D', 'G', 'A']
```
### Women's Scoring (number of places scored = 3)
```
Women's Results
['answer_key', 6]
['jerry', 4]
['thomas', 3]
```
The answer key shows the maximum score possible (3*(3+1)/2=6).

Jerry gets two points for his prediction for runner 'A' being off by only one position (3-1=2). Jerry also gets one point for his prediction for runner 'C' being off by only 1 position (2-1=1). His last point comes from correctly predicting the position of runner 'B' (1-0=1).

Thomas gets one point for his prediction for runner 'A' being off by two positions (3-2=1). Thomas gets two points for his correct prediction of runner 'C' coming in second (2-0=0). Thomas gets zero points for his prediction of runner 'B' (1-2=less than zero).

### Men's Scoring (number of places scored = 4)
```
Men's Results
['answer_key', 10]
['thomas', 6]
['jerry', 1]
```
The answer key shows the maximum score possible (4*(4+1)/2=10).

Thomas earns two points for his prediction for runner 'F' being off by two positions (4-2=2). He also earns three and one point respectively for correctly guessing the positions of runners 'E' (3-0=3) and 'C' (1-0=1).

Jerry's lone point comes from correctly predicting the position of runner 'C' (1-0=1). All other predictions are too far from the actual results to earn him points.
