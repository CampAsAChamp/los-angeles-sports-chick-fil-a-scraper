BLACK = 'black'
RED = 'red'
GREEN = 'green'
YELLOW = 'yellow'
BLUE = 'blue'
MAGENTA = 'magenta'
CYAN = 'cyan'
WHITE = 'white'

BLACK_CODE = "\033[30m"
RED_CODE = "\033[31m"
GREEN_CODE = "\033[32m"
YELLOW_CODE = "\033[33m"
BLUE_CODE = "\033[34m"
MAGENTA_CODE = "\033[35m"
CYAN_CODE = "\033[36m"
WHITE_CODE = "\033[37m"
RESET_CODE = "\033[0m"


def color_text(text: str, color: str):
    if color == BLACK:
        color = BLACK_CODE
    elif color == RED:
        color = RED_CODE
    elif color == GREEN:
        color = GREEN_CODE
    elif color == YELLOW:
        color = YELLOW_CODE
    elif color == BLUE:
        color = BLUE_CODE
    elif color == MAGENTA:
        color = MAGENTA_CODE
    elif color == CYAN:
        color = CYAN_CODE
    elif color == WHITE:
        color = WHITE_CODE
    else:
        return text

    return color + text + RESET_CODE
