import csv
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

def calculate_total_runs_by_team():
    
    total_runs_by_team = {}

    with open("../required_data/deliveries.csv") as data:
        deliveries_data = csv.DictReader(data)

        for delivery in deliveries_data:
            batting_team = delivery["batting_team"]
            runs_scored = int(delivery["total_runs"])

            if batting_team == "Rising Pune Supergiants":
                batting_team = "Rising Pune Supergiant"

            total_runs_by_team[batting_team] = total_runs_by_team.get(batting_team,0) + runs_scored

        return total_runs_by_team
    

def plot_total_runs_by_team(team_runs_data):
    
    plt.figure(figsize=(12,6))
    plt.title("Total Runs by Each Team in IPL")
    plt.bar(team_runs_data.keys(), team_runs_data.values(), color="blue")
    plt.xlabel("Teams")
    plt.ylabel("Total Runs")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


def execute():

    total_runs_data = calculate_total_runs_by_team()
    plot_total_runs_by_team(total_runs_data)


if __name__ == "__main__":

    execute()
