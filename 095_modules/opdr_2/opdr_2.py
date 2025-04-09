from modules.csv import get_personen, filter, print_persons

def main():
    personen = get_personen()

    # Test 1: Filter op voornaam met "ja"
    print("Filter op voornaam met 'ja':")
    gefilterd = filter(personen, "voornaam", "ja")
    print_persons(gefilterd, filter=["voornaam", "achternaam", "plaats"])

    # Test 2: Filter op voornaam met "Pie"
    print("\nFilter op voornaam met 'Pie':")
    gefilterd = filter(personen, "voornaam", "Pie")
    print_persons(gefilterd, filter=["voornaam", "achternaam", "plaats"])

    # Test 3: Filter op plaats met "d"
    print("\nFilter op plaats met 'd':")
    gefilterd = filter(personen, "plaats", "d")
    print_persons(gefilterd, filter=["voornaam", "achternaam", "plaats"])

if __name__ == "__main__":
    main()