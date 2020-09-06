#!/usr/bin/env python3
import sys,os,json
assert sys.version_info >= (3,8), "This script requires at least Python 3.8"

def load(l):
    f = open(os.path.join(sys.path[0], l))
    data = f.read()
    j = json.loads(data)
    return j

def find_passage(game_desc, pid):
    for p in game_desc["passages"]:
        if p["pid"] == pid:
            return p
    return {}



# ------------------------------------------------------

def update(current, game_desc, choice):
    if choice == "":
        return current
    for i in current["links"]:
        if choice == i["name"].lower():
            current = find_passage(game_desc, i["pid"])
    return current


def render(current):
    print("Location: " + current["name"])
    print(current["text"])

def get_input(current):
    choice = input("What would you like to do? (type quit to exit) ")
    choice = choice.lower()
    if choice in ["quit","q","exit"]:
        return "quit"
    return choice

# ------------------------------------------------------

def main():
    game_desc = load("adventure.json")
    current = find_passage(game_desc, game_desc["startnode"])
    choice = ""

    while choice != "quit" and current != {}:
        current = update(current, game_desc, choice)
        render(current)
        choice = get_input(current)

    print("Thanks for playing!")




if __name__ == "__main__":
    main()