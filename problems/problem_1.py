"""
This module analyzes IPL cricket data to calculate and plot
the total runs scored by each team.

It reads data from the 'deliveries.csv' file, processes the
total runs for each team, and displays the results in a bar chart.
"""

import csv
import matplotlib
import matplotlib.pyplot as plt

# Set backend immediately after importing matplotlib
matplotlib.use('TkAgg')


def calculate_total_runs_by_team():
    """
    Calculate the total runs scored by each team in the IPL based on the deliveries dataset.

    Reads data from 'deliveries.csv', and aggregates total runs for each batting team.
    Special case: normalizes 'Rising Pune Supergiants' to 'Rising Pune Supergiant'.

    Returns:
        dict: A dictionary with team names as keys and total runs as values.
    """
    total_runs_by_team = {}

    with open("../required_data/deliveries.csv", encoding="utf-8") as data:
        deliveries_data = csv.DictReader(data)

        for delivery in deliveries_data:
            batting_team = delivery["batting_team"]
            runs_scored = int(delivery["total_runs"])

            if batting_team == "Rising Pune Supergiants":
                batting_team = "Rising Pune Supergiant"

            total_runs_by_team[batting_team] = total_runs_by_team.get(batting_team,0) + runs_scored

    return total_runs_by_team


def plot_total_runs_by_team(team_runs_data):
    """
    Plot a bar chart showing total runs scored by each team.

    Args:
        team_runs_data (dict): Dictionary with team names as keys and total runs as values.

    Returns:
        None
    """
    plt.figure(figsize=(12,6))
    plt.title("Total Runs by Each Team in IPL")
    plt.bar(team_runs_data.keys(), team_runs_data.values(), color="blue")
    plt.xlabel("Teams")
    plt.ylabel("Total Runs")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


def execute():
    """
    Main function to run the analysis and visualization of IPL team total runs.

    Returns:
        None
    """
    total_runs_data = calculate_total_runs_by_team()
    plot_total_runs_by_team(total_runs_data)


if __name__ == "__main__":

    execute()
