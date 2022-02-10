import sys, pygame
pygame.init()

# Create class to define multiple objects


class GameObject:

    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(height, height)

    def move(self):
        self.pos = self.pos.move(self.speed[0], self.speed[1])

# Create objects and background


ball = pygame.image.load("intro_ball.gif")
screen = pygame.display.set_mode([1280, 720])
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))
screen.blit(background, (0, 0))

objects = []

# Create multiple objects with different starting points and speeds
for x in range(4):
    o = GameObject(ball, x*120, [(x+1)*30, (x+1)*30])
    objects.append(o)

while 1:
    # To close window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # Update screen to print every ball
    for o in objects:
        screen.blit(background, o.pos)
    # Update balls position
    for o in objects:
        o.move()
        # Change ball direction if reaches edge of screen
        if o.pos.left < 0 or o.pos.right > 1280:
            o.speed[0] = -o.speed[0]
        if o.pos.top < 0 or o.pos.bottom > 720:
            o.speed[1] = -o.speed[1]
        screen.blit(o.image, o.pos)
    pygame.display.update()
    pygame.time.delay(60)
