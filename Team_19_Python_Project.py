# Team_19_Python_Project
# Delievarble 2
# 17/05/2025

print("Welcome to LoadSheddingNoMore - your partner in efficiency!")


#Created blank schedule setup for each hour so that adjusting it can be possible later
schedule = ["-"] * 24


# Asking user to enter loadshedding stage from 1 to 6
# we must prevent value error only allowing integer inputs
def loadshedding():
        schedule[:] = ["-"] * 24                                # reset schedule first

        while True:
                s = input('Enter the loadshedding stage [1-6]:\n')
                if s.isdigit():                                         #used the letter s which will only identify as stage if it is an integer using isdigit()
                        stage = int(s)
                        if 1 <= stage <= 6:                                      #if the stage is between 1 and 6
                              break
                else:
                        print("Invalid stage. Must be an integer from 1 to 6.")

        hours_off = stage
        times = stage //2                                                #the number of time loadshedding occurs is half of stage & rounded down.
        current_hour = 0

        print (f"Stage {stage}: {hours_off}(s) & {times}(s).")  
        
        for t in range(times):
                for h in range(hours_off):
                        if current_hour < 24:
                                schedule[current_hour] = "[L]"
                                current_hour += 1
                current_hour += 1                                              # gap of 1 hour

        return stage


def record_activity():
    activity_name = input("What would you like to call the activity? ")
    try:
        duration = int(input("What is the duration of the activity in hours? "))
        start_time = int(input("What time will the activity begin? [0-23] "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    if start_time < 0 or start_time > 23:
        print("Start time must be between 0 and 23.")
        return

    if start_time + duration > 24:
        print("Note: Activity goes beyond 24 hours. Only the first part will be shown.")

    if conflict(start_time, duration):
        print()
        print("You have an activity scheduled already... Try again...")
        return 

    for i in range(start_time, min(start_time + duration, 24)):
        schedule[i] = activity_name

    print("Activity recorded...")

def view_schedule():
    print("--------Schedule for today---------\n")
    for hour in range(24):
        label = f"{hour:02d}:00 - "
        print(label + schedule[hour])

# --- Function to check if time slot is occupied or not ---
def conflict(start, duration):
    for i in range(start, min(start + duration, 24)):           #Ensure that the activity does not go beyond 24 hours
        if schedule[i] != "-":                                  #Here we are checking if the hour is already occupied
            return True
    return False



# Main_Menu---> this is to show the user the main menu and ask them to select an option
def main():
    
        loadshedding()
        
        
        while True:
                print("Please select an option: ")
                print(" 1. Record Activity")
                print(" 2. View Schedule")
                print(" 3. Exit")

                choice = input("Enter your choice (1/2/3): ")

                if choice == "1":
                        record_activity()
                elif choice == "2":
                        view_schedule()
                elif choice == "3":
                        print("Thank you for using LoadSheddingNoMore...")
                        exit()
                        break
                else:
                        print("Invalid option. Try again.")

main()


      

      




