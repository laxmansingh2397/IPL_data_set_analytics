"""
This module analyzes IPL cricket data to calculate and plot
the foreign umpire analysis.

It reads data from the 'umpires.csv' file, processes the
total_umpires and displays the results in a bar chart.
"""

import csv
import matplotlib
import matplotlib.pyplot as plt

# Set backend immediately after importing matplotlib
matplotlib.use('TkAgg')


def calculate_number_of_umpires_by_country():
    """
    Reads umpire data from the 'umpires.csv' file and calculates
    the number of umpires from each country excluding India.

    Returns:
        dict: A dictionary where keys are country names (excluding India)
              and values are the count of umpires from those countries.
    """
    total_umpires = {}

    with open("../required_data/umpires.csv", encoding="utf-8") as data:
        umpires_data = csv.DictReader(data)

        for umpires in umpires_data:
            country = umpires["Country"]

            if country != "India":
                total_umpires[country] = total_umpires.get(country,0) + 1

    return total_umpires

def plot_number_of_umpires_by_country(total_umpires_data):
    """
    Plots a bar chart representing the number of umpires from each foreign country.

    Args:
        total_umpires_data (dict): A dictionary with country names as keys and 
                                   umpire counts as values.
    """
    plt.figure(figsize=(12,6))
    plt.title("Total Number Of Umpires From Country")
    plt.bar(total_umpires_data.keys(), total_umpires_data.values(), color="green")
    plt.xlabel("Country")
    plt.ylabel("Umpire Count")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

def execute():
    """
    Executes the full analysis pipeline:
    - Calculates the number of foreign umpires
    - Plots 
    """
    umpires_data_except_india = calculate_number_of_umpires_by_country()
    plot_number_of_umpires_by_country(umpires_data_except_india)


if __name__ == "__main__":

    execute()
