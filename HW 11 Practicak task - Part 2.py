"""Write a program that analyzes the entered number and, depending on the number, gives
the day of the week that corresponds to this number (1 is Monday, 2 is Tuesday, etc.). Take
into account cases of entering numbers from 8 and more, as well as cases of entering nonnumerical data."""


def get_day_of_week(number):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    try:
        day_index = int(number) - 1  # Adjust for 0-based index
        if 0 <= day_index < len(days):
            return days[day_index]
        else:
            raise ValueError("Invalid day number")
    except ValueError as e:
        return str(e)


try:
    input_number = input("Enter a number (1-7): ")
    day_of_week = get_day_of_week(input_number)
    print(f"The day of the week corresponding to {input_number} is {day_of_week}.")
except KeyboardInterrupt:
    print("\nProgram terminated by the user.")
except Exception as e:
    print(f"An error occurred: {e}")
