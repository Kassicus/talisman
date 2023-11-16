# python module imports
import pygame

# project file imports
import lib

class DebugInterface:
    """
    overlay for displaying information, toggled by pressing [TAB]

    ...

    Attributes
    ----------
    active : bool
        determines if the interface is drawn
    offset : int
        universal offset from the right side of the screen
    font : pygame.Font
        font to render the interface with
    display_surface : pygame.Surface
        surface to draw the interface to

    Methods
    -------
    get_fps(clock: pygame.time.Clock) -> list [pygame.Surface, int]:
        creates a text object and an offset to render the fps
    get_mouse() -> list [pygame.Surface, int]:
        creates a text object and an offset to render the mouse position
    toggle_active():
        changes the active state of the interface
    draw():
        draws all of the interface objects at thier offsets
    update(cock: pygame.time.Clock):
        updates all of the interface objects
    """

    def __init__(self):
        """
        constructs all necessary objects for the interface
        """

        self.active = False
        self.font = pygame.font.SysFont("Courier", 16) # use a default font that should be on every system
        self.offset = 10
        self.display_surface = pygame.display.get_surface() # this should reference the main screen object as long as the interface is called from the main.py file

        # text objects
        self.t_fps = None
        self.t_mouse = None

        # offsets
        self.o_fps = None
        self.o_mouse = None

    def get_fps(self, clock: pygame.time.Clock) -> list [pygame.Surface, int]:
        """
        creates a text object and an offset to render the fps
        
        Returns
        -------
        list [pygame.Surface, int]
        """

        string = "FPS: " + str(int(clock.get_fps())) # get the fps, convert to int then string
        text = self.font.render(string, True, lib.color.WHITE)
        offset = int(lib.SCREEN_WIDTH - text.get_width() - self.offset)

        return text, offset

    def get_mouse(self) -> list [pygame.Surface, int]:
        """
        creates a text object and an offset to render the mouse position
        
        Returns
        -------
        list [pygame.Surface, int]
        """
        x, y = pygame.mouse.get_pos()

        string = "Mouse: " + str(x) + "," + str(y)
        text = self.font.render(string, True, lib.color.WHITE)
        offset = int(lib.SCREEN_WIDTH - text.get_width() - self.offset)

        return text, offset
    
    def toggle_active(self):
        """
        changes the active state of the interface
        
        Returns
        -------
        None
        """

        if self.active:
            self.active = False
        else:
            self.active = True

    def draw(self):
        """
        draws all of the interface objects at thier offsets
        
        Returns
        -------
        None
        """

        self.display_surface.blit(self.t_fps, (self.o_fps, 10))
        self.display_surface.blit(self.t_mouse, (self.o_mouse, 30))

    def update(self, clock: pygame.time.Clock):
        """
        updates all of the interface objects
        
        Returns
        -------
        None
        """

        self.t_fps, self.o_fps = self.get_fps(clock)
        self.t_mouse, self.o_mouse = self.get_mouse()