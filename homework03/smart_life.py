import pathlib
import random

from typing import List, Optional, Tuple

Cell = Tuple[int, int]
Cells = List[int]
Grid = List[Cells]


class GameOfLife:

    def __init__(self, size: Tuple[int, int], randomize: bool = True,
                 max_generations: Optional[float] = float('inf')) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size

        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()

        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)

        # Максимальное число поколений
        self.max_generations = max_generations

        # Текущее число поколений
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        # Copied from previous assignment
        if randomize:
            return [[randint(0, 1) for x in range(self.cell_width)] for y in range(self.cell_height)]
        else:
            return [[0 for x in range(self.cell_width)] for y in range(self.cell_height)]

    def get_neighbours(self, grid: Grid, cell: Cell) -> Cells:
        # Copy from previous assignment
        k = 0
        if cell[1] - 1 >= 0:
            k += grid[cell[0]][cell[1] - 1]
        if cell[1] - 1 >= 0 and cell[0] - 1 >= 0:
            k += grid[cell[0] - 1][cell[1] - 1]
        if cell[0] - 1 >= 0:
            k += grid[cell[0] - 1][cell[1]]
        if cell[1] + 1 < self.cell_width and cell[0] - 1 >= 0:
            k += grid[cell[0] - 1][cell[1] + 1]
        if cell[1] + 1 < self.cell_width:
            k += grid[cell[0]][cell[1] + 1]
        if cell[1] + 1 < self.cell_width and cell[0] + 1 < self.cell_height:
            k += grid[cell[0] + 1][cell[1] + 1]
        if cell[0] + 1 < self.cell_height:
            k += grid[cell[0] + 1][cell[1]]
        if cell[1] - 1 >= 0 and cell[0] + 1 < self.cell_height:
            k += grid[cell[0] + 1][cell[1] - 1]

        return k

    def get_next_generation(self, grid: Grid) -> Grid:
        # Copy from previous assignment
        new_mas = []
        for y in range(self.cell_height):
            new_mas.append([])
            for x in range(self.cell_width):
                if 2 <= self.get_neighbours(grid, [y, x]) <= 3:
                    new_mas[y].append(1)
                else:
                    new_mas[y].append(0)
        return new_mas

    def step(self) -> None:
        self.prev_generation = self.curr_generation
        self.curr_generation = self.get_next_generation(self.curr_generation)

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        count = 0
        for y in range(self.cell_height):
            for x in range(self.cell_width):
                if self.curr_generation[y][x] == 1:
                    count += 1
        if count > self.max_generations:
            return True
        else:
            return False

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        change = 0
        for y in range(self.cell_height):
            for x in range(self.cell_width):
                if self.curr_generation[y][x] == self.prev_generation[y][x]:
                    change += 1
        if change > 0:
            return False
        else:
            return True

    @staticmethod
    def from_file(filename: pathlib.Path) -> 'GameOfLife':
        """
        Прочитать состояние клеток из указанного файла.
        """
        my_file = open(filename, 'r')
        x = 0
        y = 0
        grid = Grid
        for line in my_file:
            x += 1
            if line == '\n':
                grid.append([])
                y += 1
                x = 0
            else:
                grid[y].append(line)

        game=GameOfLife((y,x))
        game.curr_generation=grid
        return game

    def save(filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        my_file = open(filename, 'w')
        for y in range(len(self.curr_generation)):
            for x in range(len(self.curr_generation[y])):
                my_file.write(self.curr_generation[y][x])
            my_file.write('\n')
        my_file.close()
