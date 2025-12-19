#Note:
# So allow me to explain some def words in this code.
# So First Tower is the source tower where all plates start.
# Second Tower is the auxiliary tower used during the process.
# Third Tower is the target tower where all plates should end up.

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
    def __init__(self):
        self.values_list = []
        self.plate_count = 0

    def generate_random_plates(self, count):
        self.plate_count = count
        self.values_list = []
        for _ in range(count):
            self.values_list.append(random.randint(1, 50))
        
        # Sort DESCENDING so largest plates are at the bottom
        self.values_list.sort(reverse=True) 

class Tower:
    def __init__(self, plates_obj, screen):
        self.screen = screen
        self.towers = {
            "First Tower": [],
            "Second Tower": [],
            "Third Tower": []
        }
        self.towers["First Tower"] = plates_obj.values_list[:]
        
        self.peg_positions = {
            "First Tower": SCREEN_WIDTH // 4,
            "Second Tower": SCREEN_WIDTH // 2,
            "Third Tower": (SCREEN_WIDTH * 3) // 4
        }
        
        self.font = pygame.font.SysFont("Arial", 20, bold=True)
        self.ui_font = pygame.font.SysFont("Arial", 24)

    def get_peg_x(self, tower_name):
        return self.peg_positions[tower_name]

    def draw_static_scene(self, move_count=0):
        # Draws everything EXCEPT the moving plate.
        self.screen.fill((30, 30, 30)) 
        
        # Create Floor
        pygame.draw.rect(self.screen, LIGHT_GRAY, (0, SCREEN_HEIGHT - BASE_HEIGHT, SCREEN_WIDTH, BASE_HEIGHT))

        # Draw Pegs and Static Plates
        for tower_name, x_pos in self.peg_positions.items():
            # Draw Peg
            peg_height = 400
            pygame.draw.rect(self.screen, LIGHT_GRAY, (x_pos - PEG_WIDTH//2, PEG_Y - peg_height, PEG_WIDTH, peg_height))
            
            # Draw Plates in this tower
            plates = self.towers[tower_name]
            for i, plate_value in enumerate(plates):
                self.draw_single_plate(plate_value, x_pos, i)

        # Draw UI (Top Right)
        ui_text = self.ui_font.render("[R] Reset  |  [Q] Quit", True, WHITE)
        self.screen.blit(ui_text, (SCREEN_WIDTH - ui_text.get_width() - 20, 20))

        # Draw Move Tracker (Top Left)
        moves_text = self.ui_font.render(f"Moves: {move_count}", True, CYAN)
        self.screen.blit(moves_text, (20, 20))

    def draw_single_plate(self, plate_value, x_center, stack_index, custom_y=None):
        #Helper to draw one plate.
        
        # Calculate Dimensions (Map 1-50 to width range)
        plate_width = MIN_PLATE_WIDTH + (plate_value * 5)
        if plate_width > MAX_PLATE_WIDTH: plate_width = MAX_PLATE_WIDTH
        
        # Determine Position
        x = x_center - (plate_width // 2)
        if custom_y is not None:
            y = custom_y
        else:
            # Stack from bottom up: Base - (Index+1)*Height
            y = SCREEN_HEIGHT - BASE_HEIGHT - ((stack_index + 1) * PLATE_HEIGHT)

        color = PLATE_COLORS[plate_value % len(PLATE_COLORS)]

        # Draw Rect and Border
        pygame.draw.rect(self.screen, color, (x, y, plate_width, PLATE_HEIGHT))
        pygame.draw.rect(self.screen, BLACK, (x, y, plate_width, PLATE_HEIGHT), 2)
        
        # Draw Number
        text = self.font.render(str(plate_value), True, BLACK)
        text_rect = text.get_rect(center=(x + plate_width//2, y + PLATE_HEIGHT//2))
        self.screen.blit(text, text_rect)

class Animation:
    # Handles visual movement, timing, and input checking during animation.
    def __init__(self, tower_obj, screen):
        self.tower_obj = tower_obj
        self.screen = screen
        self.clock = pygame.time.Clock()
        
    def check_input(self):
        # Checks for Q (Quit) or R (Restart) interrupts.
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

    def animate_move(self, plate_val, source_name, target_name, move_count):
        # Runs the animation for moving a plate from First Tower to Third Tower.
        start_x = self.tower_obj.get_peg_x(source_name)
        end_x = self.tower_obj.get_peg_x(target_name)
        
        # Calculate visual start and end Y positions
        start_y = SCREEN_HEIGHT - BASE_HEIGHT - ((len(self.tower_obj.towers[source_name]) + 1) * PLATE_HEIGHT)
        end_y = SCREEN_HEIGHT - BASE_HEIGHT - ((len(self.tower_obj.towers[target_name]) + 1) * PLATE_HEIGHT)

        # ANIMATION SPEED
        duration = 0.8 
        total_frames = int(duration * FPS)
        
        for frame in range(total_frames + 1):
            # Check for interruption
            if self.check_input() == "restart": return "restart"
            
            t = frame / total_frames
            
            # Trajectory Logic
            if t < 0.3: # Up Phase
                progress = t / 0.3
                cur_x = start_x
                cur_y = start_y + (LIFT_HEIGHT - start_y) * progress
            elif t < 0.7: # Across Phase
                progress = (t - 0.3) / 0.4
                cur_x = start_x + (end_x - start_x) * progress
                cur_y = LIFT_HEIGHT
            else: # Down Phase
                progress = (t - 0.7) / 0.3
                cur_x = end_x
                cur_y = LIFT_HEIGHT + (end_y - LIFT_HEIGHT) * progress

            # Draw the frame
            self.tower_obj.draw_static_scene(move_count) 
            self.tower_obj.draw_single_plate(plate_val, int(cur_x), -1, int(cur_y)) 
            
            pygame.display.flip()
            self.clock.tick(FPS)
            
        return "done"

class Logic:
    # Handles the Recursive Algorithm and State Management.
    def __init__(self, tower_obj, animation_obj):
        self.tower_obj = tower_obj
        self.animation = animation_obj # Reference to Animation class
        self.move_count = 0 
        self.running = True

    def hanoi_move(self, n, source, target, auxiliary):
        if not self.running: return "restart"

        if n > 0:
            # 1. Recursive Call (Move n-1 to Second Tower)
            if self.hanoi_move(n - 1, source, auxiliary, target) == "restart": return "restart"
            
            # 2. Move the Nth Plate
            if self.tower_obj.towers[source]:
                # Logic: Remove plate from source stack
                plate = self.tower_obj.towers[source].pop()
                
                # Visual: Ask Animation class to show movement
                result = self.animation.animate_move(plate, source, target, self.move_count)
                if result == "restart": return "restart"
                
                # Logic: Add plate to target stack
                self.tower_obj.towers[target].append(plate)
                
                # Update Move Counter
                self.move_count += 1
                self.tower_obj.draw_static_scene(self.move_count)
                pygame.display.flip()

            # 3. Recursive Call (Move n-1 from Aux to Target)
            if self.hanoi_move(n - 1, auxiliary, target, source) == "restart": return "restart"

    def start_simulation(self):
        # Initial Draw
        self.tower_obj.draw_static_scene(0)
        pygame.display.flip()
        time.sleep(0.5)
        
        num_plates = len(self.tower_obj.towers["First Tower"])
        return self.hanoi_move(num_plates, "First Tower", "Third Tower", "Second Tower")

def get_user_input_gui(screen):
    font = pygame.font.SysFont("Arial", 40)
    font_small = pygame.font.SysFont("Arial", 24)
    input_value = ""
    
    while True:
        screen.fill((30, 30, 30))
        
        title = font.render("Tower of Hanoi", True, WHITE)
        prompt = font_small.render("Type how many number of plates (3-8)", True, GREEN)
        prompt2 = font_small.render("Press enter to start.", True, GREEN)
        current = font.render(f"Plates: {input_value}", True, CYAN)
        
        screen.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, 150))
        screen.blit(prompt, (SCREEN_WIDTH//2 - prompt.get_width()//2, 250))
        screen.blit(prompt2, (SCREEN_WIDTH//2 - prompt2.get_width()//2, 300))
        screen.blit(current, (SCREEN_WIDTH//2 - current.get_width()//2, 400))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                
                # Accept any numeric input (Numpad or Top Row)
                if event.unicode.isnumeric():
                    input_value = event.unicode
                    
                elif event.key == pygame.K_RETURN and input_value != "":
                    try:
                        val = int(input_value)
                        if 3 <= val <= 8: 
                            return val
                    except: pass

def main():
    pygame.init()
    pygame.font.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tower of Hanoi Simulation")
    
    while True:
        num_plates = get_user_input_gui(screen)
        
        # Initialize Objects
        plates = Plates()
        plates.generate_random_plates(num_plates)
        
        tower = Tower(plates, screen)
        animation = Animation(tower, screen) # New Animation Object
        logic = Logic(tower, animation)      # Pass Animation to Logic
        
        # Start
        status = logic.start_simulation()
        
        if status == "restart":
            continue
            
        # End Screen Loop
        waiting = True
        while waiting:
            tower.draw_static_scene(logic.move_count)
            
            font = pygame.font.SysFont("Arial", 50, bold=True)
            text = font.render("Complete! Press R or Q", True, GREEN)
            screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, SCREEN_HEIGHT//2 - 50))
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_r:
                        waiting = False

if __name__ == "_main_":
    main()