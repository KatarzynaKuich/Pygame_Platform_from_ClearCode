import pygame, sys

pygame.init()
#settings----------------
screen_width = 600
screen_hight = 600
screen = pygame.display.set_mode((screen_width, screen_hight))
clock = pygame.time.Clock()
#-------------------------
#-init-----------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((30, 30, 30))  #black?
    pygame.display.flip()  #update screen
    clock.tick(60)
#-------------------------

for row_index, row in enumerate(layout):
    for col_index, cell in enumerate(row):
        x = col_index * tile_size
        y = row_index * tile_size

        if cell == 'X':
            tile = Tile((x, y), tile_size)
            self.tiles.add(tile)
