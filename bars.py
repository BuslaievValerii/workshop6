import plotly as py
import plotly.graph_objs as go
from plotly import tools
from dataset import get_data

dct = get_data()

games_dct = {}
for season in dct:
    teams = set()
    for home_team in dct[season]:
        if home_team not in teams:
            teams.add(home_team)
        for away_team in dct[season][home_team]:
            if away_team not in teams:
                teams.add(away_team)
    games_dct[season] = len(teams)
seasons = list(games_dct.keys())
num_of_teams = list(games_dct.values())
figure1 = go.Bar(x=seasons, y=num_of_teams, name='Num of teams in season')

team_games = {}
for season in dct:
    for home_team in dct[season]:
        if home_team not in team_games:
            team_games[home_team] = len(dct[season][home_team])
        team_games[home_team] += len(dct[season][home_team])
        for away_team in dct[season][home_team]:
            if away_team not in team_games:
                team_games[away_team] = dct[season][home_team].count(away_team)
            team_games[away_team] += dct[season][home_team].count(away_team)
teams = list(team_games.keys())
num_of_games = list(team_games.values())
figure2 = go.Bar(x=teams, y=num_of_games, name='Num of games')

fig = tools.make_subplots(rows=1, cols=2)
fig.append_trace(figure1, 1, 1)
fig.append_trace(figure2, 1, 2)
py.offline.plot(fig, filename='plots.html')
