import random
import time

# Function to display the numbers with a delay and color
def display_lottery_numbers():
    print("Generating your PowerBall numbers...")
    
    # Generate and print the first five numbers with a delay
    white_balls = [random.randint(1, 69) for _ in range(5)]
    for i in range(5):
        print(f"{white_balls[i]}", end="  ", flush=True)
        time.sleep(0.25)
        
    # Generate and print the last number in red with a delay
    red_ball = random.randint(1, 26)
    print(f"\033[91m{red_ball}\033[0m") # ANSI escape code for red color
    time.sleep(0.25)

# Main part of the script
def main():
    # Get the user's name
    varUserName = input("Hello! What's your name? ")

    # Greet the user
    print(f"Hi, {varUserName}! Let's generate some PowerBall numbers for you.")

    # Display the numbers
    display_lottery_numbers()

    # Farewell message
    print("Good luck! Hope you win big!")

if __name__ == "__main__":
    main()