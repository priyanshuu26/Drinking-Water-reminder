import time

def remind_to_drink_water(interval, duration):
    num_reminders = duration // interval
    for i in range(num_reminders):
        time.sleep(interval * 60)  # Convert minutes to seconds
        print("Reminder: Drink water!")

interval = int(input("Enter the interval in minutes: "))
duration = int(input("Enter the duration in minutes: "))

remind_to_drink_water(interval, duration)
