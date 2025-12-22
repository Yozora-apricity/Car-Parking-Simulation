import pygame
import random
import sys

# --- BINARY TREE LOGIC ---
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def ltr(node): # In-order
    if not node: return []
    return ltr(node.left) + [node.value] + ltr(node.right)

def tlr(node): # Pre-order
    if not node: return []
    return [node.value] + tlr(node.left) + tlr(node.right)

def lrt(node): # Post-Order
    if not node: return []
    return lrt(node.left) + lrt(node.right) + [node.value]

class BinaryTreeOrder:
    def __init__(self):
        self.root = None

    def tree_level_order(self, values):
        if not values:
            self.root = None
            return

        self.root = BinaryTreeNode(values[0])
        next_node_value = [self.root]
        node_index = 1

        while next_node_value and node_index < len(values):
            node = next_node_value.pop(0)

            if node_index < len(values):
                node.left = BinaryTreeNode(values[node_index])
                next_node_value.append(node.left)
                node_index += 1

            if node_index < len(values):
                node.right = BinaryTreeNode(values[node_index])
                next_node_value.append(node.right)
                node_index += 1

# --- GLOBAL CONSTANTS ---
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 30

# VISUAL CONSTANTS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = (40, 40, 40)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)
RED = (255, 50, 50)

# --- BINARY TREE MENU ---
class BinaryTreeMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font_title = pygame.font.SysFont("arial", 48)
        self.font_menu = pygame.font.SysFont("arial", 26)

    def draw_text_center(self, text, font, color, y):
        render = font.render(text, True, color)
        x = SCREEN_WIDTH // 2 - render.get_width() // 2
        self.screen.blit(render, (x, y))

    def draw(self):
        self.screen.fill(DARK_GRAY)

        self.draw_text_center("Binary Tree Menu", self.font_title, WHITE, 180)
        self.draw_text_center("Mode 1: Letters", self.font_menu, LIGHT_GRAY, 300)
        self.draw_text_center("Mode 2: Numbers", self.font_menu, LIGHT_GRAY, 340)
        self.draw_text_center("Press the number for the mode you want",
                              self.font_menu, WHITE, 400)
        self.draw_text_center("Press ESC to Quit", self.font_menu, RED, 460)

        pygame.display.flip()

# --- MAIN ---
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Binary Tree Menu")

    menu = BinaryTreeMenu(screen)
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        menu.draw()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()