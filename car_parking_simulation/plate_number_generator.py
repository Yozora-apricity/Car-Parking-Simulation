import random
import string

def generate_plate_number(self):
    self.letters = "".join(random.choices(string.ascii_uppercase, k=3))
    self.numbers = "".join(random.choices(string.digits, k=3))
    return f"{self.numbers}-{self.letters}"