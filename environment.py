import time  
import random  
import math  
import sys  

def get_season_temperature_range(season):
    """Return the base temperature range for each season."""
    season = season.lower()
    if season in ["winter", "1"]:
        return (-5, 10)  # Winter temperatures  
    elif season in ["spring", "2"]:
        return (10, 20)  # Spring temperatures  
    elif season in ["summer", "3"]:
        return (20, 35)  # Summer temperatures   
    elif season in ["autumn", "fall", "4"]:
        return (10, 20)  # Autumn temperatures   
    else:
        raise ValueError("Invalid season. Please use: winter, spring, summer, autumn (or 1, 2, 3, 4).")

def simulate_temperature(season):
    """Simulate temperature variations for a full day based on the season."""
    base_temp_range = get_season_temperature_range(season)
    base_temp_start = random.uniform(*base_temp_range)
    daily_temps = []

    # Simulate temperature variation based on a sine wave for a full day (24 hours)
    for i in range(48):  # 48 slices for 30-minute intervals  
        # Calculate the time in the day (0 to 24 hours)
        time_of_day = (i / 48) * (2 * math.pi)  # Convert to radians for sine function (amplitude)

        # Sine wave to simulate daily temperature variations  
        variation = 5 * math.sin(time_of_day)  # Amplitude of 5 degrees  
        current_temp = base_temp_start + variation + random.uniform(-1, 1)  # Small random variation  
        daily_temps.append(round(current_temp, 2))
        
        # Actual temperature
        print(f"{current_temp:.2f}")  # print temperature
        
    return daily_temps  

def main():
    if len(sys.argv) != 2:
        print("Usage: python environment.py <season>")
        return
    
    season = sys.argv[1]
    try:
        simulate_temperature(season)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()