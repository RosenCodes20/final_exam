some_string = input()

command = input()
ascii_get = 0
while command != "Finish":
    current_command = command.split()
    is_invalid = False
    if current_command[0] == "Replace":
        current_char, new_char = current_command[1], current_command[2]
        some_string = some_string.replace(current_char, new_char)

    elif current_command[0] == "Cut":
        start_index, end_index = int(current_command[1]), int(current_command[2])
        if start_index in range(len(some_string)) and end_index in range(len(some_string)):
            some_string = f"{some_string[:start_index]}{some_string[end_index + 1:]}"
        else:
            is_invalid = True
            print("Invalid indices!")

    elif current_command[0] == "Make":
        upper_or_lower = current_command[1]
        if upper_or_lower == "Upper":
            some_string = some_string.upper()
        elif upper_or_lower == "Lower":
            some_string = some_string.lower()

    elif current_command[0] == "Check":
        string = current_command[1]
        if string in some_string:
            is_invalid = True
            print(f"Message contains {string}")
        else:
            is_invalid = True
            print(f"Message doesn't contain {string}")

    elif current_command[0] == "Sum":
        start_index, end_index = int(current_command[1]), int(current_command[2])
        if start_index in range(len(some_string)) and end_index in range(len(some_string)):
            for char in some_string[start_index:end_index + 1]:
                is_invalid = True
                ascii_get += ord(char)
            print(ascii_get)
        else:
            is_invalid = True
            print("Invalid indices!")
    if not is_invalid:
        print(some_string)
    command = input()
