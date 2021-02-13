class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return self.name + " is available from " + self.start_time + " to " + self.end_time

    def calculate_bill(self, purchased_items):
        total = 0
        for item in purchased_items:
            total += self.items[item]
        return total

class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus
    def __repr__(self):
        return self.address


brunch = Menu("Brunch", {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, "11AM", "4PM")

print(brunch)
print(brunch.calculate_bill(['pancakes', 'coffee']))


flashship = Franchise("1213 West End Road", [brunch])
