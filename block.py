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

    interaction_controller():
        allows the block to interact with the world, player and mouse
    """

    def __init__(self, x: int, y: int):
        """
        constructs all necessary attributes for the block object
        """
        
        pygame.sprite.Sprite.__init__(self)

        self.pos = pygame.math.Vector2(x, y)
        self.size = 32
        self.hovered = False

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
        
        self.interaction_controller()

    def interaction_controller(self):
        """
        allows the block to interact with the world, player and mouse
        
        ...
        
        Returns
        -------
        None
        """
        
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if self.rect.left < mouse_x < self.rect.right:
            if self.rect.top < mouse_y < self.rect.bottom:
                self.hovered = True
            else:
                self.hovered = False
        else:
            self.hovered = False

        if self.hovered:
            if pygame.mouse.get_pressed()[0]:
                self.kill()

class Log(pygame.sprite.Sprite):
    """
    the base block for trees, also used for crafting and building
    
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

    interaction_controller():
        allows the block to interact with the world, player and mouse
    """

    def __init__(self, x: int, y: int):
        """
        constructs all necessary attributes for the block object
        """
        
        pygame.sprite.Sprite.__init__(self)

        self.pos = pygame.math.Vector2(x, y)
        self.size = 32
        self.hovered = False

        self.image = pygame.Surface([self.size, self.size])
        self.image.fill(lib.color.LOG_BROWN)
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
        
        self.interaction_controller()

    def interaction_controller(self):
        """
        allows the block to interact with the world, player and mouse
        
        ...
        
        Returns
        -------
        None
        """
        
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if self.rect.left < mouse_x < self.rect.right:
            if self.rect.top < mouse_y < self.rect.bottom:
                self.hovered = True
            else:
                self.hovered = False
        else:
            self.hovered = False

        if self.hovered:
            if pygame.mouse.get_pressed()[0]:
                self.kill()