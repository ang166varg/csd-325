#4.2 Assignment  Angela Vargas   CSD325
import csv
from datetime import datetime
import matplotlib.pyplot as plt
import sys

def load_weather_data(filename):
    """Load dates, highs, and lows from a CSV file."""
    dates, highs, lows = [], [], []
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for row in reader:
            try:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                high = int(row[5])
                low = int(row[6])
            except ValueError:
                continue
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    return dates, highs, lows

def plot_temps(dates, temps, title, color):
    """Plot the temperatures."""
    fig, ax = plt.subplots()
    ax.plot(dates, temps, c=color)
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

def main():
    filename = 'sitka_weather_2018_simple.csv'
    dates, highs, lows = load_weather_data(filename)

    while True:
        print("\nMenu:")
        print("1. View High Temperatures")
        print("2. View Low Temperatures")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            plot_temps(dates, highs, "Daily High Temperatures - 2018", 'red')
        elif choice == '2':
            plot_temps(dates, lows, "Daily Low Temperatures - 2018", 'blue')
        elif choice == '3':
            print("Exiting the program. Stay cool!")
            sys.exit()
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
