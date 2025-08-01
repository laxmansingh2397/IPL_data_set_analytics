"""
This module analyzes IPL cricket data to calculate and plot
the top ten economic bowlers in 2015.

It reads data from the 'matches.csv' and 'deliveries.csv' files,
filters matches from 2015, computes top 10 economical bowlers by each
bowling team, and displays the result as a bar chart.
"""

import csv
import matplotlib
import matplotlib.pyplot as plt

# Set backend immediately after importing matplotlib
matplotlib.use('TkAgg')


def calculate_top_ten_economic_bowler_in_2015():
    """
    Calculates the top 10 most economical bowlers in the IPL 2015 season.

    This function reads match data from 'matches.csv' and delivery data from 'deliveries.csv',
    filters matches from the 2015 season, calculates the economy rate for each bowler based on
    legal deliveries and runs conceded (excluding byes and leg byes), and returns a dictionary
    of the top 10 bowlers with the lowest economy rates.

    Returns:
        dict: A dictionary where keys are bowler names and values are their economy rates,
              sorted in ascending order of economy.
    """
    match_ids_2015 = set()
    runs_conceded = {}
    legal_deliveries = {}

    with open("../required_data/matches.csv", encoding="utf-8") as match_file:
        matches_data = csv.DictReader(match_file)

        for matches in matches_data:
            year = matches["season"]
            ids = matches["id"]

            if year == "2015":
                match_ids_2015.add(ids)

    with open("../required_data/deliveries.csv", encoding="utf-8") as delivery_file:
        delivery_data = csv.DictReader(delivery_file)

        for delivery in delivery_data:
            if delivery["match_id"] not in match_ids_2015:
                continue

            bowler = delivery["bowler"]
            total_runs = int(delivery["total_runs"])
            bye_runs = int(delivery["bye_runs"])
            legbye_runs = int(delivery["legbye_runs"])
            wide_runs = int(delivery["wide_runs"])
            noball_runs = int(delivery["noball_runs"])

            runs = total_runs - bye_runs - legbye_runs
            runs_conceded[bowler] = runs_conceded.get(bowler, 0) + runs

            if wide_runs == 0 and noball_runs == 0:
                legal_deliveries[bowler] = legal_deliveries.get(bowler, 0) + 1

    economy_rate = {}

    for bowler, runs in runs_conceded.items():
        balls = legal_deliveries.get(bowler, 0)
        if balls >= 6:
            overs = balls / 6
            economy = runs / overs
            economy_rate[bowler] = round(economy, 2)


    sorted_top_ten_economical_bowler_in_2015 = dict(
        sorted(economy_rate.items(), key=lambda x: x[1])[:10])

    return sorted_top_ten_economical_bowler_in_2015


def plot_top_ten_economic_bowler_in_2015(top_ten_economical_bowler):
    """
    Plots a bar chart of the top 10 most economical bowlers in the IPL 2015 season.

    This function uses Matplotlib to generate a bar chart showing the economy rate
    of each bowler in the input dictionary.

    Args:
        top_ten_economical_bowler (dict): A dictionary with bowler names as keys and
                                          economy rates as values.
    """
    plt.figure(figsize=(14, 6))
    plt.title("Top_10_Economical_Bowler_In_2015")
    plt.bar(top_ten_economical_bowler.keys(),
            top_ten_economical_bowler.values(), color="skyblue")
    plt.xlabel("Bowlers")
    plt.ylabel("Economic Rate")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


def execute():
    """
    Executes the full analysis and visualization pipeline.

    This function calls the function to calculate the top 10 economical bowlers
    for IPL 2015, and then plots the results using a bar chart.
    """
    top_ten_economic_bowler_in_2015 = calculate_top_ten_economic_bowler_in_2015()
    plot_top_ten_economic_bowler_in_2015(top_ten_economic_bowler_in_2015)


if __name__ == "__main__":

    execute()
