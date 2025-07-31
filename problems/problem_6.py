"""
This module analyzes IPL cricket data to calculate and plot
the total matches played per year by each team.

It reads data from the 'matches.csv', and deliveries.csv file processes the
number of matches won per team per year, and displays the results in a bar chart.
"""

import csv
import matplotlib
import matplotlib.pyplot as plt

# Set backend immediately after importing matplotlib
matplotlib.use('TkAgg')


def calculate_number_of_matches_won_per_team_per_year():
    """
    Calculates the number of IPL matches won per team for each year.

    Reads the 'matches.csv' file, extracts unique seasons (years),
    and counts the number of wins per team per season.

    Returns:
        tuple: A dictionary mapping each team to a list of wins per year,
               and a sorted list of years as strings.
    """
    years = []
    matches_won_per_team = {}

    with open("../required_data/matches.csv", encoding="utf-8") as match_file:
        matches_data = list(csv.DictReader(match_file))

        for match in matches_data:
            year = match["season"]
            if year not in years:
                years.append(year)

        years.sort()

        for match in matches_data:
            for team in [match["team1"], match["team2"]]:
                if team not in matches_won_per_team:
                    matches_won_per_team[team] = [0] * len(years)

        for match in matches_data:
            year = match["season"]
            winning_team = match["winner"]
            if year in years and winning_team in matches_won_per_team:
                index_year = years.index(year)
                matches_won_per_team[winning_team][index_year] += 1

    return matches_won_per_team, years


def plot_number_of_matches_won_per_team_per_year(number_of_matches_per_season,years):
    """
    Plots a bar chart showing the number of matches won per team per year.

    Args:
        number_of_matches_per_season (dict): Dictionary where keys are team names and
                                             values are lists of wins per year.
        years (list): List of seasons (years) as strings in sorted order.

    Displays:
        A matplotlib bar chart with years on the x-axis and match wins on the y-axis.
    """
    plt.figure(figsize=(16, 8))
    teams = list(number_of_matches_per_season.keys())
    bar_width = 0.08
    x = list(range(len(years)))

    # Plot bars for each team with slight offset
    for i, team in enumerate(teams):
        offsets = [val + i * bar_width for val in x]
        plt.bar(offsets, number_of_matches_per_season[team], width=bar_width, label=team)

    plt.xlabel("Year", fontsize=14)
    plt.ylabel("Matches Won", fontsize=14)
    plt.title("Number of Matches Won per Team per Year in IPL", fontsize=16)
    plt.xticks([val + bar_width * len(teams) / 2 for val in x], years, rotation=45)
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize="small", ncol=1)
    plt.tight_layout()
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.show()


def execute():
    """
    Orchestrates the data processing and plotting.

    Calls the function to calculate match wins per team per year,
    prints the result, and generates a bar chart visualization.
    """
    number_of_matches_played = calculate_number_of_matches_won_per_team_per_year()
    plot_number_of_matches_won_per_team_per_year(*number_of_matches_played)


if __name__ == "__main__":
    execute()
