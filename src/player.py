# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, starting_location):
        self.name = name
        self.current_location = starting_location