from typing import List
import copy


class Snake:
    def __init__(self):
        self._body = [[0, 0]]
        self.direction = self.RIGHT_DIRECTION

        self.lenght = 1
        self.color = 'green'


    def get_new_coord(self) -> List:
        """ Следующая координата головы змеи

        :return: Новая координата
        """

        new_coord = copy.deepcopy(self._body[-1])

        if self.direction == self.RIGHT_DIRECTION:
            new_coord[1] += 1
        elif self.direction == self.LEFT_DIRECTION:
            new_coord[1] -= 1
        elif self.direction == self.UP_DIRECTION:
            new_coord[0] -= 1
        elif self.direction == self.DOWN_DIRECTION:
            new_coord[0] += 1

        return new_coord

    def change_direction(self, new_direction:int=None) -> None:
        """ Поменять направление движения """
        assert new_direction in [self.RIGHT_DIRECTION, self.LEFT_DIRECTION,
                                 self.UP_DIRECTION, self.DOWN_DIRECTION, None]

        if not new_direction is None:
            self.direction = new_direction

    def step(self, direction:int=None, with_apple:bool=False) -> None:
        """ Сделать шаг змеей

        :param direction: Направление движения
        :param with_apple: Было ли съедено яблоко
        """
        self.change_direction(direction)
        new_coord = self.get_new_coord()

        self._body.append(new_coord)

        if not with_apple:
            del self._body[0]
        else:
            self.lenght += 1

    @property
    def body(self) -> List[List]:
        """ Тело змеи
        :return: Список координат тела змеи
        """
        return self._body

    @property
    def head(self) -> List:
        """ Голова змеи
        :return: Координаты головы змеи """
        return self._body[-1]

    RIGHT_DIRECTION = 0
    LEFT_DIRECTION  = 1
    UP_DIRECTION    = 2
    DOWN_DIRECTION  = 3
