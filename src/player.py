# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, starting_location):
        self.name = name
        self.current_location = starting_location

    def travel(self, direction):
        if getattr(self.current_location, f'{direction}_to') is not None:
            self.current_location = getattr(
                self.current_location, f'{direction}_to')
            print(self.current_location)
        else:
            print("You cannot go in this direction")
