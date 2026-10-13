age = int(input("Enter your age: "))
heart_rate_in_beat_per_minute = 220
maximum_heart_rate = heart_rate_in_beat_per_minute  - age

minimum_percentage = 50 / 100
maximum_percentage = 85 / 100



minimum_target_rate = maximum_heart_rate * minimum_percentage 

maximum_target_rate = maximum_heart_rate * maximum_percentage



print("Maximum heart rate:", maximum_heart_rate)
print("Target heart-rate range:", minimum_target_rate, "to", maximum_target_rate)
