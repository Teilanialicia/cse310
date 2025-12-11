import pygame

GRAVITY = 0.5

class Player:
  #12 Set up the player
  def __init__(self, x, y):
      self.rect = pygame.Rect(x, y, 40, 60)
      self.vel_x = 0
      self.vel_y = 0
      self.on_ground = False

  #13 Update the player's movement
  def update(self, keys, platforms):
    #14 Horizontal
    self.vel_x = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 5

    #15 Jump
    if keys[pygame.K_SPACE] and self.on_ground:
      self.vel_y = -10
      self.on_ground = False

    #16 Gravity
    self.vel_y += GRAVITY

    #17 Movement + collision (HORIZONTAL)
    self.rect.x += self.vel_x
    for p in platforms:
      if self.rect.colliderect(p):
        if self.vel_x > 0:
          self.rect.right = p.left
        else:
          self.rect.left = p.right

    #18 Movement + collision (VERTICAL)
    self.rect.y += self.vel_y
    self.on_ground = False
    for p in platforms:
      if self.rect.colliderect(p):
        if self.vel_y > 0:
          self.rect.bottom = p.top
          self.vel_y = 0
          self.on_ground = True
        else:
          self.rect.top = p.bottom
          self.vel_y = 0
