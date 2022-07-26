from pygame.math import Vector2 as vec
WIDTH ,HEIGHT = 700,420
FPS = 50

TOP_BOTTOM_BUFFER = 25
MAZE_WIDTH, MAZE_HEIGHT = WIDTH-TOP_BOTTOM_BUFFER, HEIGHT-TOP_BOTTOM_BUFFER

ROWS = 30
COLS = 28

# colour settings
BLACK = (0, 0, 0)
RED = (208, 22, 22)
GREY = (107, 107, 107)
WHITE = (255, 255, 255)
PLAYER_COLOUR1 = (235, 210, 52)
PLAYER_COLOUR2 = (245, 129, 66)

# font settings
START_TEXT_SIZE = 16
START_FONT = 'arial black'

PLAYER_START_POS = vec(1,1)