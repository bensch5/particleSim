import raylib as rl
from pyray import *

FPS = 60
GRID_SCALE = 16
G_WIDTH, G_HEIGHT = 100, 50


def main():
    init_window(G_WIDTH * GRID_SCALE, G_HEIGHT * GRID_SCALE, "Window")
    set_target_fps(FPS)
    tiles = [[False for _y in range(G_HEIGHT)] for _x in range(G_WIDTH)]
    while not window_should_close():
        begin_drawing()
        clear_background(BLACK)
        pos_x = (get_mouse_x() / GRID_SCALE).__floor__()
        pos_y = (get_mouse_y() / GRID_SCALE).__floor__()
        if rl.IsMouseButtonDown(0) and pos_x in range(G_WIDTH) and pos_y in range(G_HEIGHT):
            tiles[pos_x][pos_y] = True
        for x, ary in enumerate(tiles):
            for y, val in enumerate(ary):
                if val:
                    rl.DrawRectangle(x * GRID_SCALE + 1, y * GRID_SCALE + 1, GRID_SCALE, GRID_SCALE, WHITE)
        rl.DrawRectangle(pos_x * GRID_SCALE + 1, pos_y * GRID_SCALE + 1, GRID_SCALE, GRID_SCALE, RED)
        end_drawing()
    close_window()


if __name__ == '__main__':
    main()
