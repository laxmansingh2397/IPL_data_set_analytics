"""
This module analyzes IPL cricket data to calculate and plot
the total matches played per year by each team.

It reads data from the 'matches.csv', and deliveries.csv file processes the
number of games played per team per year, and displays the results in a bar chart.
"""

import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Set backend immediately after importing matplotlib
matplotlib.use('TkAgg')


def calculate_number_of_games_played_by_team_per_year():

    years = []
    number_of_games_played_by_teams = {}

    with open("../required_data/matches.csv", encoding="utf-8") as matches_file:
        matches_data = list(csv.DictReader(matches_file))

        for match in matches_data:
            year = match["season"]
            if year not in years:
                years.append(year)
        years.sort()

        for match in matches_data:
            for team in [match["team1"], match["team2"]]:
                if team not in number_of_games_played_by_teams:
                    number_of_games_played_by_teams[team] = [0] * len(years)

        for match in matches_data:
            season = match["season"]
            team1 = match["team1"]
            team2 = match["team2"]

            if season in years:
                index_year = years.index(season)
                number_of_games_played_by_teams[team1][index_year] += 1
                number_of_games_played_by_teams[team2][index_year] += 1

    
    return number_of_games_played_by_teams,years


def plot_number_of_games_played_by_team_per_year(total_number_of_games_played,years):

    plt.figure(figsize=(18, 8))
    teams = list(total_number_of_games_played.keys())
    x = np.arange(len(years))  # x-axis positions (years)

    # Initialize bottom for stacking
    bottom = np.zeros(len(years))

    for team in teams:
        team_matches = total_number_of_games_played[team]
        plt.bar(x, team_matches, bottom=bottom, label=team)
        bottom += np.array(team_matches)

    # Annotate total number of matches (divide by 2 to avoid double count)
    for i, total in enumerate(bottom):
        plt.text(x[i], total + 1, f'{int(total//2)} matches', ha='center', fontsize=8, color='black')

    plt.xlabel("Year", fontsize=14)
    plt.ylabel("Number of Games Played (Per Team)", fontsize=14)
    plt.title("Number of Games Played per Team per Year (Stacked)", fontsize=16)
    plt.xticks(x, years, rotation=45)
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize="small")
    plt.tight_layout()
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.show()

def execute():

    number_of_games_played = calculate_number_of_games_played_by_team_per_year()
    print(number_of_games_played)
    plot_number_of_games_played_by_team_per_year(*number_of_games_played)


if __name__ == "__main__":

    execute()
