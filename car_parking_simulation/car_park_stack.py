from plate_number_generator import generate_plate_number

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            return None
        return self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

class Car():
    def __init__(self, manual_plate = None):
        self.plate_number = manual_plate if manual_plate else generate_plate_number(self)
        self.arrivals = 0
        self.departures = 0

    def remove_car(self, stack, target):
        if stack.isEmpty():
            return False

        top_car = stack.pop()

        if top_car.plate_number == target:
            top_car.departures += 1
            print(f"Arrivals: {top_car.arrivals}, Departures: {top_car.departures}")
            return True

        found = self.remove_car(stack, target)
        stack.push(top_car)
        return found