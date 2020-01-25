from typing import Tuple, List


def read_map(filename: str) -> List[List[str]]:
    """ Прочитать карту из указанного файла """
    grid = [[]]
    line = 0
    for c in open(filename).read():
        if c in 'hxc.12345':
            grid[line].append(c)
        elif c == '\n':
            grid.append([])
            line += 1
    return grid


def get_coord(grid: List[List[str]]) -> Tuple[int, int]:
    """ Получить координаты замков """
    cas = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'c':
                cas.append((i, j))
    print('Castles are in ', cas)
    decision = int(input('Which castle would you like to reach (write the number): '))
    decision = cas[decision]
    return decision


"""
def make_graph(grid: List[List[str]]):
    vertex = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != 'x':
                vertex.append((i, j))
    matrix = [[0 for i in range(len(vertex))] for j in range(len(vertex))]

    line = 0
    for i in range(len(vertex)):
        for j in range(i, len(vertex)):
            if vertex[i][0] == vertex[j][0] or vertex[i][1] == vertex[j][1]:
                matrix[i][j] = 1
                matrix[j][i] = 1

"""


def make_try(grid: List[List[str]], hum_coord: Tuple[int, int], coord: Tuple[int, int], min=0, lives=5) -> int:
    """ Рекурсивно пробуем найти решения через всех соседей """
    if hum_coord == coord:
        return min
    local_min = float("inf")
    walks = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # down, left, up, right
    done = 0  # проверка "замкнутости"
    for i in range(len(walks)):
        try:
            x1 = hum_coord[0] + walks[i][0]  # текущие
            y1 = hum_coord[1] + walks[i][1]  # координаты
            if grid[x1][y1] in '.12345':
                local_grid = grid
                local_lives = lives
                # if grid[hum_coord[0] + walks[i][0]][hum_coord[1] + walks[i][1]] in '12345':
                #     local_lives -= grid[hum_coord[0] + walks[i][0]][hum_coord[1] + walks[i][1]]
                # if local_lives == 0:
                #     continue
                local_grid[hum_coord[0]][hum_coord[1]] = 'x'
                our_try = make_try(local_grid, (x1, y1), coord, min + 1, local_lives)
                if our_try == -1:
                    done += 1
                elif our_try < local_min:
                    local_min = our_try
            elif grid[x1][y1] == 'x':
                done += 1
        except IndexError:
            done += 1
    if done == 4:
        return -1
    return local_min


def find_way(grid: List[List[str]], coord: Tuple[int, int]):
    """ Решает задачу """
    this_grid = grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'h':
                hum_coord = (i, j)
            if grid[i][j] == 'c' and (i != coord[0] or j != coord[1]):
                this_grid[i][j] = 'x'
            else:
                this_grid[i][j] = '.'
    if hum_coord == coord:
        return 0
    else:
        return make_try(this_grid, hum_coord, coord)


print(find_way(read_map('map1.txt'), (2, 0)))
