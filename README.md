# Soccer Tournament Management Project in Python

In this project, I built a Python system that runs in the terminal and manages a soccer tournament.
The system saves teams, gets match results, automatically updates points and goals, and shows data and statistics about the league.

## What the system can do
* **Add team:** Adding a new team with a check that the ID and name do not already exist in the system.
* **Add match result:** Checks that both teams really exist, that they are not the same team, that goals are not negative, and that they do not play twice against each other.
* **Standings table:** Sorts all teams first by points, then by goal difference, then by goals for, and finally by team name.
* **Leading team:** Shows the team in first place, or a message that there is no leader yet if no matches were played.
* **Best attacking team:** Shows the team that scored the most goals among the teams that played at least once.
* **Team success rate:** Calculates percentage by points out of total possible points, or prints "No games" if the team did not play.
* **Teams without wins:** Shows teams that played at least one game but have zero wins.
* **Tournament summary:** Total teams, total matches, total goals, average goals per game, draw matches, and the leading team.
* **Check championship potential:** A mathematical check to see if a team still has a theoretical chance to win the tournament.
* **Error logging:** Uses the `logging` library to print warnings on invalid input or duplicate games.

## Project Structure
I divided the code into different files to keep it clean and organized:
* `main.py` - Runs the main menu in a loop and calls the right function according to user choice.
* `logic_function.py` - Contains all the functions for calculations, sorting, and updating statistics.
* `user_input.py` - Functions for taking input from the user with validations and logging.
* `data.py` - The initial mock lists of teams and matches for the tournament.

## How to run
Open the terminal in the project folder and type:
`python main.py`