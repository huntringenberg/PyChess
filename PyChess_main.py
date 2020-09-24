import sys
import pygame
from settings import *
from game_pieces import Tile, Piece


class PyChess:
    """Main class for managing PyChess game."""

    def __init__(self):
        """Initialize the game setting and assets."""
        pygame.init()

        # Create pygame window display
        self.screen = pygame.display.set_mode(WINDOWSIZE)
        pygame.display.set_caption("PyChess")
        self.screen.fill(DARK)

        # Prepare tiled background
        self.tiles = pygame.sprite.Group()
        self.pieces = pygame.sprite.Group()
        self._prep_board()
        self.move_turn = 'wht'

    def run_game(self):
        while True:
            self.events()
            self.tiles.draw(self.screen)
            for tile in self.tiles:
                tile.draw_highlights()
            for piece in self.pieces:
                piece.blit_pieces()
            pygame.display.update()

    def _prep_board(self):
        """Draw the black and white tiled checkerboard."""
        map_file = []
        with open('starting_map.txt', 'r') as f:
            for line in f:
                map_file.append(line[:-1])

        for y, row in enumerate(map_file):
            # If row is even start with a white colored tile
            if (y % 2) == 0:
                color = 1
            else:
                color = 0
            for x, piece_code in enumerate(row):
                tile = Tile(self, color)
                tile.x, tile.y = x, y
                tile.rect.x = x * TILESIZE
                tile.rect.y = y * TILESIZE
                if piece_code != '.':
                    new_piece = Piece(self, piece_code, x, y)
                    tile.piece = new_piece
                    self.pieces.add(new_piece)
                self.tiles.add(tile)
                if color == 1:
                    color = 0
                else:
                    color = 1

    def events(self):
        """Monitor the input events for the game."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_tile_select(mouse_pos)

    def check_tile_select(self, mouse_pos):
        """Checks to see if a tile was clicked for selection."""
        for tile in self.tiles:
            if tile.rect.collidepoint(mouse_pos) and tile.piece\
                    and tile.piece.color == self.move_turn:
                tile.is_highlight = True
            else:
                tile.is_highlight = False


if __name__ == "__main__":
    # Make an instance of the game
    pc = PyChess()
    pc.run_game()
