import random

# Get the user's name
varUserName = input("Hello! What's your name? ")

# Greet the user
print(f"Hi, {varUserName}! Let's generate some PowerBall numbers for you.")

# Generate the six random numbers
white_ball_1 = random.randint(1, 69)
white_ball_2 = random.randint(1, 69)
white_ball_3 = random.randint(1, 69)
white_ball_4 = random.randint(1, 69)
white_ball_5 = random.randint(1, 69)
red_ball = random.randint(1, 26)

# Print the generated numbers
# We convert each number to a string to easily add spaces between them.
print(f"Your PowerBall numbers are: {str(white_ball_1)}  {str(white_ball_2)}  {str(white_ball_3)}  {str(white_ball_4)}  {str(white_ball_5)}    {str(red_ball)}")

# Farewell message
print("Good luck! Hope you win big!")