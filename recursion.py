import random
import sys
class Plates:
    def __init__(self) ->None :
        # Put the values in a list
        self.values_list = []
    
    # input number of plates (minimum: 6)
    def input_plates(self):
        while True:
            try:
                while True:
                    self.plate_input = int(input("Input number of plates FROM 1~6: "))
                    if 1 <= self.plate_input <= 6:
                        break
                    else:
                        print("please input a number from 1~6 only")

            except:
                print("please input an integer")
            break
        print(self.plate_input) # just a testing to see if the function works as intended

                
    # Either input or randomize integers with respect to the number of plates
    def input_integers(self):
        while True:
            try:
                self.values_list = [int(input(f"input number {i+1} time: ")) for i in range(0, self.plate_input)]
            except:
                print("please input an integer")
            break
        print(self.values_list) # just a testing to see if the function works
    def input_random_integers(self):
        self.flag_variable = 0
        while self.flag_variable < self.plate_input:
            random_number = random.randint(0, 50)
            self.values_list.append(random_number)
            self.flag_variable += 1
        print(self.values_list)            

    # Sort the integers    
    def sort_values(self):
        self.values_list.sort()
        print(self.values_list)

    
class Tower:
    def __init__(self, plates_obj) ->None :
        # Create three towers as dictionaries to hold the plates.
        self.towers = {
            "First Tower": [],
            "Second Tower": [],
            "Third Tower": []
        }
        
        self.towers["First Tower"] = plates_obj.values_list[:] # Copy the plates into the first tower.
        
    def display_towers(self):
        # Loop through the towers and print their current contents.
        for tower_name, plates in self.towers.items():
            print(f"{tower_name}: {plates}")
        
class Logic:
    def __init__(self, tower_obj) ->None :
        self.tower_obj = tower_obj
        
    def hanoi_move(self, n, source, target, auxiliary):
        if n > 0:
            self.hanoi_move(n - 1, source, auxiliary, target) # Move the top stack of plates to the helper tower.
            
            # Move the bottom plate to the Third tower.
            if self.tower_obj.towers[source]:
                plate = self.tower_obj.towers[source].pop()
                self.tower_obj.towers[target].append(plate)
                print(f"Move plate {plate} from {source} to {target}")
                self.tower_obj.display_towers()
                
            self.hanoi_move(n - 1, auxiliary, target, source) # Move the plates from the helper tower to the Third tower.
            
    def start_simulation(self):
        num_plates = len(self.tower_obj.towers["First Tower"])
        self.tower_obj.display_towers()
        self.hanoi_move(num_plates, "First Tower", "Third Tower", "Second Tower") 
        #Start from First Tower to Third Tower using Second Tower as helper or auxillary.


plates = Plates()
plates.input_plates()
plates.input_random_integers()
plates.sort_values()