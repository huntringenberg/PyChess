import pygame
from pygame.sprite import Sprite
from settings import *


class Tile(Sprite):
    """Class for managing the checkerboard tiles"""

    def __init__(self, game, color_in):
        """Initialize the attributes for a PyChess tile."""
        super().__init__()
        self.pc_game = game
        self.screen = game.screen
        self.piece = None

        # Set tile color to black (0) or white (1) based on color_in value
        colors = [LIGHT, DARK]
        self.color = colors[color_in]

        # Create filled rect object corresponding to tile size and color
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(colors[color_in])
        self.rect = self.image.get_rect()

        # The x and y attributes of the class designate the row and col
        # on the chess board
        self.x = 0
        self.y = 0

        # Get image for highlighting tile during selection
        self.is_highlight = False
        self.highlight_image = pygame.image.load('images/highlight.png')
        self.highlight_rect = self.highlight_image.get_rect()

    def draw_highlights(self):
        """Method for drawing highlight over tile when selected."""
        if self.is_highlight:
            self.highlight_rect.x = self.rect.x
            self.highlight_rect.y = self.rect.y
            self.screen.blit(self.highlight_image, self.highlight_rect)


class Piece(Sprite):
    """A class for handling the chess pieces behavior."""
    def __init__(self, game, piece_code, x, y):
        """Initialize a game piece."""
        super().__init__()
        self.code = piece_code
        if self.code.islower():
            self.color = 'wht'
        else:
            self.color = 'blk'
        self.game = game
        self.screen = game.screen
        self.image = pygame.image.load(image_dict[piece_code])
        self.rect = self.image.get_rect()
        self.x, self.y = x, y

    def blit_pieces(self):
        """Draws the pieces to the screen."""
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
        self.screen.blit(self.image, self.rect)


