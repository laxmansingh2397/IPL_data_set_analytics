"""
This module analyzes IPL cricket data to calculate and plot
the total matches played per year by each team.

It reads data from the 'matches.csv' file, processes the
total runs for each team, and displays the results in a bar chart.
"""

import csv
import matplotlib
import matplotlib.pyplot as plt

# Set backend immediately after importing matplotlib
matplotlib.use('TkAgg')


def calculate_total_matches_played():
    """
    Calculates the total number of IPL matches played per year.

    Reads data from 'matches.csv', extracts the 'season' field from each record,
    and counts the number of matches played in each season.

    Returns:
        dict: A dictionary where the keys are years (integers) and the values are
              the total number of matches played in that year, sorted by year.
    """
    total_matches_played_per_year = {}

    with open("../required_data/matches.csv", encoding="utf-8") as data:
        matches_data = csv.DictReader(data)

        for matches in matches_data:
            year = int(matches["season"])

            total_matches_played_per_year[year] = total_matches_played_per_year.get(year,0) + 1
    sorted_total_matches_played_per_year = dict(sorted(total_matches_played_per_year.items()))
    return sorted_total_matches_played_per_year


def plot_total_matches_played(total_matches_per_year):
    """
    Plots a bar chart showing the total number of IPL matches played per year.

    Args:
        total_matches_per_year (dict): A dictionary with years as keys and the
                                       number of matches as values.
    """
    plt.figure(figsize=(14,6))
    plt.title("Total Matches Played Over The Years")
    plt.bar(total_matches_per_year.keys(), total_matches_per_year.values(), color="yellow")
    plt.xlabel("Years")
    plt.ylabel("Match count")
    years = list(total_matches_per_year.keys())
    plt.xticks(years, rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


def execute():
    """
    Executes the full analysis pipeline:
    - Calculates the number of matches played per year.
    - Plots the results in a bar chart.
    """
    total_matches_played = calculate_total_matches_played()
    plot_total_matches_played(total_matches_played)


if __name__ == "__main__":

    execute()