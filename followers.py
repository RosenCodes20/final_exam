command = input()
followers_dict = {}

while command != "Log out":
    current_command = command.split(": ")
    if current_command[0] == "New follower":
        username = current_command[1]
        if username not in followers_dict:
            followers_dict[username] = {"Likes": 0, "Comments": 0}

    elif current_command[0] == "Like":
        username, count = current_command[1], int(current_command[2])
        if username not in followers_dict:
            followers_dict[username] = {"Likes": count, "Comments": 0}
        else:
            followers_dict[username]["Likes"] += count

    elif current_command[0] == "Comment":
        username = current_command[1]
        if username not in followers_dict:
            followers_dict[username] = {"Likes": 0, "Comments": 1}
        else:
            followers_dict[username]["Comments"] += 1

    elif current_command[0] == "Blocked":
        username = current_command[1]
        if username in followers_dict:
            followers_dict.pop(username)
        else:
            print(f"{username} doesn't exist.")

    command = input()

print(f"{len(followers_dict)} followers")

for name, likes_comments in followers_dict.items():
    print(f"{name}: {likes_comments['Likes'] + likes_comments['Comments']}")