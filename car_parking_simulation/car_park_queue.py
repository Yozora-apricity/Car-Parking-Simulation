from plate_number_generator import generate_plate_number

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if self.isEmpty():
            return None
        return self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            return None
        return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

class Car():
    def __init__(self, manual_plate = None):
        self.plate_number = manual_plate if manual_plate else generate_plate_number(self)
        self.arrivals = 1
        self.departures = 0

    def remove_car(self, queue, target):
        if queue.isEmpty():
            return False

        front_car = queue.dequeue()
        front_car.departures += 1

        if front_car.plate_number == target:
            return True

        found = self.remove_car(queue, target)

        if found:
            queue.enqueue(front_car)
            front_car.arrivals += 1
            print(f"Car {front_car.plate_number} re-entered the queue.")
            print(f"Arrivals: {front_car.arrivals}, Departures: {front_car.departures}")
        else:
            queue.push(top_car)
            front_car.departures -= 1

        return found