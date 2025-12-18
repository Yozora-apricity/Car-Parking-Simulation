import pygame
import random
import sys
import time

# --- GLOBAL CONSTANTS ---
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

PEG_WIDTH = 10
BASE_HEIGHT = 20
PLATE_HEIGHT = 30
MIN_PLATE_WIDTH = 60
MAX_PLATE_WIDTH = 300

# Visual Constants for Animation
PEG_Y = SCREEN_HEIGHT - BASE_HEIGHT
LIFT_HEIGHT = 150 

# Colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)
GRAY = (50, 50, 50)
LIGHT_GRAY = (200, 200, 200)

PLATE_COLORS = [RED, GREEN, BLUE, ORANGE, PURPLE, CYAN]

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
        
        # VISUALIZATION DATA
        self.width = screen_width
        self.height = screen_height
        
        # Calculate X positions for the 3 pegs (25%, 50%, 75% of screen width)
        self.peg_positions = {
            "First Tower": self.width // 4,
            "Second Tower": self.width // 2,
            "Third Tower": (self.width * 3) // 4
        }
        
    def display_towers(self):
        # Loop through the towers and print their current contents.
        for tower_name, plates in self.towers.items():
            print(f"{tower_name}: {plates}")
    
    def draw(self, screen):
        # Draw the floor/base
        pygame.draw.rect(screen, WHITE, (0, self.height - BASE_HEIGHT, self.width, BASE_HEIGHT))

        # Iterate through towers to draw Pegs and Plates
        for tower_name, x_pos in self.peg_positions.items():
            # Draw Peg
            peg_height = 400 # Height of the peg
            start_pos = (x_pos, self.height - BASE_HEIGHT)
            end_pos = (x_pos, self.height - BASE_HEIGHT - peg_height)
            pygame.draw.line(screen, WHITE, start_pos, end_pos, PEG_WIDTH)

            # Draw Plates in this tower
            plates = self.towers[tower_name]
            for i, plate_value in enumerate(plates):
                # Calculate plate dimensions
                # Map value (0-50) to width range
                plate_width = MIN_PLATE_WIDTH + (plate_value * 5) 
                if plate_width > MAX_PLATE_WIDTH: plate_width = MAX_PLATE_WIDTH
                
                plate_x = x_pos - (plate_width // 2)
                plate_y = self.height - BASE_HEIGHT - ((i + 1) * PLATE_HEIGHT)
                
                # Cycle through colors based on plate value
                color = PLATE_COLORS[plate_value % len(PLATE_COLORS)]
                
                pygame.draw.rect(screen, color, (plate_x, plate_y, plate_width, PLATE_HEIGHT))
        
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
        # Start from First Tower to Third Tower using Second Tower as helper or auxillary.

def create_window():
    pygame.init()
    # Get the current display resolution
    info_object = pygame.display.Info()
    screen_width = info_object.current_w
    screen_height = info_object.current_h
    
    # Create a full screen window
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
    pygame.display.set_caption("Tower of Hanoi Simulation")
    
    return screen, screen_width, screen_height

if __name__ == "__main__":
    screen, screen_width, screen_height = create_window()
    plates = Plates() # Create an instance of Plates
    plates.input_plates()
    plates.input_random_integers()
    plates.sort_values()
    
    tower = Tower(plates) # Setup the towers with the plates.
    
    logic = Logic(tower) # Run the logic.
    logic.start_simulation()
    
    running = True #loop to keep the window open after the simulation finishes
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()