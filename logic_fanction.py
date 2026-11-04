from user_input import valid_team_name,valid_number,logging
from data import teams,matches


def add_team():
    is_exist = True
    team_name = ''
    team_id = ''
    while is_exist:
        team_name = valid_team_name()
        team_id = valid_number('Enter a team  id: ')
        if teams:
            is_exist = False
            for team in teams:
                if team.get('id') == team_id:
                    logging.warning('The id already exist')
                    is_exist = True
                elif team.get('name','').lower() == team_name.lower():
                    logging.warning('The name already exist')
                    is_exist = True
        else:
            is_exist = False
    team = {"id": team_id, "name": team_name, "played": 0,
    "wins": 0, "draws": 0, "losses": 0,
    "goals_for": 0, "goals_against": 0, "points": 0}
    teams.append(team)
    logging.info('The team was added successfully.')


def get_team_by_id(team_id):
    for team in teams:
        if team["id"] == team_id:
            return team
 
def show_teams():
    if not teams:
        print('The teams list is empty')
    else:
        for team in teams:
            print(f'name: {team.get('name')}\nid: {team.get('id')}\ngames: {team.get('played')}\npoints: {team.get('points')}\n\n')
            
def add_match_result():
    is_valid_id = False
    home_team_id  = ''
    away_team_id = ''
    while not is_valid_id:
        home_team_id  = valid_number('Enter home team id: ')
        away_team_id = valid_number('Enter away team id:  ')
        if home_team_id == away_team_id:
            logging.warning('Enter 2 different team IDs')
            continue

        found_home = False
        found_away  = False
        for team in teams:
            if team.get('id') == home_team_id:
                found_home = True
            if team.get('id') == away_team_id:
                found_away = True
        if not found_home:
            logging.warning('The home team not exist')
            continue
        if not found_away:
            logging.warning('The away team not exist')
            continue

        is_valid_id = True
        for mach in matches:
            teams_id = (mach['home_team_id'],mach['away_team_id'])
            if home_team_id  in teams_id and away_team_id  in teams_id:
                logging.warning('Two teams can play only once')
                is_valid_id = False
                break
    home_goals = valid_number('Enter the number of goals scored by the home team: ',alow_zero=True)
    away_goals = valid_number('Enter the number of goals scored by the away team: ',alow_zero=True)
    match = {"home_team_id": home_team_id, "away_team_id": away_team_id, "home_goals": home_goals, "away_goals": away_goals}
    matches.append(match)
    updating_teams_data(home_team_id,away_team_id,home_goals,away_goals)
    print(teams)
    logging.info('The game was successfully added')



def updating_teams_data(home_team_id, away_team_id, home_goals, away_goals):
    home_team = get_team_by_id(home_team_id)
    away_team = get_team_by_id(away_team_id)
    if not home_team or not away_team:
        return
    home_team["played"] += 1
    away_team["played"] += 1
    home_team["goals_for"] += home_goals
    home_team["goals_against"] += away_goals
    away_team["goals_for"] += away_goals
    away_team["goals_against"] += home_goals
    if home_goals > away_goals:
        home_team["wins"] += 1
        home_team["points"] += 3
        away_team["losses"] += 1
    elif away_goals > home_goals:
        away_team["wins"] += 1
        away_team["points"] += 3
        home_team["losses"] += 1
    else:
        home_team["draws"] += 1
        home_team["points"] += 1
        away_team["draws"] += 1
        away_team["points"] += 1


def sort_teams():
    return sorted(
        teams,
        key=lambda team: (
            -team["points"],
            -(team["goals_for"] - team["goals_against"]),
            -team["goals_for"],
            team["name"].lower(),
        ),
    )


def show_standings():
    if not teams:
        print("The teams list is empty")
        return

    sorted_teams = sort_teams()

    for team in sorted_teams:
        goal_diff = team["goals_for"] - team["goals_against"]
        print(f"name: {team['name']}")
        print(f"played: {team['played']}")
        print(f"wins: {team['wins']}")
        print(f"draws: {team['draws']}")
        print(f"losses: {team['losses']}")
        print(f"goals_for: {team['goals_for']}")
        print(f"goals_against: {team['goals_against']}")
        print(f"goal_diff: {goal_diff}")
        print(f"points: {team['points']}\n")

def leading_team():
    if not teams:
        print("The teams list is empty")
        return
    if not matches:
        print("No matches played yet, there is no leading team")
        return None
    sorted_teams = sort_teams()
    print( sorted_teams[0])


def best_attacking_team():
    active_teams = [team for team in teams if team["played"] > 0]
    if not active_teams:
        print("No teams have played any games yet")
        return
    best_attacking = max(active_teams, key=lambda x: x["goals_for"])
    for team in active_teams:
        if team["goals_for"] == best_attacking["goals_for"]:
            print(f"name: {team['name']}, goals for: {team['goals_for']}")


def  team_success_rate():
    for team in teams:
        if team['played'] == 0:
            print(f'name: {team['name']} No games played')
        else:
            print(f"name: {team['name']},success rate: {round(team['points']/(team['played'] * 3) * 100, 2)}%")
    
def teams_without_wins():
    active_teams = [team for team in teams if team["played"] > 0]
    found = False
    for team in active_teams:
        if team["wins"] == 0:
            print(
                f"name: {team['name']}, games: {team['played']}, points: {team['points']}"
            )
            found = True
    if not found:
        print("No teams without wins found")

def tournament_summary():
    total_teams = len(teams)
    total_matches = len(matches)
    if total_matches == 0:
        print(f"total teams: {total_teams}")
        print("total matches: 0")
        print("total goals: 0")
        print("average goals: 0")
        print("draw matches: 0")
        print("leading team: No leader")
        return
    total_goals = 0
    draw_matches = 0
    for match in matches:
        total_goals += match["home_goals"] + match["away_goals"]
        if match["home_goals"] == match["away_goals"]:
            draw_matches += 1
    avg_goals = total_goals / total_matches
    leader = leading_team()
    leader_name = leader["name"] if leader else "No leader"
    print(f"total teams: {total_teams}")
    print(f"total matches: {total_matches}")
    print(f"total goals: {total_goals}")
    print(f"average goals: {avg_goals:.2f}")
    print(f"draw matches: {draw_matches}")
    print(f"leading team: {leader_name}")

def check_championship_potential():
    if not teams:
        print("The teams list is empty")
        return
    total_teams = len(teams)
    for team in teams:
        remaining_games = (total_teams - 1) - team["played"]
        max_possible_points = team["points"] + (remaining_games * 3)
        can_win = True
        for other_team in teams:
            if other_team["id"] != team["id"]:
                if max_possible_points < other_team["points"]:
                    can_win = False
                    break
        if can_win:
            print(
                f"name: {team['name']}, max points: {max_possible_points} - Has potential to win"
            )
        else:
            print(
                f"name: {team['name']}, max points: {max_possible_points} - No chance"
            )   






            





    

        
                
            
        
        


