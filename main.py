# python module imports
import pygame

# project file imports
import lib
import debug
import block
import player

pygame.init() # initialize the pygame module

class Game:
    """
    the primary class representing the game
    
    ...

    Attributes
    ----------
    screen : pygame.Surface
        primary display surface for the game

    running : bool
        the current running state of the game

    clock : pygame.Clock
        controls the speed of the update loop

    debug_interface : debug.DebugInterface
        information overlay toggled with [TAB]

    terrain : pygame.sprite.Group
        contains the terrain blocks

    Methods
    -------
    run():
        main loop for the game, calls all subsequent methods for game to run

    single_events():
        handles all non-repeating event inputs (pressed keys)
    
    multi_events():
        handles all repeating event inputs (held keys)

    draw():
        handles all systems that need to draw to the screen

    update():
        handles all systems that require an update every frame. also controls the deltatime variable
    """

    def __init__(self):
        """
        constructs all the necessary attributes for the Game object
        """
        
        self.screen = pygame.display.set_mode([lib.SCREEN_WIDTH, lib.SCREEN_HEIGHT])
        pygame.display.set_caption(lib.SCREEN_TITLE)

        self.running = True
        self.clock = pygame.time.Clock()
        lib.events = pygame.event.get() # initializing the lib.events list (NONE at start)

        self.debug_interface = debug.DebugInterface()

        self.terrain = pygame.sprite.Group() # test group for the blocks
        self.generate_terrain(0, 604)

        self.player_camera = pygame.sprite.Group()
        self.player = player.Player(100, 100)
        self.player_camera.add(self.player)

    def generate_terrain(self, x_offset: int, y_offset: int):
        """
        creates the terrain, mostly a testing function currently
        
        ...

        Parameters
        ----------
        x_offset : int
            the horizontal offset of the terrain group
        y_offset : int
            the vertical offset of the terrain group
        
        Returns
        -------
        None
        """

        for x in range(60):
            for y in range(15):
                b = block.Block(int(x * 32) + x_offset, int(y * 32) + y_offset)
                self.terrain.add(b)

    def terrain_collision(self):
        """
        handle collisions between the player and the terrain objects
        
        ...
        
        Returns
        -------
        None
        """

        collision_tollerance = 10

        collisions = pygame.sprite.spritecollide(self.player, self.terrain, False)

        for block in collisions:
            if abs(self.player.rect.bottom - block.rect.top) < collision_tollerance:
                self.player.falling = False
                self.player.vel.y = 0
                self.player.pos.y = block.rect.top - (self.player.rect.height / 2)

        if len(collisions) == 0:
            self.player.falling = True         

    def run(self):
        """
        main loop for the game, calls all subsequent methods for game to run

        ...
        
        Returns
        -------
        None
        """

        while self.running:
            self.single_events()
            self.multi_events()
            self.draw()
            self.update()

    def single_events(self):
        """
        handles all non-repeating event inputs (pressed keys)

        ...

        Returns
        -------
        None
        """

        lib.events = pygame.event.get() # refresh events list

        for event in lib.events:
            # special events
            if event.type == pygame.QUIT:
                self.running = False

            # get all keydown events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                if event.key == pygame.K_q:
                    self.running = False
                if event.key == pygame.K_TAB:
                    self.debug_interface.toggle_active()

    def multi_events(self):
        """
        handles all repeating event inputs (held keys)
        
        ...

        Returns
        -------
        None
        """

        pass

    def draw(self):
        """
        handles all systems that need to draw to the screen

        ...

        Returns
        -------
        None        
        """

        self.screen.fill(lib.color.BLACK)

        # draw sprite groups
        self.terrain.draw(self.screen)
        self.player_camera.draw(self.screen)

        if self.debug_interface.active:
            self.debug_interface.draw()

    def update(self):
        """
        handles all systems that require an update every frame. also controls the deltatime variable
        
        ...

        Returns
        -------
        None
        """

        # collision updates
        self.terrain_collision()

        # update sprite groups
        self.terrain.update()
        self.player.update()

        # update game management systems
        self.debug_interface.update(self.clock)
        pygame.display.update()
        lib.delta_time = self.clock.tick(lib.framerate) / 1000


# run the game
if __name__ == '__main__':
    game = Game()
    game.run()
    pygame.quit() # clean up pygame background processes
