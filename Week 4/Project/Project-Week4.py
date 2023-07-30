"""
Weather Forecast Simulator
"""
import random
Weather_list = ["sunny", "cloudy", "rainy", "snowy"]
no_of_days = int(
    input("Please enter the number of days for the weather forecast: "))
for i in range(no_of_days):
    print("Day "+str(i+1)+": "+random.choice(Weather_list))
