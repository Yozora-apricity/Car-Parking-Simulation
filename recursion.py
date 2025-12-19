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

    def generate_random_plates(self, count):
        self.plate_count = count
        self.values_list = []
        for _ in range(count):
            self.values_list.append(random.randint(1, 50))
        
        # Sort DESCENDING so largest plates are at the bottom
        self.values_list.sort(reverse=True)
           
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
        
        # Calculate X positions for the 3 pegs (25%, 50%, 75% of screen width)
        self.peg_positions = {
            "First Tower": self.width // 4,
            "Second Tower": self.width // 2,
            "Third Tower": (self.width * 3) // 4
        }
        
        self.font = pygame.font.SysFont("Arial", 20, bold=True)
        self.ui_font = pygame.font.SysFont("Arial", 24)
        
    def display_towers(self):
        # Loop through the towers and print their current contents.
        for tower_name, plates in self.towers.items():
            print(f"{tower_name}: {plates}")
    
    def get_peg_x(self, tower_name):
        return self.peg_positions[tower_name]

    def draw_static_scene(self, move_count=0):
        self.screen.fill((30, 30, 30))

        pygame.draw.rect(
            self.screen,
            LIGHT_GRAY,
            (0, SCREEN_HEIGHT - BASE_HEIGHT, SCREEN_WIDTH, BASE_HEIGHT)
        )

        for tower_name, x_pos in self.peg_positions.items():
            peg_height = 400
            pygame.draw.rect(
                self.screen,
                LIGHT_GRAY,
                (x_pos - PEG_WIDTH//2, PEG_Y - peg_height, PEG_WIDTH, peg_height)
            )

            for i, plate_value in enumerate(self.towers[tower_name]):
                self.draw_single_plate(plate_value, x_pos, i)

        ui_text = self.ui_font.render("[R] Reset  |  [Q] Quit", True, WHITE)
        self.screen.blit(ui_text, (SCREEN_WIDTH - ui_text.get_width() - 20, 20))

        moves_text = self.ui_font.render(f"Moves: {move_count}", True, CYAN)
        self.screen.blit(moves_text, (20, 20))

    def draw_single_plate(self, plate_value, x_center, stack_index, custom_y=None):
        plate_width = min(
            MIN_PLATE_WIDTH + plate_value * 5,
            MAX_PLATE_WIDTH
        )

        x = x_center - plate_width // 2
        y = (
            custom_y
            if custom_y is not None
            else SCREEN_HEIGHT - BASE_HEIGHT - ((stack_index + 1) * PLATE_HEIGHT)
        )

        color = PLATE_COLORS[plate_value % len(PLATE_COLORS)]

        pygame.draw.rect(self.screen, color, (x, y, plate_width, PLATE_HEIGHT))
        pygame.draw.rect(self.screen, BLACK, (x, y, plate_width, PLATE_HEIGHT), 2)

        text = self.font.render(str(plate_value), True, BLACK)
        self.screen.blit(text, text.get_rect(center=(x + plate_width//2, y + PLATE_HEIGHT//2)))

class Animation:
    def __init__(self, tower_obj, screen) ->None :
        self.tower_obj = tower_obj
        self.screen = screen
        self.clock = pygame.time.Clock()
        
    def check_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_r:
                    return "restart"
        return None
    
    def animate_move(self, plate_val, source, target, move_count):
        start_x = self.tower_obj.get_peg_x(source)
        end_x = self.tower_obj.get_peg_x(target)

        start_y = SCREEN_HEIGHT - BASE_HEIGHT - (
            (len(self.tower_obj.towers[source]) + 1) * PLATE_HEIGHT
        )
        end_y = SCREEN_HEIGHT - BASE_HEIGHT - (
            (len(self.tower_obj.towers[target]) + 1) * PLATE_HEIGHT
        )

        duration = 0.8
        total_frames = int(duration * FPS)

        for frame in range(total_frames + 1):
            if self.check_input() == "restart":
                return "restart"

            t = frame / total_frames

            if t < 0.3:
                cur_x = start_x
                cur_y = start_y + (LIFT_HEIGHT - start_y) * (t / 0.3)
            elif t < 0.7:
                cur_x = start_x + (end_x - start_x) * ((t - 0.3) / 0.4)
                cur_y = LIFT_HEIGHT
            else:
                cur_x = end_x
                cur_y = LIFT_HEIGHT + (end_y - LIFT_HEIGHT) * ((t - 0.7) / 0.3)

            self.tower_obj.draw_static_scene(move_count)
            self.tower_obj.draw_single_plate(
                plate_val, int(cur_x), -1, int(cur_y)
            )

            pygame.display.flip()
            self.clock.tick(FPS)

        return "done"

class Logic:
    def __init__(self, tower_obj, animation_obj) ->None :
        self.tower_obj = tower_obj
        self.animation_obj = animation_obj
        self.move_count = 0
        self.running = True
        
    def hanoi_move(self, n, source, target, auxiliary):
        if n > 0:
            if self.hanoi_move(n - 1, source, auxiliary, target) == "restart":
                return "restart"

            plate = self.tower_obj.towers[source].pop()

            if self.animation.animate_move(
                plate, source, target, self.move_count
            ) == "restart":
                return "restart"

            self.tower_obj.towers[target].append(plate)
            self.move_count += 1

            self.tower_obj.draw_static_scene(self.move_count)
            pygame.display.flip()

            if self.hanoi_move(n - 1, auxiliary, target, source) == "restart":
                return "restart"

            
    def start_simulation(self):
        self.tower_obj.draw_static_scene(0)
        pygame.display.flip()
        time.sleep(0.5)
        
        n = len(self.tower_obj.towers["First Tower"])
        return self.hanoi_move(n, "First Tower", "Third Tower", "Second Tower")
    
def get_user_input_gui(screen):
    font = pygame.font.SysFont("Arial", 40)
    font_small = pygame.font.SysFont("Arial", 24)
    input_value = ""

    while True:
        screen.fill((30, 30, 30))

def main():
    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tower of Hanoi Simulation")

    while True:
        num_plates = get_user_input_gui(screen)

        plates = Plates()
        plates.generate_random_plates(num_plates)

        tower = Tower(plates, screen)
        animation = Animation(tower, screen)
        logic = Logic(tower, animation)

        status = logic.start_simulation()

        if status == "restart":
            continue


if __name__ == "__main__":
    main()