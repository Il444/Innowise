from colorama import Fore, Back, Style, init

init(autoreset=True)


def main():
    print(Fore.GREEN + "=== Добро пожаловать в мой проект! ===")
    print(Fore.BLUE + "Этот текст синего цвета")
    print(Fore.RED + "А этот - красного")
    print(Fore.YELLOW + Back.BLACK + "Желтый текст на черном фоне")

    name = input(Fore.CYAN + "Как вас зовут? ")
    print(Fore.MAGENTA + f"Привет, {name}!")

    print(Style.BRIGHT + Fore.WHITE + "Это яркий белый текст")
    print(Fore.GREEN + "Программа завершена успешно!")


if __name__ == "__main__":
    main()