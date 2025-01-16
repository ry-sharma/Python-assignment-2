import os
import pandas as pd

# Month names mapped to their respective numbers
month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def calculate_seasonal_average(temp_folder, output_file):
    # Dictionary to store seasonal data
    seasons = {
        "Summer": [12, 1, 2],
        "Autumn": [3, 4, 5],
        "Winter": [6, 7, 8],
        "Spring": [9, 10, 11]
    }
    seasonal_data = {season: [] for season in seasons}


    # Iterate through CSV files in the folder
    for file_name in os.listdir(temp_folder):
        if file_name.endswith(".csv"):
            file_path = os.path.join(temp_folder, file_name)
            data = pd.read_csv(file_path)

            # Ensure the CSV file contains the expected columns
            if all(month in data.columns for month in month_names):
                for season, months in seasons.items():
                    for month in months:
                        # Get all temperatures for the current month
                        month_name = month_names[month - 1]
                        monthly_temps = data[month_name]

                        # Add to the seasonal data
                        seasonal_data[season].extend(monthly_temps.dropna().tolist())

    # Calculate average for each season
    seasonal_averages = {}
    for season, temps in seasonal_data.items():
        if temps:
            seasonal_averages[season] = sum(temps) / len(temps)
        else:
            seasonal_averages[season] = None

    # Save the results to the output file
    with open(output_file, "w") as f:
        f.write("Season,Average Temperature\n")
        for season, avg_temp in seasonal_averages.items():
            f.write(f"{season},{avg_temp if avg_temp is not None else 'No Data'}\n")

def find_largest_temp_range(temp_folder, output_file):
    station_ranges = {}

    # Iterate through CSV files in the folder
    for file_name in os.listdir(temp_folder):
        if file_name.endswith(".csv"):
            file_path = os.path.join(temp_folder, file_name)
            data = pd.read_csv(file_path)

            # Ensure the CSV file contains the expected columns
            if "STATION_NAME" in data.columns and all(month in data.columns for month in month_names):
                for _, row in data.iterrows():
                    station_name = row["STATION_NAME"]
                    temperatures = row[month_names].dropna().values

                    if len(temperatures) > 0:
                        temp_range = max(temperatures) - min(temperatures)
                        station_ranges[station_name] = temp_range

    # Find the station(s) with the largest range
    max_range = max(station_ranges.values())
    largest_range_stations = [station for station, temp_range in station_ranges.items() if temp_range == max_range]

    # Save the results to the output file
    with open(output_file, "w") as f:
        f.write("Station,Temperature Range\n")
        for station in largest_range_stations:
            f.write(f"{station},{max_range}\n")

def find_warmest_and_coolest_stations(temp_folder, output_file):
    station_averages = {}

    # Iterate through CSV files in the folder
    for file_name in os.listdir(temp_folder):
        if file_name.endswith(".csv"):
            file_path = os.path.join(temp_folder, file_name)
            data = pd.read_csv(file_path)

            # Ensure the CSV file contains the expected columns
            if "STATION_NAME" in data.columns and all(month in data.columns for month in month_names):
                for _, row in data.iterrows():
                    station_name = row["STATION_NAME"]
                    temperatures = row[month_names].dropna().values

                    if len(temperatures) > 0:
                        avg_temp = sum(temperatures) / len(temperatures)
                        station_averages[station_name] = avg_temp

    # Find the warmest and coolest stations
    max_avg_temp = max(station_averages.values())
    min_avg_temp = min(station_averages.values())

    warmest_stations = [station for station, avg_temp in station_averages.items() if avg_temp == max_avg_temp]
    coolest_stations = [station for station, avg_temp in station_averages.items() if avg_temp == min_avg_temp]

    # Save the results to the output file
    with open(output_file, "w") as f:
        f.write("Category,Station,Average Temperature\n")
        for station in warmest_stations:
            f.write(f"Warmest,{station},{max_avg_temp}\n")
        for station in coolest_stations:
            f.write(f"Coolest,{station},{min_avg_temp}\n")

# Specify the folder containing temperature data and the output files
temperature_folder = "temperature_data"
seasonal_output_file = "average_temp.txt"
largest_range_output_file = "largest_temp_range_station.txt"
warmest_coolest_output_file = "warmest_and_coolest_station.txt"

# Run the functions
calculate_seasonal_average(temperature_folder, seasonal_output_file)
find_largest_temp_range(temperature_folder, largest_range_output_file)
find_warmest_and_coolest_stations(temperature_folder, warmest_coolest_output_file)

print(f"Seasonal average temperatures saved to {seasonal_output_file}.")
print(f"Largest temperature range station(s) saved to {largest_range_output_file}.")
print(f"Warmest and coolest stations saved to {warmest_coolest_output_file}.")
