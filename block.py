# python module imports
import pygame

# project file imports
import lib

class Block(pygame.sprite.Sprite):
    """
    the default block object that the world is built out of
    
    ...
    
    Attributes
    ----------
    pos : pygame.math.Vector2
        the positon of the block in the world

    size : int
        the size of the square block (size * size)

    image : pygame.Surface
        the image object that gets rendered to the screen

    rect : pygame.sprite.Rect
        object that holds all of the position and collision data of the block
    
    Methods
    -------
    update():
        updates the block
    """

    def __init__(self, x: int, y: int):
        """
        constructs all necessary attributes for the block object
        """
        
        pygame.sprite.Sprite.__init__(self)

        self.pos = pygame.math.Vector2(x, y)
        self.size = 32

        self.image = pygame.Surface([self.size, self.size])
        self.image.fill(lib.color.random_custom("g"))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def update(self):
        """
        updates the block
        
        ...
        
        Returns
        -------
        None
        """
        
        pass
