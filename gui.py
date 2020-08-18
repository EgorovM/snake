import time

import pygame

from game import SnakeGame
from snake import Snake


class GUI:
    def __init__(self, width:int=20, height:int=20, speed:int=10) -> None:
        self.WINDOW_SIZE = 640

        self.grid_width = width
        self.grid_height = height
        self.speed = speed

        self.screen = pygame.display.set_mode((self.WINDOW_SIZE, self.WINDOW_SIZE))
        self.game = SnakeGame(width, height)

        self.cell_width = 32

    def _draw_lines(self) -> None:
        """ Отрисовка линий """

        for x in range(0, self.grid_width):
            x = x * self.cell_width
            pygame.draw.line(
                self.screen,
                pygame.Color('black'),
                (x, 0),
                (x, self.WINDOW_SIZE)
            )

        for y in range(0, self.grid_height):
            y = y * self.cell_width
            pygame.draw.line(
                self.screen,
                pygame.Color('black'),
                (0, y),
                (self.WINDOW_SIZE, y)
            )

    def _draw_grid(self) -> None:
        """ Отрисовка поля """

        def draw_rectangle(color:pygame.Color, row:int, col:int) -> None:
            assert 0 <= col <= self.grid_height
            assert 0 <= row <= self.grid_width

            pygame.draw.rect(
                self.screen,
                color,
                (
                    col * self.cell_width,
                    row * self.cell_width,
                    self.cell_width,
                    self.cell_width
                )
            )

        for row in range(self.grid_height):
            for col in range(self.grid_width):
                color = self.COLORS[self.game.grid[row][col]]

                draw_rectangle(color, row, col)

        draw_rectangle(pygame.Color('green'), *self.game.snake.head)

        self._draw_lines()

    def _show_gameover(self, text:str) -> None:
        """ Показать текст об окончании игры """

        font = pygame.font.Font(None, 25)
        text = font.render(text, True, pygame.Color('white'), pygame.Color('black'))

        textRect = text.get_rect()
        textRect.center = (self.WINDOW_SIZE // 2, self.WINDOW_SIZE // 2)

        self.screen.blit(text, textRect)
        pygame.display.update()

    def _change_direction_by_event(self, event:pygame.event) -> None:
        """ Поменять направление движениязмеи """

        direction = None

        if event.key == pygame.K_RIGHT:
            direction = Snake.RIGHT_DIRECTION
        elif event.key == pygame.K_LEFT:
            direction = Snake.LEFT_DIRECTION
        elif event.key == pygame.K_UP:
            direction = Snake.UP_DIRECTION
        elif event.key == pygame.K_DOWN:
            direction = Snake.DOWN_DIRECTION

        self.game.change_direction(direction)

    def run(self) -> None:
        """ Начать игру """

        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Snake')
        self.screen.fill(pygame.Color('white'))
        running = True

        self._draw_grid()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

                elif event.type == pygame.KEYDOWN:
                    self._change_direction_by_event(event)

            error = self.game.step()

            if not error is None:
                self._show_gameover(error)

            else:
                self._draw_grid()
                pygame.display.flip()
                clock.tick(self.speed)


    COLORS = {
        0 : pygame.Color('black'),
        1 : pygame.Color('white'),
        2 : pygame.Color('red'),
        3 : pygame.Color('green')
    }
