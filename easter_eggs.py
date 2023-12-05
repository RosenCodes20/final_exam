import re

some_string = input()
found_eggs = r"[#@]+[a-z]{3,}[#@]+[^a-z0-9]+\d+/+"
find_eggs = re.findall(found_eggs, some_string)
for egg in find_eggs:
    found_color = r"\w+"
    found_amount = r"\d+"
    find_color = re.findall(found_color, egg)
    find_amount = re.findall(found_amount, egg)
    print(f"You found {int(find_amount[0])} {find_color[0]} eggs!")