import pygame
from Animal import Animal
from Environment import Environment
from Food import Food

e = Environment(50)
e.addAnimal(Animal(10, 20, 5, 30, 30, "green"))
e.runSim()

#screen = pygame.display.set_mode((e.width, e.width))
#
#running = True
#while running:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running = False
#            pygame.quit()
#pygame.display.flip()

