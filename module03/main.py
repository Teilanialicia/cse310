import pygame
import json
from Player import Player

# Loads the levels from levels.json
def load_levels(path="levels.json"):
  with open(path, "r") as f:
    return json.load(f)
    
# Gets the current level information from the levels array
def get_level(levels, index):
  level_data = levels[index]

  platforms = [
    pygame.Rect(p["x"], p["y"], p["width"], p["height"])
    for p in level_data["platforms"]
  ]

  player_start = level_data["player_start"]

  end_data = level_data["end"]
  end_rect = pygame.Rect(
    end_data["x"], end_data["y"], end_data["width"], end_data["height"]
  )

  return platforms, player_start, end_rect

# Start pygame
pygame.init()

# Start the music
pygame.mixer.init()
pygame.init()

# Load the background music
pygame.mixer.music.load("Nebulite - Breath.mp3")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)

# Set up the screen size
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Load the levels
levels = load_levels()
current_level = 0

# Set up the level
platforms, start, end_rect = get_level(levels, current_level)
player = Player(start["x"], start["y"])

# Run the game
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  keys = pygame.key.get_pressed()
  player.update(keys, platforms)

  # DRAW
  screen.fill((0, 0, 0))

  pygame.draw.rect(screen, (255, 0, 0), player.rect)

  # Check if player touched the end zone
  if player.rect.colliderect(end_rect):
    current_level += 1

    if current_level >= len(levels):
      current_level = 0

    platforms, start, end_rect = get_level(levels, current_level)
    player = Player(start["x"], start["y"])

  # Draw everything
  for p in platforms:
    pygame.draw.rect(screen, (0, 255, 0), p)

  pygame.draw.rect(screen, (255, 215, 0), end_rect)

  pygame.display.flip()
  clock.tick(60)

pygame.quit()
