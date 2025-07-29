"""
This module analyzes IPL cricket data to calculate and plot
the top ten batsman.

It reads data from the 'deliveries.csv' file, processes the
top ten batsman for RCB and displays the results in a bar chart.
"""

import csv
import matplotlib
import matplotlib.pyplot as plt

# Set backend immediately after importing matplotlib
matplotlib.use('TkAgg')

def calculate_top_ten_batsman_of_rcb():
    """
    Calculate the top ten run-scorers for Royal Challengers Bangalore (RCB)
    by reading the deliveries CSV file and summing individual batsmen's runs.

    Returns:
        dict: A dictionary of the top 10 RCB batsmen with their total runs, 
              sorted in descending order.
    """
    total_batsman_of_rcb = {}

    with open("../required_data/deliveries.csv", encoding="utf-8") as data:
        deliveries_data = csv.DictReader(data)

        for delivery in deliveries_data:
            batsman = delivery["batsman"]
            runs_scored = int(delivery["batsman_runs"])

            if delivery["batting_team"] == "Royal Challengers Bangalore":
                total_batsman_of_rcb[batsman] = total_batsman_of_rcb.get(batsman,0) + runs_scored
    sorted_top_ten_batsman = dict(
        sorted(total_batsman_of_rcb.items(),
                key=lambda x:x[1], reverse=True)[:10])


    return sorted_top_ten_batsman


def plot_top_ten_batsman_of_rcb(top_ten_batsman_data):
    """
    Plot a bar chart of the top 10 RCB batsmen based on total runs scored.

    Args:
        top_ten_batsman_data (dict): Dictionary with batsman names as keys 
                                     and total runs as values.
    """
    plt.figure(figsize=(12,6))
    plt.title("Top Ten Batsman Of Royal Challengers Bangalore")
    plt.bar(top_ten_batsman_data.keys(), top_ten_batsman_data.values(), color="blue")
    plt.xlabel("Top Ten Batsman")
    plt.ylabel("Total Runs")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


def execute():
    """
    Execute the data analysis pipeline: calculate and plot
    the top ten RCB batsmen by total runs scored.
    """
    top_ten_batsman = calculate_top_ten_batsman_of_rcb()
    plot_top_ten_batsman_of_rcb(top_ten_batsman)


if __name__ == "__main__":
    execute()
