import random

class Plates:
    def __init__(self) ->None :
        # Put the values in a list
        self.values_list = []
    
    # input number of plates (minimum: 6)
    def input_plates(self):
        while True:
            try:
                while True:
                    self.plate_input = int(input("input input number of plates FFROM 1~6: "))
                    if 0 < self.plate_input == 6:
                        break
                    else:
                        print("please input a number from 1~6")

            except:
                print("please input an integer")
            break
        print(self.plate_input) # just a testing to see if the function works as intended

                
    # Either input or randomize integers with respect to the number of plates
    def input_or_randomize(self):
        pass

    # Sort the integers    
    def sort_values(self):
        pass

    
class Tower:
    pass
class Logic:
    pass
plates = Plates()
plates.input_plates()