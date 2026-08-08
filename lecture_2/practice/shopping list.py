def print_list(list):
    if not list:
        print("Your list is empty")
    for item in list:
        print(f"{item}")

def main_logic():
    list = []
    wishes = ""

    print("Let's make the list of items that you require. You can do it by typing Add/Remove ... "
          "Also the moment you are done just write enough: ")
    while wishes != "enough":
        wishes = input("")
        if wishes[0:3].lower() == "add":
            item = wishes[3:].strip()
            list.append(item)
            print(f"Added {item}")
        elif wishes[0:6].lower() == "remove":
            item = wishes[6:].strip()
            if item in list:
                list.remove(item)
                print(f"Removed {item}")
            else:
                print(f"{item} is not in the list")
        elif wishes.strip().lower() == "enough":
            break
        else:
            print("Wow, it seeams you made a mistake. Try again!")

    print("Here is your list: ")
    print_list(list)
    print(f"Total amount of items: {len(list)}")

if __name__ == "__main__":
    main_logic()