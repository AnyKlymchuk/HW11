"""Write a program that prompts the user to enter their age, and then displays a
message stating whether the age is even or odd. The program must provide the ability
to enter a negative number, and in this case generate an exception. The master code
should call a function that processes the information entered."""
import logging

# Configure the logging system
logging.basicConfig(filename='age.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

def check_age():
    try:
        age = int(input("Please enter your age: "))
        if age < 0:
            raise ValueError("Age cannot be negative")
        if age % 2 == 0:
            print(f"Your age, {age}, is even.")
            logging.info(f"Age entered: {age}, Even")
        else:
            print(f"Your age, {age}, is odd.")
            logging.info(f"Age entered: {age}, Odd")
    except ValueError as ve:
        print(f"Error: {ve}")
        logging.error(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    check_age()