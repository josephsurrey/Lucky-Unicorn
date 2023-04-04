"""Written by Joseph Surrey, 4/04/2023

Function to get a valid input from the user.
Takes 5 input variables, prompt is what the function should prompt the user,
input_type is the type that the input should be,
valid_input is a list of valid variables (only used if there are a limited number of variables)
input_min and input_max are variables used if a valid input is in a range of numbers
"""

def get_valid_input(prompt, input_type, valid_input, input_min, input_max):
    # Loop that runs until a valid input is achieved
    while True:
        user_input = input(prompt)
        # Tries to convert input to the required data type
        try:
            user_input = input_type(user_input)
        except ValueError:
            # Print error message if input cannot be converted
            print("Invalid Input")
            continue
        # If the valid_input variable contains data check to see if the input is in the valid_input list
        if len(valid_input) != 0:
            if user_input not in valid_input:
                # Print error message if user input is not in valid_input
                print("Invalid Input")
                continue
        else:
            # Check if user input is within input_min and input_max range
            if user_input < input_min or user_input > input_max:
                # Print error message if user input is not within range
                print("Invalid Input")
                continue
        # Return user input if it is valid
        return user_input
