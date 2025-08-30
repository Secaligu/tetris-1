import pygame, sys, random
from pygame.math import Vector2

pygame.init()
 
  #<|variables|>#
BG_COLOR = (156, 200, 255)
SNAKE_COLOR = (2, 74, 191)
SNAKE_FOOD = (2, 76, 204)

cell_size = 30
number_of_cell = 25

class Food:
    def __init__(self):
      self.position = self.generate_ramdom_pos()
    def draw(self):
        Food_rect = pygame.Rect(self.position.x * cell_size, self.position.y * cell_size, cell_size, cell_size)
        screen.blit(food_surface, Food_rect)
        
    def generate_ramdom_pos(self):
      x = random.randint(0, number_of_cell - 1)
      y = random.randint(0, number_of_cell - 1)
      position = Vector2(x, y)
      return position

class Snake:
  def __init__(self):
    self.body = [Vector2(6, 9), Vector2(5,9), Vector2 (4,9)]
    
  def draw(self):
    for segment in self.body:
      segment_rect = (segment.x * cell_size, segment.y * cell_size, cell_size, cell_size)
      pygame.draw.rect(screen, SNAKE_COLOR, segment_rect,0, 6)
      

screen = pygame.display.set_mode((cell_size*number_of_cell, cell_size*number_of_cell ))

pygame.display.set_caption("retro snake")

clock = pygame.time.Clock()

Food = Food()
snake = Snake()
food_surface = pygame.image.load("grafics/arandano.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #Drawing zone
    screen.fill(BG_COLOR)
    Food.draw()
    snake.draw()
            
    
    pygame.display.update()
    clock.tick(60)          
            