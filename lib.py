# python module imports
import pygame
from random import randint

# constants
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN_TITLE = "Project Talisman"

GRAVITY = 10

class Colors:
    """
    contains color objects and methods for creating random colors

    ...

    Attributes
    ----------
    BLACK : pygame.Color
    
    WHITE : pygame.Color

    Methods
    -------
    random():
        generates a random color
    
    random_gray():
        generates a random grayscale color

    random_custom(channels: str):
        generates a random color only on the selected channels
    """

    def __init__(self):
        """
        constructs all color objects
        """

        self.BLACK = pygame.Color(0, 0, 0, 255)
        self.WHITE = pygame.Color(255, 255, 255, 255)
        self.LOG_BROWN = pygame.Color(64, 40, 13, 255)

    def random(self) -> pygame.Color:
        """
        generates a random color

        ...
        
        Returns
        -------
        pygame.Color
        """

        color = pygame.Color(randint(0, 255), randint(0, 255), randint(0, 255), 255)

        return color
    
    def random_gray(self) -> pygame.Color:
        """
        generates a random grayscale color
        
        ...
        
        Returns
        -------
        pygame.Color
        """

        scale = randint(0, 255) # determine the random scale

        color = pygame.Color(scale, scale, scale, 255)

        return color
    
    def random_custom(self, channels: str) -> pygame.Color:
        """
        generates a random color only on the selected channels

        'rb' will generate a color on the red and blue channels
        'g' will just generate a color on the green channel

        ...

        Parameters
        ----------
        channels : str
            determines the channels that the random color will use during generation

        Returns
        -------
        pygame.Color        
        """
        
        red_channel = 0
        green_channel = 0
        blue_channel = 0
        
        if 'r' in channels:
            red_channel = randint(0, 255)
        if 'g' in channels:
            green_channel = randint(0, 255)
        if 'b' in channels:
            blue_channel = randint(0, 255)

        color = pygame.Color(red_channel, green_channel, blue_channel, 255)

        return color
        

color = Colors() # color object for reference in other files

# initialize game loop stuff
delta_time = 0
events = None
framerate = 120