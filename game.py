from typing import List
from snake import Snake

import random


class SnakeGame:
    def __init__(self, height:int=32, width:int=32) -> None:
        self.height = height
        self.width = width

        self.grid = [[self.BLANK_CELL for _ in range(self.width)]
                                      for _ in range(self.height)]

        self.snake = Snake()
        self.grid = self._generate_grid()

        self._generate_apple()

    def _generate_grid(self) -> List:
        """ Генерация поля

        0 - свободная ячейка
        1 - змея
        2 - яблоко

        :return: Поле
        """

        grid = [[self.BLANK_CELL for _ in range(self.width)]
                                 for _ in range(self.height)]

        for x, y in self.snake.body:
            grid[x][y] = self.SNAKE_CELL

        grid[self.apple_coord[0]][self.apple_coord[1]] = self.APPLE_CELL

        return grid

    def _generate_apple(self) -> None:
        """ Создание нового яблока """

        x = random.randint(0, self.width-1)
        y = random.randint(0, self.height-1)

        if self.grid[y][x] == self.SNAKE_CELL:
            return self._generate_apple()

        self.apple_coord = [y, x]

    def _snake_step(self, direction:int=None) -> str:
        """ Выполнить шаг змеей.

        Генерируется новое яблоко, если его съели.

        :param direction: Направление движения змеи
        :return: Текст gameover-а
        """

        new_coord = self.snake.get_new_coord()
        new_coord[0] %= self.height; new_coord[1] %= self.width

        if not (self.grid[new_coord[0]][new_coord[1]] == self.BLANK_CELL or
                self.grid[new_coord[0]][new_coord[1]] == self.APPLE_CELL):

            return "Змея съела саму себя"

        with_apple = False
        if new_coord == self.apple_coord:
            with_apple = True
            self._generate_apple()

        self.snake.step(direction, with_apple)
        self.snake._body[-1] = new_coord

    def step(self) -> None:
        """ Шаг игры """

        error = self._snake_step()

        if not error is None:
            return error

        self.grid = self._generate_grid()

    def change_direction(self, direction:int) -> None:
        """ Поменять направление движения змеи """
        self.snake.change_direction(direction)


    BLANK_CELL = 0
    SNAKE_CELL = 1
    APPLE_CELL = 2

game = SnakeGame()
