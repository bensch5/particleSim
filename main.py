import raylib as rl
from particle import Particle
from pyray import *

FPS = 60
GRID_SCALE = 40
G_WIDTH, G_HEIGHT = 40, 20  # multiplied by grid scale


def process_input(tiles, x, y):
    if x in range(G_WIDTH) and y in range(G_HEIGHT):
        if rl.IsMouseButtonDown(0) and rl.IsMouseButtonDown(1):  # erase particle
            tiles[x][y] = Particle(0, x, y)
        elif rl.IsMouseButtonDown(0):  # right click, sand particle
            tiles[x][y] = Particle(1, x, y)
        elif rl.IsMouseButtonDown(1):  # left click, water particle
            tiles[x][y] = Particle(2, x, y)


def do_simulation_step(tiles, display_tiles):
    for x, ary in enumerate(tiles):
        for y, p in enumerate(ary):
            match p.p_id:
                case 0:
                    pass
                case 1:
                    simulate_sand(tiles, display_tiles, p, len(tiles) - 2, len(ary) - 1)


def simulate_sand(tiles, display_tiles, particle, max_x, max_y):
    y = particle.pos_y
    x = particle.pos_x
    if y < max_y:
        if tiles[x][y + 1].p_id == 0:  # directly below
            display_tiles[x][y] = Particle(0, x, y)
            display_tiles[x][y + 1] = Particle(particle.p_id, x, y + 1)
        elif x > 0 and tiles[x - 1][y + 1].p_id == 0:  # bottom left
            display_tiles[x][y] = Particle(0, x, y)
            display_tiles[x - 1][y + 1] = Particle(particle.p_id, x - 1, y + 1)
        elif x < max_x and tiles[x+1][y+1].p_id == 0:  # bottom right
            display_tiles[x][y] = Particle(0, x, y)
            display_tiles[x + 1][y + 1] = Particle(particle.p_id, x + 1, y + 1)


def display_frame(display_tiles):
    for x, ary in enumerate(display_tiles):
        for y, p in enumerate(ary):
            rl.DrawRectangle(x * GRID_SCALE + 1, y * GRID_SCALE + 1, GRID_SCALE, GRID_SCALE, p.color)


def main():
    init_window(G_WIDTH * GRID_SCALE, G_HEIGHT * GRID_SCALE, "Window")
    set_target_fps(FPS)
    # initialize tile array with "empty" particles
    tiles = [[]]
    for x in range(G_WIDTH):
        tiles.append([])
        for y in range(G_HEIGHT):
            tiles[x].append(Particle(0, x, y))

    while not window_should_close():
        begin_drawing()
        clear_background(BLACK)
        pos_x = (get_mouse_x() / GRID_SCALE).__floor__()
        pos_y = (get_mouse_y() / GRID_SCALE).__floor__()
        if rl.IsMouseButtonDown(0) or rl.IsMouseButtonDown(1):
            process_input(tiles, pos_x, pos_y)
        display_tiles = tiles.copy()
        do_simulation_step(tiles, display_tiles)
        display_frame(display_tiles)
        tiles = display_tiles.copy()

        # show indicator for current drawing position
        rl.DrawRectangle(pos_x * GRID_SCALE + 1, pos_y * GRID_SCALE + 1, GRID_SCALE, GRID_SCALE, RED)
        end_drawing()
    close_window()


if __name__ == '__main__':
    main()
