# python module imports
import pygame

# project file imports
import lib

class Player(pygame.sprite.Sprite):
    """
    the player object
    
    ...
    
    Attributes
    ----------
    pos : pygame.math.Vector2
        the position of the player in the world

    vel : pygame.math.Vector2
        the velocity of the player in the x and y directions

    size : pygame.math.Vector2
        the players size in the x and y directions

    speed : int
        the speed at which the player moves (horizontal only)

    falling : bool
        indicates if the player is actively falling

    image : pygame.Surface
        the image object that gets rendered to the screen

    rect : pygame.sprite.Rect
        object that holds all of the position and collision data of the player

    Methods
    -------
    update():
        updates the player, calls the movement_controller

    movement_controller():
        handles the inputs specific to moving the player
    """
    def __init__(self, x: int, y: int):
        """
        constructs the player object
        """
        
        pygame.sprite.Sprite.__init__(self)

        self.pos = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2()
        self.size = pygame.math.Vector2(32, 64)
        self.speed = 250
        self.falling = True

        self.image = pygame.Surface([self.size.x, self.size.y])
        self.image.fill(lib.color.WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self):
        """
        updates the player, calls the movement_controller
        
        ...
        
        Returns
        -------
        None
        """
        
        self.pos += self.vel * lib.delta_time
        self.rect.center = self.pos

        if self.vel.y != 0:
            self.falling = True

        if self.falling:
            self.vel.y += lib.GRAVITY

        self.movement_controller()

    def movement_controller(self):
        """
        handles the inputs specific to moving the player
        
        ...

        Returns
        -------
        None
        """
        
        keys = pygame.key.get_pressed()

        # check for horizontal movement and set fixed move speed
        if keys[pygame.K_d]:
            self.vel.x = self.speed
        elif keys[pygame.K_a]:
            self.vel.x = -self.speed
        else:
            self.vel.x = 0

        # check for [SPACE] in events list and jump
        for event in lib.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.falling == False:
                        self.vel.y = -500
