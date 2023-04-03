def get_valid_input(prompt, input_type, valid_input, input_min, input_max):
    while True:
        user_input = input(prompt)
        try:
            user_input = input_type(user_input)
        except ValueError:
            print("Invalid Input")
            continue
        if len(valid_input) != 0:
            if user_input not in valid_input:
                print("Invalid Input")
                continue
        else:
            if user_input < input_min or user_input > input_max:
                print("Invalid Input")
                continue
        return user_input

