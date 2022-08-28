# ARCL Scorecard Generator

A simple script that generates the scorecard given the ball-by-ball information of a particular player.

# Usage

`python main.py [path]`

## Arguments

-   `path`: relative path to the JSON file containing the scorecard
-   `-h`: show help message

# Formatting A Scorecard

## Formatting the ball-by-ball information

For each ball in the ball-by-ball scorecard of a particular bowler or batsman, use the following table to deduce the appropriate symbol to use.

| Condition | Symbol(s) |
| --------- | --------- |
| 0         | `.`, `0`  |
| 1         | `1`       |
| 2         | `2`       |
| 4         | `4`       |
| 5         | `5`       |
| 6         | `6`       |
| Wide      | `w`       |
| No Ball   | `n`       |
| Wicket    | `o`       |
| Bye       | `1`       |
| Run-out\* | `.`, `0`  |

\*_Note: a specific symbol for run-out still needs to be created_

Then, after finding the correct symbol for a particular delivery, merge all the symbols together into one. Some examples are shown below.

| Final String | Description                           |
| ------------ | ------------------------------------- |
| `oooooo`     | 6-wickets                             |
| `....00`     | 6 dots                                |
| `w1n66660`   | 1 wide, 1 no-ball, 4 sixes, and 1 dot |

## Formatting the final JSON File

The JSON file (containing the scorecard information) should adhere to the following format:

```json
{
    "first_innings": {
        "batting": {
            "player_name": "player_information"
        },
        "bowling": {
            "player_name": "player_information"
        }
    },
    "second_innings": {
        "batting": {
            "player_name": "player_information"
        },
        "bowling": {
            "player_name": "player_information"
        }
    }
}
```

Please consult `example.json` if you require any additional information regarding formatting.

# Sample Output

Below is the output of the program if the `example.json` file is used.

```
Batting

Name       Runs    Balls    4s    6s      SR
-------  ------  -------  ----  ----  ------
Aran          6       11     1     0   54.55
Neal         43       39     2     2  110.26
Advay        60       43     7     0  139.53
Anirudh      11        3     1     1  366.67
-----------------------------------------------------------------

Bowling

Name        Overs    No Balls    Wides    Runs    Wickets    Eco
--------  -------  ----------  -------  ------  ---------  -----
Anirudh         2           0        1      10          1   5
Thiru           2           1        2      15          0   7.5
Harshith        3           0        1      24          0   8
Abhiram         4           1        1      25          1   6.25
Krish           2           0        2      22          0  11
Shubh           2           0        0      15          0   7.5
Vishank         1           0        0      20          0  20
-----------------------------------------------------------------

Second Innings:


Batting

Name        Runs    Balls    4s    6s      SR
--------  ------  -------  ----  ----  ------
Vishank        6       10     0     0   60
Adit           0        2     0     0    0
Abhi           4        5     0     0   80
Shubh          8       10     1     0   80
Krish         11        4     1     1  275
Anirudh       21       32     2     0   65.62
Harshith      16       16     1     0  100
Thiru          0        1     0     0    0
-----------------------------------------------------------------

Bowling

Name       Overs    No Balls    Wides    Runs    Wickets    Eco
-------  -------  ----------  -------  ------  ---------  -----
Anirudh        4           4        2      25          2   6.25
Advay          4           0        2      14          2   3.5
Neal           3           1        1      13          1   4.33
Ronak          3           0        4      29          1   9.67
-----------------------------------------------------------------
```

# Todos

-   [ ] Add symbol for run-out
