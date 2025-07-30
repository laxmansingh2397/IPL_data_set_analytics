"""
This module analyzes IPL cricket data to calculate and plot
the extra runs conceded by each team during the 2016 season.

It reads data from the 'matches.csv' and 'deliveries.csv' files,
filters matches from 2016, computes extra runs conceded by each
bowling team, and displays the result as a bar chart.
"""

import csv
import matplotlib
import matplotlib.pyplot as plt

# Set backend immediately after importing matplotlib
matplotlib.use('TkAgg')

def calculate_extra_run_conceded_per_team_in_2016():
    """
    Calculates the total extra runs conceded by each team during the 2016 IPL season.

    This function first identifies all match IDs from the 2016 season using 'matches.csv',
    and then sums up the 'extra_runs' from 'deliveries.csv' for each bowling team
    in those matches.

    Returns:
        dict: A dictionary with team names as keys and the total extra runs conceded
              as values.
    """
    year_ids = set()
    extra_run_conceded_per_team_in_2016 = {}

    with open("../required_data/matches.csv", encoding="utf-8") as matches_file:
        matches_data = csv.DictReader(matches_file)

        for match in matches_data:
            if match["season"] == "2016":
                year_ids.add(match["id"])


    with open("../required_data/deliveries.csv", encoding="utf-8") as delivery_file:
        delivery_data = csv.DictReader(delivery_file)

        for delivery in delivery_data:
            match_id = delivery["match_id"]

            if match_id in year_ids:
                bowling_team = delivery["bowling_team"]
                extra_runs = int(delivery["extra_runs"])
                extra_run_conceded_per_team_in_2016[bowling_team] = extra_run_conceded_per_team_in_2016.get(bowling_team, 0) + extra_runs
    
    return extra_run_conceded_per_team_in_2016



def plot_extra_run_conceded_per_team_in_2016(extra_run_conceded_per_team):
    """
    Plots a bar chart of extra runs conceded by each team during the 2016 IPL season.

    Args:
        extra_run_conceded_per_team (dict): A dictionary with team names as keys and
                                            total extra runs conceded as values.
    """
    plt.figure(figsize=(14,6))
    plt.title("Extra Run Conceded Per Team In 2016")
    plt.bar(extra_run_conceded_per_team.keys(), extra_run_conceded_per_team.values(), color="pink")
    plt.xlabel("Teams")
    plt.ylabel("Total Runs Conceded")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


def execute():
    """
    Executes the full analysis pipeline:
    - Calculates the extra runs conceded per team in the 2016 season.
    - Plots the results in a bar chart.
    """
    extra_run_conceded_per_team = calculate_extra_run_conceded_per_team_in_2016()
    plot_extra_run_conceded_per_team_in_2016(extra_run_conceded_per_team)


if __name__ == "__main__":

    execute()