"""
Replace the contents of this module docstring with your own details
Name: Jessica Spokes
Date started: 30/08/2020
GitHub URL: https://github.com/cp1404-students/travel-tracker-assignment-1-JessicaSpokes
"""


def main():
    print("Travel Tracker 1.0 - by Jessica Spokes")

    data_list = []
    extract_data(data_list)
    MENU = "Menu:\nL - List Places\nA - Add new place\nM - Mark a place as visited\nQ - Quit"

    print(MENU)
    choice = input(">>> ").upper()
    choice = check_choice(MENU, choice)
    while choice != "Q":
        if choice == "L":
            print_list_of_places(data_list)
            print(MENU)
            choice = input(">>> ").upper()
            choice = check_choice(MENU, choice)
        elif choice == "A":
            name_string = "Name"
            name = input("Name: ")
            name = check_input(name, name_string)
            country_string = "Country"
            country = input("Country: ")
            country = check_input(country, country_string)
            priority_string = "Priority:"
            priority = check_integer_input(priority_string)
            print("{} in {} (priority {}) added to Travel Tracker.".format(name, country, priority))
            new_data = [name, country, priority, "n"]
            data_list.append(new_data)
            print(MENU)
            choice = input(">>> ").upper()
            choice = check_choice(MENU, choice)
        elif choice == "M":
            while data_list[0][-1] != "v":
                print_list_of_places(data_list)
                print("Enter a number of a place that you want to mark as visited")
                mark_places_visited_choice_string = ">>>"
                mark_places_visited_choice = check_integer_input(mark_places_visited_choice_string)
                while mark_places_visited_choice not in [1, 2, 3, 4]:
                    print("Invalid number")
                    mark_places_visited_choice_string = ">>>"
                    mark_places_visited_choice = check_integer_input(mark_places_visited_choice_string)
                if mark_places_visited_choice == 1:
                    if data_list[0][-1] == "n":
                        data_list[0][-1] = "v"
                        print("{} in {} visited!".format(data_list[0][0], data_list[0][1]))
                    else:
                        print("That place is already visited")
                elif mark_places_visited_choice == 2:
                    if data_list[1][-1] == "n":
                        data_list[1][-1] = "v"
                        print("{} in {} visited!".format(data_list[1][0], data_list[1][1]))
                    else:
                        print("That place is already visited")
                elif mark_places_visited_choice == 3:
                    if data_list[2][-1] == "n":
                        data_list[2][-1] = "v"
                        print("{} in {} visited!".format(data_list[2][0], data_list[2][1]))
                    else:
                        print("That place is already visited")
                elif mark_places_visited_choice == 4:
                    if data_list[3][-1] == "n":
                        data_list[3][-1] = "v"
                        print("{} in {} visited!".format(data_list[3][0], data_list[3][1]))
                    else:
                        print("That place is already visited")
            if data_list[0][-1] == "v":
                print("No unvisited places")
            print_list_of_places(data_list)
            print(MENU)
            choice = input(">>> ").upper()
            choice = check_choice(MENU, choice)
    if choice == "Q":
        added_data_count = import_data_to_file(data_list)
        print("{} places saved to places.csv.".format(added_data_count))
        print("Have a nice day :)")


def extract_data(data):
    """Extract data from the places.csv file into list form."""
    in_file = open("places.csv", "r")
    for line in in_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        data.append(parts)
    in_file.close()


def check_choice(MENU, choice):
    """Check choice input."""
    while choice not in ["L", "A", "M", "Q"]:
        print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    return choice


def check_input(variable, variable_str):
    """Checks the inputs for name and country variables"""
    while variable == "":
        print("Input can not be blank")
        variable = input("{}: ".format(variable_str))
    return variable


def check_integer_input(variable_str):
    """Checks the input for an integer variable"""
    variable = 0
    finished = False
    while not finished:
        try:
            variable = int(input("{} ".format(variable_str)))
            while variable < 0:
                print("Number must be > 0")
                variable = int(input("{} ".format(variable_str)))
            else:
                finished = True
        except ValueError:
            print("Invalid input; enter a valid number")
    return variable


def print_list_of_places(data_list):
    """Prints a list of places with the correct formatting."""
    from operator import itemgetter
    data_num = 0
    not_visited = 0
    data_list.sort(key=itemgetter(-1, 2))
    for data in data_list:
        data_num += 1
        if data[-1] == "n":
            print("*{:1}. {:8} in {:11} priority {:2}".format(data_num, *data))
            not_visited += 1
        else:
            print("{:2}. {:8} in {:11} priority {:2}".format(data_num, *data))
    if not_visited != 0:
        print("{} places. You still want to visit {} places.".format(len(data_list), not_visited))
    else:
        print("{} places. No places left to visit. Why not add a place?".format((len(data_list))))


def import_data_to_file(data_list):
    """Saves data in data_list into a csv file"""
    added_data_count = 0
    out_file = open("places.csv", "w")
    for data in data_list:
        print("{},{},{},{}".format(*data), file=out_file)
        added_data_count += 1
    out_file.close()
    return added_data_count


if __name__ == '__main__':
    main()
