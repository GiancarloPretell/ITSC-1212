import csv
import random

# Function created to read and organize the info in CoromonDataset.csv
def read_data(file_name):
    coromon_data = {}
    with open(file_name, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            coromon_type = row['Type']
            if coromon_type not in coromon_data:
                coromon_data[coromon_type] = []
            coromon_data[coromon_type].append(row)
    return coromon_data

# Function to calculate averages for each type of Coromon
def calculate_averages(coromon_data):
    averages = {}
    for coromon_type, coromons in coromon_data.items():
        # Initialize a dictionary to hold total the stats for the coromon type
        total_stats = {key: 0 for key in coromons[0].keys() if key not in ['Name', 'Type']}
        count = len(coromons)

        for coromon in coromons:
            for key, value in coromon.items():
                if key not in ['Name', 'Type'] and value.replace('.','',1).isdigit():
                    total_stats[key] += float(value)

        # Calculate averages of coromon stats
        averages[coromon_type] = {stat: round(total / count, 2) for stat, total in total_stats.items()}
    return averages

# Function to find the type with highest and lowest average 
def find_extremes(averages, property_name):
    max_value = -1
    min_value = float('inf')
    max_types = []
    min_types = []
    #For loop to find min and max value of each coromon type stats
    for coromon_type, props in averages.items():
        value = props[property_name]
        if value > max_value:
            max_value = value
            max_types = [coromon_type]
        elif value == max_value:
            max_types.append(coromon_type)
        
        if value < min_value:
            min_value = value
            min_types = [coromon_type]
        elif value == min_value:
            min_types.append(coromon_type)

    return max_types, min_types

# Main function to display information
def display_information(file_name):
    coromon_data = read_data(file_name)
    averages = calculate_averages(coromon_data)

    print(f"Total number of Coromons: {sum(len(coromons) for coromons in coromon_data.values())}")
    random_type = random.choice(list(coromon_data.keys()))
    random_coromon = random.choice(coromon_data[random_type])
    print(f"Random Coromon: {random_coromon}")
    print(f"Different types of Coromons: {list(coromon_data.keys())}")

    for coromon_type, avg_values in averages.items():
        print(f"Average values for {coromon_type}: {avg_values}")

    for property_name in ['Health Points', 'Attack', 'Special Attack', 'Defense', 'Special Defense', 'Speed']:
        max_types, min_types = find_extremes(averages, property_name)
        print(f"{property_name} - Highest: {max_types}, Lowest: {min_types}")

# Run the program
display_information('CoromonDataset.csv') 