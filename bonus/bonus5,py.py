waiting_list = ("me", "tu", "we")

for index, item in enumerate(waiting_list):
    row = "{index + 1}-{item.capitalize()}"
    print(row)