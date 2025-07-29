# IPL DATA Set Analytics

* This project reads IPL deliveries and matches data from a CSV file and visualizes the data with the help of matplotlib

## Prerequisites
* Python3.x installled on your system 
* pip(Python Package Manager)

## Installation

### 1. **Clone this repository with (SSH key) or (download the code files):**
```
git clone git@github.com:laxmansingh2397/ipl_data_set_analytics.git
```
### 2. **Install required packages from requirement.txt.**
```
pip freeze > requirements.txt
```
This command will install all required package you want to run this project.

This file is along with READEME.md file

### 3. **Ensure your CSV file is present correctly.**
Place the deliveries.csv and matches.csv file at the following path (or update the script with your path):
```
"../required_data/deliveries.csv"
"../required_data/matches.csv"
```
### 4. **Data file in zip form**
Please download the zip file inside the required_data file and after extract the csv file paste it inside itself.

### 5. **Output**
If you want to see the output of the result in the form of plot it is given in the output folder.

### 6. **Usage**

1. **Edit the file path(if needed):**
If your CSV file is in a different location, update the path in the script:
```
deliveries_data = csv.DictReader(open("path/to/your/deliveries.csv"))
matches_data = csv.DictReader(open("path/to/your/matches.csv"))
```

2. **Run the script:**
```
python3 your_script_name.py
```
If you are using any **IDE** you can run it from there
