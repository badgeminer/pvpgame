"""import pygame
width = 500
hight = 500
black = (0,0,0)
win = pygame.display.set_mode((width,hight))
pygame.display.set_caption("client")
clientNumber = 0

class player():
  def __init__(self,x,y,width,hight,color):
    self.x = x
    self.y = y
    self.width = width
    self.hight = hight
    self.color = color
    self.rect = (x,y,width,hight)
    self.vel = 1
  def draw(self, win):
    pygame.draw.rect(win, self.color,self.rect)
  def move(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
      self.x -= self.vel
    if keys[pygame.K_d]:
      self.x += self.vel
    if keys[pygame.K_w]:
      self.y -= self.vel
    if keys[pygame.K_s]:
      self.y += self.vel
    self.rect = (self.x,self.y,self.width,self.hight)
    





def redrawWindow(win,p):
  win.fill(black)
  p.draw(win)
  pygame.display.update()
def main():
  run = True
  p = player(50,50,100,100,(255,0,0))
  while run:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
       run = False
       pygame.quit()
    p.move()
    redrawWindow(win,p)
main()"""
import network