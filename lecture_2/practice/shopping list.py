def print_list(list):
    for item in list:
        print(item);

def main_logic():
    list = []
    wishes = ""

    print("Let's make the list of items that you require. You can do it by typing Add/Remove ...: ")
    while wishes != "enough":
        wishes = input("")
        if wishes[0:3].lower() == "add":
            list.append(wishes[3:])
        elif wishes[0:6].lower() == "remove":
            list.remove(wishes[6:])
        elif wishes.strip().lower() == "enough":
            break
        else:
            print("Wow, it seeams you made a mistake. Try again!")
            continue

    print("Here is your list: ")
    print_list(list)

if __name__ == "__main__":
    main_logic()